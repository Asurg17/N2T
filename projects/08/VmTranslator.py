import sys
import os
from collections import Counter

counter = 0
cnt = 0

#####################################################################
def popLastElemFromStack(outputFile):
    outputFile.write('@SP\n') #A instruction to get SP
    
    outputFile.write('AM=M-1\n') #A=M-1 (*SP--) and M=M-1 (*SP=*SP-1)

    outputFile.write('D=M\n') #D=*A (*(*SP-1))

####################################################################

def getLastElemPointer(outputFile):
    outputFile.write("@SP\n") #A instruction to get SP
    
    outputFile.write("A=M-1\n") #A=M-1 (*SP--)

#####################################################################

def addPopedElemToLastElemInStack(outputFile):
    getLastElemPointer(outputFile)

    outputFile.write("M=M+D\n") # last elem + D

def addAddAsmInstruction(outputFile):
    outputFile.write('//add\n')

    popLastElemFromStack(outputFile)
    addPopedElemToLastElemInStack(outputFile)

#####################################################################

def subtractPopedElemFromLastElemInStack(outputFile):
    getLastElemPointer(outputFile)

    outputFile.write('M=M-D\n') # last elem - D

def addSunbtractionInstruction(outputFile):
    outputFile.write('//sub\n')

    popLastElemFromStack(outputFile)
    subtractPopedElemFromLastElemInStack(outputFile)

#####################################################################    

def addNegInstruction(outputFile):
    outputFile.write('//neg\n')

    getLastElemPointer(outputFile)
    outputFile.write("M=-M\n")

#####################################################################

def compareIfEquals(outputFile, specificCharacter):
    getLastElemPointer(outputFile)
    outputFile.write("D=D-M\n")

    outputFile.write("@ASSIGN_MINUS_ONE" + specificCharacter + '\n')

    outputFile.write("D,JEQ\n") #equals to 0 so they are equal

#if not equals
    
    getLastElemPointer(outputFile)
    outputFile.write("M=0\n")

    outputFile.write("@NEXT_ITERATION" + specificCharacter + '\n')

    outputFile.write("0;JMP\n")

###
    
    outputFile.write("(ASSIGN_MINUS_ONE" + specificCharacter + ")\n")

    getLastElemPointer(outputFile)
    outputFile.write("M=-1\n")

    outputFile.write("(NEXT_ITERATION" + specificCharacter + ")\n")


def addEqInstruction(outputFile, specificCharacter):
    outputFile.write('//eq\n')

    popLastElemFromStack(outputFile)
    compareIfEquals(outputFile, specificCharacter)

#####################################################################

def compareIfGreater(outputFile, specificCharacter):
    getLastElemPointer(outputFile)
    outputFile.write("D=D-M\n")

    outputFile.write("@ASSIGN_MINUS_ONE" + specificCharacter + '\n')

    outputFile.write("D,JLT\n") #equals to 0 so they are equal

#if not less

    getLastElemPointer(outputFile)
    outputFile.write("M=0\n")

    outputFile.write("@NEXT_ITERATION" + specificCharacter + '\n')

    outputFile.write("0;JMP\n")

###

    outputFile.write("(ASSIGN_MINUS_ONE" + specificCharacter + ")\n")

    getLastElemPointer(outputFile)
    outputFile.write("M=-1\n")

    outputFile.write("(NEXT_ITERATION" + specificCharacter + ")\n")


def addGtInstruction(outputFile, specificCharacter):
    outputFile.write('//gt\n')

    popLastElemFromStack(outputFile)
    compareIfGreater(outputFile, specificCharacter)


#####################################################################

def compareIfLess(outputFile, specificCharacter):
    getLastElemPointer(outputFile)
    outputFile.write("D=D-M\n")

    outputFile.write("@ASSIGN_MINUS_ONE" + specificCharacter + '\n')

    outputFile.write("D,JGT\n") #equals to 0 so they are equal

#if not less

    getLastElemPointer(outputFile)
    outputFile.write("M=0\n")

    outputFile.write("@NEXT_ITERATION" + specificCharacter + '\n')

    outputFile.write("0;JMP\n")

###

    outputFile.write("(ASSIGN_MINUS_ONE" + specificCharacter + ")\n")

    getLastElemPointer(outputFile)
    outputFile.write("M=-1\n")

    outputFile.write("(NEXT_ITERATION" + specificCharacter + ")\n")

