import sys
import os
import JackTokenizer
import SymbolTable
import VMWriter
from collections import Counter


class CompilationEngine:

    statements = ['let', 'if', 'do', 'return', 'while']
    types = ['int', 'boolean', 'char']
    op = ['+', '-', '*', '/', '&amp;', '|', '&lt;', '&gt;', '=']
    unaryOp = ['~', '-']
    keywordConstant = ['true', 'false', 'null', 'this']


    output = ""
    tabs = ""

    className = ''
    curFName = ''
    count = 0

    whileCount = 0
    ifCount = 0

    func = ''

####################################################################################################################
####################################################################################################################        
####################################################################################################################
####################################################################################################################


    def compileExpressionList(self):

        if(self.tokenizer.curToken != ')'):

            self.compileExpression()

            while(True):

                self.count += 1

                if(self.tokenizer.curToken == ','):
                    self.tokenizer.advance()
                    
                    self.compileExpression()
                
                else:

                    break



    def compileTerm(self):
        
        name = self.tokenizer.curToken
        kind = self.smb.kindOf(name)

        if(self.tokenizer.tType == 'integerConstant'):
            self.writer.writePush('CONST', name)
            self.tokenizer.advance()
        
        elif(self.tokenizer.tType == 'stringConstant'):
           
           size = len(name)

           self.writer.writePush('CONST', size)

           self.writer.writeCall('String.new', 1)

           for ch in name:

               asciiCode = ord(ch)

               self.writer.writePush('CONST', asciiCode)

               self.writer.writeCall('String.appendChar', 2)
            
           self.tokenizer.advance()          

        elif(self.tokenizer.tType == 'keyword'):

            if(self.tokenizer.curToken == 'true'):
                self.writer.writePush('CONST', 1)
                self.writer.writeArithmetic('neg')
            elif(self.tokenizer.curToken == 'false'):
                self.writer.writePush('CONST', 0)
            elif(self.tokenizer.curToken == 'this'):
                self.writer.writePush('POINTER', 0)
            elif(self.tokenizer.curToken == 'that'):
                self.writer.writePush('POINTER', 1)
            elif(self.tokenizer.curToken == 'null'):
                self.writer.writePush('CONST', 0)
            
            self.tokenizer.advance()
        
        elif(self.tokenizer.tType == 'identifier'):

            savedToken = self.tokenizer.curToken

            self.tokenizer.advance()

            if(self.tokenizer.curToken == '['):

                if(kind != 'NONE'):
                    if(kind == 'local'):
                        self.writer.writePush('LOCAL', self.smb.indexOf(savedToken))
                    elif(kind == 'argument'):
                        self.writer.writePush('ARG', self.smb.indexOf(savedToken))
                    elif(kind == 'static'):
                        self.writer.writePush('STATIC', self.smb.indexOf(savedToken))
                    elif(kind == 'field'):
                        self.writer.writePush(kind, self.smb.indexOf(savedToken)) 
                else:
                    print('Variable is not declared')

                self.tokenizer.advance()
                            
                self.compileExpression()

                self.compileExpression()

                self.writer.writeArithmetic('add')

                if(self.tokenizer.curToken == ']'):
                    self.tokenizer.advance()

                self.writer.writePop('POINTER', 1)

                self.writer.writePush('THAT', 0)

            elif(savedToken in self.unaryOp):
           
                self.compileTerm()

            elif(self.tokenizer.curToken == '('):
    
                self.tokenizer.advance()
                               
                self.compileExpressionList()

                if(self.tokenizer.curToken == ')'):
                    self.tokenizer.advance()

            elif(self.tokenizer.curToken == '.'):

                name = savedToken

                if(kind != 'NONE'):
                    savedToken = self.smb.typeOf(savedToken)
                    self.count = 1

                if(kind == 'field'):
                    self.writer.writePush('THIS', self.smb.indexOf(name))
                
                savedToken += self.tokenizer.curToken
                self.tokenizer.advance()

                if(self.tokenizer.tType == 'identifier'):
                    savedToken += self.tokenizer.curToken
                    self.tokenizer.advance()       

                if(self.tokenizer.curToken == '('):    
                    self.tokenizer.advance()
           
                self.compileExpressionList()

                if(self.tokenizer.curToken == ')'):
                    self.tokenizer.advance()

                self.writer.writeCall(savedToken, self.count)

                self.count = 0
            
            else:

                kind = self.smb.kindOf(savedToken)
                
                if(kind != 'NONE'):
                    if(kind == 'local'):
                        self.writer.writePush('LOCAL', self.smb.indexOf(name))
                    elif(kind == 'argument'):
                        self.writer.writePush('ARG', self.smb.indexOf(name))
                    elif(kind == 'static'):
                        self.writer.writePush('STATIC', self.smb.indexOf(name))
                    elif(kind == 'field'):
                        self.writer.writePush('THIS', self.smb.indexOf(name))
                else:
                    print('Variable is not declared')

     
        elif(self.tokenizer.curToken in self.unaryOp):
            
            operation = self.tokenizer.curToken
            
            self.tokenizer.advance()
            
            self.compileTerm()

            if(operation == '-'):
                self.writer.writeArithmetic('neg')
            elif(operation == '~'):
                self.writer.writeArithmetic('not')

        elif(self.tokenizer.tType == 'symbol'):
            
            if(self.tokenizer.curToken == '('):
                self.tokenizer.advance()
                
                self.compileExpression()

                if(self.tokenizer.curToken == ')'):
                    self.tokenizer.advance()


    def compileExpression(self):

        self.compileTerm()

        while(True):

            if(self.tokenizer.curToken in self.op):

                operation = self.tokenizer.curToken

                self.tokenizer.advance()
                
                self.compileTerm()

                if(operation == '&lt;' or operation == '&gt;'):
                    self.writer.writeArithmetic(operation[1:len(operation)-1])
                elif(operation == '+'):
                    self.writer.writeArithmetic('add')
                elif(operation == '/'):
                    self.writer.writeCall('Math.divide', 2)
                elif(operation == '*'):
                    self.writer.writeCall('Math.multiply', 2)
                elif(operation == '-'):
                    self.writer.writeArithmetic('sub')
                elif(operation == '&amp;'):
                    self.writer.writeArithmetic('and')
                elif(operation == '='):
                    self.writer.writeArithmetic('eq')
                elif(operation == '|'):
                    self.writer.writeArithmetic('or')

            else:
               
                break


