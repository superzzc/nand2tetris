#! /usr/bin/python3
import sys
from pathlib import Path
from pkg.CompilationEngine import CompilationEngine


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
        comp_engine=CompilationEngine(infile)
        comp_engine.classTree.write(outfile,encoding='utf-8',xml_declaration=False)

if __name__=='__main__':
    main()  
