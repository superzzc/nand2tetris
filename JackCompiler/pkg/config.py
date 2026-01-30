from enum import IntEnum

class Kind(IntEnum):
    STATIC=0
    FIELD=1
    ARG=2
    VAR=3

class Seg(IntEnum):
    CONST=0
    ARG=1
    LOCAL=2
    STATIC=3
    THIS=4
    THAT=5
    POINTER=6
    TEMP=7

p=('constant','argument','local','static','this','that','pointer','temp')
k={'static':Kind.STATIC,'field':Kind.FIELD,'var':Kind.VAR}

op_map = {
    '+': 'add',
    '-': 'sub',  
    '=': 'eq',
    '>': 'gt',
    '<': 'lt',
    '&': 'and',
    '|': 'or',
    '~': 'not'
}

var_map={Kind.STATIC:Seg.STATIC,Kind.FIELD:Seg.THIS,Kind.ARG:Seg.ARG,Kind.VAR:Seg.LOCAL}