def addLtInstruction(outputFile, specificCharacter):
    outputFile.write('//lt\n')

    popLastElemFromStack(outputFile)
    compareIfLess(outputFile, specificCharacter)

#####################################################################

def addAndInstruction(outputFile):
    outputFile.write('//and\n')

    popLastElemFromStack(outputFile)
    getLastElemPointer(outputFile)

    outputFile.write("M=M&D\n")

#####################################################################

def addOrInstruction(outputFile):
    outputFile.write('//or\n')

    popLastElemFromStack(outputFile)
    getLastElemPointer(outputFile)

    outputFile.write("M=M|D\n")

#####################################################################

def addNotInstruction(outputFile):
    outputFile.write('//not\n')

    getLastElemPointer(outputFile)

    outputFile.write("M=!M\n")    

#####################################################################
#####################################################################

def addPushConstantInstruction(index, outputFile):
    outputFile.write('//push constant\n')

    outputFile.write('@')
    outputFile.write(index + '\n')

    outputFile.write('D=A\n')

    outputFile.write('@SP\n')
    
    outputFile.write('A=M\n')

    outputFile.write('M=D\n')
    
    outputFile.write('@SP\n')
    
    outputFile.write('M=M+1\n')

#####################################################################

def addPushInstruction(baseIndex, index, outputFile):
    outputFile.write('//push segment\n')

    outputFile.write('@') #segment
    outputFile.write(baseIndex + '\n')

    outputFile.write('D=M\n') #*segment

    outputFile.write('@R13\n')

    outputFile.write('M=D\n')

    outputFile.write('@')
    outputFile.write(index + '\n')

    outputFile.write('D=A\n')

    outputFile.write('@R13\n')

    outputFile.write('M=M+D\n')

    outputFile.write('@R13\n')

    outputFile.write('A=M\n')

    outputFile.write('D=M\n') #*R13

    outputFile.write('@SP\n')

    outputFile.write('A=M\n')

    outputFile.write('M=D\n') #*SP = *R13

    outputFile.write('@SP\n')
    
    outputFile.write('M=M+1\n')


#####################################################################

def addPopInstruction(baseIndex, index, outputFile):
    outputFile.write('//pop segment\n')

    outputFile.write('@') #segment
    outputFile.write(baseIndex + '\n')

    outputFile.write('D=M\n') #*segment

    outputFile.write('@R13\n')

    outputFile.write('M=D\n')

    outputFile.write('@')
    outputFile.write(index + '\n')

    outputFile.write('D=A\n')

    outputFile.write('@R13\n')

    outputFile.write('M=M+D\n')

    outputFile.write('@SP\n')
    
    outputFile.write('M=M-1\n')

    outputFile.write('@SP\n')

    outputFile.write('A=M\n')

    outputFile.write('D=M\n') #*SP

    outputFile.write('@R13\n')

    outputFile.write('A=M\n')

    outputFile.write('M=D\n') #*R13 = *SP



#####################################################################

def addTempPushInstruction(baseIndex, index, outputFile):
    outputFile.write('//push instruction' + baseIndex + '\n')

    outputFile.write('@')
    outputFile.write(baseIndex + '\n')

    outputFile.write('D=A\n') 

    outputFile.write('@R13\n')

    outputFile.write('M=D\n') 

    outputFile.write('@')
    outputFile.write(index + '\n')

    outputFile.write('D=A\n')

    outputFile.write('@R13\n')

    outputFile.write('M=M+D\n') #*R13 from where need to take 

    outputFile.write('@R13\n')

    outputFile.write('A=M\n')

    outputFile.write('D=M\n')

    outputFile.write('@SP\n')

    outputFile.write('A=M\n')

    outputFile.write('M=D\n')

    outputFile.write('@SP\n')

    outputFile.write('M=M+1\n')

#####################################################################

def addTempPopInstruction(baseIndex, index, outputFile):
    outputFile.write('//pop instruction' + baseIndex + '\n')

    outputFile.write('@')
    outputFile.write(baseIndex + '\n')

    outputFile.write('D=A\n') 

    outputFile.write('@R13\n')

    outputFile.write('M=D\n')

    outputFile.write('@')
    outputFile.write(index + '\n')

    outputFile.write('D=A\n')

    outputFile.write('@R13\n')

    outputFile.write('M=M+D\n')

    outputFile.write('@SP\n')
    
    outputFile.write('M=M-1\n')

    outputFile.write('@SP\n')

    outputFile.write('A=M\n')

    outputFile.write('D=M\n') #*SP

    outputFile.write('@R13\n')

    outputFile.write('A=M\n')

    outputFile.write('M=D\n') #*R13 = *SP

