from AbstractVisitor import ASTVisitor
from AST import *

class VariableDeclarationVisitor(ASTVisitor):    
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

    def post_visit_VariableDeclaration(self, node: ASTVariableDeclaration):
        label = self.get_instructionLables_label(node)
        for x in self.TerminalIDS:
            if node.ID == x[0]:
                if node.Initializer.Initializer != None:
                    flag = self.get_temporary_variable_from_table(node.Initializer.Initializer.Expression)
                    if node.finalType == 'int':
                        self.add_line_asm(node, f"{label} ", "LDR", "R3,", f"{flag}")
                        self.add_line_asm(node, " ", "LDR", "R3,", "R3")
                        self.add_line_asm(node, " ", "STR", "R3,", f"{x[0]}")
                    elif node.finalType == 'char' or node.finalType == 'bool':
                        self.add_line_asm(node, f"{label} ", "LDR", "R3,", f"{flag}")
                        self.add_line_asm(node, " ", "LDB", "R3,", "R3")
                        self.add_line_asm(node, " ", "STR", "R3,", f"{x[0]}")
                    elif node.finalType == "string":
                        self.add_line_asm(node, f"{label} ", "LDR", "R3,", f"{flag}")
                        self.add_line_asm(node, " ", "STR", "R3,", f"{x[0]}")

