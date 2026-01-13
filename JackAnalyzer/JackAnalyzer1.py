#! /usr/bin/python3
import sys
from pathlib import Path
from pkg.JackTokenizer import JackTokenizer
import xml.etree.ElementTree as ET


def main():
    dest = Path(sys.argv[1])
    current_dir= dest if dest.is_dir() else dest.parent
    outdir=current_dir/"outXML"
    if not outdir.exists():
        outdir.mkdir()
    # print(dest.resolve())
    input_list = []
    if dest.is_dir():
        input_list = [str(f.resolve()) for f in dest.iterdir() if f.is_file() and f.suffix=='.jack']

    elif dest.is_file() and dest.suffix=='.jack':
        input_list.append(str(dest.resolve()))
    
    for infile in input_list:
        outfile = outdir/Path(infile).with_suffix(".xml").name
        tokens = ET.Element("tokens")
        tokenizer=JackTokenizer(infile)
        while tokenizer.hasMoreCommands():
            tokenizer.advance()
            subelement=ET.SubElement(tokens,tokenizer.tokenType())
            if tokenizer.tokenType()=='keyword':
                subelement.text=tokenizer.keyword()
            elif tokenizer.tokenType()=='identifier':
                subelement.text=tokenizer.indentifier()
            elif tokenizer.tokenType()=='symbol':
                subelement.text=tokenizer.symbol()     # ElementTree 可以自动处理转义，< > & 不用手动处理
            elif tokenizer.tokenType()=='integerConstant':
                subelement.text=str(tokenizer.intVal())
            elif tokenizer.tokenType()=='stringConstant':
                subelement.text=tokenizer.stringVal()
        token_tree = ET.ElementTree(tokens)
        ET.indent(token_tree,space='\t',level=0)
        
        token_tree.write(outfile,encoding='utf-8',xml_declaration=False)

if __name__=='__main__':
    main()  
