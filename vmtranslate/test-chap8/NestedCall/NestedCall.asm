(Sys.init)

// push constant x
@4000
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop pointer 0

// pop value to D reg
@SP
M=M-1
A=M
D=M

@tmp.0
M=D
// M[pointer[0]]
@3
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
@5000
D=A
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

@tmp.1
M=D
// M[pointer[1]]
@3
D=A
@1
D=D+A
@addr.1
M=D
@tmp.1
D=M
@addr.1
A=M
M=D

// call Sys.main 0
@return-address.Sys.main.0
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

@Sys.main
0;JMP
(return-address.Sys.main.0)
// end of call Sys.main 0 translation
// pop temp 1

// pop value to D reg
@SP
M=M-1
A=M
D=M

@tmp.2
M=D
// M[temp[1]]
@5
D=A
@1
D=D+A
@addr.2
M=D
@tmp.2
D=M
@addr.2
A=M
M=D

(Sys.init$LOOP)

@Sys.init$LOOP
0;JMP
(Sys.main)

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

@0
D=A

// push D reg value to stack
@SP
A=M
M=D
@SP
M=M+1

// push constant x
@4001
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop pointer 0

// pop value to D reg
@SP
M=M-1
A=M
D=M

@tmp.3
M=D
// M[pointer[0]]
@3
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
@5001
D=A
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

@tmp.4
M=D
// M[pointer[1]]
@3
D=A
@1
D=D+A
@addr.4
M=D
@tmp.4
D=M
@addr.4
A=M
M=D

// push constant x
@200
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop local 1

// pop value to D reg
@SP
M=M-1
A=M
D=M

@tmp.5
M=D
// M[local[1]]
@LCL
D=M
@1
D=D+A
@addr.5
M=D
@tmp.5
D=M
@addr.5
A=M
M=D

// push constant x
@40
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop local 2

// pop value to D reg
@SP
M=M-1
A=M
D=M

@tmp.6
M=D
// M[local[2]]
@LCL
D=M
@2
D=D+A
@addr.6
M=D
@tmp.6
D=M
@addr.6
A=M
M=D

// push constant x
@6
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop local 3

// pop value to D reg
@SP
M=M-1
A=M
D=M

@tmp.7
M=D
// M[local[3]]
@LCL
D=M
@3
D=D+A
@addr.7
M=D
@tmp.7
D=M
@addr.7
A=M
M=D

// push constant x
@123
D=A
@SP
A=M
M=D
@SP
M=M+1

// call Sys.add12 1
@return-address.Sys.add12.1
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

@Sys.add12
0;JMP
(return-address.Sys.add12.1)
// end of call Sys.add12 1 translation
// pop temp 0

// pop value to D reg
@SP
M=M-1
A=M
D=M

@tmp.8
M=D
// M[temp[0]]
@5
D=A
@0
D=D+A
@addr.8
M=D
@tmp.8
D=M
@addr.8
A=M
M=D

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

// push local 2
// M[local[2]]
@LCL
D=M
@2
A=D+A
D=M

// push D reg value to stack
@SP
A=M
M=D
@SP
M=M+1

// push local 3
// M[local[3]]
@LCL
D=M
@3
A=D+A
D=M

// push D reg value to stack
@SP
A=M
M=D
@SP
M=M+1

// push local 4
// M[local[4]]
@LCL
D=M
@4
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
(Sys.add12)

// push constant x
@4002
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop pointer 0

// pop value to D reg
@SP
M=M-1
A=M
D=M

@tmp.9
M=D
// M[pointer[0]]
@3
D=A
@0
D=D+A
@addr.9
M=D
@tmp.9
D=M
@addr.9
A=M
M=D

// push constant x
@5002
D=A
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

@tmp.10
M=D
// M[pointer[1]]
@3
D=A
@1
D=D+A
@addr.10
M=D
@tmp.10
D=M
@addr.10
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
@12
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