#####################################################################

def addStaticPushInstruction(fileName, index, outputFile):
    outputFile.write('//push static ' + fileName + '\n')
    
    outputFile.write('@' + fileName + '$' + index + '\n')
    outputFile.write('D=M\n')

    outputFile.write('@SP\n')
    outputFile.write('A=M\n')
    outputFile.write('M=D\n')

    outputFile.write('@SP\n')
    outputFile.write('M=M+1\n')

#####################################################################

def addStaticPopInstruction(fileName, index, outputFile):
    outputFile.write('//pop static ' + fileName + '\n')

    outputFile.write('@SP\n')
    outputFile.write('AM=M-1\n')
    outputFile.write('D=M\n')

    outputFile.write('@' + fileName + '$' + index + '\n')
    outputFile.write('M=D\n')

#####################################################################

def addThisThatPopInstruction(baseIndex, outputFile):
    outputFile.write('//pop this/that' + baseIndex + '\n')

    popLastElemFromStack(outputFile)

    outputFile.write('@' + baseIndex + '\n')

    outputFile.write('M=D\n')

#####################################################################

def addThisThatPushInstruction(baseIndex, outputFile):
    outputFile.write('//push this/that' + baseIndex + '\n')
   
    outputFile.write('@' + baseIndex + '\n')

    outputFile.write('D=M\n')

    outputFile.write('@SP\n')

    outputFile.write('A=M\n')

    outputFile.write('M=D\n')

    outputFile.write('@SP\n')

    outputFile.write('M=M+1\n')

#####################################################################
#####################################################################

#branching

def addLabelInstruction(outputFile, label):
    outputFile.write('//label\n')
    outputFile.write('(' + label + ')\n')

def addGotoInstruction(outputFile, label):
    outputFile.write('//goto\n')
    outputFile.write('@' + label + '\n')
    outputFile.write('0;JMP\n')

def addIfgoInstruction(outputFile, label):
    outputFile.write('//if-goto\n')
    popLastElemFromStack(outputFile)
    outputFile.write('@' + label + '\n')
    outputFile.write('D;JNE\n') #if not 0 (not equals to False) then go to label

#####################################################################

def pushElemIntoStack(outputFile):
    outputFile.write('@SP\n')
    outputFile.write('A=M\n')
    outputFile.write('M=D\n')
    outputFile.write('@SP\n')
    outputFile.write('M=M+1\n')

#####################################################################

def  addCallFunctionInstruction(functionName, nArgs, outputFile, num):
    outputFile.write('//call function\n')
    
    outputFile.write('@' + functionName + '$' + 'ret.' + nArgs + num +'\n') #create return label
    outputFile.write('D=A\n')
    pushElemIntoStack(outputFile) #push return addres 

    outputFile.write('@LCL\n')
    outputFile.write('D=M\n')
    pushElemIntoStack(outputFile) #push LCL 

    outputFile.write('@ARG\n')
    outputFile.write('D=M\n')
    pushElemIntoStack(outputFile) #push ARG 

    outputFile.write('@THIS\n')
    outputFile.write('D=M\n')
    pushElemIntoStack(outputFile) #push THIS 

    outputFile.write('@THAT\n')
    outputFile.write('D=M\n')
    pushElemIntoStack(outputFile) #push THAT 

#reposition ARG
    outputFile.write('@SP\n')
    outputFile.write('D=M\n')

    outputFile.write('@ARG\n')
    outputFile.write('M=D\n')
    
    outputFile.write('@5\n')
    outputFile.write('D=A\n')

    outputFile.write('@ARG\n')
    outputFile.write('M=M-D\n')

    outputFile.write('@' + nArgs + '\n')
    outputFile.write('D=A\n')

    outputFile.write('@ARG\n')
    outputFile.write('M=M-D\n')

#LCL = SP
    outputFile.write('@SP\n')
    outputFile.write('D=M\n')

    outputFile.write('@LCL\n')
    outputFile.write('M=D\n')    

#goto function
    addGotoInstruction(outputFile, functionName)

#push label (returnAddress)
    outputFile.write('(' + functionName + '$' + 'ret.' + nArgs + num +')\n')

#####################################################################

def addFunctionInstruction(functionName, nVars, outputFile):
    outputFile.write('//function\n')

    outputFile.write('(' + functionName + ')\n')

    outputFile.write('@' + nVars + '\n')
    outputFile.write('D=A\n')

    outputFile.write('@R13\n')
    outputFile.write('M=D\n') #save nVars for loop 

