from AbstractVisitor import ASTVisitor
from AST import *

class ExpressionParenVisitor(ASTVisitor):
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
    
    def post_visit_ExpressionPAREN(self, node: ASTExpressionPAREN):
        label = self.get_instructionLables_label(node)
        flag = self.get_temporary_variable_from_table(node.Expression)
        for x in self.temporary_symbol_table:
            if node == x[0]:
                self.add_line_asm(node, f"{label} ", "LDR", "R3,", f"{flag}")
                self.add_line_asm(node, " ", "STR", "R3,", f"{x[1]}")
