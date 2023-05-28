from DesugaringVisitors.DataSegmentVisitor import *
from DesugaringVisitors.MainVisitor import *
from DesugaringVisitors.TempVarCreateVisitor import *
from DesugaringVisitors.TerminalVisitor import *
from DesugaringVisitors.VariableDeclarationVisitor import *
from DesugaringVisitors.COUTVisitor import *
from DesugaringVisitors.ExEqualEx2Visitor import *
from DesugaringVisitors.TCODE import *


def desugar(parsed_AST, symbolTable):

    dataSeg = DataSegmentVisitor()
    dataSeg.symbolTable = symbolTable
    parsed_AST.accept(dataSeg)

    mainVisitor = MainVisitor(dataSeg.dataSeg, dataSeg.TerminalID, dataSeg.counter)
    parsed_AST.accept(mainVisitor)

    tempVarCreate = TempVarCreateVisitor(mainVisitor.dataSeg, mainVisitor.TerminalIDS, mainVisitor.temp_counter, mainVisitor.temporary_symbol_table, mainVisitor.instructionLables)
    parsed_AST.accept(tempVarCreate)

    terminalVisitor = TerminalVisitor(mainVisitor.dataSeg, mainVisitor.TerminalIDS, mainVisitor.temp_counter, mainVisitor.temporary_symbol_table, mainVisitor.instructionLables)
    parsed_AST.accept(terminalVisitor)

    # variableDeclarationVisit =VariableDeclarationVisitor(terminalVisitor.dataSeg, terminalVisitor.TerminalIDS, terminalVisitor.temp_counter, terminalVisitor.temporary_symbol_table, terminalVisitor.instructionLables)
    # parsed_AST.accept(variableDeclarationVisit)

    # coutVisit = COUTVisitor(variableDeclarationVisit.dataSeg, variableDeclarationVisit.TerminalIDS, variableDeclarationVisit.temp_counter, variableDeclarationVisit.temporary_symbol_table, variableDeclarationVisit.instructionLables)
    # parsed_AST.accept(coutVisit)

    coutVisit = COUTVisitor(mainVisitor.dataSeg, mainVisitor.TerminalIDS, mainVisitor.temp_counter, mainVisitor.temporary_symbol_table, mainVisitor.instructionLables)
    parsed_AST.accept(coutVisit)

    # ExEqualEx2Visit = ExEqualEx2Visitor(coutVisit.dataSeg, coutVisit.TerminalIDS, coutVisit.temp_counter, coutVisit.temporary_symbol_table, coutVisit.instructionLables)
    # parsed_AST.accept(ExEqualEx2Visitor)
    #add temp variables to dataSeg

    TCODEgenerate = TCODE()
    TCODEgenerate.dataSeg = dataSeg.dataSeg
    parsed_AST.accept(TCODEgenerate)

    
    tcode = '\n'.join((dataSeg.dataSeg + TCODEgenerate.TCODE))
    print(tcode)
    # tmp = []
    # for x in TCODEgenerate.TCODE:
    #     tmp += x

    # TCODEgenerate.TCODE = tmp
    #print(TCODEgenerate.TCODE)
