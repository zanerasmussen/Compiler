import sys
from SupportFiles.mainHelper import *
from SupportFiles.theLexer import *
from SupportFiles.theParser import *
from SupportFiles.theSemantics import *

def main(argv):
    if len(argv) == 0:
        file = open(".\TestFiles\BGrade.kxi", "r")
        file = file.read()
        tokens = theLexerReturnFucntion(file)
        parsed = Parse(file)
        semantics(parsed)
        print("Done")
        

    elif argv[0] == '-l':
        DoLexer() 

    elif argv[0] == '-p':
        DoParser()
        
    elif argv[0] == '-s':
        DoSemantics()

    else:
        try:
            file = open(sys.argv[0], "r")
            file = file.read()
            theLexerPrintFunction(file)
        except:
            print("Unable to open file")



if __name__ == "__main__":

    main(sys.argv[1:])