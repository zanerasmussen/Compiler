from AbstractVisitor import ASTVisitor
from AST import *

class ExEqualEx2Visitor(ASTVisitor):
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

    def post_visit_ExpressionEEqualE(self, node: ASTExpressionEEqualE):
        label = self.get_instructionLables_label(node)
        flag = self.get_temporary_variable_from_table(node.Expression)
        flag2 = self.get_temporary_variable_from_table(node.Expression2)

        if node.type == "string":
            written = False
            if isinstance(node.Expression2, ASTTerminal) :
                if node.Expression2.Terminal[0] == '$':
                    written = True
                    self.add_line_asm(node, f"{label} ", "LDR", "R6,", f"{flag2}")
                    self.add_line_asm(node, " ", "LDR", "R7,", f"{flag}")
                    self.add_line_asm(node, " ", "STR", "R6,", "R7")
            if written == False:       
                
                self.add_line_asm(node, ";", " ", " ", " ")
                self.add_line_asm(node, ";", " ", " ", " ")
                self.add_line_asm(node, ";", " ", " ", " ") 
                self.add_line_asm(node, f"{label} ", "LDR", "R6,", f"{flag2}")
                self.add_line_asm(node, " ", "LDR", "R7,", f"{flag}")
                self.add_line_asm(node, " ", "LDR", "R8,", "R6")
                self.add_line_asm(node, " ", "STR", "R8,", "R7")
                for x in self.temporary_symbol_table:
                    if node == x[0]:
                        self.add_line_asm(node, ";", " ", " ", " ")
                        self.add_line_asm(node, ";", " ", " ", " ")
                        self.add_line_asm(node, " ", "STR", "R8,", f"{flag}")
                        self.add_line_asm(node, " ", "LDA", "R3,", f"{flag}")
                        self.add_line_asm(node, " ", "STR", "R3,", f"{x[1]}")
                self.add_line_asm(node, ";", " ", " ", " ")

        elif node.type == "char":
            self.add_line_asm(node, f"{label} ", "LDR", "R6,", f"{flag2}")
            self.add_line_asm(node, " ", "LDB", "R6,", "R6")
            self.add_line_asm(node, " ", "LDR", "R7,", f"{flag}")
            self.add_line_asm(node, " ", "STB", "R6,", "R7")
            for x in self.temporary_symbol_table:
                if node == x[0]:
                    self.add_line_asm(node, " ", "STB", "R6,", f"{flag}")
                    self.add_line_asm(node, " ", "LDA", "R3,", f"{flag}")
                    self.add_line_asm(node, " ", "STR", "R3,", f"{x[1]}") #i changed STB to STR
            self.add_line_asm(node, ";", " ", " ", " ")

        elif node.type == "int" or node.type == 'false' or node.type == 'true' or node.type == "bool":
            self.add_line_asm(node, f"{label} ", "LDR", "R6,", f"{flag2}")
            self.add_line_asm(node, " ", "LDR", "R6,", "R6")
            self.add_line_asm(node, " ", "LDR", "R7,", f"{flag}")
            self.add_line_asm(node, " ", "STR", "R6,", "R7")
            for x in self.temporary_symbol_table:
                if node == x[0]:
                    self.add_line_asm(node, " ", "STR", "R6,", f"{flag}")
                    self.add_line_asm(node, " ", "LDA", "R3,", f"{flag}")
                    self.add_line_asm(node, " ", "STR", "R3,", f"{x[1]}")
            self.add_line_asm(node, ";", " ", " ", " ")