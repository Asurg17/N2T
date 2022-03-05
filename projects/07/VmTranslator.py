import sys
from collections import Counter

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
    outputFile.write('//gt\n')

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

def addStaticOrTempPushInstruction(baseIndex, index, outputFile):
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

def addStaticOrTempPopInstruction(baseIndex, index, outputFile):
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
#####################################################################

def translate(text, pathToOutputFile):

    outputFile = open(pathToOutputFile, 'w')

    counter = 0

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
                addStaticOrTempPushInstruction('16', args[2], outputFile)
            elif(args[1] == 'temp'):
                addStaticOrTempPushInstruction('5', args[2], outputFile)
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
                addStaticOrTempPopInstruction('16', args[2], outputFile)
            elif(args[1] == 'temp'):
                addStaticOrTempPopInstruction('5', args[2], outputFile)
            elif(args[1] == 'pointer'):
                if(args[2] == '0'):
                    addThisThatPopInstruction('3', outputFile)
                else:
                    addThisThatPopInstruction('4', outputFile)

        
def removeWhitespaces(text):
    
    textWithoutWhitespaces = ''
    
    for line in text.splitlines():
        if(line.strip() != "" and line[0] != '/'):
            textWithoutWhitespaces += line
            textWithoutWhitespaces += '\n'

    return textWithoutWhitespaces

def runVmTranslator(fullPath, fileName, pathToTheDirectory):

    text = open(fullPath, "r").read()
    
    text = removeWhitespaces(text)

    outputFile = ''
    for i in range(len(fileName)-3):
        outputFile += fileName[i]

    outputFile += '.asm'

    translate(text, pathToTheDirectory + '/' + outputFile) 


#Takes as second argument path to the file directory and 
#as thirs argument the ---.vm file
if __name__=="__main__":
    
    pathToTheDirectory = sys.argv[1]
    fileName = sys.argv[2]
    
    #Find out full path 
    fullPath = pathToTheDirectory + '/' + fileName 
    runVmTranslator(fullPath, fileName, pathToTheDirectory)