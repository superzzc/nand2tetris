from nandtotetris.JackAnalyzer.pkg.JackTokenizer import JackTokenizer
from pkg.config import symbol_op
import xml.etree.ElementTree as ET


class CompilationEngine():
    def __init__(self,inputfile,outputfile):
        self.outfile=outputfile
        self.tokenizer=JackTokenizer(inputfile)
        # 假定tokenizer中tokens列表中的第一个字元一定是class
        self.CompileClass()
    
    def CompileClass(self):
        # class root
        Class = ET.Element("class")
        self.__read_until(Class,'{')
        # {
        symbol_left=ET.SubElement(Class,'symbol')
        symbol_left.text=self.tokenizer.symbol()
        
        ### 如何处理多个类变量声明 ？ 
        self.CompileClassVarDec(Class)
        
        self.CompileSubroutine(Class)

        # }
        symbol_right=ET.SubElement(Class,'symbol')
        symbol_right.text=self.tokenizer.symbol()

        # 整体写入XML
        tree=ET.ElementTree(Class)
        tree.write(self.outfile,encoding='utf-8',xml_declaration=False)

    def CompileClassVarDec(self,Element):
        # classVarDec root
        classVarDec = ET.SubElement(Element,"classVarDec")
        self.__read_until(classVarDec,';')
        symbol_end=ET.SubElement(classVarDec,'symbol')
        symbol_end.text=self.tokenizer.symbol()

    def CompileSubroutine(self,Element):
        # subroutineDec root
        subDec=ET.SubElement(Element,'subroutineDec')
        # 处理方法声明部分
        self.__read_until(subDec,'(')

        symbol_leftslash=ET.SubElement(subDec,'symbol')
        symbol_leftslash.text=self.tokenizer.symbol()
        self.CompileParameterList(subDec)
        symbol_rightslash=ET.SubElement(subDec,'symbol')
        symbol_rightslash.text=self.tokenizer.symbol()
        self.CompileSubroutineBody(subDec)
        
    def CompileParameterList(self,Element):
        # ParameterList root
        paraList=ET.SubElement(Element,'parameterList')
        self.__read_until(paraList,')')
 
    def CompileSubroutineBody(self,Element):
        # SubroutineBody root
        subBody=ET.SubElement(Element,'subroutineBody')
        if self.tokenizer.hasMoreCommands():
            self.tokenizer.advance() 
        symbol_leftslash=ET.SubElement(subBody,'symbol')
        symbol_leftslash.text=self.tokenizer.symbol()

        self.CompileVarDec(subBody)
        self.CompileStatements(subBody)
        
        symbol_rightslash=ET.SubElement(subBody,'symbol')
        symbol_rightslash.text=self.tokenizer.symbol()


    def CompileVarDec(self,Element):
        # VarDec root
        VarDec = ET.SubElement(Element,'VarDec')
        self.__read_until(VarDec,';')
        # ;
        symbol = ET.SubElement(Element,'symbol')
        symbol.text=self.tokenizer.symbol()

    def CompileStatements():
        pass

    def CompileDo(self,Element):
        # do root
        doStatememt=ET.SubElement(Element,'doStatememt')
        self.__read_until(doStatememt,'(')
        # (
        symbol_left = ET.SubElement(doStatememt,'symbol')
        symbol_left.text=self.tokenizer.symbol()
        # expr
        self.CompileExpressionList(doStatememt)
        # )
        symbol_right = ET.SubElement(doStatememt,'symbol')
        symbol_right.text=self.tokenizer.symbol()
        

        pass

    def CompileLet():
        pass

    def CompileWhile():
        pass

    def CompileReturn():
        pass
    
    def CompileIf():
        pass
    
    def CompileExpressionList(self,Element):
        # ExpressionList root
        expressionList=ET.SubElement(Element,'expressionList')
        if self.tokenizer.hasMoreCommands():
            self.tokenizer.advance()
        while self.tokenizer.current_token != ')':
            # 期望CompileExpression正确处理,并在碰到,的时候返回
            self.CompileExpression(expressionList)
            symbol_dot=ET.SubElement(expressionList,'symbol')
            symbol_dot.text=','
            if self.tokenizer.hasMoreCommands():
                self.tokenizer.advance()
    
    def CompileExpression(self,Element):
        # Expression root
        expression=ET.SubElement(Element,'expression')
        self.CompileTerm(expression)
        # 增加是否存在op的判断条件
        if self.tokenizer.hasMoreCommands():
            self.tokenizer.advance()
        while self.tokenizer.current_token in symbol_op:
            op = ET.SubElement(expression,'symbol')
            op.text = self.tokenizer.symbol()
            self.CompileTerm(expression)
            if self.tokenizer.hasMoreCommands():
                self.tokenizer.advance()
    
    def CompileTerm():
        pass


    def __read_until(self,rootElem,end):
        if self.tokenizer.hasMoreCommands():
            self.tokenizer.advance() 
        while self.tokenizer.current_token != end:
            if self.tokenizer.tokenType()=='KEYWORD':
                keyword=ET.SubElement(rootElem,'keyword')
                keyword.text=self.tokenizer.keyword()
            if self.tokenizer.tokenType()=='SYMBOL':
                keyword=ET.SubElement(rootElem,'symbol')
                keyword.text=self.tokenizer.keyword()
            elif self.tokenizer.tokenType()=='IDENTIFIER':
                ident=ET.SubElement(rootElem,'identifier')
                ident.text=self.tokenizer.indentifier()
            if self.tokenizer.hasMoreCommands():
                self.tokenizer.advance() 




