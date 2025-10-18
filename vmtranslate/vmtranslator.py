#! /usr/bin/python3

import sys
from pathlib import Path
from pkg.parser import Parser
from pkg.codewriter import CodeWriter


def main():
    dest = Path(sys.argv[1])
    if dest.is_dir():
        for file in dest.iterdir():
            if Path(file).suffix == ".vm":
                full_path = file.absolute()
                encode_file(full_path)

    elif dest.is_file():
        encode_file(dest)


def encode_file(file):
    inputfile = file
    outputfile = file.with_suffix(".asm")
    p = Parser(inputfile)
    c = CodeWriter(outputfile)
    while p.hasMoreCommands():
        p.advance()
        cmd_type = p.commandType()
        if cmd_type == "C_ARITHMETIC":
            c.writeArithmetic(p.current_cmd)
        elif cmd_type == "C_PUSH" or cmd_type == "C_POP":
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
    c.close()


if __name__ == "__main__":
    main()
