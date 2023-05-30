from DesugaringVisitors.DataSegmentVisitor import *
from DesugaringVisitors.MainVisitor import *
from DesugaringVisitors.TempVarCreateVisitor import *
from DesugaringVisitors.TerminalVisitor import *
from DesugaringVisitors.VariableDeclarationVisitor import *
from DesugaringVisitors.ExEqualEx2Visitor import *
from DesugaringVisitors.EPlusEVisitor import *
from DesugaringVisitors.ExpressionParenVisitor import *
from DesugaringVisitors.EMinusEVisitor import *
from DesugaringVisitors.ETimesEVisitor import *
from DesugaringVisitors.EDivideEVisitory import *
from DesugaringVisitors.EPlusEqualEVisitor import *
from DesugaringVisitors.EMinusEqualEVisitor import *
from DesugaringVisitors.ETimesEqualEVisitor import *
from DesugaringVisitors.EDivideEqualEVisitor import *
from DesugaringVisitors.ECompEqualEVisitor import *
from DesugaringVisitors.ENotEqualEVisitor import *
from DesugaringVisitors.ELessEVisitor import *
from DesugaringVisitors.ELessEqualEVisitor import *
from DesugaringVisitors.EGreaterEVisitor import *
from DesugaringVisitors.EGreaterEqualEVisitor import *
from DesugaringVisitors.EAANDEVisitor import *
from DesugaringVisitors.EOOREVisitor import *
from DesugaringVisitors.PlusEVisitor import *
from DesugaringVisitors.MinusEVisitor import *
from DesugaringVisitors.NotEVisitor import *
from DesugaringVisitors.COUTVisitor import *
from DesugaringVisitors.CINVisitor import *
from DesugaringVisitors.StatementExpressionVisitor import *
from DesugaringVisitors.IFVisitor import *

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

    variableDeclarationVisit =VariableDeclarationVisitor(terminalVisitor.dataSeg, terminalVisitor.TerminalIDS, terminalVisitor.temp_counter, terminalVisitor.temporary_symbol_table, terminalVisitor.instructionLables, tempVarCreate.statementLabelStack)
    parsed_AST.accept(variableDeclarationVisit)

    ExEqualEx2Visit = ExEqualEx2Visitor(variableDeclarationVisit.dataSeg, variableDeclarationVisit.TerminalIDS, variableDeclarationVisit.temp_counter, variableDeclarationVisit.temporary_symbol_table, variableDeclarationVisit.instructionLables)
    parsed_AST.accept(ExEqualEx2Visit)

    EParenVisit = ExpressionParenVisitor(ExEqualEx2Visit.dataSeg, ExEqualEx2Visit.TerminalIDS, ExEqualEx2Visit.temp_counter, ExEqualEx2Visit.temporary_symbol_table, ExEqualEx2Visit.instructionLables)
    parsed_AST.accept(EParenVisit)

    EPlusEVisit = EPlusEVisitor(EParenVisit.dataSeg, EParenVisit.TerminalIDS, EParenVisit.temp_counter, EParenVisit.temporary_symbol_table, EParenVisit.instructionLables)
    parsed_AST.accept(EPlusEVisit)

    EMinusEVisit = EMinusEVisitor(EPlusEVisit.dataSeg, EPlusEVisit.TerminalIDS, EPlusEVisit.temp_counter, EPlusEVisit.temporary_symbol_table, EPlusEVisit.instructionLables)
    parsed_AST.accept(EMinusEVisit)

    ETimesEVisit = ETimesEVisitor(EMinusEVisit.dataSeg, EMinusEVisit.TerminalIDS, EMinusEVisit.temp_counter, EMinusEVisit.temporary_symbol_table, EMinusEVisit.instructionLables)
    parsed_AST.accept(ETimesEVisit)

    EDivideEVisit = EDivideEVisitor(ETimesEVisit.dataSeg, ETimesEVisit.TerminalIDS, ETimesEVisit.temp_counter, ETimesEVisit.temporary_symbol_table, ETimesEVisit.instructionLables)
    parsed_AST.accept(EDivideEVisit)

    EPlusEqualEVisit = EPlusEqualEVisitor(EDivideEVisit.dataSeg, EDivideEVisit.TerminalIDS, EDivideEVisit.temp_counter, EDivideEVisit.temporary_symbol_table, EDivideEVisit.instructionLables)
    parsed_AST.accept(EPlusEqualEVisit)

    EMinusEqualEVisit = EMinusEqualEVisitor(EPlusEqualEVisit.dataSeg, EPlusEqualEVisit.TerminalIDS, EPlusEqualEVisit.temp_counter, EPlusEqualEVisit.temporary_symbol_table, EPlusEqualEVisit.instructionLables)
    parsed_AST.accept(EMinusEqualEVisit)

    ETimesEqualEVisit = ETimesEqualEVisitor(EMinusEqualEVisit.dataSeg, EMinusEqualEVisit.TerminalIDS, EMinusEqualEVisit.temp_counter, EMinusEqualEVisit.temporary_symbol_table, EMinusEqualEVisit.instructionLables)
    parsed_AST.accept(ETimesEqualEVisit)
    
    EDivideEqualEVisit = EDivideEqualEVisitor(ETimesEqualEVisit.dataSeg, ETimesEqualEVisit.TerminalIDS, ETimesEqualEVisit.temp_counter, ETimesEqualEVisit.temporary_symbol_table, ETimesEqualEVisit.instructionLables)
    parsed_AST.accept(EDivideEqualEVisit)

    ECompEqualEVisit = ECompEqualEVisitor(EDivideEqualEVisit.dataSeg, EDivideEqualEVisit.TerminalIDS, EDivideEqualEVisit.temp_counter, EDivideEqualEVisit.temporary_symbol_table, EDivideEqualEVisit.instructionLables)
    parsed_AST.accept(ECompEqualEVisit)

    ENotEqualEVisit = ENotEqualEVisitor(ECompEqualEVisit.dataSeg, ECompEqualEVisit.TerminalIDS, ECompEqualEVisit.temp_counter, ECompEqualEVisit.temporary_symbol_table, ECompEqualEVisit.instructionLables)
    parsed_AST.accept(ENotEqualEVisit)

    ELessEVisit = ELessEVisitor(ENotEqualEVisit.dataSeg, ENotEqualEVisit.TerminalIDS, ENotEqualEVisit.temp_counter, ENotEqualEVisit.temporary_symbol_table, ENotEqualEVisit.instructionLables)
    parsed_AST.accept(ELessEVisit)

    ELessEqualEVisit = ELessEqualEVisitor(ELessEVisit.dataSeg, ELessEVisit.TerminalIDS, ELessEVisit.temp_counter, ELessEVisit.temporary_symbol_table, ELessEVisit.instructionLables)
    parsed_AST.accept(ELessEqualEVisit)

    EGreaterEVisit = EGreaterEVisitor(ELessEqualEVisit.dataSeg, ELessEqualEVisit.TerminalIDS, ELessEqualEVisit.temp_counter, ELessEqualEVisit.temporary_symbol_table, ELessEqualEVisit.instructionLables)
    parsed_AST.accept(EGreaterEVisit)

    EGreaterEqualEVisit = EGreaterEqualEVisitor(EGreaterEVisit.dataSeg, EGreaterEVisit.TerminalIDS, EGreaterEVisit.temp_counter, EGreaterEVisit.temporary_symbol_table, EGreaterEVisit.instructionLables)
    parsed_AST.accept(EGreaterEqualEVisit)

    EAANDEVisit = EAANDEVisitor(EGreaterEqualEVisit.dataSeg, EGreaterEqualEVisit.TerminalIDS, EGreaterEqualEVisit.temp_counter, EGreaterEqualEVisit.temporary_symbol_table, EGreaterEqualEVisit.instructionLables)
    parsed_AST.accept(EAANDEVisit)

    EOOREVisit = EOOREVisitor(EAANDEVisit.dataSeg, EAANDEVisit.TerminalIDS, EAANDEVisit.temp_counter, EAANDEVisit.temporary_symbol_table, EAANDEVisit.instructionLables)
    parsed_AST.accept(EOOREVisit)

    PlusEVisit = PlusEVisitor(EOOREVisit.dataSeg, EOOREVisit.TerminalIDS, EOOREVisit.temp_counter, EOOREVisit.temporary_symbol_table, EOOREVisit.instructionLables)
    parsed_AST.accept(PlusEVisit)

    MinusEVisit = MinusEVisitor(PlusEVisit.dataSeg, PlusEVisit.TerminalIDS, PlusEVisit.temp_counter, PlusEVisit.temporary_symbol_table, PlusEVisit.instructionLables)
    parsed_AST.accept(MinusEVisit)

    NotEVisit = NotEVisitor (MinusEVisit.dataSeg, MinusEVisit.TerminalIDS, MinusEVisit.temp_counter, MinusEVisit.temporary_symbol_table, MinusEVisit.instructionLables)
    parsed_AST.accept(NotEVisit)

    coutVisit = COUTVisitor(NotEVisit.dataSeg, NotEVisit.TerminalIDS, NotEVisit.temp_counter, NotEVisit.temporary_symbol_table, NotEVisit.instructionLables, variableDeclarationVisit.statementLabelStack)
    parsed_AST.accept(coutVisit)

    cinVisit = CINVisitor(coutVisit.dataSeg, coutVisit.TerminalIDS, coutVisit.temp_counter, coutVisit.temporary_symbol_table, coutVisit.instructionLables, coutVisit.statementLabelStack)
    parsed_AST.accept(cinVisit)

    StatementExpressionVisit = StatementExpressionVisitor(cinVisit.dataSeg, cinVisit.TerminalIDS, cinVisit.temp_counter, cinVisit.temporary_symbol_table, cinVisit.instructionLables, cinVisit.statementLabelStack)
    parsed_AST.accept(StatementExpressionVisit)

    # IFVisit = IFVisitor(StatementExpressionVisit.dataSeg, StatementExpressionVisit.TerminalIDS, StatementExpressionVisit.temp_counter, StatementExpressionVisit.temporary_symbol_table, StatementExpressionVisit.instructionLables, StatementExpressionVisit.statementLabelStack)
    # parsed_AST.accept(IFVisit)

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