####################################################################################################################        
####################################################################################################################
####################################################################################################################

    def compileReturnStatement(self):

        if(self.tokenizer.curToken == 'return'):
            self.tokenizer.advance()    

        if(self.tokenizer.curToken == ';'):
            self.writer.writePush('CONST', 0)
            self.tokenizer.advance()
        
        else:
            
            self.compileExpression()
            
            if(self.tokenizer.curToken == ';'):
                self.tokenizer.advance()

        self.writer.writeReturn()

        
    
    def compileDoStatement(self):

        label = ''
        isLocalCall = 0

        if(self.tokenizer.curToken == 'do'):
            self.tokenizer.advance() 

        if(self.tokenizer.tType == 'identifier'):
            label = self.tokenizer.curToken
            self.tokenizer.advance() 
            
        kind = self.smb.kindOf(label)
        name = label

        if(kind != 'NONE'):

            if(kind == 'local'):
                self.writer.writePush('LOCAL', self.smb.indexOf(name))
            elif(kind == 'argument'):
                self.writer.writePush('ARG', self.smb.indexOf(name))
            elif(kind == 'static'):
                self.writer.writePush('STATIC', self.smb.indexOf(name))
            elif(kind == 'field'):
                self.writer.writePush('THIS', self.smb.indexOf(name)) 

            label = self.smb.typeOf(name)

        if(self.tokenizer.curToken != '('):
            
            if(self.tokenizer.curToken == '.'):
                isLocalCall = 1
                label += self.tokenizer.curToken
                self.tokenizer.advance() 

            if(self.tokenizer.tType == 'identifier'):
                label += self.tokenizer.curToken
                self.tokenizer.advance() 


        if(self.tokenizer.curToken == '('):
            self.tokenizer.advance()

        self.count = 0

        if(isLocalCall == 0):
            self.writer.writePush('POINTER', 0)

        self.compileExpressionList()

        if(kind != 'NONE' or isLocalCall == 0):
            self.count += 1

        if(isLocalCall == 0):
            self.writer.writeCall(self.className + '.' + label, self.count)
        else:
            self.writer.writeCall(label, self.count)

        self.count = 0        

        if(self.tokenizer.curToken == ')'):
            self.tokenizer.advance()

        if(self.tokenizer.curToken == ';'):
            self.tokenizer.advance()    

        self.writer.writePop('TEMP', 0)



    def compileWhileStatement(self):

        fcnt = self.whileCount
        self.whileCount += 1

        if(self.tokenizer.curToken == 'while'):
            self.writer.writeLabel('WHILE' + str(fcnt) + '_S')
            self.tokenizer.advance()   

        if(self.tokenizer.curToken == '('):
            self.tokenizer.advance()
  
        self.compileExpression()

        if(self.tokenizer.curToken == ')'):
            self.tokenizer.advance()

        self.writer.writeArithmetic('not')

        self.writer.writeIf('WHILE' + str(fcnt) + '_E')

        if(self.tokenizer.curToken == '{'):
            self.tokenizer.advance()
    
        self.compileStatements()     

        self.writer.writeGoto('WHILE' + str(fcnt) + '_S')  

        self.writer.writeLabel('WHILE' + str(fcnt) + '_E') 

        if(self.tokenizer.curToken == '}'):
            self.tokenizer.advance()
            

    def compileIfStatement(self):

        if(self.tokenizer.curToken == 'if'):
            self.tokenizer.advance()

        if(self.tokenizer.curToken == '('):
            self.tokenizer.advance()
        
        self.compileExpression()

        self.writer.writeArithmetic('not')

        fLab = self.ifCount
        self.writer.writeIf('IF' + str(fLab))
        self.ifCount += 1

        if(self.tokenizer.curToken == ')'):
            self.tokenizer.advance() 

        if(self.tokenizer.curToken == '{'):
            self.tokenizer.advance()
        
        self.compileStatements()  

        sLab = self.ifCount
        self.ifCount += 1      
        
        self.writer.writeGoto('IF' + str(sLab))

        if(self.tokenizer.curToken == '}'):
            self.tokenizer.advance()

        self.writer.writeLabel('IF' + str(fLab))

        if(self.tokenizer.curToken == 'else'):

            self.tokenizer.advance()

            if(self.tokenizer.curToken == '{'):
                self.tokenizer.advance()
     
            self.compileStatements()        

            if(self.tokenizer.curToken == '}'):
                self.tokenizer.advance()

        self.writer.writeLabel('IF' + str(sLab))

        

    def compileLetStatement(self):

        name = ''

        if(self.tokenizer.curToken == 'let'):
            self.tokenizer.advance()
        
        if(self.tokenizer.tType == 'identifier'):
            name = self.tokenizer.curToken
            
            self.tokenizer.advance()


        if(self.tokenizer.curToken == '['):

            self.tokenizer.advance()

            kind = self.smb.kindOf(name)

            if(kind != 'NONE'):
                if(kind == 'local'):
                    self.writer.writePush('LOCAL', self.smb.indexOf(name))
                elif(kind == 'argument'):
                    self.writer.writePush('ARG', self.smb.indexOf(name))
                elif(kind == 'static'):
                    self.writer.writePush('STATIC', self.smb.indexOf(name))
                elif(kind == 'field'):
                    self.writer.writePush('THIS', self.smb.indexOf(name))
            else:
                print('Variable is not declared')
 
            self.compileExpression()

            self.writer.writeArithmetic('add')

            if(self.tokenizer.curToken == ']'):
                self.tokenizer.advance()

            if(self.tokenizer.curToken == '='):
                self.tokenizer.advance()
            
            self.compileExpression()

            self.writer.writePop('TEMP', 0)

            self.writer.writePop('POINTER', 1)

            self.writer.writePush('TEMP', 0)

            self.writer.writePop('THAT', 0)

            if(self.tokenizer.curToken == ';'):
                self.tokenizer.advance()
        
        else:

            if(self.tokenizer.curToken == '='):
                self.tokenizer.advance()
            
            self.compileExpression()

            if(self.tokenizer.curToken == ';'):
                self.tokenizer.advance()

            kind = self.smb.kindOf(name)

            if(kind != 'NONE'):
                if(kind == 'local'):
                    self.writer.writePop('LOCAL', self.smb.indexOf(name))
                elif(kind == 'argument'):
                    self.writer.writePop('ARG', self.smb.indexOf(name))
                elif(kind == 'static'):
                    self.writer.writePop('STATIC', self.smb.indexOf(name))
                elif(kind == 'field'):
                    self.writer.writePop('THIS', self.smb.indexOf(name)) 
            else:
                print('Not declared error!')

      
    def compileStatements(self):

        while(self.tokenizer.curToken in self.statements):
            
            if(self.tokenizer.curToken == 'let'):
                
                self.compileLetStatement()
            
            elif(self.tokenizer.curToken == 'while'):
                
                self.compileWhileStatement()
            
            elif(self.tokenizer.curToken == 'if'):
                
                self.compileIfStatement()
            
            elif(self.tokenizer.curToken == 'do'):
                
                self.compileDoStatement()
            
            elif(self.tokenizer.curToken == 'return'):
                
                self.compileReturnStatement()
        

