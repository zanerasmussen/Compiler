from SemanticsVisitors.CreateSymbolTableVisitor import SymbolTableVisitor
from SemanticsVisitors.UndeclaredVisitor import UndeclaredVisitor

def semantics(parsed_AST):
    symbolTable = SymbolTableVisitor()
    parsed_AST.accept(symbolTable)
    if len(symbolTable.errors) != 0:
        for x in symbolTable.errors:
            print(x)
    print("semantics")

    undeclared = UndeclaredVisitor()
    undeclared.oldSymbols = symbolTable.symbol_tables
    parsed_AST.accept(undeclared)
    if len(undeclared.errors) != 0:
        for x in undeclared.errors:
            print(x)

# from SymbolTableVisitor import SymbolTableVisitor
# from UndeclaredVarVistitor import *
# from ObjectInitializerAndTypeVisitor import ObjectInitializerAndTypeVisitor
# from TypeParamModifierVistior import TypeParamModifierVistior
# import sys

# def semantics(parsed_AST):
#     symbolTable = SymbolTableVisitor()
#     parsed_AST.accept(symbolTable)
#     if symbolTable.has_Error == True:
#         for x in symbolTable.errors:
#             print(x)
#         sys.exit(1)
#     parameters = symbolTable.paramList
#     symbols = symbolTable.symbol_tables

#     undeclaredVariableVistior = UndeclaredVisitor()
#     undeclaredVariableVistior.oldSymbols = symbols
#     undeclaredVariableVistior.paramList = parameters
#     parsed_AST.accept(undeclaredVariableVistior)
#     if undeclaredVariableVistior.has_Error == True:
#         for x in undeclaredVariableVistior.errors:
#             print(x)
#         sys.exit(2)

#     objectInitializerAndTypeVisitor = ObjectInitializerAndTypeVisitor()
#     objectInitializerAndTypeVisitor.symbol_tables = symbols
#     parsed_AST.accept(objectInitializerAndTypeVisitor)
#     if objectInitializerAndTypeVisitor.has_Error == True:
#         for x in objectInitializerAndTypeVisitor.errors:
#             print(x)
#         sys.exit(3)

#     # typeParamModifierVistior = TypeParamModifierVistior()
#     # typeParamModifierVistior.symbolTable = symbols
#     # typeParamModifierVistior.paramList = parameters
#     # parsed_AST.accept(typeParamModifierVistior)
#     # if typeParamModifierVistior.has_Error == True:
#     #     for x in typeParamModifierVistior.errors:
#     #         print(x)
#     #     sys.exit(5)

#     print("semantics")
    
 