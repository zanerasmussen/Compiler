from SymbolTableVisitor import SymbolTableVisitor
from PrintVisitor import PrintDotVisitor
from UndeclaredVarVistitor import *
import sys

def semantics(parsed_AST):
    symbolTable = SymbolTableVisitor()
    parsed_AST.accept(symbolTable)
    if symbolTable.has_Error == True:
        for x in symbolTable.errors:
            print(x)
        sys.exit(1)
    symbols = symbolTable.symbol_tables
    undeclaredVariableVistior = UndeclaredVisitor()
    undeclaredVariableVistior.symbols = symbols
    parsed_AST.accept(undeclaredVariableVistior)
    print("semantics")
    
