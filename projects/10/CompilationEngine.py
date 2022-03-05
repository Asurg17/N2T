import sys
import os
import JackTokenizer
from collections import Counter


class CompilationEngine:

    statements = ['let', 'if', 'do', 'return', 'while']
    types = ['int', 'boolean', 'char']
    op = ['+', '-', '*', '/', '&amp;', '|', '&lt;', '&gt;', '=']
    unaryOp = ['~', '-']
    keywordConstant = ['true', 'false', 'null', 'this']


    output = ""
    tabs = ""

####################################################################################################################

    def putLine(self):
        self.output += self.tabs + '\t<' + self.tokenizer.tType + '> ' + self.tokenizer.curToken + ' </' + self.tokenizer.tType + '>\n'
        self.tokenizer.advance()

####################################################################################################################        
####################################################################################################################
####################################################################################################################


    def compileExpressionList(self):
        
        self.output += self.tabs + '<expressionList>\n'

        if(self.tokenizer.curToken != ')'):

            self.tabs += "\t"
            self.compileExpression()

            while(True):

                if(self.tokenizer.curToken == ','):
                    self.putLine()

                    self.tabs += "\t"
                    self.compileExpression()
                
                else:

                    break

        self.output += self.tabs + '</expressionList>\n'

        self.tabs = self.tabs[:len(self.tabs)-1]


    def compileTerm(self):
        
        self.output += self.tabs + '<term>\n'
        
        if(self.tokenizer.tType == 'stringConstant' or self.tokenizer.tType == 'integerConstant' or self.tokenizer.tType == 'keyword'):
           self.putLine()
        
        elif(self.tokenizer.tType == 'identifier'):

            savedType = self.tokenizer.tType
            savedToken = self.tokenizer.curToken

            self.output += self.tabs + '\t<' + savedType + '> ' + savedToken + ' </' + savedType + '>\n'
            self.tokenizer.advance()

            if(self.tokenizer.curToken == '['):
                
                self.putLine()
                
                self.tabs += "\t"
                self.compileExpression()
                
                if(self.tokenizer.curToken == ']'):
                    self.putLine()

            elif(savedToken in self.unaryOp):

                self.tabs += "\t"
                self.compileTerm()

            elif(self.tokenizer.curToken == '('):
    
                self.putLine()
                
                self.tabs += "\t"
                self.compileExpressionList()

                if(self.tokenizer.curToken == ')'):
                    self.putLine()

            elif(self.tokenizer.curToken == '.'):
                
                self.putLine()

                if(self.tokenizer.tType == 'identifier'):
                    self.putLine()       

                if(self.tokenizer.curToken == '('):    
                    self.putLine()

                self.tabs += "\t"
                self.compileExpressionList()

                if(self.tokenizer.curToken == ')'):
                    self.putLine()

        elif(self.tokenizer.curToken in self.unaryOp):
            self.putLine()

            self.tabs += "\t"
            self.compileTerm()

        elif(self.tokenizer.tType == 'symbol'):
            
            if(self.tokenizer.curToken == '('):
                self.putLine()

                self.tabs += "\t"
                self.compileExpression()

                if(self.tokenizer.curToken == ')'):
                    self.putLine()

        self.output += self.tabs + '</term>\n'

        self.tabs = self.tabs[:len(self.tabs)-1]


    def compileExpression(self):
        
        self.output += self.tabs + '<expression>\n'
        
        self.tabs += "\t"
        self.compileTerm()

        while(True):

            if(self.tokenizer.curToken in self.op):
                self.putLine()

                self.tabs += "\t"
                self.compileTerm()
            
            else:
               
                break

        self.output += self.tabs + '</expression>\n'

        self.tabs = self.tabs[:len(self.tabs)-1]

