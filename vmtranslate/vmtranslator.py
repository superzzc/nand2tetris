#! /usr/bin/python3

import sys
import os
from pathlib import Path
from pkg.parser import Parser
from pkg.codewriter import CodeWriter

def main():
    dest=sys.argv[1]
    if os.path.isdir(dest):
        for file in os.listdir(dest):
            if Path(file).suffix == '.vm':
                full_path = os.path.join(dest,file)
                encode_file(full_path)
            
    elif os.path.isfile(dest):
        encode_file(dest)

def encode_file(file):
        inputfile=file
        outputfile=file.replace('.vm','.asm')
        p=Parser(inputfile)
        c=CodeWriter(outputfile)
        while p.hasMoreCommands():
            p.advance()
            cmd_type =p.commandType()
            if cmd_type=='C_ARITHMETIC':
                c.writeArithmetic(p.current_cmd)
            elif cmd_type=='C_PUSH' or cmd_type=='C_POP':
                c.writePushPop(cmd_type,p.arg1(),p.arg2())
        c.close()


if __name__ == "__main__":
    main()