#initialize nVars local variables

    outputFile.write('(' + functionName + '$' + 'forLoop.' + nVars +')\n')
    
    outputFile.write('@R13\n')
    outputFile.write('D=M\n')

    outputFile.write('@' + functionName + 'Continue' + '\n')
    outputFile.write('D,JEQ\n')

    outputFile.write('@0\n')
    outputFile.write('D=A\n')

    pushElemIntoStack(outputFile)

    outputFile.write('@R13\n')
    outputFile.write('M=M-1\n')

    outputFile.write('@' + functionName + '$' + 'forLoop.' + nVars + '\n')
    outputFile.write('0;JMP\n')

    outputFile.write('(' + functionName + 'Continue'+ ')\n')

#####################################################################

def addReturnInstruction(outputFile):
    outputFile.write('//return\n')

# endFrame = LCL
    outputFile.write('@LCL\n')
    outputFile.write('D=M\n')

    outputFile.write('@R14\n')
    outputFile.write('M=D\n')

#retAddr = *(endFrame - 5)
    outputFile.write('@R14\n')
    outputFile.write('D=M\n')

    outputFile.write('@5\n')
    outputFile.write('D=D-A\n')

    outputFile.write('A=D\n')
    outputFile.write('D=M\n')

    outputFile.write('@R15\n')
    outputFile.write('M=D\n')

#*ARG = pop()
    popLastElemFromStack(outputFile)

    outputFile.write('@ARG\n')
    outputFile.write('A=M\n')
    outputFile.write('M=D\n')

#SP = ARG + 1
    outputFile.write('@ARG\n')
    outputFile.write('D=M\n')

    outputFile.write('@1\n')
    outputFile.write('D=D+A\n')

    outputFile.write('@SP\n')
    outputFile.write('M=D\n')

#THAT
    outputFile.write('@R14\n')
    outputFile.write('D=M\n')

    outputFile.write('@1\n')
    outputFile.write('D=D-A\n')

    outputFile.write('A=D\n')
    outputFile.write('D=M\n')

    outputFile.write('@THAT\n')
    outputFile.write('M=D\n')

#THIS
    outputFile.write('@R14\n')
    outputFile.write('D=M\n')

    outputFile.write('@2\n')
    outputFile.write('D=D-A\n')

    outputFile.write('A=D\n')
    outputFile.write('D=M\n')

    outputFile.write('@THIS\n')
    outputFile.write('M=D\n')

#ARG
    outputFile.write('@R14\n')
    outputFile.write('D=M\n')

    outputFile.write('@3\n')
    outputFile.write('D=D-A\n')

    outputFile.write('A=D\n')
    outputFile.write('D=M\n')

    outputFile.write('@ARG\n')
    outputFile.write('M=D\n')

#LCL
    outputFile.write('@R14\n')
    outputFile.write('D=M\n')

    outputFile.write('@4\n')
    outputFile.write('D=D-A\n')

    outputFile.write('A=D\n')
    outputFile.write('D=M\n')

    outputFile.write('@LCL\n')
    outputFile.write('M=D\n')

#goto terAddr
    outputFile.write('@R15\n')
    outputFile.write('A=M\n')

    outputFile.write('0;JMP\n')

#####################################################################
#####################################################################
#####################################################################

