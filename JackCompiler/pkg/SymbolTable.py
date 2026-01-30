from pkg.config import Kind


class SymbolTable:
    def __init__(self):
        """
        Docstring for __init__

        table entry {name:(type,kind,index)}
        """
        # static field arg var index
        self.index = [0, 0, 0, 0]
        self.classTable = {}
        self.subroutineTable = {}
        self.subroutineScope = False

    def startSubroutine(self):
        """
        重置subroutineTable为空,以及subroutine相关index计数
        """
        self.subroutineTable.clear()
        self.index[Kind.ARG] = 0
        self.index[Kind.VAR] = 0
        self.subroutineScope = True

    def define(self, name, type, kind):
        """
        新增一个条目到对应table中
        """
        if kind == Kind.STATIC or kind == Kind.FIELD:
            self.classTable[name] = (type, kind, self.index[kind])
            self.index[kind] += 1
        elif kind == Kind.ARG or kind == Kind.VAR:
            self.subroutineTable[name] = (type, kind, self.index[kind])
            self.index[kind] += 1

    def varCount(self, kind):
        """
        返回定义在当前作用域内的变量数量
        """
        return self.index[kind]

    def typeOf(self, name):
        """
        返回作用域内的标识符类型,查找失败返回None
        """
        return (
            self.subroutineTable[name][0]
            if name in self.subroutineTable
            else self.classTable[name][0] if name in self.classTable else None
        )

    def kindOf(self, name):
        """
        返回作用域内的标识符种类,查找失败返回None
        """
        return (
            self.subroutineTable[name][1]
            if name in self.subroutineTable
            else self.classTable[name][1] if name in self.classTable else None
        )

    def indexOf(self, name):
        """
        返回作用域内标识符索引,查找失败返回-1
        """
        return (
            self.subroutineTable[name][2]
            if name in self.subroutineTable
            else self.classTable[name][2] if name in self.classTable else -1
        )
