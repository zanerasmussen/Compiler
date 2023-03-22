import sys, getopt
from theLexer import *

def main(argv):
#    inputFile = ''
#    opts, args = getopt.getopt(argv,"l")
    if len(argv) == 0:
        file = open("big_parser_test.kxi", "r")
        file = file.read()
        tokens = theLexerPrintFunction(file)
    else:
        try:
            file = open(sys.argv[1], "r")
            file = file.read()
            theLexerPrintFunction(file)
        except:
            print("Unable to open file")

if __name__ == "__main__":
    main(sys.argv[1:])