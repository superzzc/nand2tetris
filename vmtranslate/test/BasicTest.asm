
// push constant x
@10
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

@tmp.4
M=D
// M[local[0]]
@LCL
D=M
@0
D=D+A
@addr.4
M=D
@tmp.4
D=M
@addr.4
A=M
M=D

// push constant x
@21
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant x
@22
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop argument 2

// pop value to D reg
@SP
M=M-1
A=M
D=M

@tmp.5
M=D
// M[argument[2]]
@ARG
D=M
@2
D=D+A
@addr.5
M=D
@tmp.5
D=M
@addr.5
A=M
M=D
// pop argument 1

// pop value to D reg
@SP
M=M-1
A=M
D=M

@tmp.6
M=D
// M[argument[1]]
@ARG
D=M
@1
D=D+A
@addr.6
M=D
@tmp.6
D=M
@addr.6
A=M
M=D

// push constant x
@36
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop this 6

// pop value to D reg
@SP
M=M-1
A=M
D=M

@tmp.7
M=D
// M[this[6]]
@THIS
D=M
@6
D=D+A
@addr.7
M=D
@tmp.7
D=M
@addr.7
A=M
M=D

// push constant x
@42
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant x
@45
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop that 5

// pop value to D reg
@SP
M=M-1
A=M
D=M

@tmp.8
M=D
// M[that[5]]
@THAT
D=M
@5
D=D+A
@addr.8
M=D
@tmp.8
D=M
@addr.8
A=M
M=D
// pop that 2

// pop value to D reg
@SP
M=M-1
A=M
D=M

@tmp.9
M=D
// M[that[2]]
@THAT
D=M
@2
D=D+A
@addr.9
M=D
@tmp.9
D=M
@addr.9
A=M
M=D

// push constant x
@510
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop temp 6

// pop value to D reg
@SP
M=M-1
A=M
D=M

@tmp.10
M=D
// M[temp[6]]
@5
D=A
@6
D=D+A
@addr.10
M=D
@tmp.10
D=M
@addr.10
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

// push that 5
// M[that[5]]
@THAT
D=M
@5
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

// push this 6
// M[this[6]]
@THIS
D=M
@6
A=D+A
D=M

// push D reg value to stack
@SP
A=M
M=D
@SP
M=M+1

// push this 6
// M[this[6]]
@THIS
D=M
@6
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
M=M-D
D=M

// push D reg value to stack
@SP
A=M
M=D
@SP
M=M+1

// push temp 6
// M[temp[6]]
@5
D=A
@6
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
