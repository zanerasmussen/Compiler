from AbstractVisitor import ASTVisitor
from AST import *

class EMinusEqualEVisitor(ASTVisitor):
    def __init__(self, dataSeg, TerminalIDS, counter, temporary_symbol_table, instructionLables):
        self.dataSeg = dataSeg
        self.TerminalIDS = TerminalIDS
        self.temp_counter = counter
        self.temporary_symbol_table = temporary_symbol_table
        self.instructionLables = instructionLables

        #visitor specific

    def add_line_asm(self, node, param1, param2, param3, param4):
        node.asm.extend([f"{param1:<15} {param2:<15} {param3:<15} {param4:<15}"])

    def get_instructionLables_label(self, node):
        for x in self.instructionLables:
            if x[0] == node:
                return x[1]
        return ""

    def get_temporary_variable_from_table(self, node):
        for x in self.temporary_symbol_table:
            if x[0] == node:
                return x[1]

    def post_visit_ExpressionEMinusEqualE(self, node: ASTExpressionEMinusEqualE):
        label = self.get_instructionLables_label(node)
        flag = self.get_temporary_variable_from_table(node.Expression)
        flag2 = self.get_temporary_variable_from_table(node.Expression2)

        self.add_line_asm(node, f"{label} ", "LDR", "R1,", f"{flag}")
        self.add_line_asm(node, " ", "LDR", "R1,", "R1")
        self.add_line_asm(node, " ", "LDR", "R4,", f"{flag2}")
        self.add_line_asm(node, " ", "LDR", "R4,", "R4")
        self.add_line_asm(node, " ", "SUB", "R1,", "R4")

        self.add_line_asm(node, " ", "LDR", "R7,", f"{flag}")
        self.add_line_asm(node, " ", "STR", "R1,", "R7")
        for x in self.temporary_symbol_table:
            if node == x[0]:
                self.add_line_asm(node, " ", "STR", "R1,", f"{flag}")
                self.add_line_asm(node, " ", "LDA", "R4,", f"{flag}")
                self.add_line_asm(node, " ", "STR", "R4,", f"{x[1]}")
