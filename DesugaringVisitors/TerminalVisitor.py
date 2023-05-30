from AbstractVisitor import ASTVisitor
from AST import *

class TerminalVisitor(ASTVisitor):
    def __init__(self, dataSeg, TerminalIDS, counter, temporary_symbol_table, instructionLables):
        self.dataSeg = dataSeg
        self.TerminalIDS = TerminalIDS
        self.temp_counter = counter
        self.temporary_symbol_table = temporary_symbol_table
        self.instructionLables = instructionLables

        #visitor specific


    def get_instructionLables_label(self, node):
        for x in self.instructionLables:
            if x[0] == node:
                return x[1]
        return ""

    def add_line_asm(self, node, param1, param2, param3, param4):
        node.asm.extend([f"{param1:<15} {param2:<15} {param3:<15} {param4:<15}"])

    def get_temporary_variable_from_table(self, node):
        for x in self.temporary_symbol_table:
            if x[0] == node:
                return x[1]

    def post_visit_Terminal(self, node: ASTTerminal):
        label = self.get_instructionLables_label(node)
        flag = self.get_temporary_variable_from_table(node)
        for i in self.temporary_symbol_table:
            if node == i[0] and node.Terminal[0] != '%':
                self.add_line_asm(node, f"{label} ", "LDA", "R7,", f"{node.Terminal}")
                self.add_line_asm(node, " ", "STR", "R7,", f"{flag}")
            elif node == i[0] and node.Terminal[0] == '%':
                self.add_line_asm(node, f"{label} ", "LDA", "R15,", f"{node.Terminal}")
                self.add_line_asm(node, " ", "STR", "R15,", f"{flag}")
