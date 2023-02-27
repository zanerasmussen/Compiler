import sys, getopt
from theLexer import *

def main(argv):
    inputFile = ''
    opts, args = getopt.getopt(argv,"l")
    if True:
        file = open("data.txt", "r")
        file = file.read()
        theLexerPrintFunction(file)

if __name__ == "__main__":
    main(sys.argv[1:])