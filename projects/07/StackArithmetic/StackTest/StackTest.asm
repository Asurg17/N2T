//push constant
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
//eq
@SP
AM=M-1
D=M
@SP
A=M-1
D=D-M
@ASSIGN_MINUS_ONE0
D,JEQ
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
//push constant
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
//eq
@SP
AM=M-1
D=M
@SP
A=M-1
D=D-M
@ASSIGN_MINUS_ONE1
D,JEQ
@SP
A=M-1
M=0
@NEXT_ITERATION1
0;JMP
(ASSIGN_MINUS_ONE1)
@SP
A=M-1
M=-1
(NEXT_ITERATION1)
//push constant
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
//eq
@SP
AM=M-1
D=M
@SP
A=M-1
D=D-M
@ASSIGN_MINUS_ONE2
D,JEQ
@SP
A=M-1
M=0
@NEXT_ITERATION2
0;JMP
(ASSIGN_MINUS_ONE2)
@SP
A=M-1
M=-1
(NEXT_ITERATION2)
//push constant
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
//gt
@SP
AM=M-1
D=M
@SP
A=M-1
D=D-M
@ASSIGN_MINUS_ONE3
D,JGT
@SP
A=M-1
M=0
@NEXT_ITERATION3
0;JMP
(ASSIGN_MINUS_ONE3)
@SP
A=M-1
M=-1
(NEXT_ITERATION3)
//push constant
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
//gt
@SP
AM=M-1
D=M
@SP
A=M-1
D=D-M
@ASSIGN_MINUS_ONE4
D,JGT
@SP
A=M-1
M=0
@NEXT_ITERATION4
0;JMP
(ASSIGN_MINUS_ONE4)
@SP
A=M-1
M=-1
(NEXT_ITERATION4)
//push constant
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
//gt
@SP
AM=M-1
D=M
@SP
A=M-1
D=D-M
@ASSIGN_MINUS_ONE5
D,JGT
@SP
A=M-1
M=0
@NEXT_ITERATION5
0;JMP
(ASSIGN_MINUS_ONE5)
@SP
A=M-1
M=-1
(NEXT_ITERATION5)
//push constant
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
//gt
@SP
AM=M-1
D=M
@SP
A=M-1
D=D-M
@ASSIGN_MINUS_ONE6
D,JLT
@SP
A=M-1
M=0
@NEXT_ITERATION6
0;JMP
(ASSIGN_MINUS_ONE6)
@SP
A=M-1
M=-1
(NEXT_ITERATION6)
//push constant
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
//gt
@SP
AM=M-1
D=M
@SP
A=M-1
D=D-M
@ASSIGN_MINUS_ONE7
D,JLT
@SP
A=M-1
M=0
@NEXT_ITERATION7
0;JMP
(ASSIGN_MINUS_ONE7)
@SP
A=M-1
M=-1
(NEXT_ITERATION7)
//push constant
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
//gt
@SP
AM=M-1
D=M
@SP
A=M-1
D=D-M
@ASSIGN_MINUS_ONE8
D,JLT
@SP
A=M-1
M=0
@NEXT_ITERATION8
0;JMP
(ASSIGN_MINUS_ONE8)
@SP
A=M-1
M=-1
(NEXT_ITERATION8)
//push constant
@57
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant
@31
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant
@53
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
//push constant
@112
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
//neg
@SP
A=M-1
M=-M
//and
@SP
AM=M-1
D=M
@SP
A=M-1
M=M&D
//push constant
@82
D=A
@SP
A=M
M=D
@SP
M=M+1
//or
@SP
AM=M-1
D=M
@SP
A=M-1
M=M|D
//not
@SP
A=M-1
M=!M