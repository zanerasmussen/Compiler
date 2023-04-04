import sys, getopt
from theLexer import *
from theParser import *

def main(argv):
    if len(argv) == 0:
        #file = open("big_parser_test.kxi", "r")
        file = open("simpleParserTest.kxi", "r")
        file = file.read()
        tokens = theLexerReturnFucntion(file)
        parsed = Parse(file)

    elif argv[0] == '-l':
        DoLexer()

    # elif argv[0] == '-p':
    #     DoParser()
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

if __name__ == "__main__":

    main(sys.argv[1:])