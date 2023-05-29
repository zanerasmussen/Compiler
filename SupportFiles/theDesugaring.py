from DesugaringVisitors.DataSegmentVisitor import *
from DesugaringVisitors.MainVisitor import *
from DesugaringVisitors.TempVarCreateVisitor import *
from DesugaringVisitors.TerminalVisitor import *
from DesugaringVisitors.VariableDeclarationVisitor import *
from DesugaringVisitors.ExEqualEx2Visitor import *
from DesugaringVisitors.EPlusEVisitor import *
from DesugaringVisitors.ExpressionParenVisitor import *


from DesugaringVisitors.COUTVisitor import *


from DesugaringVisitors.TCODE import *


def desugar(parsed_AST, symbolTable):

    dataSeg = DataSegmentVisitor()
    dataSeg.symbolTable = symbolTable
    parsed_AST.accept(dataSeg)

    mainVisitor = MainVisitor(dataSeg.dataSeg, dataSeg.TerminalID, dataSeg.counter)
    parsed_AST.accept(mainVisitor)

    tempVarCreate = TempVarCreateVisitor(mainVisitor.dataSeg, mainVisitor.TerminalIDS, mainVisitor.temp_counter, mainVisitor.temporary_symbol_table, mainVisitor.instructionLables)
    parsed_AST.accept(tempVarCreate)

    terminalVisitor = TerminalVisitor(tempVarCreate.dataSeg, tempVarCreate.TerminalIDS, tempVarCreate.temp_counter, tempVarCreate.temporary_symbol_table, tempVarCreate.instructionLables)
    parsed_AST.accept(terminalVisitor)

    variableDeclarationVisit =VariableDeclarationVisitor(terminalVisitor.dataSeg, terminalVisitor.TerminalIDS, terminalVisitor.temp_counter, terminalVisitor.temporary_symbol_table, terminalVisitor.instructionLables)
    parsed_AST.accept(variableDeclarationVisit)

    ExEqualEx2Visit = ExEqualEx2Visitor(variableDeclarationVisit.dataSeg, variableDeclarationVisit.TerminalIDS, variableDeclarationVisit.temp_counter, variableDeclarationVisit.temporary_symbol_table, variableDeclarationVisit.instructionLables)
    parsed_AST.accept(ExEqualEx2Visit)

    EPlusEVisit = EPlusEVisitor(ExEqualEx2Visit.dataSeg, ExEqualEx2Visit.TerminalIDS, ExEqualEx2Visit.temp_counter, ExEqualEx2Visit.temporary_symbol_table, ExEqualEx2Visit.instructionLables)
    parsed_AST.accept(EPlusEVisit)

    EParenVisit = ExpressionParenVisitor(EPlusEVisit.dataSeg, EPlusEVisit.TerminalIDS, EPlusEVisit.temp_counter, EPlusEVisit.temporary_symbol_table, EPlusEVisit.instructionLables)
    parsed_AST.accept(EParenVisit)





    coutVisit = COUTVisitor(EPlusEVisit.dataSeg, EPlusEVisit.TerminalIDS, EPlusEVisit.temp_counter, EPlusEVisit.temporary_symbol_table, EPlusEVisit.instructionLables)
    parsed_AST.accept(coutVisit)

    TCODEgenerate = TCODE()
    TCODEgenerate.dataSeg = dataSeg.dataSeg
    parsed_AST.accept(TCODEgenerate)

    
    tcode = '\n'.join((dataSeg.dataSeg + TCODEgenerate.TCODE))
    print(tcode)

    with open(r"C:\Users\zanea\OneDrive\Documents\School\Fall 2022\CS 4380\VM\VM\Project1\desugar.asm", 'w') as file:
        file.write(tcode)
    # tmp = []
    # for x in TCODEgenerate.TCODE:
    #     tmp += x

    # TCODEgenerate.TCODE = tmp
    #print(TCODEgenerate.TCODE)
