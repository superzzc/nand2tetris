import re
from pkg.config import a_command_pattern, l_command_pattern, c_command_pattern

class Parser():

    def __init__(self,filename):
        self.file = open(filename, 'r')
        self.file.seek(0)
        self.current_command = None
    
    def hasMoreCommands(self):
        '''
        如果输入中还有更多的命令，则返回真，否则返回假
        '''
        current = self.file.tell()
        self.file.seek(0, 2)  # 移动到文件末尾
        end = self.file.tell()
        self.file.seek(current)  # 恢复原来的位置
        return current != end
        
    def advance(self):
        '''
        从输入中读取下一条命令，并使其成为当前命令
        仅当hasMoreCommands()为真时调用
        '''
        line = self.file.readline()
        # 去除注释和空白
        line = re.split(r'#|//', line)[0].strip()
        while line == '' and self.hasMoreCommands():
            line = self.file.readline()
            line = re.split(r'#|//', line)[0].strip()
        self.current_command = line

    def commandType(self):
        '''
        返回当前命令的类型
        A_COMMAND, @xxx
        C_COMMAND, dest=comp;jump/dest=comp/comp
        L_COMMAND中的一个,(XXX) 例如(LOOP)
        '''
        if re.match(a_command_pattern, self.current_command):
            return 'A_COMMAND'
        elif re.match(l_command_pattern, self.current_command):
            return 'L_COMMAND'
        elif re.match(c_command_pattern, self.current_command):
            return 'C_COMMAND'
        else:
            return 'UNKNOWN_COMMAND'

    def symbol(self):
        '''
        返回当前命令的符号或十进制数
        仅当commandType()为A_COMMAND或L_COMMAND时调用
        '''
        pass

    def dest(self):
        '''
        返回当前C_COMMAND的dest部分
        仅当commandType()为C_COMMAND时调用
        '''
        match = re.match(c_command_pattern, self.current_command)
        if match:
            return match.group(1) if match.group(1) else 'null'

    def comp(self):
        '''
        返回当前C_COMMAND的comp部分
        仅当commandType()为C_COMMAND时调用
        '''
        match = re.match(c_command_pattern, self.current_command)
        if match:
            return match.group(2) if match.group(2) else 'null'

    def jump(self):
        '''
        返回当前C_COMMAND的jump部分
        仅当commandType()为C_COMMAND时调用
        '''
        match = re.match(c_command_pattern, self.current_command)
        if match:
            return match.group(3) if match.group(3) else 'null'

    def __del__(self):
        self.file.close()
