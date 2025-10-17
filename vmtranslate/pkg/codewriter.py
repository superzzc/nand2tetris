from textwrap import dedent
import os

class CodeWriter():
    label_count=0
    var_count=0
    _instance = None

    # 使用单例
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
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
        

    def writePushPop(self,cmd_type,segment,index):
        '''
        将push、pop操作翻译为汇编写到文件
        push segment index 将segment[index]压入stack
        pop segment index 将segment[index]弹出stack
        '''
        mem2reg = {
            'argument':'ARG',
            'local':'LCL',
            'this':'THIS',
            'that':'THAT',
            'temp':5,
            'pointer':3,
            'static':'NULL'
        }
        filename=os.path.basename(self.outfile)
        if cmd_type == 'C_PUSH':
            # stage 1: 实现push constant x命令
            if segment == 'constant':
                x = index
                asm = f'''
                // push constant x
                @{x}
                D=A
                @SP
                A=M
                M=D
                @SP
                M=M+1
                '''
                asm = dedent(asm)
                self.fd.write(asm)

            # stage 2: 实现剩余内存段的处理
            # local arg this that temp pointer 
            elif segment in mem2reg.keys():
                reg = mem2reg[segment]
                asm_1=f'''
                // push {segment} {index}
                // M[{segment}[{index}]]
                @{reg if reg !='NULL' else f'{filename}.{index}'}
                D={'M' if segment not in ('temp','pointer')  else 'A'}
                @{index if reg!='NULL' else 0}
                A=D+A
                D=M
                '''
                asm_1=dedent(asm_1)
                asm_2=self._push()
                self.fd.write(asm_1+asm_2)

        elif cmd_type == 'C_POP':
            asm_1=f'// pop {segment} {index}\n'
            asm_2=self._pop()
            # local arg this that temp pointer
            if segment in mem2reg.keys():
                reg = mem2reg[segment]
                asm_3=f'''
                @tmp.{CodeWriter.var_count}
                M=D
                // M[{segment}[{index}]]
                @{reg if reg !='NULL' else f'{filename}.{index}'}
                D={'M' if segment not in ('temp','pointer')  else 'A'}
                @{index if reg!='NULL' else 0}
                D=D+A
                @addr.{CodeWriter.var_count}
                M=D
                @tmp.{CodeWriter.var_count}
                D=M
                @addr.{CodeWriter.var_count}
                A=M
                M=D
                '''
                asm_3=dedent(asm_3)
                self.fd.write(asm_1+asm_2+asm_3)
                CodeWriter.var_count += 1
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
        # D reg 入栈操作
        asm='''
        // push D reg value to stack
        @SP
        A=M
        M=D
        @SP
        M=M+1
        '''
        asm=dedent(asm)
        return asm
    
    def _pop(self): 
        # 出栈操作 D reg
        asm='''
        // pop value to D reg
        @SP
        M=M-1
        A=M
        D=M
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
        @{op}.{CodeWriter.label_count}
        D;J{op}
        @N{op}.{CodeWriter.label_count}
        0;JMP
        ({op}.{CodeWriter.label_count})
        @0
        D=!A
        @GOTO.{CodeWriter.label_count}
        0;JMP
        (N{op}.{CodeWriter.label_count})
        @0
        D=A
        (GOTO.{CodeWriter.label_count})
        '''
        asm_2=dedent(asm_2)
        asm_3=self._push()
        self.fd.write(asm_1+asm_2+asm_3)
        CodeWriter.label_count += 1