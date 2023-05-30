from AbstractVisitor import ASTVisitor
from AST import *

class TempVarCreateVisitor(ASTVisitor):    
    def __init__(self, dataSeg, TerminalIDS, counter, temporary_symbol_table, instructionLables):
        self.dataSeg = dataSeg
        self.TerminalIDS = TerminalIDS
        self.temp_counter = counter
        self.temporary_symbol_table = temporary_symbol_table
        self.instructionLables = instructionLables

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

    def pre_visit_Case(self, node: ASTCase):
        pass

    def post_visit_Case(self, node: ASTCase):
        pass

    def pre_visit_CaseBlock(self, node: ASTCaseBlock):
        pass

    def post_visit_CaseBlock(self, node: ASTCaseBlock):
        pass

    def post_visit_ExpressionMinus(self, node: ASTExpressionMinus):
        self.add_to_temporary_symbol_table(node.Expression)

    def post_visit_ExpressionNot(self, node: ASTExpressionNot):
        self.add_to_temporary_symbol_table(node.Expression)

    def post_visit_ExpressionPlus(self, node: ASTExpressionPlus):
        self.add_to_temporary_symbol_table(node.Expression)
    
    def post_visit_ExpressionPAREN(self, node: ASTExpressionPAREN):
        self.add_to_temporary_symbol_table(node.Expression)

    def post_visit_ExpressionEAANDE(self, node: ASTExpressionEAANDE):
        self.add_to_temporary_symbol_table(node.Expression)
        self.add_to_temporary_symbol_table(node.Expression2)

    def post_visit_ExpresssionECEqualE(self, node: ASTExpressionECEqualE):
        self.add_to_temporary_symbol_table(node.Expression)
        self.add_to_temporary_symbol_table(node.Expression2)

    def post_visit_ExpressionEDivideE(self, node: ASTExpressionEDivideE):
        self.add_to_temporary_symbol_table(node.Expression)
        self.add_to_temporary_symbol_table(node.Expression2)

    def post_visit_ExpressionEDivideEqualE(self, node: ASTExpressionEDivideEqualE):
        self.add_to_temporary_symbol_table(node.Expression)
        self.add_to_temporary_symbol_table(node.Expression2)

    def post_visit_ExpressionEEqualE(self, node: ASTExpressionEEqualE):
        self.add_to_temporary_symbol_table(node.Expression)
        self.add_to_temporary_symbol_table(node.Expression2)

    def post_visit_ExpressionEGreaterE(self, node: ASTExpressionEGreaterE):
        self.add_to_temporary_symbol_table(node.Expression)
        self.add_to_temporary_symbol_table(node.Expression2)

    def post_visit_ExpressionEGreaterEqualE(self, node: ASTExpressionEGreaterEqualE):
        self.add_to_temporary_symbol_table(node.Expression)
        self.add_to_temporary_symbol_table(node.Expression2)

    def post_visit_ExpressionELessE(self, node: ASTExpressionELessE):
        self.add_to_temporary_symbol_table(node.Expression)
        self.add_to_temporary_symbol_table(node.Expression2)

    def post_visit_ExpressionELessEqualE(self, node: ASTExpressionELessEqualE):
        self.add_to_temporary_symbol_table(node.Expression)
        self.add_to_temporary_symbol_table(node.Expression2)

    def post_visit_ExpressionEMinusE(self, node: ASTExpressionEMinusE):
        self.add_to_temporary_symbol_table(node.Expression)
        self.add_to_temporary_symbol_table(node.Expression2)

    def post_visit_ExpressionEMinusEqualE(self, node: ASTExpressionEMinusEqualE):
        self.add_to_temporary_symbol_table(node.Expression)
        self.add_to_temporary_symbol_table(node.Expression2)

    def post_visit_ExpressionENotEqualE(self, node: ASTExpressionENotEqualE):
        self.add_to_temporary_symbol_table(node.Expression)
        self.add_to_temporary_symbol_table(node.Expression2)

    def post_visit_ExpressionEOORE(self, node: ASTExpressionEOORE):
        self.add_to_temporary_symbol_table(node.Expression)
        self.add_to_temporary_symbol_table(node.Expression2)
 
    def post_visit_ExpressionEPlusE(self, node: ASTExpressionEPlusE):
        self.add_to_temporary_symbol_table(node.Expression)
        self.add_to_temporary_symbol_table(node.Expression2)

    def post_visit_ExpressionEPlusEqualE(self, node: ASTExpressionEPlusEqualE):
        self.add_to_temporary_symbol_table(node.Expression)
        self.add_to_temporary_symbol_table(node.Expression2)

    def post_visit_ExpressionETimesE(self, node: ASTExpressionETimesE):
        self.add_to_temporary_symbol_table(node.Expression)
        self.add_to_temporary_symbol_table(node.Expression2)

    def post_visit_ExpressionETimesEqualE(self, node: ASTExpressionETimesEqualE):
        self.add_to_temporary_symbol_table(node.Expression)
        self.add_to_temporary_symbol_table(node.Expression2)

    def post_visit_Initializer(self, node: ASTInitializer):
        self.add_to_temporary_symbol_table(node)



    def post_visit_MultipleCase(self, node: ASTMultipleCase):
        pass

    def post_visit_MultipleStatement(self, node: ASTMultipleStatement):
        pass

    def post_visit_StatementBreak(self, node: ASTStatementBreak):
        pass    

    def post_visit_StatementCIN(self, node: ASTStatementCIN):
        pass

    def post_visit_StatementCOUT(self, node: ASTStatementCOUT):
        self.add_to_temporary_symbol_table(node.Expression)

    def post_visit_StatementExpression(self, node: ASTStatementExpression):
        pass

    def post_visit_StatementIF(self, node: ASTStatementIF):
        pass

    def post_visit_StatementIFELSE(self, node: ASTStatementIFELSE):
       pass

    def post_visit_StatementMultipleStatement(self, node: ASTStatementMultipleStatement):
        pass

    def post_visit_StatementToVariableDeclaration(self, node: ASTStatementToVariableDeclaration):
        pass

    def post_visit_StatementReturn(self, node: ASTStatementReturn):
        pass

    def post_visit_StatementSwitch(self, node: ASTStatementSwitch):
        pass

    def post_visit_StatementWhile(self, node: ASTStatementWhile):
        pass

    def post_visit_Terminal(self, node: ASTTerminal):
        self.add_to_temporary_symbol_table(node)