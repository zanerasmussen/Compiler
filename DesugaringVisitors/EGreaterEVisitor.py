from AbstractVisitor import ASTVisitor
from AST import *

class EGreaterEVisitor(ASTVisitor):
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

    def post_visit_ExpressionEGreaterE(self, node: ASTExpressionEGreaterE):
        label = self.get_instructionLables_label(node)
        flag = self.get_temporary_variable_from_table(node.Expression)
        flag2 = self.get_temporary_variable_from_table(node.Expression2)

        if node.type == "int":
            self.add_line_asm(node, f"{label} ", "LDR", "R10,", f"{flag}")
            self.add_line_asm(node, " ", "LDR", "R10,", "R10")
            self.add_line_asm(node, " ", "LDR", "R11,", f"{flag2}")
            self.add_line_asm(node, " ", "LDR", "R11,", "R11")
            self.add_line_asm(node, " ", "CMP", "R10,", "R11")
            self.add_line_asm(node," ", "MOV", "R7,", "PC")
            self.add_line_asm(node," ", "ADI", "R7,", "#48") #set Value
            self.add_line_asm(node," ", "BRZ", "R10,", "$CMPFALSE") 
            self.add_line_asm(node," ", "BLT", "R10,", "$CMPFALSE") 
            self.add_line_asm(node," ", "BGT", "R10,", "$CMPTRUE") 

            variable = self.get_temp_variable()
            self.add_temp_variable_to_data_segment(variable)

            self.add_line_asm(node, " ", "LDA", "R12,", f"{variable}")
            self.add_line_asm(node, " ", "STR", "R10,", "R12")
            for x in self.temporary_symbol_table:
                if node == x[0]:
                    self.add_line_asm(node, " ", "STR", "R10,", f"{variable}")
                    self.add_line_asm(node, " ", "LDA", "R4,", f"{variable}")
                    self.add_line_asm(node, " ", "STR", "R4,", f"{x[1]}")
        
        elif node.type == "char":
            self.add_line_asm(node, f"{label} ", "LDR", "R10,", f"{flag}")
            self.add_line_asm(node, " ", "LDB", "R10,", "R10")
            self.add_line_asm(node, " ", "LDR", "R11,", f"{flag2}")
            self.add_line_asm(node, " ", "LDB", "R11,", "R11")
            self.add_line_asm(node, " ", "CMP", "R10,", "R11")
            self.add_line_asm(node," ", "MOV", "R7,", "PC")
            self.add_line_asm(node," ", "ADI", "R7,", "#48") #set Value
            self.add_line_asm(node," ", "BRZ", "R10,", "$CMPFALSE") 
            self.add_line_asm(node," ", "BLT", "R10,", "$CMPFALSE") 
            self.add_line_asm(node," ", "BGT", "R10,", "$CMPTRUE") 

            variable = self.get_temp_variable()
            self.add_temp_variable_to_data_segment(variable)

            self.add_line_asm(node, " ", "LDA", "R12,", f"{variable}")
            self.add_line_asm(node, " ", "STR", "R10,", "R12")
            for x in self.temporary_symbol_table:
                if node == x[0]:
                    self.add_line_asm(node, " ", "STR", "R10,", f"{variable}")
                    self.add_line_asm(node, " ", "LDA", "R4,", f"{variable}")
                    self.add_line_asm(node, " ", "STR", "R4,", f"{x[1]}")
