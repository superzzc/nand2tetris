#! /usr/bin/python3

import sys
import os
from pkg.parser import Parser
from pkg.codewriter import CodeWriter

def main():
    dest=sys.argv[1]
    if os.path.isdir(dest):
        pass
    elif os.path.isfile(dest):
        inputfile=dest
        outputfile=dest.replace('.vm','.asm')
        p=Parser(inputfile)
        c=CodeWriter(outputfile)
        while p.hasMoreCommands():
            p.advance()
            if p.commandType()=='C_ARITHMETIC':
                c.writeArithmetic(p.current_cmd)
            elif p.commandType()=='C_PUSH':
                c.writePushPop(p.current_cmd)


if __name__ == "__main__":
    main()