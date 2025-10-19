from textwrap import dedent
import os


class CodeWriter:
    label_count = 0
    var_count = 0
    return_count = 0
    call_count = 0
    _instance = None

    # 使用单例
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, outfile):
        self.outfile = outfile
        self.fd = open(self.outfile, "w")
        self._boottrap()

    def writeArithmetic(self, arit_cmd):
        """
        将算数操作翻译为汇编命令写到文件
        共7个算数操作命令:add sub and or neg not eq gt lt
        隐式操作stack
        """
        ops2_map = {"add": "+", "sub": "-", "and": "&", "or": "|"}
        ops1_map = {"not": "!", "neg": "-"}
        ops_cmp = ("eq", "lt", "gt")
        if arit_cmd in ops2_map.keys():
            self._write_2ops(ops2_map[arit_cmd])
        elif arit_cmd in ops1_map.keys():
            self._write_1ops(ops1_map[arit_cmd])
        elif arit_cmd in ops_cmp:
            self._write_cmpops(arit_cmd)

    def writePushPop(self, cmd_type, segment, index):
        """
        将push、pop操作翻译为汇编写到文件
        push segment index 将segment[index]压入stack
        pop segment index 将segment[index]弹出stack
        """
        mem2reg = {
            "argument": "ARG",
            "local": "LCL",
            "this": "THIS",
            "that": "THAT",
            "temp": 5,
            "pointer": 3,
            "static": "NULL",
        }
        filename = os.path.basename(self.outfile)
        if cmd_type == "C_PUSH":
            # stage 1: 实现push constant x命令
            if segment == "constant":
                x = index
                asm = f"""
                // push constant x
                @{x}
                D=A
                @SP
                A=M
                M=D
                @SP
                M=M+1
                """
                asm = dedent(asm)
                self.fd.write(asm)

            # stage 2: 实现剩余内存段的处理
            # local arg this that temp pointer
            elif segment in mem2reg.keys():
                reg = mem2reg[segment]
                asm_1 = f"""
                // push {segment} {index}
                // M[{segment}[{index}]]
                @{reg if reg !='NULL' else f'{filename}.{index}'}
                D={'M' if segment not in ('temp','pointer')  else 'A'}
                @{index if reg!='NULL' else 0}
                A=D+A
                D=M
                """
                asm_1 = dedent(asm_1)
                asm_2 = self._push()
                self.fd.write(asm_1 + asm_2)

        elif cmd_type == "C_POP":
            asm_1 = f"// pop {segment} {index}\n"
            asm_2 = self._pop()
            # local arg this that temp pointer
            if segment in mem2reg.keys():
                reg = mem2reg[segment]
                asm_3 = f"""
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
                """
                asm_3 = dedent(asm_3)
                self.fd.write(asm_1 + asm_2 + asm_3)
                CodeWriter.var_count += 1
            pass

    def writeLabel(self, label):
        """
        生成label xxx对应的asm
        """
        asm = f"""
        ({label})
        """
        asm = dedent(asm)
        self.fd.write(asm)

    def writeGoto(self, label):
        """
        生成goto对应的asm
        """
        asm = f"""
        @{label}
        0;JMP
        """
        asm = dedent(asm)
        self.fd.write(asm)

    def writeIf(self, label):
        """
        生成if-goto对应的asm
        """
        asm_1 = self._pop()
        asm_2 = f"""
        @{label}
        D;JNE
        """
        asm_2 = dedent(asm_2)
        self.fd.write(asm_1 + asm_2)

    def writeFunction(self, funcName, numArgs):
        """
        生成function f k 對應的asm
        """
        asm = f"({funcName})\n"
        for _ in range(int(numArgs)):
            asm_1 = """
            @0
            D=A
            """
            asm_1 = dedent(asm_1)
            asm_1 += self._push()
            asm += asm_1
        self.fd.write(asm)

    def writeReturn(self):
        """
        生成return 对应的asm
        """
        # 获取返回地址
        asm_1 = f"""
        // get return addr
        @LCL
        D=M
        @5
        D=D-A
        @return_addr.{CodeWriter.return_count}
        M=D
        """
        asm_1 = dedent(asm_1)
        # 将返回值压入arg段底部
        asm_2 = self._pop()
        asm_3 = f"""
        // set return value to argument[0]
        @ARG
        A=M
        M=D
        // reset call stack
        @ARG
        D=M
        D=D+1
        @SP
        M=D
        """
        asm_3 = dedent(asm_3)
        # 恢复调用者的寄存器
        asm_4 = self._reset_reg()
        # 跳转到返回地址继续执行
        asm_5 = f"""
        @return_addr.{CodeWriter.return_count}
        A=M
        0;JMP
        """
        asm_5 = dedent(asm_5)
        self.fd.write(asm_1 + asm_2 + asm_3 + asm_4 + asm_5)
        CodeWriter.return_count += 1

    def writeCall(self, funcName, numArgs):
        """
        生成call对应的asm
        """
        asm_1 = f"""
        // call {funcName} {numArgs}
        @return_{funcName}.{CodeWriter.call_count}
        D=A
        """
        asm_1 = dedent(asm_1)
        # 将返回地址入栈
        asm_2 = self._push()
        # 将调用者的寄存器变量入栈
        asm_3 = self._save_reg()
        # 设置ARG及LCL
        asm_4 = f"""
        @SP
        D=M
        @{5+int(numArgs)}
        D=D-A
        @ARG
        M=D
        @SP
        D=M
        @LCL
        M=D
        """
        asm_4 = dedent(asm_4)
        self.fd.write(asm_1 + asm_2 + asm_3 + asm_4)
        # 控制流跳转
        self.writeGoto(funcName)
        # 返回地址标签
        self.fd.write(f"(return_{funcName}.{CodeWriter.call_count})\n")
        # for debug info
        self.fd.write(f"// end of call {funcName} {numArgs} translation\n")
        # 更新count，确保标签唯一
        CodeWriter.call_count += 1

    def close(self):
        """
        显式关闭outIO
        """
        self.fd.close()

    def _get2ops(self, opcode):
        # 获取两个操作数并运算
        asm = f"""
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
        """
        asm = dedent(asm)
        return asm

    def _get1ops(self, opcode):
        # 获取一个操作数,并运算
        asm = f"""
        // pop from stack to get 1 ops
        @SP
        M=M-1
        A=M
        D=M
        D={opcode}D
        """
        asm = dedent(asm)
        return asm

    def _push(self):
        # D reg 入栈操作
        asm = """
        // push D reg value to stack
        @SP
        A=M
        M=D
        @SP
        M=M+1
        """
        asm = dedent(asm)
        return asm

    def _pop(self):
        # 出栈操作 D reg
        asm = """
        // pop value to D reg
        @SP
        M=M-1
        A=M
        D=M
        """
        asm = dedent(asm)
        return asm

    def _write_2ops(self, opcode):
        asm_1 = self._get2ops(opcode)
        asm_2 = self._push()
        self.fd.write(asm_1 + asm_2)

    def _write_1ops(self, opcode):
        asm_1 = self._get1ops(opcode)
        asm_2 = self._push()
        self.fd.write(asm_1 + asm_2)

    def _write_cmpops(self, opcode):
        # sub x,y
        asm_1 = self._get2ops("-")
        #
        op = opcode.upper()
        asm_2 = f"""
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
        """
        asm_2 = dedent(asm_2)
        asm_3 = self._push()
        self.fd.write(asm_1 + asm_2 + asm_3)
        CodeWriter.label_count += 1

    def _save_reg(self):
        """
        函数调用时，将调用者的寄存器值保存到栈上
        """
        reg_list = ["LCL", "ARG", "THIS", "THAT"]
        asm = ""
        for i in range(len(reg_list)):
            asm_1 = f"""
            @{reg_list[i]}
            D=M
            """
            asm_1 = dedent(asm_1)
            asm_2 = self._push()
            asm += asm_1 + asm_2
        return asm

    def _reset_reg(self):
        """
        函数返回时，从栈上还原保存的寄存器值
        """
        reg_list = ["LCL", "ARG", "THIS", "THAT"]
        asm = ""
        for i in range(len(reg_list)):
            asm_1 = f"""
            // reset {reg_list[i]} from stack
            @return_addr.{CodeWriter.return_count}
            D=M
            @{i+1}
            A=D+A
            D=M
            @{reg_list[i]}
            M=D
            """
            asm += asm_1
        asm = dedent(asm)
        return asm

    def _boottrap(self):
        """
        生成vm引导程序对应的asm
        """
        asm_1 = f"""
        // init SP point to RAM[256]
        @256
        D=A
        @SP
        M=D
        """
        asm_1 = dedent(asm_1)
        self.fd.write(asm_1)
        self.writeCall("Sys.init", 0)
        # Sys.init will never return
