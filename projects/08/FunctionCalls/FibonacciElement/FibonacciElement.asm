@256
D=A
@SP
M=D
//call function
@Sys.init$ret.0
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@ARG
M=D
@5
D=A
@ARG
M=M-D
@0
D=A
@ARG
M=M-D
@SP
D=M
@LCL
M=D
//goto
@Sys.init
0;JMP
(Sys.init$ret.0)
//function
(Sys.init)
@0
D=A
@R13
M=D
(Sys.init$forLoop.0)
@R13
D=M
@Sys.initContinue
D,JEQ
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@R13
M=M-1
@Sys.init$forLoop.0
0;JMP
(Sys.initContinue)
//push constant
@4
D=A
@SP
A=M
M=D
@SP
M=M+1
//call function
@Main.fibonacci$ret.10
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@ARG
M=D
@5
D=A
@ARG
M=M-D
@1
D=A
@ARG
M=M-D
@SP
D=M
@LCL
M=D
//goto
@Main.fibonacci
0;JMP
(Main.fibonacci$ret.10)
//label
(WHILE)
//goto
@WHILE
0;JMP
//function
(Main.fibonacci)
@0
D=A
@R13
M=D
(Main.fibonacci$forLoop.0)
@R13
D=M
@Main.fibonacciContinue
D,JEQ
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@R13
M=M-1
@Main.fibonacci$forLoop.0
0;JMP
(Main.fibonacciContinue)
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
//lt
@SP
AM=M-1
D=M
@SP
A=M-1
D=D-M
@ASSIGN_MINUS_ONE0
D,JGT
@SP
A=M-1
M=0
@NEXT_ITERATION0
0;JMP
(ASSIGN_MINUS_ONE0)
@SP
A=M-1
M=-1
(NEXT_ITERATION0)
//if-goto
@SP
AM=M-1
D=M
@IF_TRUE
D;JNE
//goto
@IF_FALSE
0;JMP
//label
(IF_TRUE)
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
//return
@LCL
D=M
@R14
M=D
@R14
D=M
@5
D=D-A
A=D
D=M
@R15
M=D
@SP
AM=M-1
D=M
@ARG
A=M
M=D
@ARG
D=M
@1
D=D+A
@SP
M=D
@R14
D=M
@1
D=D-A
A=D
D=M
@THAT
M=D
@R14
D=M
@2
D=D-A
A=D
D=M
@THIS
M=D
@R14
D=M
@3
D=D-A
A=D
D=M
@ARG
M=D
@R14
D=M
@4
D=D-A
A=D
D=M
@LCL
M=D
@R15
A=M
0;JMP
//label
(IF_FALSE)
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
//call function
@Main.fibonacci$ret.11
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@ARG
M=D
@5
D=A
@ARG
M=M-D
@1
D=A
@ARG
M=M-D
@SP
D=M
@LCL
M=D
//goto
@Main.fibonacci
0;JMP
(Main.fibonacci$ret.11)
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
//call function
@Main.fibonacci$ret.12
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@ARG
M=D
@5
D=A
@ARG
M=M-D
@1
D=A
@ARG
M=M-D
@SP
D=M
@LCL
M=D
//goto
@Main.fibonacci
0;JMP
(Main.fibonacci$ret.12)
//add
@SP
AM=M-1
D=M
@SP
A=M-1
M=M+D
//return
@LCL
D=M
@R14
M=D
@R14
D=M
@5
D=D-A
A=D
D=M
@R15
M=D
@SP
AM=M-1
D=M
@ARG
A=M
M=D
@ARG
D=M
@1
D=D+A
@SP
M=D
@R14
D=M
@1
D=D-A
A=D
D=M
@THAT
M=D
@R14
D=M
@2
D=D-A
A=D
D=M
@THIS
M=D
@R14
D=M
@3
D=D-A
A=D
D=M
@ARG
M=D
@R14
D=M
@4
D=D-A
A=D
D=M
@LCL
M=D
@R15
A=M
0;JMP