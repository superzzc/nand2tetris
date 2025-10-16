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
@EQ.0
D;JEQ.0
@NEQ.0
0;JMP
(EQ.0)
@0
D=!A
@GOTO.0
0;JMP
(NEQ.0)
@0
D=A
(GOTO.0)

// push result to stack
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
@EQ.1
D;JEQ.1
@NEQ.1
0;JMP
(EQ.1)
@0
D=!A
@GOTO.1
0;JMP
(NEQ.1)
@0
D=A
(GOTO.1)

// push result to stack
@SP
A=M
M=D
@SP
M=M+1
