from pkg.config import p


class VMWriter:
    def __init__(self, outfile):
        self.fd = open(outfile, "w")

    def writePush(self, segment, index):
        self.fd.write(f"push {p[segment]} {index}\n")

    def writePop(self, segment, index):
        self.fd.write(f"pop {p[segment]} {index}\n")

    def writeArithmetic(self, command):
        self.fd.write(f"{command}\n")

    def writeLabel(self, label):
        self.fd.write(f"label {label}\n")

    def writeGoto(self, label):
        self.fd.write(f"goto {label}\n")

    def writeIf(self, label):
        self.fd.write(f"if-goto {label}\n")

    def writeCall(self, name, nArgs):
        self.fd.write(f"call {name} {nArgs}\n")

    def writeFunction(self, name, nArgs):
        self.fd.write(f"function {name} {nArgs}\n")

    def writeReturn(self):
        self.fd.write("return\n")

    def close(self):
        self.fd.close()
