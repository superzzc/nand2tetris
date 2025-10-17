
// push constant x
@3030
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop pointer 0

// pop value to D reg
@SP
M=M-1
A=M
D=M

@tmp.11
M=D
// M[pointer[0]]
@3
D=A
@0
D=D+A
@addr.11
M=D
@tmp.11
D=M
@addr.11
A=M
M=D

// push constant x
@3040
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop pointer 1

// pop value to D reg
@SP
M=M-1
A=M
D=M

@tmp.12
M=D
// M[pointer[1]]
@3
D=A
@1
D=D+A
@addr.12
M=D
@tmp.12
D=M
@addr.12
A=M
M=D

// push constant x
@32
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop this 2

// pop value to D reg
@SP
M=M-1
A=M
D=M

@tmp.13
M=D
// M[this[2]]
@THIS
D=M
@2
D=D+A
@addr.13
M=D
@tmp.13
D=M
@addr.13
A=M
M=D

// push constant x
@46
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop that 6

// pop value to D reg
@SP
M=M-1
A=M
D=M

@tmp.14
M=D
// M[that[6]]
@THAT
D=M
@6
D=D+A
@addr.14
M=D
@tmp.14
D=M
@addr.14
A=M
M=D

// push pointer 0
// M[pointer[0]]
@3
D=A
@0
A=D+A
D=M

// push D reg value to stack
@SP
A=M
M=D
@SP
M=M+1

// push pointer 1
// M[pointer[1]]
@3
D=A
@1
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

// push this 2
// M[this[2]]
@THIS
D=M
@2
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

// push that 6
// M[that[6]]
@THAT
D=M
@6
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
