from SymbolTableVisitor import SymbolTableVisitor
from PrintVisitor import PrintDotVisitor

def semantics(parsed_AST):
    symbolTable = SymbolTableVisitor()
    parsed_AST.accept(symbolTable)
