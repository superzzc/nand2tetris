
// init SP point to RAM[256]
@256
D=A
@SP
M=D

// call Sys.init 0
@return_Sys.init.0
D=A

// push D reg value to stack
@SP
A=M
M=D
@SP
M=M+1

@LCL
D=M

// push D reg value to stack
@SP
A=M
M=D
@SP
M=M+1

@ARG
D=M

// push D reg value to stack
@SP
A=M
M=D
@SP
M=M+1

@THIS
D=M

// push D reg value to stack
@SP
A=M
M=D
@SP
M=M+1

@THAT
D=M

// push D reg value to stack
@SP
A=M
M=D
@SP
M=M+1

@SP
D=M
@LCL
M=D
@5
D=D-A
@ARG
M=D

@Sys.init
0;JMP
(return_Sys.init.0)
// end of call Sys.init 0 translation
(Sys.init)

// push constant x
@4
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant x
@3
D=A
@SP
A=M
M=D
@SP
M=M+1

// call Main.SimpleFunction.test 2
@return_Main.SimpleFunction.test.1
D=A

// push D reg value to stack
@SP
A=M
M=D
@SP
M=M+1

@LCL
D=M

// push D reg value to stack
@SP
A=M
M=D
@SP
M=M+1

@ARG
D=M

// push D reg value to stack
@SP
A=M
M=D
@SP
M=M+1

@THIS
D=M

// push D reg value to stack
@SP
A=M
M=D
@SP
M=M+1

@THAT
D=M

// push D reg value to stack
@SP
A=M
M=D
@SP
M=M+1

@SP
D=M
@LCL
M=D
@7
D=D-A
@ARG
M=D

@Main.SimpleFunction.test
0;JMP
(return_Main.SimpleFunction.test.1)
// end of call Main.SimpleFunction.test 2 translation

(END)

@END
0;JMP
(Main.SimpleFunction.test)

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
@return_addr.0
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
@return_addr.0
D=M
@1
A=D+A
D=M
@LCL
M=D

// reset ARG from stack
@return_addr.0
D=M
@2
A=D+A
D=M
@ARG
M=D

// reset THIS from stack
@return_addr.0
D=M
@3
A=D+A
D=M
@THIS
M=D

// reset THAT from stack
@return_addr.0
D=M
@4
A=D+A
D=M
@THAT
M=D

@return_addr.0
A=M
0;JMP
