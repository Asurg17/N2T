import sys
import os
from collections import Counter
    

class VMWriter:

    outputFile = ""

    def constructor(self, file):
        self.outputFile = file

    def writePush(self, segment, index):
        if(segment == 'CONST'):
            self.outputFile.write('push constant ' + str(index) + '\n')
        elif (segment == 'ARG'):
            self.outputFile.write('push argument ' + str(index) + '\n')
        elif (segment == 'LOCAL'):
            self.outputFile.write('push local ' + str(index) + '\n')
        elif (segment == 'STATIC'):
            self.outputFile.write('push static ' + str(index) + '\n')
        elif (segment == 'THIS'):
            self.outputFile.write('push this ' + str(index) + '\n') 
        elif (segment == 'THAT'):
            self.outputFile.write('push that ' + str(index) + '\n')
        elif (segment == 'POINTER'):
            self.outputFile.write('push pointer ' + str(index) + '\n')
        elif (segment == 'TEMP'):
            self.outputFile.write('push temp ' + str(index) + '\n')


    def writePop(self, segment, index):
        if (segment == 'ARG'):
            self.outputFile.write('pop argument ' + str(index) + '\n')
        elif (segment == 'LOCAL'):
            self.outputFile.write('pop local ' + str(index) + '\n')
        elif (segment == 'STATIC'):
            self.outputFile.write('pop static ' + str(index) + '\n')
        elif (segment == 'THIS'):
            self.outputFile.write('pop this ' + str(index) + '\n') 
        elif (segment == 'THAT'):
            self.outputFile.write('pop that ' + str(index) + '\n')
        elif (segment == 'POINTER'):
            self.outputFile.write('pop pointer ' + str(index) + '\n')
        elif (segment == 'TEMP'):
            self.outputFile.write('pop temp ' + str(index) + '\n')


    def writeArithmetic(self, command):
        self.outputFile.write(command + '\n')


    def writeLabel(self, label):
        self.outputFile.write('label ' + label + '\n')


    def writeGoto(self, label):
        self.outputFile.write('goto ' + label + '\n')


    def writeIf(self, label):
        self.outputFile.write('if-goto ' + label + '\n')


    def writeCall(self, name, nArgs):
        self.outputFile.write('call ' + name + ' ' + str(nArgs) + '\n')


    def writeFunction(self, name, nLocals):
        self.outputFile.write('function ' + name + ' ' + str(nLocals) + '\n')


    def writeReturn(self):
        self.outputFile.write('return\n')


    def close(self):
        self.outputFile.close()