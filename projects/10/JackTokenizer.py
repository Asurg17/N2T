import sys
import os
from collections import Counter


class JackTokenizer:

    keywords = ["class", "constructor", "function", "method", "field", "static",
            "var", "int", "char", "boolean", "void", "true", "false", "null",
            "this", "let", "do", "if", "else", "while", "return"]
        
    symbols = ['{', '}', '(', ')', '[', ']', '.', ',', ';', '+', '-', '*', 
            '/', '&', '|', '<', '>', '=', '~']

    text = "" #text to be tokenized
    tokensString = "" #string to save tokens
    tokens = "" #tokens array

    #######################################################################################

    alocLen = 0
    logLen = 0

    curToken = ""
    tType = ""

    def hasMoreTokens(self):

        if(self.alocLen - 1 > self.logLen):
            return True

        return False

    def tokenType(self):

        return self.tType

    #-------------------------------------

    def keyWord(self):

        return self.curToken

    def symbol(self):

        return self.curToken[0]

    def identifier(self):

        return self.curToken

    def intVal(self):

        return int(self.curToken)

    def stringVal(self):

        return self.curToken

    #------------------------------------

    def getToken(self, line):

        return line


    def getTType(self, line):

        return line[1:len(line)-2]


    def advance(self):
        
        counter = self.logLen

        #print(counter)

        line1 = self.tokens[counter]
        line2 = self.tokens[counter + 1]
        # line3 = tokens[counter + 2]

        self.logLen += 3

        self.tType = self.getTType(line1) 

        self.curToken = self.getToken(line2)



    #######################################################################################


    def removeWhitespaces(self, txt):
        
        textWithoutWhitespaces = ''
        
        for line in txt.splitlines():
            
            if(line.strip() != "" and line[0] != '/'):
            
                textWithoutWhitespaces += line
                textWithoutWhitespaces += '\n'

        return textWithoutWhitespaces

    def removeSideCommnets(self, txt):

        newText = ""
        
        isStr = False
        
        for line in txt.splitlines():

            index = 0

            counter = 0

            for i in range(len(line)):

                if(line[i] != ' '):
                    counter += 1
                
                if(i != len(line) - 1 and (not isStr) and 
                ((line[i] == '/' and line[i+1] == '/') or (line[i] == '/' and line[i+1] == '*') or (line[i] == '*' and counter == 1))):
                    
                    break
                
                elif(line[i] == '"' and isStr):
                
                    isStr = False
                
                elif(line[i] == '"' and (not isStr)):
                
                    isStr = True

                index += 1

            newText += line[:index]
            newText += "\n"

        return newText
            

    def init(self, pathToTheFile):

        txt = open(pathToTheFile, "r").read()
        
        self.text = self.removeWhitespaces(txt)

        self.text = self.removeSideCommnets(self.text)

    def initTokensString(self):

        identifier = ""
        string = ""
        integer = ""
        
        isStringConstant = False

        for i in range(len(self.text)):
        
            if(self.text[i] != '\n' and self.text[i] != '\t'):
                
                if(self.text[i] == '"'):
                    
                    if(isStringConstant):

                        isStringConstant = False    

                        self.tokensString += "<stringConstant> \n"
                        self.tokensString += string + "\n"
                        self.tokensString += " </stringConstant>\n"

                        string = ""

                    else:
                        
                        isStringConstant = True

                elif(isStringConstant):
                    
                    string += self.text[i]

                elif((not self.text[i].isalpha()) and (not self.text[i].isdigit())):

                    if(self.text[i] == '_'):

                        identifier += self.text[i]

                        continue

                    elif(len(identifier) != 0):
                        
                        if(identifier in self.keywords):
                            
                            self.tokensString += "<keyword> \n"
                            self.tokensString += identifier +  "\n"
                            self.tokensString += " </keyword>\n"

                        else:

                            self.tokensString += "<identifier> \n"
                            self.tokensString += identifier + "\n"
                            self.tokensString += " </identifier>\n"

                        identifier = ""

                    elif(len(integer) != 0):
                        
                        self.tokensString += "<integerConstant> \n" 
                        self.tokensString += integer + "\n" 
                        self.tokensString += " </integerConstant>\n"

                        integer = ""
                    
                    if(self.text[i] in self.symbols):
                        
                        ch = self.text[i]
                        
                        if(self.text[i] == '>'):
                            
                            ch = "&gt;"
                        
                        elif(self.text[i] == '<'):

                            ch = "&lt;"

                        elif(self.text[i] == '&'):

                            ch = "&amp;"

                        elif(self.text[i] == '"'):

                            ch = "&quot;"
                        
                        self.tokensString += "<symbol> \n"
                        self.tokensString += ch + "\n"
                        self.tokensString += " </symbol>\n"
                
                elif(self.text[i].isdigit()):

                    if(len(identifier) == 0):
                        
                        integer += self.text[i]

                    else:

                        identifier += self.text[i]

                elif(self.text[i].isalpha()):
                    
                    identifier += self.text[i]


    def initialize(self, pathToTheFile):

        self.init(pathToTheFile)

        self.initTokensString()

        self.tokens = self.tokensString.splitlines()

        # print(self.tokens)

    #---Initialize

        self.alocLen = len(self.tokens)

        self.logLen = 0

        self.curToken = ""

        self.tType = ""

        # print(self.tokens)
        # print(len(self.tokens))      



            