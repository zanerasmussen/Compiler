from AbstractVisitor import ASTVisitor
from AST import *

class COUTVisitor(ASTVisitor):
    def __init__(self, dataSeg, TerminalIDS, counter, temporary_symbol_table, instructionLables):
        self.dataSeg = dataSeg
        self.TerminalIDS = TerminalIDS
        self.temp_counter = counter
        self.temporary_symbol_table = temporary_symbol_table
        self.instructionLables = instructionLables

        #visitor specific

    def add_line_asm(self, node, param1, param2, param3, param4):
        node.asm.extend([f"{param1:<15} {param2:<15} {param3:<15} {param4:<15}"])

    def get_instructionLables_label(self, node: ASTStatementCOUT):
        for x in self.instructionLables:
            if x[0] == node:
                return x[1]
        return ""

    def get_temporary_variable_from_table(self, node):
        for x in self.temporary_symbol_table:
            if x[0] == node:
                return x[1]
 
    def post_visit_StatementCOUT(self, node: ASTStatementCOUT):
        label = self.get_instructionLables_label(node)
        flag = self.get_temporary_variable_from_table(node.Expression)

        if node.type == "int":
            type = 1
            self.add_line_asm(node, f"{label} ", "LDR", "R3,", f"{flag}")
            self.add_line_asm(node, " ", "LDR", "R3,", "R3")
            self.add_line_asm(node, " ", "TRP", f"#{type}", " ")

        elif node.type == "bool" or node.type == "char":
            type = 3
            self.add_line_asm(node, f"{label} ",  "LDR", "R3,", f"{flag}")
            self.add_line_asm(node, " ", "LDB", "R3,", "R3")
            self.add_line_asm(node, " ", "TRP", f"#{type}", " ")

        elif node.type == "string":
            type = 3
            self.add_line_asm(node, f"{label} ",  "LDR", "R0,", f"{flag}")
            self.add_line_asm(node, " ", "MOV", "R7,", "PC")
            self.add_line_asm(node, " ", "ADI", "R7,", "#24")
            self.add_line_asm(node, " ", "JMP", "PRINT", " ")
