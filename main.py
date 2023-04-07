import sys, getopt
from theLexer import *
from theParser import *

def main(argv):
    if len(argv) == 0:
        file = open("TestFile.kxi", "r")
        file = file.read()
        tokens = theLexerReturnFucntion(file)
        #tokens = theLexerPrintFunction(file)
        parsed = Parse(file)

    elif argv[0] == '-l':
        DoLexer()

    elif argv[0] == '-p':
        DoParser()
        
    else:
        try:
            file = open(sys.argv[0], "r")
            file = file.read()
            theLexerPrintFunction(file)
        except:
            print("Unable to open file")


def DoLexer():
    stuff = input("Enter KXI:")
    theLexerPrintFunction(stuff)

def DoParser():
    stuff = input("Enter KXI:")
    tokens = theLexerReturnFucntion(stuff)
    parsed = ParseDotPrinter(stuff)

if __name__ == "__main__":

    main(sys.argv[1:])