from SymbolTableVisitor import SymbolTableVisitor
from UndeclaredVarVistitor import *
from ObjectInitializerAndTypeVisitor import ObjectInitializerAndTypeVisitor
from TypeParamModifierVistior import TypeParamModifierVistior
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
    undeclaredVariableVistior.oldSymbols = symbols
    parsed_AST.accept(undeclaredVariableVistior)
    if undeclaredVariableVistior.has_Error == True:
        for x in undeclaredVariableVistior.errors:
            print(x)
        sys.exit(2)
    parameters = undeclaredVariableVistior.paramList

    objectInitializerAndTypeVisitor = ObjectInitializerAndTypeVisitor()
    objectInitializerAndTypeVisitor.symbol_tables = symbols
    parsed_AST.accept(objectInitializerAndTypeVisitor)
    if objectInitializerAndTypeVisitor.has_Error == True:
        for x in objectInitializerAndTypeVisitor.errors:
            print(x)
        sys.exit(3)

    typeParamModifierVistior = TypeParamModifierVistior()
    typeParamModifierVistior.symbolTable = symbols
    typeParamModifierVistior.paramList = parameters
    parsed_AST.accept(typeParamModifierVistior)
    if typeParamModifierVistior.has_Error == True:
        for x in typeParamModifierVistior.errors:
            print(x)
        sys.exit(5)

    print("semantics")
    
 