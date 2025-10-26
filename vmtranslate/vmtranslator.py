#! /usr/bin/python3

import sys
from pathlib import Path
from pkg.parser import Parser
from pkg.codewriter import CodeWriter


def main():
    dest = Path(sys.argv[1])
    # 参数是路径时，将目录下的所有.vm编译到同一个.asm中
    if dest.is_dir():
        outputfile = dest.absolute() / f"{dest.name}.asm"
        c = CodeWriter(outputfile)
        for file in dest.iterdir():
            if Path(file).suffix == ".vm":
                full_path = file.absolute()
                encode_file(full_path, c)

    elif dest.is_file():
        outputfile = dest.with_suffix(".asm")
        c = CodeWriter(outputfile)
        encode_file(dest, c)
    c.close()


def encode_file(inputfile, c):
    p = Parser(inputfile)
    while p.hasMoreCommands():
        p.advance()
        cmd_type = p.commandType()
        if cmd_type == "C_ARITHMETIC":
            c.writeArithmetic(p.current_cmd)
        elif cmd_type == "C_PUSH" or cmd_type == "C_POP":
            c.setFileName(inputfile.stem)
            c.writePushPop(cmd_type, p.arg1(), p.arg2())
        elif cmd_type == "C_LABEL":
            c.writeLabel(p.arg1())
        elif cmd_type == "C_GOTO":
            c.writeGoto(p.arg1())
        elif cmd_type == "C_IF":
            c.writeIf(p.arg1())
        elif cmd_type == "C_FUNCTION":
            c.writeFunction(p.arg1(), p.arg2())
        elif cmd_type == "C_RETURN":
            c.writeReturn()
        elif cmd_type == "C_CALL":
            c.writeCall(p.arg1(), p.arg2())

if __name__ == "__main__":
    main()
