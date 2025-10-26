
// push argument 1
// M[argument[1]]
@ARG
D=M
@1
A=D+A
D=M

// push D reg value to stack
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

@tmp.0
M=D
// M[pointer[1]]
@3
D=A
@1
D=D+A
@addr.0
M=D
@tmp.0
D=M
@addr.0
A=M
M=D

// push constant x
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop that 0

// pop value to D reg
@SP
M=M-1
A=M
D=M

@tmp.1
M=D
// M[that[0]]
@THAT
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

// push constant x
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop that 1

// pop value to D reg
@SP
M=M-1
A=M
D=M

@tmp.2
M=D
// M[that[1]]
@THAT
D=M
@1
D=D+A
@addr.2
M=D
@tmp.2
D=M
@addr.2
A=M
M=D

// push argument 0
// M[argument[0]]
@ARG
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

// push constant x
@2
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

// push D reg value to stack
@SP
A=M
M=D
@SP
M=M+1
// pop argument 0

// pop value to D reg
@SP
M=M-1
A=M
D=M

@tmp.3
M=D
// M[argument[0]]
@ARG
D=M
@0
D=D+A
@addr.3
M=D
@tmp.3
D=M
@addr.3
A=M
M=D

(LOOP)

// push argument 0
// M[argument[0]]
@ARG
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

// pop value to D reg
@SP
M=M-1
A=M
D=M

@COMPUTE_ELEMENT
D;JNE

@END
0;JMP

(COMPUTE_ELEMENT)

// push that 0
// M[that[0]]
@THAT
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

// push that 1
// M[that[1]]
@THAT
D=M
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
// pop that 2

// pop value to D reg
@SP
M=M-1
A=M
D=M

@tmp.4
M=D
// M[that[2]]
@THAT
D=M
@2
D=D+A
@addr.4
M=D
@tmp.4
D=M
@addr.4
A=M
M=D

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

// push constant x
@1
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

// push D reg value to stack
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

@tmp.5
M=D
// M[pointer[1]]
@3
D=A
@1
D=D+A
@addr.5
M=D
@tmp.5
D=M
@addr.5
A=M
M=D

// push argument 0
// M[argument[0]]
@ARG
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

// push constant x
@1
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

// push D reg value to stack
@SP
A=M
M=D
@SP
M=M+1
// pop argument 0

// pop value to D reg
@SP
M=M-1
A=M
D=M

@tmp.6
M=D
// M[argument[0]]
@ARG
D=M
@0
D=D+A
@addr.6
M=D
@tmp.6
D=M
@addr.6
A=M
M=D

@LOOP
0;JMP

(END)
