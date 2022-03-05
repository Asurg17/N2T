import sys
import os
import JackTokenizer
import CompilationEngine
from collections import Counter


if __name__=="__main__":
    
    if(len(sys.argv) == 0 or len(sys.argv) > 2):
            
        print("Wrong number of arguments ~ Should pass only path!")
        
    else:

        if(os.path.isfile(sys.argv[1])): # file
            
            pathToTheFile = sys.argv[1]

            cmpeng = CompilationEngine.CompilationEngine()

            path = pathToTheFile[0:len(pathToTheFile)-5]+'.vm'

            outputFile = open(path, 'w')

            cmpeng.constructor(outputFile, pathToTheFile)

        else: # directory

            for curFile in os.listdir(sys.argv[1]):
                
                if(curFile[len(curFile)-5 : ] == '.jack'):

                    cmpeng = CompilationEngine.CompilationEngine()

                    path = sys.argv[1] + '/' +  curFile[0:len(curFile) - 5] +'.vm'

                    outputFile = open(path, 'w')

                    cmpeng.constructor(outputFile, sys.argv[1] + '/' + curFile)