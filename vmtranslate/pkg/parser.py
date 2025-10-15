from pkg.config import *
import re

class Parser():
    def __init__(self,inputfile):
        self.fd = open(inputfile,'r')
        self.fd.seek(0)
        self.current_cmd=None
    
    def hasMoreCommands(self):
        '''
        如果输入中还有更多的命令，则返回真，否则返回假
        '''
        current = self.fd.tell()
        self.fd.seek(0, 2)  # 移动到文件末尾
        end = self.fd.tell()
        self.fd.seek(current)  # 恢复原来的位置
        return current != end
    
    def advance(self):
        '''
        从输入中读取下一条命令，将其指定为当前命令
        '''
        while self.hasMoreCommands():
            line = self.fd.readline()
            line = re.split(r'#|//', line, 1)[0].strip()
            if line:
                break
        self.current_cmd = line

    def commandType(self):
        '''
        返回当前vm命令类型
        C_ARITHMETIC C_PUSH C_POP C_LABEL C_GOTO C_IF
        C_FUNCTION C_RETURN C_CALL
        '''
        # stage 1：实现算数与逻辑命令以及push constant x命令
        if  self.current_cmd in Arithmetic_label:
            return 'C_ARITHMETIC'
        elif self.current_cmd.split()[0] == 'push':
            return 'C_PUSH'
        elif self.current_cmd.split()[0] == 'pop':
            return 'C_POP'
        # stage 2:实现内存访问命令

    def arg1(self):
        '''
        返回当前命令的第一个参数,C_RETURN不允许调用
        '''
        return self.current_cmd.split()[0]
        
    
    def arg2(self):
        '''
        返回当前命令的第二个参数, C_PUSH C_POP C_FUNCTION C_CALL
        类型命令才允许调用
        '''
        return self.current_cmd.split()[1]
