from AbstractVisitor import ASTVisitor
from AST import *

class WhileStatementVisitor(ASTVisitor):
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

    def add_line_asm(self, node, param1, param2, param3, param4):
        node.asm.extend([f"{param1:<15} {param2:<15} {param3:<15} {param4:<15}"])

    def add_line_asm_mid(self, node, param1, param2, param3, param4):
        node.asm_mid.extend([f"{param1:<15} {param2:<15} {param3:<15} {param4:<15}"])

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

    def pre_visit_StatementWhile(self, node: ASTStatementWhile):
        label = self.get_instructionLables_label(node)
        flag = self.get_temporary_variable_from_table(node.Expression)

        ex = ""
        for i in range(len(self.statementLabelStack) -1):
            if self.statementLabelStack[i][0] == node.Expression:
                ex = self.statementLabelStack.pop(i+1)
                ex = ex[1]
        if ex == "":
            ex = "###FINAL"
        sta = ""
        for i in range(len(self.statementLabelStack) -1):
            if self.statementLabelStack[i][0] == node.Statement:
                sta = self.statementLabelStack.pop(i)
                sta = sta[1]
        done = ""
        for i in range(len(self.statementLabelStack)-1):
            if self.statementLabelStack[i][0] == str(node)+"!":
                done = self.statementLabelStack.pop(i)
                done = done[1]
                break
        start = ""
        for i in range(len(self.statementLabelStack)-1):
            if self.statementLabelStack[i][0] == str(node)+"!!":
                start = self.statementLabelStack.pop(i)
                start = start[1]
                break
        self.add_line_asm_pre(node, f"{start} ", "ADI", "R0,", "#0")
        self.add_line_asm_mid(node, f"{label} ", "LDR", "R13,", f"{flag}")
        self.add_line_asm_mid(node, " ", "LDR", "R13,", "R13")
        self.add_line_asm_mid(node, " ", "CMPI", "R13,", "#0")
        self.add_line_asm_mid(node, " ", "BRZ", "R13,", f"{done}")
        self.add_line_asm(node, f"{done}", "ADI", "R0,", "#0")

