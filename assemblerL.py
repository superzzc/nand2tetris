#!/usr/bin/python3

from pkg.parser import Parser
from pkg.code import Code

import re
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python nosymbol-assemble.py <inputfile>")
        return
    inputfile = sys.argv[1]
    outputfile = inputfile.replace('.asm', '.hack')
    p=Parser(inputfile)
    c=Code()
    with open(outputfile, 'w') as outf:
        while p.hasMoreCommands():
            p.advance()
            if p.commandType()=='A_COMMAND':
                # @value, assert value is a number
                a_value_pattern = r'^@([0-9]+)$'
                value=re.match(a_value_pattern, p.current_command).group(1)
                a_instruction = '0' + format(int(value), '015b')
                outf.write(a_instruction + '\n')
            elif p.commandType()=='C_COMMAND':
                # 111 ac1c2c3c4c5c6 d1d2d3 j1j2j3
                dest=p.dest()
                comp=p.comp()
                jump=p.jump()
                c_instruction = '111' + c.comp(comp) + c.dest(dest) + c.jump(jump)
                outf.write(c_instruction + '\n')
            elif p.commandType()=='L_COMMAND':
                # 暂不处理
                pass
            else:
                print(f"Error: Unknown command type for command '{p.current_command}'")
                continue

if __name__ == "__main__":
    main()