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
D;JEQ
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
D;JEQ
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
// push constant x
@16
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
@EQ.2
D;JEQ
@NEQ.2
0;JMP
(EQ.2)
@0
D=!A
@GOTO.2
0;JMP
(NEQ.2)
@0
D=A
(GOTO.2)

// push result to stack
@SP
A=M
M=D
@SP
M=M+1
// push constant x
@892
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant x
@891
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
@LT.3
D;JLT
@NLT.3
0;JMP
(LT.3)
@0
D=!A
@GOTO.3
0;JMP
(NLT.3)
@0
D=A
(GOTO.3)

// push result to stack
@SP
A=M
M=D
@SP
M=M+1
// push constant x
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant x
@892
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
@LT.4
D;JLT
@NLT.4
0;JMP
(LT.4)
@0
D=!A
@GOTO.4
0;JMP
(NLT.4)
@0
D=A
(GOTO.4)

// push result to stack
@SP
A=M
M=D
@SP
M=M+1
// push constant x
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant x
@891
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
@LT.5
D;JLT
@NLT.5
0;JMP
(LT.5)
@0
D=!A
@GOTO.5
0;JMP
(NLT.5)
@0
D=A
(GOTO.5)

// push result to stack
@SP
A=M
M=D
@SP
M=M+1
// push constant x
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant x
@32766
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
@GT.6
D;JGT
@NGT.6
0;JMP
(GT.6)
@0
D=!A
@GOTO.6
0;JMP
(NGT.6)
@0
D=A
(GOTO.6)

// push result to stack
@SP
A=M
M=D
@SP
M=M+1
// push constant x
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant x
@32767
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
@GT.7
D;JGT
@NGT.7
0;JMP
(GT.7)
@0
D=!A
@GOTO.7
0;JMP
(NGT.7)
@0
D=A
(GOTO.7)

// push result to stack
@SP
A=M
M=D
@SP
M=M+1
// push constant x
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant x
@32766
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
@GT.8
D;JGT
@NGT.8
0;JMP
(GT.8)
@0
D=!A
@GOTO.8
0;JMP
(NGT.8)
@0
D=A
(GOTO.8)

// push result to stack
@SP
A=M
M=D
@SP
M=M+1
// push constant x
@57
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant x
@31
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant x
@53
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
// push constant x
@112
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

// push result to stack
@SP
A=M
M=D
@SP
M=M+1

// pop from stack to get 1 ops
@SP
M=M-1
A=M
D=M
D=-D

// push result to stack
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
M=M&D
D=M

// push result to stack
@SP
A=M
M=D
@SP
M=M+1
// push constant x
@82
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
M=M|D
D=M

// push result to stack
@SP
A=M
M=D
@SP
M=M+1

// pop from stack to get 1 ops
@SP
M=M-1
A=M
D=M
D=!D

// push result to stack
@SP
A=M
M=D
@SP
M=M+1
