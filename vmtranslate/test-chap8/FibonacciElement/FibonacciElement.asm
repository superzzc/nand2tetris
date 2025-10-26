
// init SP point to RAM[256]
@256
D=A
@SP
M=D

// call Sys.init 0
@return-address.Sys.init.0
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
@5
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D

@Sys.init
0;JMP
(return-address.Sys.init.0)
// end of call Sys.init 0 translation
(Main.fibonacci)

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

// eq/gt/lt
@LT.0
D;JLT
@NLT.0
0;JMP
(LT.0)
@0
D=!A
@GOTO.0
0;JMP
(NLT.0)
@0
D=A
(GOTO.0)

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

@Main.fibonacci$N_LT_2
D;JNE

@Main.fibonacci$N_GE_2
0;JMP

(Main.fibonacci$N_LT_2)

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

(Main.fibonacci$N_GE_2)

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

// call Main.fibonacci 1
@return-address.Main.fibonacci.1
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
@6
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D

@Main.fibonacci
0;JMP
(return-address.Main.fibonacci.1)
// end of call Main.fibonacci 1 translation

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

// call Main.fibonacci 1
@return-address.Main.fibonacci.2
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
@6
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D

@Main.fibonacci
0;JMP
(return-address.Main.fibonacci.2)
// end of call Main.fibonacci 1 translation

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
(Sys.init)

// push constant x
@4
D=A
@SP
A=M
M=D
@SP
M=M+1

// call Main.fibonacci 1
@return-address.Main.fibonacci.3
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
@6
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D

@Main.fibonacci
0;JMP
(return-address.Main.fibonacci.3)
// end of call Main.fibonacci 1 translation

(Sys.init$END)

@Sys.init$END
0;JMP
