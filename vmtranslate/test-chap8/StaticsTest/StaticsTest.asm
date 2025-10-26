
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
(Sys.init)

// push constant x
@6
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

// call Class1.set 2
@return-address.Class1.set.1
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
@7
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D

@Class1.set
0;JMP
(return-address.Class1.set.1)
// end of call Class1.set 2 translation
// pop temp 0

// pop value to D reg
@SP
M=M-1
A=M
D=M

@tmp.0
M=D
// M[temp[0]]
@5
D=A
@0
D=D+A
@addr.0
M=D
@tmp.0
D=M
@addr.0
A=M
M=D

// push constant x
@23
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant x
@15
D=A
@SP
A=M
M=D
@SP
M=M+1

// call Class2.set 2
@return-address.Class2.set.2
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
@7
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D

@Class2.set
0;JMP
(return-address.Class2.set.2)
// end of call Class2.set 2 translation
// pop temp 0

// pop value to D reg
@SP
M=M-1
A=M
D=M

@tmp.1
M=D
// M[temp[0]]
@5
D=A
@0
D=D+A
@addr.1
M=D
@tmp.1
D=M
@addr.1
A=M
M=D

// call Class1.get 0
@return-address.Class1.get.3
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

@Class1.get
0;JMP
(return-address.Class1.get.3)
// end of call Class1.get 0 translation

// call Class2.get 0
@return-address.Class2.get.4
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

@Class2.get
0;JMP
(return-address.Class2.get.4)
// end of call Class2.get 0 translation

(Sys.init$END)

@Sys.init$END
0;JMP
(Class2.set)

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
// pop static 0

// pop value to D reg
@SP
M=M-1
A=M
D=M

@tmp.2
M=D
// M[static[0]]
@Class2.0
D=A
@0
D=D+A
@addr.2
M=D
@tmp.2
D=M
@addr.2
A=M
M=D

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
// pop static 1

// pop value to D reg
@SP
M=M-1
A=M
D=M

@tmp.3
M=D
// M[static[1]]
@Class2.1
D=A
@0
D=D+A
@addr.3
M=D
@tmp.3
D=M
@addr.3
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
(Class2.get)

// push static 0
// M[static[0]]
@Class2.0
D=A
@0
A=D+A
D=M

// push D reg value to stack
@SP
A=M
M=D
@SP
M=M+1

// push static 1
// M[static[1]]
@Class2.1
D=A
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
(Class1.set)

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
// pop static 0

// pop value to D reg
@SP
M=M-1
A=M
D=M

@tmp.4
M=D
// M[static[0]]
@Class1.0
D=A
@0
D=D+A
@addr.4
M=D
@tmp.4
D=M
@addr.4
A=M
M=D

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
// pop static 1

// pop value to D reg
@SP
M=M-1
A=M
D=M

@tmp.5
M=D
// M[static[1]]
@Class1.1
D=A
@0
D=D+A
@addr.5
M=D
@tmp.5
D=M
@addr.5
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
(Class1.get)

// push static 0
// M[static[0]]
@Class1.0
D=A
@0
A=D+A
D=M

// push D reg value to stack
@SP
A=M
M=D
@SP
M=M+1

// push static 1
// M[static[1]]
@Class1.1
D=A
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
