//push constant
@3030
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop this/that3
@SP
AM=M-1
D=M
@3
M=D
//push constant
@3040
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop this/that4
@SP
AM=M-1
D=M
@4
M=D
//push constant
@32
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop segment
@3
D=M
@R13
M=D
@2
D=A
@R13
M=M+D
@SP
M=M-1
@SP
A=M
D=M
@R13
A=M
M=D
//push constant
@46
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop segment
@4
D=M
@R13
M=D
@6
D=A
@R13
M=M+D
@SP
M=M-1
@SP
A=M
D=M
@R13
A=M
M=D
//push this/that3
@3
D=M
@SP
A=M
M=D
@SP
M=M+1
//push this/that4
@4
D=M
@SP
A=M
M=D
@SP
M=M+1
//add
@SP
AM=M-1
D=M
@SP
A=M-1
M=M+D
//push segment
@3
D=M
@R13
M=D
@2
D=A
@R13
M=M+D
@R13
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1
//sub
@SP
AM=M-1
D=M
@SP
A=M-1
M=M-D
//push segment
@4
D=M
@R13
M=D
@6
D=A
@R13
M=M+D
@R13
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1
//add
@SP
AM=M-1
D=M
@SP
A=M-1
M=M+D
