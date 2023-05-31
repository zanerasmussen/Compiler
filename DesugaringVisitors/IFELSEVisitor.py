from AbstractVisitor import ASTVisitor
from AST import *

class IFELSEVisitor(ASTVisitor):
    def __init__(self, dataSeg, TerminalIDS, counter, temporary_symbol_table, instructionLables, statementLabelStack):
        self.dataSeg = dataSeg
        self.TerminalIDS = TerminalIDS
        self.temp_counter = counter
        self.temporary_symbol_table = temporary_symbol_table
        self.instructionLables = instructionLables
        self.statementLabelStack = statementLabelStack

        #visitor specific

    def add_line_asm_after_exp(self, node, param1, param2, param3, param4):
        node.asm_after_exp.extend([f"{param1:<15} {param2:<15} {param3:<15} {param4:<15}"])

    def add_line_asm(self, node, param1, param2, param3, param4):
        node.asm.extend([f"{param1:<15} {param2:<15} {param3:<15} {param4:<15}"])

    def add_line_asm_after_statement_one(self, node, param1, param2, param3, param4):
        node.asm_after_statement1.extend([f"{param1:<15} {param2:<15} {param3:<15} {param4:<15}"])

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


    def pre_visit_StatementIFELSE(self, node: ASTStatementIFELSE):
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
        else_sta = ""
        for i in range(len(self.statementLabelStack)-1):
            if self.statementLabelStack[i][0] == str(node)+"!!":
                else_sta = self.statementLabelStack.pop(i)
                else_sta = else_sta[1]
                break
        done = ""
        for i in range(len(self.statementLabelStack)-1):
            if self.statementLabelStack[i][0] == str(node)+"!":
                done = self.statementLabelStack.pop(i)
                done = done[1]
                break

        self.add_line_asm_after_exp(node, f"{label} ", "LDR", "R13,", f"{flag}")
        self.add_line_asm_after_exp(node, " ", "LDR", "R13,", "R13")
        self.add_line_asm_after_exp(node, " ", "CMPI", "R13,", "#0")
        self.add_line_asm_after_exp(node, " ", "BRZ", "R13,", f"{else_sta}")
        self.add_line_asm_after_statement_one(node, f"{else_sta}", "ADI", "R0,", "#0")
        self.add_line_asm(node, f"{done}", "ADI", "R0,", "#0")




