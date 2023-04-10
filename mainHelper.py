from theLexer import *
from theParser import *

def DoLexer():
    stuff = input("Enter path to KXI file:") 
    file = open(stuff, "r")
    file = file.read()
    theLexerPrintFunction(file)
    
def DoParser():
    stuff = input("Enter path to KXI file:")
    file = open(stuff, "r")
    file = file.read()
    tokens = theLexerReturnFucntion(file)
    tokenChecker(tokens)
    ParseDotPrinter(file)