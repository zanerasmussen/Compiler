from AbstractVisitor import ASTVisitor
from AST import *

class MainVisitor(ASTVisitor):
    def __init__(self, dataSeg, TerminalID, counter):
        self.dataSeg = dataSeg
        self.TerminalIDS = TerminalID
        self.temp_counter = counter
        self.temporary_symbol_table = []
        self.instructionLables = []

    def get_label(self):
        pass

    def get_temp_variable(self):
        temp_var = f"${self.temp_counter}"
        self.temp_counter += 1
        return temp_var

    def add_line_asm(self, node, param1, param2, param3, param4):
        node.asm.extend([f"{param1:<15} {param2:<15} {param3:<15} {param4:<15}"])


    def pre_visit_CompilationUnit(self, node: ASTCompilationUnit): 
        self.add_line_asm(node, " ", "JMP", "MAIN", " ")
        self.add_line_asm(node, "PRINT", "LDB", "R3,", "R0")
        self.add_line_asm(node, " ", "BRZ", "R3,", "PRNTEND")
        self.add_line_asm(node, " ", "TRP", "#3", " ")        
        self.add_line_asm(node, " ", "ADI", "R0,", "#1")
        self.add_line_asm(node, " ", "JMP", "PRINT", " ")
        self.add_line_asm(node, ";", " ", " ", " ")
        self.add_line_asm(node, "PRNTEND", "JMR", "R7", " ")   
        self.add_line_asm(node, ";", " ", " ", " ")
        self.add_line_asm(node, "$CMPTRUE", "MOVI", "R10,", "#1")
        self.add_line_asm(node, " ", "JMR", "R7", " ")
        self.add_line_asm(node, "$CMPFALSE", "MOVI", "R10,", "#0")
        self.add_line_asm(node, " ", "JMR", "R7", " ")
        self.add_line_asm(node, "$POSITIVE", "MULI", "R9,", "#-1")
        self.add_line_asm(node, " ", "JMR", "R7", " ")
        self.add_line_asm(node, "$NEGATEZERO", "ADI", "R9,", "#1")
        self.add_line_asm(node, " ", "JMR", "R7", " ")
        self.add_line_asm(node, "$NEGATEONE", "MOVI", "R9,", "#0")
        self.add_line_asm(node, " ", "JMR", "R7", " ")
        self.add_line_asm(node, "MAIN", "ADI", "R8,", "#0")

        if node.MethodBody.MultipleStatement.Statement != None:
            pass
            #self.instructionLables.append((node.MethodBody.MultipleStatement.Statement, "MAIN"))
        else:        
            self.add_line_asm(node, "MAIN", "ADI", "R8,", "#0")


