from AbstractVisitor import ASTVisitor
from AST import *

class StatementExpressionVisitor(ASTVisitor):    

    def __init__(self, dataSeg , TerminalIDS, counter, temporary_symbol_table, instructionLables, statementLabelStack):
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

    def get_instructionLables_label(self, node):
        for x in self.instructionLables:
            if x[0] == node:
                return x[1]
        return ""

    def get_temporary_variable_from_table(self, node):
        for x in self.temporary_symbol_table:
            if x[0] == node:
                return x[1] 

    def get_temp_variable(self):
        temp_var = f"@{self.temp_counter}"
        self.temp_counter += 1
        return temp_var
    
    def add_temp_variable_to_data_segment(self, variable):
            param1 = f"{variable}"
            param2 = ".INT" 
            self.dataSeg.append(f"{param1:<15} {param2:<15}")
            self.dataSeg.extend([";"])

    def add_to_temporary_symbol_table(self, node):
        alreadyAdded = False
        for x in self.temporary_symbol_table:
            if x[0] == node:
                alreadyAdded = True

        if alreadyAdded == False:
            variable = self.get_temp_variable()
            self.temporary_symbol_table.append((node, variable))
            self.add_temp_variable_to_data_segment(variable)   

    def pre_visit_StatementExpression(self, node: ASTStatementExpression):
        label = self.get_instructionLables_label(node)
        self.add_line_asm_pre(node, f"{label} ", "ADI", "R0,", "#0")

    def post_visit_StatementExpression(self, node: ASTStatementExpression):
        next = ""
        for i in range(len(self.statementLabelStack) -1):
            if self.statementLabelStack[i][0] == node:
                next = self.statementLabelStack.pop(i+1)
                next = next[1]
        if next != "":
            self.add_line_asm_post(node, " ", "JMP", f"{next}", " ")