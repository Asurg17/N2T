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
@6
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant
@8
D=A
@SP
A=M
M=D
@SP
M=M+1
//call function
@Class1.set$ret.20
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
@2
D=A
@ARG
M=M-D
@SP
D=M
@LCL
M=D
//goto
@Class1.set
0;JMP
(Class1.set$ret.20)
//pop instruction5
@5
D=A
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
@23
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant
@15
D=A
@SP
A=M
M=D
@SP
M=M+1
//call function
@Class2.set$ret.21
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
@2
D=A
@ARG
M=M-D
@SP
D=M
@LCL
M=D
//goto
@Class2.set
0;JMP
(Class2.set$ret.21)
//pop instruction5
@5
D=A
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
//call function
@Class1.get$ret.02
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
@Class1.get
0;JMP
(Class1.get$ret.02)
//call function
@Class2.get$ret.03
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
@Class2.get
0;JMP
(Class2.get$ret.03)
//label
(WHILE)
//goto
@WHILE
0;JMP
//function
(Class1.set)
@0
D=A
@R13
M=D
(Class1.set$forLoop.0)
@R13
D=M
@Class1.setContinue
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
@Class1.set$forLoop.0
0;JMP
(Class1.setContinue)
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
//pop static Class1.vm
@SP
AM=M-1
D=M
@Class1.vm$0
M=D
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
//pop static Class1.vm
@SP
AM=M-1
D=M
@Class1.vm$1
M=D
//push constant
@0
D=A
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
//function
(Class1.get)
@0
D=A
@R13
M=D
(Class1.get$forLoop.0)
@R13
D=M
@Class1.getContinue
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
@Class1.get$forLoop.0
0;JMP
(Class1.getContinue)
//push static Class1.vm
@Class1.vm$0
D=M
@SP
A=M
M=D
@SP
M=M+1
//push static Class1.vm
@Class1.vm$1
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
//function
(Class2.set)
@0
D=A
@R13
M=D
(Class2.set$forLoop.0)
@R13
D=M
@Class2.setContinue
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
@Class2.set$forLoop.0
0;JMP
(Class2.setContinue)
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
//pop static Class2.vm
@SP
AM=M-1
D=M
@Class2.vm$0
M=D
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
//pop static Class2.vm
@SP
AM=M-1
D=M
@Class2.vm$1
M=D
//push constant
@0
D=A
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
//function
(Class2.get)
@0
D=A
@R13
M=D
(Class2.get$forLoop.0)
@R13
D=M
@Class2.getContinue
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
@Class2.get$forLoop.0
0;JMP
(Class2.getContinue)
//push static Class2.vm
@Class2.vm$0
D=M
@SP
A=M
M=D
@SP
M=M+1
//push static Class2.vm
@Class2.vm$1
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
