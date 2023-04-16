from SymbolTableVisitor import SymbolTableVisitor
from PrintVisitor import PrintDotVisitor
import sys

def semantics(parsed_AST):
    symbolTable = SymbolTableVisitor()
    parsed_AST.accept(symbolTable)
    if symbolTable.has_Error == True:
        sys.exit(1)
    print("semantics")
    



    # def create_symbol(name: str, type, offset: int, isPrivate: bool, isPublic: bool, hasIndex: bool) -> Symbol:
    #     return Symbol(name=name, type=type, offset=offset, isPrivate=isPrivate, isPublic=isPublic, hasIndex=hasIndex)
