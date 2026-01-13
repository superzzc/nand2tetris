from pkg.config import token_pattern,p_string,p_identifier,p_int,p_keyword,p_symbol
import re


class JackTokenizer:
    def __init__(self, inputfile):
        # 读取源文件，跳过注释并按空白拆分成字元
        with open(inputfile, "r") as f:
            code = f.read()
        lines = self.__remove_comment(code)
        # print(lines)
        self.tokens = re.findall(token_pattern, lines)  
        self.current_token = None
        self.index = -1
        # debug only
        # print(self.tokens)

    def hasMoreCommands(self):
        """
        如果输入中还有更多的命令，则返回真，否则返回假
        """
        return self.index < len(self.tokens)-1

    def advance(self):
        """
        从输入中读取下一条命令，将其指定为当前命令
        """
        self.index += 1
        self.current_token = self.tokens[self.index]

    def tokenType(self):
        if re.match(p_keyword,self.current_token):
            return "keyword"
        elif re.match(p_symbol,self.current_token):
            return "symbol"
        elif re.match(p_identifier, self.current_token):
            return "identifier"
        elif re.match(p_string, self.current_token):
            return "stringConstant"
        elif re.match(p_int,self.current_token) and  0 <= int(self.current_token) and int(self.current_token) <= 32767:
            return "integerConstant"

    def keyword(self):
        return self.current_token

    def symbol(self):
        return self.current_token

    def indentifier(self):
        return self.current_token

    def intVal(self):
        return int(self.current_token)

    # 返回字符串值，没有双引号
    def stringVal(self):

        pattern = re.compile(r'^"(.*)"$')
        return pattern.sub(r"\1", self.current_token)

    def __remove_comment(self, code):
        pattern = re.compile(
            r"""
        //.*?$           |   # 单行注释
        /\*[\s\S]*?\*/       # 块注释或文档注释
        """,
            re.MULTILINE | re.VERBOSE,
        )

        # 替换匹配到的注释为空字符串
        code_no_comments = pattern.sub("", code)

        # 去掉每行首尾空格，并删除空行
        lines = [line.strip() for line in code_no_comments.splitlines()]
        return "\n".join(line for line in lines if line)
