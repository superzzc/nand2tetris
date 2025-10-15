#!/usr/bin/python3

from pkg.parser import Parser
from pkg.code import Code
from pkg.symboltable import SymbolTable

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
    symboltable=SymbolTable(inputfile)

    with open(outputfile, 'w') as outf:
        while p.hasMoreCommands():
            p.advance()
            if p.commandType()=='A_COMMAND':
                a_value_pattern = r'^@([0-9]+)$'
                a_var_pattern = r'^@(.+)$'
                value=re.match(a_value_pattern, p.current_command)
                var=re.match(a_var_pattern, p.current_command)
                if value:   
                    a_instruction = '0' + format(int(value.group(1)), '015b')
                elif var:
                    var_label=var.group(1)
                    # 处理非预定义符号以及标签符号，即变量的情况
                    if var_label not in symboltable.symbols.keys():
                        symboltable.addEntry(var_label)
                    addr = symboltable.getAddress(var_label)
                    a_instruction = '0' + format(addr, '015b')
                outf.write(a_instruction + '\n') 

            elif p.commandType()=='C_COMMAND':
                # 111 ac1c2c3c4c5c6 d1d2d3 j1j2j3
                dest=p.dest()
                comp=p.comp()
                jump=p.jump()
                c_instruction = '111' + c.comp(comp) + c.dest(dest) + c.jump(jump)
                outf.write(c_instruction + '\n')

            elif p.commandType()=='L_COMMAND':
                # 预读阶段已经处理过标签符号，这里不需要做任何操作
                pass
            
            else:
                print(f"Error: Unknown command type for command '{p.current_command}'")
                continue

if __name__ == "__main__":
    main()