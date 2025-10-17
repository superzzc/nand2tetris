
// push constant x
@111
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant x
@333
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant x
@888
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop static 8

// pop value to D reg
@SP
M=M-1
A=M
D=M

@tmp.0
M=D
// M[static[8]]
@StaticTest.asm.8
D=M
@0
D=D+A
@addr.0
M=D
@tmp.0
D=M
@addr.0
A=M
M=D
// pop static 3

// pop value to D reg
@SP
M=M-1
A=M
D=M

@tmp.1
M=D
// M[static[3]]
@StaticTest.asm.3
D=M
@0
D=D+A
@addr.1
M=D
@tmp.1
D=M
@addr.1
A=M
M=D
// pop static 1

// pop value to D reg
@SP
M=M-1
A=M
D=M

@tmp.2
M=D
// M[static[1]]
@StaticTest.asm.1
D=M
@0
D=D+A
@addr.2
M=D
@tmp.2
D=M
@addr.2
A=M
M=D

// push static 3
// M[static[3]]
@StaticTest.asm.3
D=M
@0
A=D+A
D=M

// push D reg value to stack
@SP
A=M
M=D
@SP
M=M+1

// push static 1
// M[static[1]]
@StaticTest.asm.1
D=M
@0
A=D+A
D=M

// push D reg value to stack
@SP
A=M
M=D
@SP
M=M+1

// pop from stack to get 2 ops
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
M=M-D
D=M

// push D reg value to stack
@SP
A=M
M=D
@SP
M=M+1

// push static 8
// M[static[8]]
@StaticTest.asm.8
D=M
@0
A=D+A
D=M

// push D reg value to stack
@SP
A=M
M=D
@SP
M=M+1

// pop from stack to get 2 ops
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
M=M+D
D=M

// push D reg value to stack
@SP
A=M
M=D
@SP
M=M+1