####################################################################################################################        
####################################################################################################################
####################################################################################################################

    def compileReturnStatement(self):
        
        self.output += self.tabs + '<returnStatement>\n'

        if(self.tokenizer.curToken == 'return'):
            self.putLine()    

        if(self.tokenizer.curToken == ';'):
            self.putLine()
        
        else:
            
            self.tabs += "\t"
            self.compileExpression()
            
            if(self.tokenizer.curToken == ';'):
                self.putLine()

        self.output += self.tabs + '</returnStatement>\n'

        self.tabs = self.tabs[:len(self.tabs)-1]

    
    def compileDoStatement(self):
        
        self.output += self.tabs + '<doStatement>\n'

        if(self.tokenizer.curToken == 'do'):
            self.putLine() 

        if(self.tokenizer.tType == 'identifier'):
            self.putLine() 

        if(self.tokenizer.curToken != '('):
            
            if(self.tokenizer.curToken == '.'):
                self.putLine() 

            if(self.tokenizer.tType == 'identifier'):
                self.putLine() 


        if(self.tokenizer.curToken == '('):
            self.putLine()

        self.tabs += "\t"
        self.compileExpressionList()


        if(self.tokenizer.curToken == ')'):
            self.putLine()

        if(self.tokenizer.curToken == ';'):
            self.putLine()    


        self.output += self.tabs + '</doStatement>\n'

        self.tabs = self.tabs[:len(self.tabs)-1]


    def compileWhileStatement(self):

        self.output += self.tabs + '<whileStatement>\n'

        if(self.tokenizer.curToken == 'while'):
            self.putLine()   

        if(self.tokenizer.curToken == '('):
            self.putLine()

        self.tabs += "\t"
        self.compileExpression()

        if(self.tokenizer.curToken == ')'):
            self.putLine()

        if(self.tokenizer.curToken == '{'):
            self.putLine()
        
        self.tabs += "\t"
        self.compileStatements()        

        if(self.tokenizer.curToken == '}'):
            self.putLine()
            
        self.output += self.tabs + '</whileStatement>\n'

        self.tabs = self.tabs[:len(self.tabs)-1]
        

    def compileIfStatement(self):
        
        self.output += self.tabs + '<ifStatement>\n'

        if(self.tokenizer.curToken == 'if'):
            self.putLine()

        if(self.tokenizer.curToken == '('):
            self.putLine()

        self.tabs += "\t"
        self.compileExpression()

        if(self.tokenizer.curToken == ')'):
            self.putLine() 

        if(self.tokenizer.curToken == '{'):
            self.putLine()
        
        self.tabs += "\t"
        self.compileStatements()        

        if(self.tokenizer.curToken == '}'):
            self.putLine()

        if(self.tokenizer.curToken == 'else'):
    
            self.putLine()

            if(self.tokenizer.curToken == '{'):
                self.putLine()

            self.tabs += "\t"
            self.compileStatements()        

            if(self.tokenizer.curToken == '}'):
                self.putLine()

        self.output += self.tabs + '</ifStatement>\n'

        self.tabs = self.tabs[:len(self.tabs)-1]


    def compileLetStatement(self):

        self.output += self.tabs + '<letStatement>\n'

        if(self.tokenizer.curToken == 'let'):
            self.putLine()
        
        if(self.tokenizer.tType == 'identifier'):
            self.putLine()


        if(self.tokenizer.curToken == '['):
            self.putLine()

            self.tabs += "\t"
            self.compileExpression()

            if(self.tokenizer.curToken == ']'):
                self.putLine()


        if(self.tokenizer.curToken == '='):
            self.putLine()

        self.tabs += "\t"
        self.compileExpression()

        if(self.tokenizer.curToken == ';'):
            self.putLine()

        self.output += self.tabs + '</letStatement>\n'
        
        self.tabs = self.tabs[:len(self.tabs)-1]


    def compileStatements(self):

        self.output += self.tabs + '<statements>\n'

        while(self.tokenizer.curToken in self.statements):
            if(self.tokenizer.curToken == 'let'):
                self.tabs += "\t"
                self.compileLetStatement()
            elif(self.tokenizer.curToken == 'while'):
                self.tabs += "\t"
                self.compileWhileStatement()
            elif(self.tokenizer.curToken == 'if'):
                self.tabs += "\t"
                self.compileIfStatement()
            elif(self.tokenizer.curToken == 'do'):
                self.tabs += "\t"
                self.compileDoStatement()
            elif(self.tokenizer.curToken == 'return'):
                self.tabs += "\t"
                self.compileReturnStatement()

        self.output += self.tabs + '</statements>\n'

        self.tabs = self.tabs[:len(self.tabs)-1]
        