def translate(text, outputFile, fileName):

    global counter
    global cnt

    for line in text.splitlines():
        args = line.split(" ")
       
        if(args[0] == 'add'):
            addAddAsmInstruction(outputFile)
        elif(args[0] == 'sub'):
            addSunbtractionInstruction(outputFile)
        elif(args[0] == 'neg'):
            addNegInstruction(outputFile)
        elif(args[0] == 'eq'):
            addEqInstruction(outputFile, str(counter))
            counter += 1
        elif(args[0] == 'gt'):
            addGtInstruction(outputFile, str(counter))
            counter += 1
        elif(args[0] == 'lt'):
            addLtInstruction(outputFile, str(counter))
            counter += 1
        elif(args[0] == 'and'):
            addAndInstruction(outputFile)
        elif(args[0] == 'or'):
            addOrInstruction(outputFile)
        elif(args[0] == 'not'):
            addNotInstruction(outputFile)

            
        elif(args[0] == 'push'):
            if(args[1] == 'constant'):
                addPushConstantInstruction(args[2], outputFile)
            elif(args[1] == 'local'):
                addPushInstruction('1', args[2], outputFile)
            elif(args[1] == 'argument'):
                addPushInstruction('2', args[2], outputFile)
            elif(args[1] == 'this'):
                addPushInstruction('3', args[2], outputFile)
            elif(args[1] == 'that'):
                addPushInstruction('4', args[2], outputFile)
            elif(args[1] == 'static'):
                addStaticPushInstruction(fileName, args[2], outputFile)
            elif(args[1] == 'temp'):
                addTempPushInstruction('5', args[2], outputFile)
            elif(args[1] == 'pointer'):
                if(args[2] == '0'):
                    addThisThatPushInstruction('3', outputFile)
                else:
                    addThisThatPushInstruction('4', outputFile)
                
                
        elif(args[0] == 'pop'):
            if(args[1] == 'local'):
                addPopInstruction('1', args[2], outputFile)
            elif(args[1] == 'argument'):
                addPopInstruction('2', args[2], outputFile)
            elif(args[1] == 'this'):
                addPopInstruction('3', args[2], outputFile)
            elif(args[1] == 'that'):
                addPopInstruction('4', args[2], outputFile)
            elif(args[1] == 'static'):
                addStaticPopInstruction(fileName, args[2], outputFile)
            elif(args[1] == 'temp'):
                addTempPopInstruction('5', args[2], outputFile)
            elif(args[1] == 'pointer'):
                if(args[2] == '0'):
                    addThisThatPopInstruction('3', outputFile)
                else:
                    addThisThatPopInstruction('4', outputFile)


        elif(args[0] == 'label'):
            addLabelInstruction(outputFile, args[1])
        elif(args[0] == 'goto'):
            addGotoInstruction(outputFile, args[1])
        elif(args[0] == 'if-goto'):
            addIfgoInstruction(outputFile, args[1])
        

        elif(args[0] == 'call'): #call function
            addCallFunctionInstruction(args[1], args[2], outputFile, str(cnt))
            cnt += 1
        elif(args[0] == 'function'):
            addFunctionInstruction(args[1], args[2], outputFile)
        elif(args[0] == 'return'):
            addReturnInstruction(outputFile)

            
def initializeAtStart(outputFile):
    outputFile.write('@256\n')
    outputFile.write('D=A\n')
    outputFile.write('@SP\n')
    outputFile.write('M=D\n')

    addCallFunctionInstruction('Sys.init', '0', outputFile, '') 

def removeWhitespaces(text):
    
    textWithoutWhitespaces = ''
    
    for line in text.splitlines():
        if(line.strip() != "" and line[0] != '/'):
            textWithoutWhitespaces += line
            textWithoutWhitespaces += '\n'

    return textWithoutWhitespaces

def runVmTranslator(fullPath, outputFile, fileName):

    text = open(fullPath, "r").read()
    
    text = removeWhitespaces(text)

    translate(text, outputFile, fileName)


#Takes as second argument path to the file directory and 
#as thirs argument the ---.vm file
if __name__=="__main__":
    
    if(len(sys.argv) == 3): #if given third argument - filename 

        pathToTheDirectory = sys.argv[1]
        fileName = sys.argv[2]
    
        #Find out full path 
        fullPath = pathToTheDirectory + '/' + fileName 

        fileName = fileName[:len(fileName) - 3] + '.asm'

        pathToOutputFile = pathToTheDirectory + '/' + fileName
        
        outputFile = open(pathToOutputFile, 'w')

        runVmTranslator(fullPath, outputFile, fileName)

    else: #if not it means that given directory
        
        pathToTheDirectory = sys.argv[1]

        elems = pathToTheDirectory.split("/")

        directoryName = elems[1]

        directoryName = directoryName + '.asm'

        pathToOutputFile = pathToTheDirectory + '/' + directoryName
        
        outputFile = open(pathToOutputFile, 'w')

        if (os.listdir(sys.argv[1]).__contains__('Sys.vm')):
            initializeAtStart(outputFile)
            runVmTranslator(pathToTheDirectory + '/' + 'Sys.vm', outputFile, '')

        for curFile in os.listdir(sys.argv[1]):

            if(curFile[len(curFile) - 3 :] == '.vm' and curFile != 'Sys.vm'):
                fileName = curFile
                
                #Find out full path 
                fullPath = pathToTheDirectory + '/' + fileName
                
                runVmTranslator(fullPath, outputFile, fileName)


