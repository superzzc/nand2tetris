from pkg.JackTokenizer import JackTokenizer
import xml.etree.ElementTree as ET
from pkg.config import symbol_op,keyword_const,unaryOP


class CompilationEngine:
    def __init__(self, inputfile):
        self.tokenizer = JackTokenizer(inputfile)
        self.classTree = self.CompileClass()

    def CompileClass(self):
        while self.tokenizer.hasMoreCommands():
            self.tokenizer.advance()
            # class
            if (
                self.tokenizer.tokenType() == "keyword"
                and self.tokenizer.keyword() == "class"
            ):
                Class = ET.Element("class")
                keyword_class=ET.SubElement(Class,'keyword')
                keyword_class.text=self.tokenizer.keyword()
            # className
            elif self.tokenizer.tokenType() == "identifier":
                ident = ET.SubElement(Class, "identifier")
                ident.text = self.tokenizer.indentifier()
            # {
            elif (
                self.tokenizer.tokenType() == "symbol"
                and self.tokenizer.current_token == "{"
            ):
                symbol_left = ET.SubElement(Class, "symbol")
                symbol_left.text = self.tokenizer.symbol()
            # classVarDec
            elif (
                self.tokenizer.tokenType() == "keyword"
                and self.tokenizer.keyword() in ("static", "field")
            ):
                self.CompileClassVarDec(Class)
            # subroutineDec
            elif (
                self.tokenizer.tokenType() == "keyword"
                and self.tokenizer.keyword() in ("constructor", "function", "method")
            ):
                self.CompileSubroutine(Class)
            # }
            elif (
                self.tokenizer.tokenType() == "symbol"
                and self.tokenizer.symbol() == "}"
            ):
                symbol_right = ET.SubElement(Class, "symbol")
                symbol_right.text = self.tokenizer.symbol()

        tree = ET.ElementTree(Class)
        ET.indent(tree=tree, space="\t", level=0)
        return tree

    def CompileClassVarDec(self, Element):
        # classVarDec root
        classVarDec = ET.SubElement(Element, "classVarDec")
        keyword_sf=ET.SubElement(classVarDec,'keyword')
        keyword_sf.text=self.tokenizer.keyword()
        # static | field type varName ...
        self.__parse_until(classVarDec, ";")
        # ;
        symbol = ET.SubElement(classVarDec, "symbol")
        symbol.text = self.tokenizer.symbol()

    def CompileSubroutine(self, Element):
        # subroutineDec root
        subDec = ET.SubElement(Element, "subroutineDec")
        keyword_cfm=ET.SubElement(subDec,'keyword')
        keyword_cfm.text=self.tokenizer.keyword()
        # (
        self.__parse_until(subDec, "(")
        symbol_left = ET.SubElement(subDec, "symbol")
        symbol_left.text = self.tokenizer.symbol()
        # parameter list
        self.CompileParameterList(subDec)
        # )
        symbol_right = ET.SubElement(subDec, "symbol")
        symbol_right.text = self.tokenizer.symbol()
        # subroutineBody
        self.CompileSubroutineBody(subDec)

    def CompileSubroutineBody(self, Element):
        # SubroutineBody root
        subBody = ET.SubElement(Element, "subroutineBody")
        while self.tokenizer.hasMoreCommands():
            self.tokenizer.advance()
            if (
                self.tokenizer.tokenType() == "symbol"
                and self.tokenizer.current_token == "{"
            ):
                symbol_left = ET.SubElement(subBody, "symbol")
                symbol_left.text = self.tokenizer.symbol()
            elif (
                self.tokenizer.tokenType() == "keyword"
                and self.tokenizer.keyword() == "var"
            ):
                self.CompileVarDec(subBody)
            elif (
                self.tokenizer.tokenType() == "symbol"
                and self.tokenizer.current_token == "}"
            ):
                symbol_right = ET.SubElement(subBody, "symbol")
                symbol_right.text = self.tokenizer.symbol()
                break
            else:
                self.tokenizer.stepback()
                self.CompileStatements(subBody)
            
    def CompileParameterList(self, Element):
        # ParameterList root
        paraList = ET.SubElement(Element, "parameterList")
        # 强制不使用自闭合标签，textcompare比较使用，测试通过后可去掉
        paraList.text='\n'

        self.__parse_until(paraList, ")")

    def CompileVarDec(self, Element):
        # VarDec root
        VarDec = ET.SubElement(Element, "varDec")
        keyword_var = ET.SubElement(VarDec,'keyword')
        keyword_var.text=self.tokenizer.keyword()
        self.__parse_until(VarDec, ";")
        # ;
        symbol = ET.SubElement(VarDec, "symbol")
        symbol.text = self.tokenizer.symbol()

    def CompileStatements(self, Element):
        Statements = ET.SubElement(Element, "statements")
        # 强制不使用自闭合标签，textcompare比较使用，测试通过后可去掉
        Statements.text='\n'

        while self.tokenizer.hasMoreCommands():
            self.tokenizer.advance()
            # 处理空statement的情况{}
            if self.tokenizer.current_token=='}':
                self.tokenizer.stepback()
                return
            if (
                self.tokenizer.tokenType() == "keyword"
                and self.tokenizer.keyword() == "let"
            ):
                self.CompileLet(Statements)
            elif (
                self.tokenizer.tokenType() == "keyword"
                and self.tokenizer.keyword() == "if"
            ):
                self.CompileIf(Statements)
            elif (
                self.tokenizer.tokenType() == "keyword"
                and self.tokenizer.keyword() == "while"
            ):
                self.CompileWhile(Statements)
            elif (
                self.tokenizer.tokenType() == "keyword"
                and self.tokenizer.keyword() == "do"
            ):
                self.CompileDo(Statements)
            elif (
                self.tokenizer.tokenType() == "keyword"
                and self.tokenizer.keyword() == "return"
            ):
                self.CompileReturn(Statements)
                break
    
            
    def CompileLet(self, Element):
        let = ET.SubElement(Element,'letStatement')
        keyword_let=ET.SubElement(let,'keyword')
        keyword_let.text=self.tokenizer.keyword()
        # varName
        self.tokenizer.advance()
        varName=ET.SubElement(let,'identifier')
        varName.text=self.tokenizer.indentifier()
        # [ or =
        self.tokenizer.advance()
        symbol = ET.SubElement(let,'symbol')
        symbol.text=self.tokenizer.symbol()
        # [expression] ?
        if self.tokenizer.symbol()=='[':
            # expression
            self.CompileExpression(let)
            # ]
            self.tokenizer.advance()
            symbol = ET.SubElement(let,'symbol')
            symbol.text=self.tokenizer.symbol()
            # =
            self.tokenizer.advance()
            symbol = ET.SubElement(let,'symbol')
            symbol.text=self.tokenizer.symbol()
        self.CompileExpression(let)
        # ;
        self.tokenizer.advance()
        symbol_end = ET.SubElement(let, "symbol")
        symbol_end.text = self.tokenizer.symbol()

    def CompileIf(self, Element):
        iF = ET.SubElement(Element, "ifStatement")
        keyword_if=ET.SubElement(iF,'keyword')
        keyword_if.text=self.tokenizer.keyword()
        while self.tokenizer.hasMoreCommands():
            self.tokenizer.advance()
            if (
                self.tokenizer.tokenType() == "symbol"
                and self.tokenizer.current_token == "("
            ):
                symbol_left = ET.SubElement(iF, "symbol")
                symbol_left.text = self.tokenizer.symbol()
                self.CompileExpression(iF)
            elif (
                self.tokenizer.tokenType() == "symbol"
                and self.tokenizer.current_token == ")"
            ):
                symbol_right = ET.SubElement(iF, "symbol")
                symbol_right.text = self.tokenizer.symbol()
            elif (
                self.tokenizer.tokenType() == "symbol"
                and self.tokenizer.current_token == "{"
            ):
                symbol_left = ET.SubElement(iF, "symbol")
                symbol_left.text = self.tokenizer.symbol()
                self.CompileStatements(iF)
            elif (
                self.tokenizer.tokenType() == "symbol"
                and self.tokenizer.current_token == "}"
            ):
                symbol_right = ET.SubElement(iF, "symbol")
                symbol_right.text = self.tokenizer.symbol()
                break
        # (else {statements}) ?
        self.tokenizer.advance()
        if (
            self.tokenizer.tokenType() == "keyword"
            and self.tokenizer.current_token == "else"
        ):
            keyword_else=ET.SubElement(iF,'keyword')
            keyword_else.text=self.tokenizer.keyword()
            # {
            self.tokenizer.advance()
            symbol_left = ET.SubElement(iF, "symbol")
            symbol_left.text = self.tokenizer.symbol()
            # expr
            self.CompileStatements(iF)
            # }
            self.tokenizer.advance()
            symbol_right = ET.SubElement(iF, "symbol")
            symbol_right.text = self.tokenizer.symbol()
        else:
            self.tokenizer.stepback()

    def CompileWhile(self, Element):
        wHILE = ET.SubElement(Element, "whileStatement")
        keyword_while=ET.SubElement(wHILE,'keyword')
        keyword_while.text=self.tokenizer.keyword()
            
        # (
        self.tokenizer.advance()
        symbol_left = ET.SubElement(wHILE, "symbol")
        symbol_left.text = self.tokenizer.symbol()
        # expression
        self.CompileExpression(wHILE)
        # )
        self.tokenizer.advance()
        symbol_ritht = ET.SubElement(wHILE, "symbol")
        symbol_ritht.text = self.tokenizer.symbol()
        # {
        self.tokenizer.advance()
        symbol_left = ET.SubElement(wHILE, "symbol")
        symbol_left.text = self.tokenizer.symbol()
        # statements
        self.CompileStatements(wHILE)
        # }
        self.tokenizer.advance()
        symbol_ritht = ET.SubElement(wHILE, "symbol")
        symbol_ritht.text = self.tokenizer.symbol()

    def CompileDo(self, Element):
        doStatememt = ET.SubElement(Element, "doStatement")
        keyword_do=ET.SubElement(doStatememt,'keyword')
        keyword_do.text=self.tokenizer.keyword()
        # subroutine call
        self.__parse_until(doStatememt, "(")
        # (
        symbol_left = ET.SubElement(doStatememt, "symbol")
        symbol_left.text = self.tokenizer.symbol()
        # expr
        self.CompileExpressionList(doStatememt)
        # )
        self.tokenizer.advance()
        symbol_right = ET.SubElement(doStatememt, "symbol")
        symbol_right.text = self.tokenizer.symbol()
        # ;
        self.tokenizer.advance()
        symbol_right = ET.SubElement(doStatememt, "symbol")
        symbol_right.text = self.tokenizer.symbol()


    def CompileReturn(self, Element):
        rETURN = ET.SubElement(Element,'returnStatement')
        keyword_return=ET.SubElement(rETURN,'keyword')
        keyword_return.text=self.tokenizer.keyword()
        if self.tokenizer.tokens[self.tokenizer.index+1] != ";":
            self.CompileExpression(rETURN)
        # ；
        self.tokenizer.advance()
        symbol=ET.SubElement(rETURN,'symbol')
        symbol.text=self.tokenizer.symbol()

    def CompileExpressionList(self, Element):
        # ExpressionList root
        expressionList = ET.SubElement(Element, "expressionList")
        # 强制不使用自闭合标签，textcompare比较使用，测试通过后可去掉
        expressionList.text='\n'
        # 处理无表达式情况
        if self.tokenizer.tokens[self.tokenizer.index+1] == ")":
            return
        self.CompileExpression(expressionList)
        while self.tokenizer.hasMoreCommands() and self.tokenizer.tokens[self.tokenizer.index+1]==',':
            self.tokenizer.advance()
            symbol_dot=ET.SubElement(expressionList,'symbol')
            symbol_dot.text=self.tokenizer.symbol()
            self.CompileExpression(expressionList)

    def CompileExpression(self, Element):
        # Expression root
        expression = ET.SubElement(Element, "expression")
        self.CompileTerm(expression)
        if self.tokenizer.tokens[self.tokenizer.index+1] in symbol_op: 
            self.tokenizer.advance()
            op =ET.SubElement(expression,'symbol')
            op.text=self.tokenizer.symbol()
            self.CompileTerm(expression)
        
    def CompileTerm(self, Element):
        # term root
        term=ET.SubElement(Element,'term')
        while self.tokenizer.hasMoreCommands():
            self.tokenizer.advance()
            # int val
            if self.tokenizer.tokenType()=='integerConstant':
                integer=ET.SubElement(term,'integerConstant')
                integer.text=str(self.tokenizer.intVal())
                break
            # str val
            elif self.tokenizer.tokenType()=='stringConstant':
                string=ET.SubElement(term,'stringConstant')
                string.text=self.tokenizer.stringVal()
                break
            # keyword const
            elif self.tokenizer.tokenType()=='keyword' and self.tokenizer.current_token in keyword_const:
                key_const=ET.SubElement(term,'keyword')
                key_const.text=self.tokenizer.keyword()
                break
            elif self.tokenizer.tokenType()=='identifier':
                ident=ET.SubElement(term,'identifier')
                ident.text=self.tokenizer.indentifier()
                self.tokenizer.advance()
                # array
                if self.tokenizer.tokenType()=='symbol' and self. tokenizer.current_token=='[':
                    self.tokenizer.stepback()
                    self.__CompileArray(term)
                # subroutinecall
                elif self.tokenizer.tokenType()=='symbol' and self. tokenizer.current_token in ('(','.'):
                    self.tokenizer.stepback()
                    self.__CompileSubCall(term)
                # varName
                else:
                    self.tokenizer.stepback()
                break
            # '('expression')'
            elif self.tokenizer.tokenType()=='symbol' and self.tokenizer.symbol()=='(':
                # (
                symbol=ET.SubElement(term,'symbol')
                symbol.text=self.tokenizer.symbol()
                # expression
                self.CompileExpression(term)
                # )
                self.tokenizer.advance()
                symbol=ET.SubElement(term,'symbol')
                symbol.text=self.tokenizer.symbol()
                break
            # unaryop term
            elif self.tokenizer.tokenType()=='symbol' and self.tokenizer.symbol() in unaryOP:
                # - ~
                unaryop=ET.SubElement(term,'symbol')
                unaryop.text=self.tokenizer.symbol()
                # term
                self.CompileTerm(term)
                break

    def __parse_until(self, rootElem, end):
        while self.tokenizer.hasMoreCommands():
            self.tokenizer.advance()
            if self.tokenizer.current_token == end:
                break
            if self.tokenizer.tokenType() == "keyword":
                keyword = ET.SubElement(rootElem, "keyword")
                keyword.text = self.tokenizer.keyword()
            elif self.tokenizer.tokenType() == "symbol":
                symbol = ET.SubElement(rootElem, "symbol")
                symbol.text = self.tokenizer.symbol()
            elif self.tokenizer.tokenType() == "identifier":
                ident = ET.SubElement(rootElem, "identifier")
                ident.text = self.tokenizer.indentifier()
    
    def __CompileArray(self,Element):
        # [
        self.tokenizer.advance()
        symbol =ET.SubElement(Element,'symbol')
        symbol.text=self.tokenizer.symbol()
        # expression
        self.CompileExpression(Element)
        # ] 
        self.tokenizer.advance()
        symbol =ET.SubElement(Element,'symbol')
        symbol.text=self.tokenizer.symbol()


    def __CompileSubCall(self,Element):
        # . or (
        self.tokenizer.advance()
        symbol =ET.SubElement(Element,'symbol')
        symbol.text=self.tokenizer.symbol()
        if symbol.text =='.':
            # subroutineName
            self.tokenizer.advance()
            subName=ET.SubElement(Element,'identifier')
            subName.text=self.tokenizer.indentifier()
            # (
            self.tokenizer.advance()
            symbol=ET.SubElement(Element,'symbol')
            symbol.text=self.tokenizer.symbol()
        # expressionList
        self.CompileExpressionList(Element)
        # )
        self.tokenizer.advance()
        symbol=ET.SubElement(Element,'symbol')
        symbol.text=self.tokenizer.symbol()
