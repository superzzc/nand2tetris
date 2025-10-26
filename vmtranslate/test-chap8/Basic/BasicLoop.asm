
// push constant x
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop local 0

// pop value to D reg
@SP
M=M-1
A=M
D=M

@tmp.0
M=D
// M[local[0]]
@LCL
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

// push local 0
// M[local[0]]
@LCL
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
// pop local 0

// pop value to D reg
@SP
M=M-1
A=M
D=M

@tmp.1
M=D
// M[local[0]]
@LCL
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

@tmp.2
M=D
// M[argument[0]]
@ARG
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

@LOOP
D;JNE

// push local 0
// M[local[0]]
@LCL
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
