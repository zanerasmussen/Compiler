import sys
from SupportFiles.mainHelper import *
from SupportFiles.theLexer import *
from SupportFiles.theParser import *
from SupportFiles.theSemantics import *
from SupportFiles.theDesugaring import *

def main(argv):
    if len(argv) == 0:
        file = open(".\TestFiles\desugar.kxi", "r")
        file = file.read()
        tokens = theLexerReturnFucntion(file)
        parsed = Parse(file)
        symbols = semantics(parsed)
        desugar(parsed, symbols)
        

    elif argv[0] == '-l':
        DoLexer() 

    elif argv[0] == '-p':
        DoParser()
        
    elif argv[0] == '-s':
        DoSemantics()

    elif argv[0] == '-c':
        DoDesugaring()

    else:
        try:
            file = open(sys.argv[0], "r")
            file = file.read()
            theLexerPrintFunction(file)
        except:
            print("Unable to open file")



if __name__ == "__main__":

    main(sys.argv[1:])