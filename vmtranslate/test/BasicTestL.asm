
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

@tmp.3
M=D
// M[temp[6]]
@5
D=A
@6
D=D+A
@addr.3
M=D
@tmp.3
D=M
@addr.3
A=M
M=D