####################################################################################################################        
####################################################################################################################
####################################################################################################################


    def compileVarDec(self):
        
        self.output += self.tabs + '<varDec>\n'

        if(self.tokenizer.curToken == 'var'):
            self.putLine()

        if(self.tokenizer.curToken in self.types or self.tokenizer.tType == 'identifier'):
            self.putLine()

        if(self.tokenizer.tType == 'identifier'):
            self.putLine()

        while(True):

            if(self.tokenizer.curToken == ';'):
                self.putLine()
                break
        
            if(self.tokenizer.curToken == ','):
                self.putLine()

            if(self.tokenizer.tType == 'identifier'):
                self.putLine()
        

        self.output += self.tabs + '</varDec>\n'
        self.tabs = self.tabs[:len(self.tabs)-1]


    def compileSubroutineBody(self):
        
        self.output += self.tabs + '<subroutineBody>\n'

        if(self.tokenizer.curToken == '{'):
            self.putLine()  

        while(True):

            if(self.tokenizer.curToken != 'var'):
                break

            self.tabs += "\t"
            self.compileVarDec()

        self.tabs += "\t"
        self.compileStatements()

        if(self.tokenizer.curToken == '}'):
            self.putLine()  

        self.output += self.tabs + '</subroutineBody>\n'
        self.tabs = self.tabs[:len(self.tabs)-1]

    def compileParameterList(self):
        
        self.output += self.tabs + '<parameterList>\n'

        while(True):

            if(self.tokenizer.curToken == ')'):
                break
            
            if(self.tokenizer.curToken in self.types or self.tokenizer.tType == 'identifier'):
                self.putLine()

            if(self.tokenizer.tType == 'identifier'):
                self.putLine()

            if(self.tokenizer.curToken == ','):
                self.putLine()            

        self.output += self.tabs + '</parameterList>\n'
        self.tabs = self.tabs[:len(self.tabs)-1]


    def compileSubroutineDec(self):

        self.output += self.tabs + '<subroutineDec>\n'

        if(self.tokenizer.curToken == 'constructor' or self.tokenizer.curToken == 'function' or self.tokenizer.curToken == 'method'):
            self.putLine()

        if(self.tokenizer.curToken == 'void' or self.tokenizer.curToken in self.types or self.tokenizer.tType == 'identifier'):
            self.putLine()

        if(self.tokenizer.tType == 'identifier'):
            self.putLine()

        if(self.tokenizer.curToken == '('):
            self.putLine()

        self.tabs += "\t"
        self.compileParameterList()        
    
        if(self.tokenizer.curToken == ')'):
            self.putLine()

        self.tabs += "\t"
        self.compileSubroutineBody()

        self.output += self.tabs + '</subroutineDec>\n'
        self.tabs = self.tabs[:len(self.tabs)-1]

    
    def compileClassVarDec(self):
        
        self.output += self.tabs + '<classVarDec>\n'

        if(self.tokenizer.curToken == 'static' or self.tokenizer.curToken == 'field'):
            self.putLine()

        if(self.tokenizer.tType == 'keyword'):
            if(self.tokenizer.curToken in self.types or self.tokenizer.tType == 'identifier'):
                self.putLine()

        while(True):

            if(self.tokenizer.curToken == ';'):
                self.putLine()
                break
            
            if(self.tokenizer.tType == 'identifier'):
                self.putLine()
            
            if(self.tokenizer.curToken == ','):
                self.putLine()
        
        self.output += self.tabs + '</classVarDec>\n'
        self.tabs = self.tabs[:len(self.tabs)-1]


    def compileClass(self):

        self.output += self.tabs + '<class>\n'

        if(self.tokenizer.curToken == 'class'):
            self.putLine()   

        if(self.tokenizer.tType == 'identifier'):
            self.putLine() 
        
        if(self.tokenizer.curToken == '{'):
            self.putLine()

        while(True):

            if(self.tokenizer.curToken != 'static' and self.tokenizer.curToken != 'field'):
                break

            self.tabs += "\t"
            self.compileClassVarDec()

        while(True):

            if(self.tokenizer.curToken != 'constructor' and self.tokenizer.curToken != 'function' and self.tokenizer.curToken != 'method'):
                break            

            self.tabs += "\t"
            self.compileSubroutineDec()
        

        if(self.tokenizer.curToken == '}'):
            self.output += self.tabs + '\t<' + self.tokenizer.tType + '> ' + self.tokenizer.curToken + ' </' + self.tokenizer.tType + '>\n'

        self.output += self.tabs + '</class>\n'

        return 0

    def constructor(self, pathToTheFile):

        self.output = ""

        self.tokenizer = JackTokenizer.JackTokenizer()
        
        self.tokenizer.initialize(pathToTheFile)

        self.tokenizer.advance()
        
        if(self.tokenizer.keyWord() == 'class'):

            self.compileClass()

        # print(self.output)

        return self.output

        #print(self.tokenizer.alocLen/3)

    