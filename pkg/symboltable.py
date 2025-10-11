
import re
class SymbolTable():
    l_command_pattern = r'^\(([A-Z]+)\)$'

    def __init__(self,inputfile):
        self.inputfile=inputfile
        self.var_address=16
        self.rom_address=0
        # 预定义符号
        self.symbols={
            "SP":0,
            "LCL":1,
            "ARG":2,
            "THIS":3,
            "THAT":4,
            "SCREEN":16384,
            "KBD":24576,
        }
        for i in range(16):
            self.symbols[f"R{i}"]=i
        # 预读处理标签符号
        self._preread()
        
    def contains(self,symbol):
        return symbol in self.symbols
    
    def getAddress(self,symbol):
        return self.symbols.get(symbol)
    
    def addEntry(self,symbol):
        '''
        向符号表中添加一个变量符号
        '''
        self.symbols[symbol]=self.var_address
        self.var_address += 1
    
    def _preread(self):
        '''
        预读一遍，向符号表中添加标签符号
        '''
        with open(self.inputfile,'r') as f:
            for line in f.readlines():
                line = re.split(r'#|//',line)[0].strip()
                # 跳过注释行和空行
                if line == '':
                    continue
                # 匹配L_COMMAND
                match=re.match(SymbolTable.l_command_pattern,line)
                if match:
                    label=match.group(1)
                    if label not in self.symbols:
                        self.symbols[label]=self.rom_address
                self.rom_address += 1





    
