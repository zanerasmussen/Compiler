from SymbolTableVisitor import SymbolTableVisitor
from PrintVisitor import PrintDotVisitor
import sys

def semantics(parsed_AST):
    symbolTable = SymbolTableVisitor()
    parsed_AST.accept(symbolTable)
    if symbolTable.has_Error == True:
        for x in symbolTable.errors:
            print(x)
        sys.exit(1)
    
    #undeclaredVariableVistior = UndeclaredVisitor()
    print("semantics")
    
