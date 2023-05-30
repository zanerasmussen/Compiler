from AbstractVisitor import ASTVisitor
from AST import *

class PlusEVisitor(ASTVisitor):
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

    def post_visit_ExpressionPlus(self, node: ASTExpressionPlus):
        label = self.get_instructionLables_label(node)
        flag = self.get_temporary_variable_from_table(node.Expression)

        self.add_line_asm(node, f"{label} ", "LDR", "R10,", f"{flag}")
        self.add_line_asm(node, " ", "LDR", "R10,", "R10")
        self.add_line_asm(node, " ", "MOV", "R9,", "R10")
        self.add_line_asm(node, " ", "CMPI", "R10,", "#0")
        self.add_line_asm(node, " ", "MOV", "R7,", "PC")
        self.add_line_asm(node, " ", "ADI", "R7,", "#24")
        self.add_line_asm(node, " ", "BLT", "R10,", "$POSITIVE")
        self.add_line_asm(node, " ", "STR", "R9,", f"{flag}")
        for x in self.temporary_symbol_table:
            if node == x[0]:
                self.add_line_asm(node, " ", "LDA", "R3,", f"{flag}")
                self.add_line_asm(node, " ", "STR", "R3,", f"{x[1]}")


