from SupportFiles.theLexer import *
from SupportFiles.theParser import *
from SupportFiles.theSemantics import *

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

def DoSemantics():
    stuff = input("Enter path to KXI file:")
    file = open(stuff, "r")
    file = file.read()
    tokens = theLexerReturnFucntion(file)
    tokenChecker(tokens)
    myAST = Parse(file)
    semantics(myAST)