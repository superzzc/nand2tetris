(SimpleFunction.test)

@0
D=A

// push D reg value to stack
@SP
A=M
M=D
@SP
M=M+1

@0
D=A

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

// push local 1
// M[local[1]]
@LCL
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

// pop from stack to get 1 ops
@SP
M=M-1
A=M
D=M
D=!D

// push D reg value to stack
@SP
A=M
M=D
@SP
M=M+1

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

// get return addr
@LCL
D=M
@5
D=D-A
@R13
M=D

@LCL
D=M
@5
A=D-A
D=M
@R14
M=D

// pop value to D reg
@SP
M=M-1
A=M
D=M

// set return value to argument[0]
@ARG
A=M
M=D
// reset call stack
@ARG
D=M
D=D+1
@SP
M=D

// reset LCL from stack
@R13
D=M
@1
A=D+A
D=M
@LCL
M=D

// reset ARG from stack
@R13
D=M
@2
A=D+A
D=M
@ARG
M=D

// reset THIS from stack
@R13
D=M
@3
A=D+A
D=M
@THIS
M=D

// reset THAT from stack
@R13
D=M
@4
A=D+A
D=M
@THAT
M=D

@R14
A=M
0;JMP
