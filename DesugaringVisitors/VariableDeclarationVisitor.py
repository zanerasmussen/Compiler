from AbstractVisitor import ASTVisitor
from AST import *

class VariableDeclarationVisitor(ASTVisitor):    
    def __init__(self, dataSeg, TerminalIDS, counter, temporary_symbol_table, instructionLables, statementLabelStack):
        self.dataSeg = dataSeg
        self.TerminalIDS = TerminalIDS
        self.temp_counter = counter
        self.temporary_symbol_table = temporary_symbol_table
        self.instructionLables = instructionLables
        self.statementLabelStack = statementLabelStack
        self.firstAdded = False


        #visitor specific
    
    def get_instructionLables_label(self, node):
        for x in self.instructionLables:
            if x[0] == node:
                return x[1]
        return ""

    def add_line_asm_pre(self, node, param1, param2, param3, param4):
        node.asm_pre.extend([f"{param1:<15} {param2:<15} {param3:<15} {param4:<15}"])

    def add_line_asm(self, node, param1, param2, param3, param4):
        node.asm.extend([f"{param1:<15} {param2:<15} {param3:<15} {param4:<15}"])

    def get_temporary_variable_from_table(self, node):
        for x in self.temporary_symbol_table:
            if x[0] == node:
                return x[1]

    def pre_visit_StatementToVariableDeclaration(self, node: ASTVariableDeclaration):
        label = self.get_instructionLables_label(node)
        self.add_line_asm_pre(node, f"{label} ", "ADI", "R0,", "#0")

    def post_visit_VariableDeclaration(self, node: ASTVariableDeclaration):
        next = ""
        for i in range(len(self.statementLabelStack) -1):
            if self.statementLabelStack[i][0] == node:
                next = self.statementLabelStack.pop(i+1)
                next = next[1]
        for x in self.TerminalIDS:
            if node.ID == x[0]:
                if node.Initializer.Initializer != None:
                    flag = self.get_temporary_variable_from_table(node.Initializer.Initializer.Expression)
                    if node.finalType == 'int' or node.finalType == 'bool':
                        self.add_line_asm(node, " ", "LDR", "R3,", f"{flag}")
                        self.add_line_asm(node, " ", "LDR", "R3,", "R3")
                        self.add_line_asm(node, " ", "STR", "R3,", f"{x[0]}")
                        if next != "":
                            self.add_line_asm(node, " ", "JMP", f"{next}", " ")
                    elif node.finalType == 'char' :
                        self.add_line_asm(node, " ", "LDR", "R3,", f"{flag}")
                        self.add_line_asm(node, " ", "LDB", "R3,", "R3")
                        self.add_line_asm(node, " ", "STR", "R3,", f"{x[0]}")
                        if next != "":
                            self.add_line_asm(node, " ", "JMP", f"{next}", " ")
                    elif node.finalType == "string":
                        self.add_line_asm(node, " ", "LDR", "R3,", f"{flag}")
                        self.add_line_asm(node, " ", "STR", "R3,", f"{x[0]}")
                        if next != "":
                            self.add_line_asm(node, " ", "JMP", f"{next}", " ")


    def post_visit_StatementToVariableDeclaration(self, node: ASTVariableDeclaration):
        next = ""
        for i in range(len(self.statementLabelStack) -1):
            if self.statementLabelStack[i][0] == node:
                next = self.statementLabelStack.pop(i+1)
                next = next[1]
        if next != "":
            self.add_line_asm(node, " ", "JMP", f"{next}", " ")
