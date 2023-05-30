from AbstractVisitor import ASTVisitor
from AST import *

class COUTVisitor(ASTVisitor):
    def __init__(self, dataSeg, TerminalIDS, counter, temporary_symbol_table, instructionLables, statementLabelStack):
        self.dataSeg = dataSeg
        self.TerminalIDS = TerminalIDS
        self.temp_counter = counter
        self.temporary_symbol_table = temporary_symbol_table
        self.instructionLables = instructionLables
        self.statementLabelStack = statementLabelStack

        #visitor specific

    def add_line_asm_pre(self, node, param1, param2, param3, param4):
        node.asm_pre.extend([f"{param1:<15} {param2:<15} {param3:<15} {param4:<15}"])

    def add_line_asm_post(self, node, param1, param2, param3, param4):
        node.asm_post.extend([f"{param1:<15} {param2:<15} {param3:<15} {param4:<15}"])

    def get_instructionLables_label(self, node: ASTStatementCOUT):
        for x in self.instructionLables:
            if x[0] == node:
                return x[1]
        return ""

    def get_temporary_variable_from_table(self, node):
        for x in self.temporary_symbol_table:
            if x[0] == node:
                return x[1]
 
    def pre_visit_StatementCOUT(self, node: ASTStatementCOUT):
        label = self.get_instructionLables_label(node)
        self.add_line_asm_pre(node, f"{label} ", "ADI", "R0,", "#0")
 
    def post_visit_StatementCOUT(self, node: ASTStatementCOUT):
        flag = self.get_temporary_variable_from_table(node.Expression)
        next = ""
        for i in range(len(self.statementLabelStack) -1):
            if self.statementLabelStack[i][0] == node:
                next = self.statementLabelStack.pop(i+1)
                next = next[1]

        if node.type == "int" or node.type == 'bool' or node.type == 'true' or node.type == 'false':
            type = 1
            self.add_line_asm_post(node, " ", "LDR", "R3,", f"{flag}")
            self.add_line_asm_post(node, " ", "LDR", "R3,", "R3")
            self.add_line_asm_post(node, " ", "TRP", f"#{type}", " ")
            if next != "":
                self.add_line_asm_post(node, " ", "JMP", f"{next}", " ")


        elif node.type == "char":
            type = 3
            self.add_line_asm_post(node, " ",  "LDR", "R3,", f"{flag}")
            self.add_line_asm_post(node, " ", "LDB", "R3,", "R3")
            self.add_line_asm_post(node, " ", "TRP", f"#{type}", " ")
            if next != "":
                self.add_line_asm_post(node, " ", "JMP", f"{next}", " ")

        elif node.type == "string" and node.isID == True:
            type = 3
            self.add_line_asm_post(node, " ",  "LDR", "R0,", f"{flag}")
            self.add_line_asm_post(node, " ", "LDR", "R0,", "R0")
            self.add_line_asm_post(node, " ", "MOV", "R7,", "PC")
            self.add_line_asm_post(node, " ", "ADI", "R7,", "#24")
            self.add_line_asm_post(node, " ", "JMP", "PRINT", " ")
            if next != "":
                self.add_line_asm_post(node, " ", "JMP", f"{next}", " ")

        elif node.type == "string" and node.isID == False:
            type = 3
            self.add_line_asm_post(node, " ",  "LDR", "R0,", f"{flag}")
            self.add_line_asm_post(node, " ", "MOV", "R7,", "PC")
            self.add_line_asm_post(node, " ", "ADI", "R7,", "#24")
            self.add_line_asm_post(node, " ", "JMP", "PRINT", " ")
            if next != "":
                self.add_line_asm_post(node, " ", "JMP", f"{next}", " ")