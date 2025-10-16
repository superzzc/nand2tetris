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
@EQ
D;JEQ
@NEQ
0;JMP
(EQ)
@0
D=!A
@CONTINUE
0;JMP
(NEQ)
@0
D=A
(CONTINUE)

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
@EQ
D;JEQ
@NEQ
0;JMP
(EQ)
@0
D=!A
@CONTINUE
0;JMP
(NEQ)
@0
D=A
(CONTINUE)

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
@EQ
D;JEQ
@NEQ
0;JMP
(EQ)
@0
D=!A
@CONTINUE
0;JMP
(NEQ)
@0
D=A
(CONTINUE)

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
@LT
D;JLT
@NLT
0;JMP
(LT)
@0
D=!A
@CONTINUE
0;JMP
(NLT)
@0
D=A
(CONTINUE)

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
@LT
D;JLT
@NLT
0;JMP
(LT)
@0
D=!A
@CONTINUE
0;JMP
(NLT)
@0
D=A
(CONTINUE)

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
@LT
D;JLT
@NLT
0;JMP
(LT)
@0
D=!A
@CONTINUE
0;JMP
(NLT)
@0
D=A
(CONTINUE)

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
@GT
D;JGT
@NGT
0;JMP
(GT)
@0
D=!A
@CONTINUE
0;JMP
(NGT)
@0
D=A
(CONTINUE)

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
@GT
D;JGT
@NGT
0;JMP
(GT)
@0
D=!A
@CONTINUE
0;JMP
(NGT)
@0
D=A
(CONTINUE)

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
@GT
D;JGT
@NGT
0;JMP
(GT)
@0
D=!A
@CONTINUE
0;JMP
(NGT)
@0
D=A
(CONTINUE)

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
