// push constant x
@7
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant x
@8
D=A
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

// push result to stack
@SP
A=M
M=D
@SP
M=M+1
