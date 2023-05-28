from SemanticsVisitors.CreateSymbolTableVisitor import SymbolTableVisitor
from SemanticsVisitors.UndeclaredVisitor import UndeclaredVisitor
from SemanticsVisitors.TypeChecking import TypeChecking
from SemanticsVisitors.AssignmentVisitor import AssignmentVisitor
from SemanticsVisitors.BreakVisitor import BreakVisitor
import sys

def semantics(parsed_AST):
    symbolTable = SymbolTableVisitor()
    parsed_AST.accept(symbolTable)
    if len(symbolTable.errors) != 0:
        for x in symbolTable.errors:
            print(x)
        sys.exit(1)

    undeclared = UndeclaredVisitor()
    undeclared.oldSymbols = symbolTable.symbol_tables
    parsed_AST.accept(undeclared)
    if len(undeclared.errors) != 0:
        for x in undeclared.errors:
            print(x)
        sys.exit(2)

    typeCheck = TypeChecking()
    typeCheck.paramList = symbolTable.paramList
    typeCheck.symbol_tables = symbolTable.symbol_tables
    parsed_AST.accept(typeCheck)
    if len(typeCheck.errors) != 0:
        for x in typeCheck.errors:
            print(x)
        sys.exit(3)

    assignmentCheck = AssignmentVisitor()
    assignmentCheck.paramList = symbolTable.paramList
    assignmentCheck.symbol_tables = symbolTable.symbol_tables
    parsed_AST.accept(assignmentCheck)
    if len(assignmentCheck.errors) != 0:
        for x in assignmentCheck.errors:
            print(x)
        sys.exit(4)

    breakReturn = BreakVisitor()
    parsed_AST.accept(breakReturn)
    if len(breakReturn.errors) != 0:
        for x in breakReturn.errors:
            print(x)
        sys.exit(5)

    return symbolTable.symbol_tables
    
 