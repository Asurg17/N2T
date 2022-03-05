import sys
import os
from collections import Counter


class SymbolTable:

    classSTB = {}
    subroutineSTB = {}

    static = 0
    field = 0
    arg = 0
    var = 0

    def constructor(self):
        self.classSTB = {}
        self.subroutineSTB = {}

        self.static = 0
        self.field = 0
        self.arg = 0
        self.var = 0
        

    def startSubroutine(self):
        self.arg = 0
        self.var = 0

        self.subroutineSTB = {}


    def define(self, name, type, kind):
        if(kind == 'static'):
            self.classSTB[name] = (type, 'static', self.static)
            self.static += 1
        elif(kind == 'field'):
            self.classSTB[name] = (type, 'field', self.field)
            self.field += 1
        elif(kind == 'ARG'):
            self.subroutineSTB[name] = (type, 'argument', self.arg)
            self.arg += 1
        elif(kind == 'VAR'):
            self.subroutineSTB[name] = (type, 'local', self.var)
            self.var += 1


    def varCount(self, kind):
        if(kind == 'STATIC'):
            return self.static
        elif(kind == 'FIELD'):
            return self.field
        elif(kind == 'ARG'):
            return self.arg
        elif(kind == 'VAR'):
            return self.var


    def kindOf(self, name):
        if name in self.classSTB.keys():
            return self.classSTB[name][1]
        elif name in self.subroutineSTB.keys():
            return self.subroutineSTB[name][1]
        else:
            return 'NONE'


    def typeOf(self, name):
        if name in self.classSTB.keys():
            return self.classSTB[name][0]
        elif name in self.subroutineSTB.keys():
            return self.subroutineSTB[name][0]
    

    def indexOf(self, name):
        if name in self.classSTB.keys():
            return self.classSTB[name][2]
        elif name in self.subroutineSTB.keys():
            return self.subroutineSTB[name][2]