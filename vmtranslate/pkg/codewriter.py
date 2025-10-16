from textwrap import dedent

class CodeWriter():
    def __init__(self, outfile):
        self.outfile=outfile
        self.fd=open(self.outfile,'w')

    def writeArithmetic(self,arit_cmd):
        '''
        将算数操作翻译为汇编命令写到文件
        共7个算数操作命令:add sub and or neg not eq gt lt
        隐式操作stack
        '''
        ops2_map={
            'add':'+',
            'sub':'-',
            'and':'&',
            'or':'|'
        }
        ops1_map={
            'not':'!',
            'neg':'-'
        }
        ops_cmp=('eq','lt','gt')
        if arit_cmd in ops2_map.keys():
            self._write_2ops(ops2_map[arit_cmd])
        elif arit_cmd in ops1_map.keys():
            self._write_1ops(ops1_map[arit_cmd])
        elif arit_cmd in ops_cmp:
            self._write_cmpops(arit_cmd)
        

    def writePushPop(self,stack_cmd):
        '''
        将push、pop操作翻译为汇编写到文件
        push segment index 将segment[index]压入stack
        pop segment index 将segment[index]弹出stack
        '''
        # stage 1: 先实现push constant x命令
        cmds=stack_cmd.split()
        if cmds[0] == 'push':
            if cmds[1] == 'constant':
                x = cmds[2]
                self.fd.writelines((
                    '// push constant x\n',
                    f'@{x}\n',
                    'D=A\n',
                    '@SP\n',
                    'A=M\n',
                    'M=D\n'
                    '@SP\n',
                    'M=M+1\n',
                    '\n'
                )) 
        elif cmds[0] == 'pop':
            pass
    
    def close(self):
        '''
        显式关闭outIO
        '''
        self.fd.close()
    
    def _get2ops(self,opcode):
         # 获取两个操作数并运算
        asm=f'''
        // pop from stack to get 2 ops
        @SP
        M=M-1
        A=M
        D=M
        @SP
        M=M-1
        A=M
        M=M{opcode}D
        D=M
        '''
        asm=dedent(asm)
        return asm
    
    def _get1ops(self,opcode):
        # 获取一个操作数,并运算
        asm=f'''
        // pop from stack to get 1 ops
        @SP
        M=M-1
        A=M
        D=M
        D={opcode}D
        '''
        asm=dedent(asm)
        return asm
    
    def _push(self):
        # 结果入栈操作
        asm='''
        // push result to stack
        @SP
        A=M
        M=D
        @SP
        M=M+1
        '''
        asm=dedent(asm)
        return asm
    
    def _write_2ops(self,opcode):
        asm_1 = self._get2ops(opcode)
        asm_2=self._push()
        self.fd.write(asm_1+asm_2)

    def _write_1ops(self,opcode):
        asm_1=self._get1ops(opcode)
        asm_2=self._push()
        self.fd.write(asm_1+asm_2)
    
    def _write_cmpops(self,opcode):
        # sub x,y
        asm_1=self._get2ops('-')
        # 
        op=opcode.upper()
        asm_2=f'''
        // eq/gt/lt
        @{op}
        D;J{op}
        @N{op}
        0;JMP
        ({op})
        @0
        D=!A
        @CONTINUE
        0;JMP
        (N{op})
        @0
        D=A
        (CONTINUE)
        '''
        asm_2=dedent(asm_2)
        asm_3=self._push()
        self.fd.write(asm_1+asm_2+asm_3)

    def _write_pop(self):
        '''
        生成对应pop命令的汇编指令
        '''

        
    def _write_push(self):
         '''
        生成push命令的汇编指令
        '''