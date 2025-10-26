
// push constant x
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant x
@17
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
M=M-D
D=M

// eq/gt/lt
@EQ.9
D;JEQ
@NEQ.9
0;JMP
(EQ.9)
@0
D=!A
@GOTO.9
0;JMP
(NEQ.9)
@0
D=A
(GOTO.9)

// push D reg value to stack
@SP
A=M
M=D
@SP
M=M+1

// push constant x
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant x
@16
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
M=M-D
D=M

// eq/gt/lt
@EQ.10
D;JEQ
@NEQ.10
0;JMP
(EQ.10)
@0
D=!A
@GOTO.10
0;JMP
(NEQ.10)
@0
D=A
(GOTO.10)

// push D reg value to stack
@SP
A=M
M=D
@SP
M=M+1
