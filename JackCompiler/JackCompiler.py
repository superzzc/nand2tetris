#! /usr/bin/python3

from pathlib import Path
import sys
from pkg.CompilationEngine import CompilationEngine


def main():
    path = Path(sys.argv[1])
    if path.is_dir():
        jackfiles = [f for f in path.iterdir() if f.is_file() and f.suffix == ".jack"]
        for infile in jackfiles:
            outfile = infile.with_suffix(".vm")
            compiler = CompilationEngine(str(infile), str(outfile))
            compiler.CompileClass()

    elif path.is_file() and path.suffix == ".jack":
        infile = path
        outfile = infile.with_suffix(".vm")
        compiler = CompilationEngine(str(infile), str(outfile))
        compiler.CompileClass()

if __name__ == "__main__":
    main()
