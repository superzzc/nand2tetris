from pkg.JackTokenizer import JackTokenizer
from pkg.SymbolTable import SymbolTable
from pkg.VMWriter import VMWriter
from pkg.config import k, op_map, var_map, Kind, Seg
from pkg.config2 import symbol_op, keyword_const, unaryOP


class CompilationEngine:
    def __init__(self, inputfile, outputfile):
        self.tokenizer = JackTokenizer(inputfile)
        self.writer = VMWriter(outputfile)
        self.symbolTable = SymbolTable()
        # 保存当前类、子程序相关信息
        self.className = None
        self.subroutineName = None
        self.subroutineType = None  # constructor | method | function
        self.returnType = None  # void | int | char | class ...
        # if_label标签计数
        self.if_label_count = 0
        # while_label标签计数
        self.while_label_count = 0

    def CompileClass(self):
        while self.tokenizer.hasMoreCommands():
            self.tokenizer.advance()
            # className
            if self.tokenizer.tokenType() == "identifier":
                self.className = self.tokenizer.indentifier()
            # classVarDec
            elif (
                self.tokenizer.tokenType() == "keyword"
                and self.tokenizer.keyword() in ("static", "field")
            ):
                self.CompileClassVarDec()
            # subroutineDec
            elif (
                self.tokenizer.tokenType() == "keyword"
                and self.tokenizer.keyword() in ("constructor", "function", "method")
            ):
                self.CompileSubroutine()

    def CompileClassVarDec(self):
        while self.tokenizer.current_token != ";":
            # static | field
            kind = self.tokenizer.keyword()
            # type
            self.tokenizer.advance()
            _type = self.tokenizer.indentifier()
            # varName
            self.tokenizer.advance()
            name = self.tokenizer.indentifier()
            # add entry to symbol table
            self.symbolTable.define(name, _type, k[kind])
            self.tokenizer.advance()
            while self.tokenizer.current_token == ",":
                # varName
                self.tokenizer.advance()
                name = self.tokenizer.indentifier()
                # add entry to symbol table
                self.symbolTable.define(name, _type, k[kind])
                self.tokenizer.advance()
        
    def CompileVarDec(self):
        # var type varName (,varName)*;
        # kind = k[self.tokenizer.keyword()]
        self.tokenizer.advance()
        while self.tokenizer.current_token != ";":
            # type
            _type = self.tokenizer.current_token
            # varName
            self.tokenizer.advance()
            name = self.tokenizer.indentifier()
            # add to symbol table
            self.symbolTable.define(name, _type, Kind.VAR)
            self.tokenizer.advance()
            while self.tokenizer.current_token == ",":
                # varName
                self.tokenizer.advance()
                name = self.tokenizer.indentifier()
                # add to symbol table
                self.symbolTable.define(name, _type, Kind.VAR)
                self.tokenizer.advance()

    def CompileSubroutine(self):
        self.symbolTable.startSubroutine()
        # constructor
        if self.tokenizer.keyword() == "constructor":
            self.subroutineType = "constructor"
            # className
            self.returnType = self.tokenizer.advance()
            # functionName
            self.tokenizer.advance()
            self.subroutineName = self.tokenizer.indentifier()
        # function
        elif self.tokenizer.keyword() == "function":
            self.subroutineType = "function"
            self.tokenizer.advance()
            self.returnType = self.tokenizer.current_token
            self.tokenizer.advance()
            self.subroutineName = self.tokenizer.indentifier()
        # method
        else:
            # add this entry to symboltable
            self.subroutineType = "method"
            self.symbolTable.define("this", self.className, Kind.ARG)
            self.tokenizer.advance()
            self.returnType = self.tokenizer.current_token
            self.tokenizer.advance()
            self.subroutineName = self.tokenizer.indentifier()
        # (
        self.tokenizer.advance()
        # parameter list
        self.CompileParameterList()
        # subroutineBody
        self.CompileSubroutineBody()

    def CompileSubroutineBody(self):
        """
        Docstring for CompileSubroutineBody
        将变量添加到符号表，根据subroutine类型生成合适的入口，并编译子程序主体
        """
        # {
        self.tokenizer.advance()
        # varDec*
        while self.tokenizer.tokens[self.tokenizer.index + 1] == "var":
            self.tokenizer.advance()
            self.CompileVarDec()
        # write function entry
        nlocals = self.symbolTable.varCount(Kind.VAR)
        self.writer.writeFunction(f"{self.className}.{self.subroutineName}", nlocals)
        if self.subroutineType == "constructor":
            nfileds = self.symbolTable.varCount(Kind.FIELD)
            self.writer.writePush(Seg.CONST, nfileds)
            self.writer.writeCall("Memory.alloc", 1)
            self.writer.writePop(Seg.POINTER, 0)
        elif self.subroutineType == "method":
            self.writer.writePush(Seg.ARG, 0)
            self.writer.writePop(Seg.POINTER, 0)
        # statements
        self.CompileStatements()
        # }
        self.tokenizer.advance()


    def CompileStatements(self):
        while self.tokenizer.hasMoreCommands():
            self.tokenizer.advance()
            # 处理空statement的情况{}
            if self.tokenizer.current_token == "}":
                self.tokenizer.stepback()
                return
            if (
                self.tokenizer.tokenType() == "keyword"
                and self.tokenizer.keyword() == "let"
            ):
                self.CompileLet()
            elif (
                self.tokenizer.tokenType() == "keyword"
                and self.tokenizer.keyword() == "if"
            ):
                self.CompileIf()
            elif (
                self.tokenizer.tokenType() == "keyword"
                and self.tokenizer.keyword() == "while"
            ):
                self.CompileWhile()
            elif (
                self.tokenizer.tokenType() == "keyword"
                and self.tokenizer.keyword() == "do"
            ):
                self.CompileDo()
            elif (
                self.tokenizer.tokenType() == "keyword"
                and self.tokenizer.keyword() == "return"
            ):
                self.CompileReturn()
                break
  
    def CompileLet(self):
        # varName
        self.tokenizer.advance()
        varName = self.tokenizer.indentifier()
        var_kind = self.symbolTable.kindOf(varName)
        var_index = self.symbolTable.indexOf(varName)
        # check if it's an array assignment
        if self.tokenizer.tokens[self.tokenizer.index + 1] == "[":
            self.tokenizer.advance()
            # 计算a[i] address
            self.CompileExpression()
            self.writer.writePush(var_map[var_kind], var_index)
            self.writer.writeArithmetic("add")
            # skip ]
            self.tokenizer.advance()
            # skip =
            self.tokenizer.advance()
            # 计算右侧表达式
            self.CompileExpression()
            # 保存右侧表达式计算结果，回到左侧处理赋值
            self.writer.writePop(Seg.TEMP, 0)
            self.writer.writePop(Seg.POINTER, 1)
            self.writer.writePush(Seg.TEMP, 0)
            self.writer.writePop(Seg.THAT, 0)
            # 跳过后续token，直接到赋值语句结束
            while self.tokenizer.current_token != ";":
                self.tokenizer.advance()
            return
        else:
            # skip =
            self.tokenizer.advance()
            # 处理右侧表达式
            self.CompileExpression()
            # assign value to varName
            self.writer.writePop(var_map[var_kind], var_index)
            # 跳过后续token，直接到赋值语句结束
            while self.tokenizer.current_token != ";":
                self.tokenizer.advance()
            return

    def CompileIf(self):
        l1_label = f"IF_L1_{self.if_label_count}"
        l2_label = f"IF_L2_{self.if_label_count}"
        self.if_label_count += 1
        # (
        self.tokenizer.advance()
        # expression
        self.CompileExpression()
        self.writer.writeArithmetic("not")
        self.writer.writeIf(l1_label)
        # )
        self.tokenizer.advance()
        # {
        self.tokenizer.advance()
        # statements
        self.CompileStatements()
        # }
        self.tokenizer.advance()
        # 跳过else部分
        self.writer.writeGoto(l2_label)
        self.writer.writeLabel(l1_label)
        # else statements
        self.tokenizer.advance()
        if (
            self.tokenizer.tokenType() == "keyword"
            and self.tokenizer.keyword() == "else"
        ):
            # {
            self.tokenizer.advance()
            # expr
            self.CompileStatements()
            self.writer.writeLabel(l2_label)
            # }
            self.tokenizer.advance()
        else:
            self.tokenizer.stepback()
            self.writer.writeLabel(l2_label)

    def CompileWhile(self):
        while_label_l1 = f"WHILE_L1_{self.while_label_count}"
        while_label_l2 = f"WHILE_L2_{self.while_label_count}"
        self.while_label_count += 1
        # (
        self.tokenizer.advance()
        self.writer.writeLabel(while_label_l1)
        # expression
        self.CompileExpression()
        self.writer.writeArithmetic("not")
        self.writer.writeIf(while_label_l2)
        # )
        self.tokenizer.advance()
        # {
        self.tokenizer.advance()
        # statements
        self.CompileStatements()
        self.writer.writeGoto(while_label_l1)
        self.writer.writeLabel(while_label_l2)
        # }
        self.tokenizer.advance()

    def CompileDo(self):
        # subroutineCall
        self.tokenizer.advance()
        subName = self.tokenizer.indentifier()
        self.__CompileSubCall(subName)
        # pop temp 0 to discard return value
        self.writer.writePop(Seg.TEMP, 0)
        # ;
        self.tokenizer.advance()

    def CompileReturn(self):
        if self.returnType == "void":
            self.writer.writePush(Seg.CONST, 0)
            self.writer.writeReturn()
        else:
            if self.tokenizer.tokens[self.tokenizer.index + 1] != ";":
                self.CompileExpression()
            self.writer.writeReturn()
        # ；
        self.tokenizer.advance()

    def CompileParameterList(self):
        """
        Docstring for CompileParameterList
        解析参数列表，将其添加到符号表中
        """
        self.tokenizer.advance()
        while self.tokenizer.current_token != ")":
            if self.tokenizer.current_token == ",":
                self.tokenizer.advance()
            # type
            _type = self.tokenizer.current_token
            # varName
            self.tokenizer.advance()
            name = self.tokenizer.indentifier()
            # add to symbol table
            self.symbolTable.define(name, _type, Kind.ARG)
            # pass ,
            self.tokenizer.advance()

    def CompileExpressionList(self):
        # ExpressionList
        nargs = 0
        # 处理无表达式情况
        if self.tokenizer.tokens[self.tokenizer.index + 1] == ")":
            return nargs
        self.CompileExpression()
        nargs += 1
        while (
            self.tokenizer.hasMoreCommands()
            and self.tokenizer.tokens[self.tokenizer.index + 1] == ","
        ):
            # ,
            self.tokenizer.advance()
            self.CompileExpression()
            nargs += 1
        return nargs

    def CompileExpression(self):
        # Expression root
        self.CompileTerm()
        if self.tokenizer.tokens[self.tokenizer.index + 1] in symbol_op:
            self.tokenizer.advance()
            op = self.tokenizer.symbol()
            self.CompileTerm()
            if op == "*":
                self.writer.writeCall("Math.multiply", 2)
            elif op == "/":
                self.writer.writeCall("Math.divide", 2)
            else:
                self.writer.writeArithmetic(op_map[op])

    def CompileTerm(self):
        # term root
        while self.tokenizer.hasMoreCommands():
            self.tokenizer.advance()
            # int val
            if self.tokenizer.tokenType() == "integerConstant":
                integer = self.tokenizer.intVal()
                self.writer.writePush(Seg.CONST, integer)
                break
            # str val
            elif self.tokenizer.tokenType() == "stringConstant":
                string = self.tokenizer.stringVal()
                strLen = len(string)
                self.writer.writePush(Seg.CONST, strLen)
                self.writer.writeCall("String.new", 1)
                for i in range(0, strLen):
                    self.writer.writePush(Seg.CONST, ord(string[i]))
                    # 方法调用默认第一个参数为this，找到当前操作的对象。call String.new的时候，栈顶已经把对象引用放好了，不用手动处理入栈
                    self.writer.writeCall("String.appendChar", 2)
                break
            # keyword const
            elif (
                self.tokenizer.tokenType() == "keyword"
                and self.tokenizer.current_token in keyword_const
            ):
                # true false null this
                key_const = self.tokenizer.keyword()
                if key_const in ("false", "null"):
                    self.writer.writePush(Seg.CONST, 0)
                elif key_const == "true":
                    self.writer.writePush(Seg.CONST, 1)
                    self.writer.writeArithmetic("neg")
                else:
                    self.writer.writePush(Seg.POINTER, 0)
                break
            elif self.tokenizer.tokenType() == "identifier":
                ident = self.tokenizer.indentifier()
                self.tokenizer.advance()
                # array
                if (
                    self.tokenizer.tokenType() == "symbol"
                    and self.tokenizer.current_token == "["
                ):
                    self.tokenizer.stepback()
                    self.__CompileArray(ident)
                # subroutinecall
                elif (
                    self.tokenizer.tokenType() == "symbol"
                    and self.tokenizer.current_token in ("(", ".")
                ):
                    self.tokenizer.stepback()
                    self.__CompileSubCall(ident)
                # varName
                else:
                    self.tokenizer.stepback()
                    var_index = self.symbolTable.indexOf(ident)
                    var_kind = self.symbolTable.kindOf(ident)
                    self.writer.writePush(var_map[var_kind], var_index)
                break
            # '('expression')'
            elif (
                self.tokenizer.tokenType() == "symbol"
                and self.tokenizer.symbol() == "("
            ):
                # expression
                self.CompileExpression()
                # )
                self.tokenizer.advance()
                break
            # unaryop term
            elif (
                self.tokenizer.tokenType() == "symbol"
                and self.tokenizer.symbol() in unaryOP
            ):
                # - ~
                unaryop = self.tokenizer.symbol()
                # term
                self.CompileTerm()
                self.writer.writeArithmetic("neg" if unaryop == "-" else "not")
                break

    def __CompileArray(self, arrayName):
        array_kind = self.symbolTable.kindOf(arrayName)
        array_index = self.symbolTable.indexOf(arrayName)
        self.writer.writePush(var_map[array_kind], array_index)
        # [
        self.tokenizer.advance()
        # expression
        self.CompileExpression()
        # 假定compileExpression已经处理好了表达式，此时栈顶结果即为索引，接下来只需要add偏移量即可
        self.writer.writeArithmetic("add")
        # 将元素地址存入pointer 1
        self.writer.writePop(Seg.POINTER, 1)
        # 二次引用获得arrary[i]
        self.writer.writePush(Seg.THAT, 0)
        # ]
        self.tokenizer.advance()

    def __CompileSubCall(self, Name):
        # . or (
        self.tokenizer.advance()
        symbol = self.tokenizer.symbol()
        if symbol == ".":
            self.tokenizer.advance()
            subName = self.tokenizer.indentifier()
            # varName.subroutineName(expressionList) 某个对象的method调用
            if (
                Name in self.symbolTable.subroutineTable
                or Name in self.symbolTable.classTable
            ):
                var_kind = self.symbolTable.kindOf(Name)
                var_index = self.symbolTable.indexOf(Name)
                var_type = self.symbolTable.typeOf(Name)
                # push this
                self.writer.writePush(var_map[var_kind], var_index)
                # (
                self.tokenizer.advance()
                nargs = self.CompileExpressionList()
                self.writer.writeCall(f"{var_type}.{subName}", nargs + 1)
            # className.subroutineName(expressionList) 某个类的function调用
            else:
                # (
                self.tokenizer.advance()
                nargs = self.CompileExpressionList()
                self.writer.writeCall(f"{Name}.{subName}", nargs)

        elif symbol == "(":
            # subroutineName(expressionList) 当前对象的method调用，隐式传入this
            self.writer.writePush(Seg.POINTER, 0)
            nargs = self.CompileExpressionList()
            self.writer.writeCall(f"{self.className}.{Name}", nargs + 1)
        # )
        self.tokenizer.advance()
