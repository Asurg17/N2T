import sys
from collections import Counter

PREDEFINED_SYMBOLS = {"R0":0, "R1":1, "R2":2, "R3":3, "R4":4, "R5":5, "R6":6, "R7":7, "R8":8, "R9":9, "R10":10, "R11":11, "R12":12, "R13":13, 
                      "R14":14, "R15":15, "SCREEN":16384, "KBD":24576, "SP":0, "LCL":1, "ARG":2, "THIS":3, "THAT":4} 

COMPARE_SYMBOLS = {"0":"0101010", "1":"0111111", "-1":"0111010", "D":"0001100", "A":"0110000", "!D":"0001101", "!A":"0110001", "-D":"0001111",
                   "-A":"0110011", "D+1":"0011111", "A+1":"0110111", "D-1":"0001110", "A-1":"0110010", "D+A":"0000010", "D-A":"0010011", "A-D":"0000111",
                   "D&A":"0000000", "D|A":"0010101", "M":"1110000", "!M":"1110001", "-M":"1110011", "M+1":"1110111", "M-1":"1110010", "D+M":"1000010",
                   "D-M":"1010011", "M-D":"1000111", "D&M":"1000000", "D|M":"1010101"}

DEST_SYMBOLS = {"null":"000", "M":"001", "D":"010", "MD":"011", "A":"100", "AM":"101", "AD":"110", "AMD":"111"}

JUMP_SYMBOLS = {"null":"000", "JGT":"001", "JEQ":"010", "JGE":"011", "JLT":"100", "JNE":"101", "JLE":"110", "JMP":"111"}

# Add to symbolTable predefined symbols
symbolTable = PREDEFINED_SYMBOLS

def modify(text):
    modifiedText = ''

    for line in text.splitlines():
        
        size = len(line)
        curLine = ''
        
        for i in range(size):
            if(line[i] == '/'):
                break
            else:
                if(line[i] != ' '):
                    curLine += line[i]

        modifiedText += curLine
        modifiedText += '\n'
    
    return modifiedText


def removeWhitespaces(text):

    textWithoutWhitespaces = ''
    
    for line in text.splitlines():
        if(line.strip() != "" and line[0] != '/'):
            textWithoutWhitespaces += line
            textWithoutWhitespaces += '\n'

    return textWithoutWhitespaces
    

def FirstPass(text, index):
    for line in text.splitlines():
        
        if(line[0] == '('):
            size = len(line)
            label = ''
            
            for i in range(size-1):
                if(line[i+1] == ')'):
                    break
                else:
                    label += line[i+1] 

            symbolTable[label] = index
        
        else:
        
            index = index + 1


def SecondPass(text, n):
    for line in text.splitlines():
        
        if(line[0] == '@'):
            size = len(line)
            variable = ''
            
            for i in range(size):
                if(line[i] != '@'):
                    variable += line[i]

            
            if(not (variable in symbolTable) and not (variable.isnumeric()) ):
                symbolTable[variable] = n
                n = n + 1

def get15BitBinaryNumber(number):
    result = ''
    while number > 0:  
        result = str(number%2) + result
        number = number // 2 

    size = len(result)
    
    neededSize = 15 - size

    for i in range(neededSize):
        result = '0' + result

    return result

def getCIntruction(line):
    dest = 'null'
    comp = ''
    jump = 'null'

    size = len(line)

    if(line[1] == '='):
        dest = line[0]
                   
        i = 2
        while i < size:
            comp += line[i]            
            i+=1                        

    elif(line[2] == '='):
        dest = line[0] + line[1]            

        i = 3
        while i < size:
            comp += line[i]
            i+=1

    elif(line[1] == ';'):
        jump = line[2] + line[3] + line[4]
                    
        comp = line[0]
               
    elif(line[2] == ';'):
        jump = line[3] + line[4] + line[5]
                   
        comp = line[0] + line[1]

    elif(line[3] == '='):
        dest = line[0] + line[1] + line[2]

        i = 4
        while i < size:
            comp += line[i]
            i+=1

    elif(line[3] == ';'):
        jump = line[4] + line[5] + line[6]
                    
        comp = line[0] + line[1] + line[2]

    return dest, comp, jump

def FinalPass(text, pathToOutputFile):
   
    outputFile = open(pathToOutputFile, 'w')

    for line in text.splitlines():
        
        if(line[0] != '('):
            
            if(line[0] == '@'): #A instruction
                number = line[1:len(line)] #line without @
                outputLavue = '0'
                if(number.isnumeric()):
                    outputLavue += get15BitBinaryNumber(int(number))
                else:
                    outputLavue += get15BitBinaryNumber(symbolTable[number])

                outputFile.write(outputLavue)
                outputFile.write('\n')

            else: #C instruction
                dest,comp,jump = getCIntruction(line)
                
                #print(dest, comp, jump)

                outputLavue = '111' + COMPARE_SYMBOLS[comp] +  DEST_SYMBOLS[dest] + JUMP_SYMBOLS[jump]
                
                outputFile.write(outputLavue)
                outputFile.write('\n')




def runAssembler(fullPath, fileName, pathToTheDirectory):
    text = open(fullPath, "r").read()
    
    text = removeWhitespaces(text)

    text = modify(text)

    #At first
    FirstPass(text, 0) #Assign labels
    SecondPass(text, 16) #Assign variables

    outputFile = ''
    for i in range(len(fileName)-4):
        outputFile += fileName[i]

    outputFile += '.hack'

    FinalPass(text, pathToTheDirectory + '/' + outputFile) #Translation
    
    # for line in text.splitlines():
    #     print(line)
    # for elem in symbolTable:
    #     print(elem)
    #     print(symbolTable[elem])


#Takes as second argument path to the file directory and 
#as thirs argument the ---.asm file
if __name__=="__main__":

    pathToTheDirectory = sys.argv[1]
    fileName = sys.argv[2]
    
    #Find out full path 
    fullPath = pathToTheDirectory + '/' + fileName 

    runAssembler(fullPath, fileName, pathToTheDirectory)