####################################################################################################################        
####################################################################################################################
####################################################################################################################


    def compileVarDec(self):

        curKind = 'VAR'
        curType = ''
        curName = ''

        if(self.tokenizer.curToken == 'var'):
            self.tokenizer.advance()

        if(self.tokenizer.curToken in self.types or self.tokenizer.tType == 'identifier'):
            curType = self.tokenizer.curToken
            self.tokenizer.advance()

        if(self.tokenizer.tType == 'identifier'):
            curName = self.tokenizer.curToken
            self.smb.define(curName, curType, curKind)
            self.tokenizer.advance()

        while(True):

            if(self.tokenizer.curToken == ';'):
                self.tokenizer.advance()
                break
        
            if(self.tokenizer.curToken == ','):
                self.tokenizer.advance()

            if(self.tokenizer.tType == 'identifier'):
                curName = self.tokenizer.curToken
                self.smb.define(curName, curType, curKind)
                self.tokenizer.advance()


    def compileSubroutineBody(self):

        if(self.tokenizer.curToken == '{'):
            self.tokenizer.advance()  

        while(True):

            if(self.tokenizer.curToken != 'var'):
                break

            self.compileVarDec()

        if(self.func == 'constructor'):
            self.writer.writeFunction(self.className + '.' + self.curFName,  self.smb.varCount('VAR'))
            self.writer.writePush('CONST', self.smb.varCount('FIELD'))
            self.writer.writeCall('Memory.alloc', 1)
            self.writer.writePop('POINTER', 0)
        elif(self.func == 'method'):
            self.writer.writeFunction(self.className + '.' + self.curFName,  self.smb.varCount('VAR'))
            self.writer.writePush('ARG', 0)
            self.writer.writePop('POINTER', 0)
        else:
            self.writer.writeFunction(self.className + '.' + self.curFName,  self.smb.varCount('VAR'))

        self.compileStatements()

        if(self.tokenizer.curToken == '}'):
            self.tokenizer.advance()  


    def compileParameterList(self):

        curKind = 'ARG'
        curType = ''
        curName = ''
        
        while(True):

            if(self.tokenizer.curToken == ')'):
                break
            
            if(self.tokenizer.curToken in self.types or self.tokenizer.tType == 'identifier'):
                curType = self.tokenizer.curToken
                self.tokenizer.advance()

            if(self.tokenizer.tType == 'identifier'):
                curName = self.tokenizer.curToken
                self.smb.define(curName, curType, curKind)
                self.tokenizer.advance()

            if(self.tokenizer.curToken == ','):
                self.tokenizer.advance()            


    def compileSubroutineDec(self):

        self.func = self.tokenizer.curToken

        if(self.func == 'constructor'):
            self.tokenizer.advance()
        elif(self.func== 'method'):
            self.smb.define('this', self.className, 'ARG')
            self.tokenizer.advance()
        elif(self.func == 'function'):
            self.tokenizer.advance()

        if(self.tokenizer.curToken == 'void' or self.tokenizer.curToken in self.types or self.tokenizer.tType == 'identifier'):
            self.tokenizer.advance()

        if(self.tokenizer.tType == 'identifier'):
            self.curFName = self.tokenizer.curToken
            self.tokenizer.advance()

        if(self.tokenizer.curToken == '('):
            self.tokenizer.advance()

        self.compileParameterList()        
    
        if(self.tokenizer.curToken == ')'):
            self.tokenizer.advance()

        self.compileSubroutineBody()

    
    def compileClassVarDec(self):

        curKind = ''
        curType = ''
        curName = ''

        if(self.tokenizer.curToken == 'static' or self.tokenizer.curToken == 'field'):
            curKind = self.tokenizer.curToken
            self.tokenizer.advance()

        if(self.tokenizer.curToken in self.types or self.tokenizer.tType == 'identifier'):
            curType = self.tokenizer.curToken
            self.tokenizer.advance()

        while(True):

            if(self.tokenizer.curToken == ';'):
                self.tokenizer.advance()
                break
            
            if(self.tokenizer.tType == 'identifier'):
                curName = self.tokenizer.curToken
                self.smb.define(curName, curType, curKind)
                self.tokenizer.advance()
            
            if(self.tokenizer.curToken == ','):
                self.tokenizer.advance()


    def compileClass(self):

        if(self.tokenizer.curToken == 'class'):
            self.tokenizer.advance()   

        if(self.tokenizer.tType == 'identifier'):
            self.className = self.tokenizer.curToken
            self.tokenizer.advance() 
        
        if(self.tokenizer.curToken == '{'):
            self.tokenizer.advance()

        while(True):

            if(self.tokenizer.curToken != 'static' and self.tokenizer.curToken != 'field'):
                break

            self.compileClassVarDec()

        while(True):

            if(self.tokenizer.curToken != 'constructor' and self.tokenizer.curToken != 'function' and self.tokenizer.curToken != 'method'):
                break          

            self.smb.startSubroutine()

            self.compileSubroutineDec()
        

    def constructor(self, file, pathToTheFile):

        self.tokenizer = JackTokenizer.JackTokenizer()
        
        self.tokenizer.initialize(pathToTheFile)

        
        self.smb = SymbolTable.SymbolTable()

        self.smb.constructor()


        self.writer = VMWriter.VMWriter()

        self.writer.constructor(file)


        self.tokenizer.advance()
        
        if(self.tokenizer.keyWord() == 'class'):
            
            self.compileClass()

    