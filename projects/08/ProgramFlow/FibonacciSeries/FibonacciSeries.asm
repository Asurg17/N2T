//push segment
@2
D=M
@R13
M=D
@1
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
//pop this/that4
@SP
AM=M-1
D=M
@4
M=D
//push constant
@0
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
@0
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
@1
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
@1
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
//push segment
@2
D=M
@R13
M=D
@0
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
//push constant
@2
D=A
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
//pop segment
@2
D=M
@R13
M=D
@0
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
//label
(MAIN_LOOP_START)
//push segment
@2
D=M
@R13
M=D
@0
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
//if-goto
@SP
AM=M-1
D=M
@COMPUTE_ELEMENT
D;JNE
//goto
@END_PROGRAM
0;JMP
//label
(COMPUTE_ELEMENT)
//push segment
@4
D=M
@R13
M=D
@0
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
//push segment
@4
D=M
@R13
M=D
@1
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
//pop segment
@4
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
//push this/that4
@4
D=M
@SP
A=M
M=D
@SP
M=M+1
//push constant
@1
D=A
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
//pop this/that4
@SP
AM=M-1
D=M
@4
M=D
//push segment
@2
D=M
@R13
M=D
@0
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
//push constant
@1
D=A
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
//pop segment
@2
D=M
@R13
M=D
@0
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
//goto
@MAIN_LOOP_START
0;JMP
//label
(END_PROGRAM)
