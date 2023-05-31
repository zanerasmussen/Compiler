from AbstractVisitor import ASTVisitor
from AST import *

class TCODE(ASTVisitor):
    def __init__(self):
        self.TCODE = []
        self.firstAdded = False

        
    def add_line_asm(self, node, param1, param2, param3, param4):
        self.TCODE.extend([f"{param1:<15} {param2:<15} {param3:<15} {param4:<15}"])

    def post_visit_Argument(self, node: ASTArgument):
        self.TCODE.extend(node.asm)

    def post_visit_ArgumentList(self, node: ASTArgumentList):
        self.TCODE.extend(node.asm)

    def post_visit_ArgOrIdx(self, node: ASTArgOrIdx):
        self.TCODE.extend(node.asm)
    
    def post_visit_Case(self, node: ASTCase):
        self.TCODE.extend(node.asm)

    def post_visit_CaseBlock(self, node: ASTCaseBlock):
        self.TCODE.extend(node.asm)

    def post_visit_ClassDefinition(self, node: ASTClassDefinition):
        self.TCODE.extend(node.asm)
    
    def post_visit_ClassMemberDefinition(self, node: ASTClassMemberDefinition):
        self.TCODE.extend(node.asm)

    def pre_visit_CompilationUnit(self, node: ASTCompilationUnit):
        self.TCODE.extend(node.asm)
        
    def post_visit_CompilationUnit(self, node: ASTCompilationUnit):        
        param1 = "###FINAL"
        param2 = "TRP"
        param3 = "#0"
        param4 = " "
        self.TCODE.extend([f"{param1:<15} {param2:<15} {param3:<15} {param4:<15}"])

    def post_visit_ConstructorDeclaration(self, node: ASTConstructorDeclaration):
        self.TCODE.extend(node.asm)

    def post_visit_DataMemberDeclaration(self, node: ASTDataMemberDeclaration):
        self.TCODE.extend(node.asm)

    def post_visit_ExpressionArgIdx(self, node: ASTExpressionArgIdx):
        self.TCODE.extend(node.asm)

    def post_visit_ExpressionDotID(self, node: ASTExpressionDotID):
        self.TCODE.extend(node.asm)

    def post_visit_ExpressionMinus(self, node: ASTExpressionMinus):
        self.TCODE.extend(node.asm)

    def post_visit_ExpressionNew(self, node: ASTExpressionNew):
        self.TCODE.extend(node.asm)

    def post_visit_ExpressionNot(self, node: ASTExpressionNot):
        self.TCODE.extend(node.asm)

    def post_visit_ExpressionPlus(self, node: ASTExpressionPlus):
        self.TCODE.extend(node.asm)

    def post_visit_ExpressionPAREN(self, node: ASTExpressionPAREN):
        self.TCODE.extend(node.asm)
    
    def post_visit_ExpressionEAANDE(self, node: ASTExpressionEAANDE):
        self.TCODE.extend(node.asm)

    def post_visit_ExpresssionECEqualE(self, node: ASTExpressionECEqualE):
        self.TCODE.extend(node.asm)

    def post_visit_ExpressionEDivideE(self, node: ASTExpressionEDivideE):
        self.TCODE.extend(node.asm)

    def post_visit_ExpressionEDivideEqualE(self, node: ASTExpressionEDivideEqualE):
        self.TCODE.extend(node.asm)
    
    def post_visit_ExpressionEEqualE(self, node: ASTExpressionEEqualE):
        self.TCODE.extend(node.asm)

    def post_visit_ExpressionEGreaterE(self, node: ASTExpressionEGreaterE):
        self.TCODE.extend(node.asm)

    def post_visit_ExpressionEGreaterEqualE(self, node: ASTExpressionEGreaterEqualE):
        self.TCODE.extend(node.asm)

    def post_visit_ExpressionELessE(self, node: ASTExpressionELessE):
        self.TCODE.extend(node.asm)

    def post_visit_ExpressionELessEqualE(self, node: ASTExpressionELessEqualE):
        self.TCODE.extend(node.asm)

    def post_visit_ExpressionEMinusE(self, node: ASTExpressionEMinusE):
        self.TCODE.extend(node.asm)

    def post_visit_ExpressionEMinusEqualE(self, node: ASTExpressionEMinusEqualE):
        self.TCODE.extend(node.asm)

    def post_visit_ExpressionENotEqualE(self, node: ASTExpressionENotEqualE):
        self.TCODE.extend(node.asm)

    def post_visit_ExpressionEOORE(self, node: ASTExpressionEOORE):
        self.TCODE.extend(node.asm)

    def post_visit_ExpressionEPlusE(self, node: ASTExpressionEPlusE):
        self.TCODE.extend(node.asm)
    
    def post_visit_ExpressionEPlusEqualE(self, node: ASTExpressionEPlusEqualE):
        self.TCODE.extend(node.asm)

    def post_visit_ExpressionETimesE(self, node: ASTExpressionETimesE):
        self.TCODE.extend(node.asm)

    def post_visit_ExpressionETimesEqualE(self, node: ASTExpressionETimesEqualE):
        self.TCODE.extend(node.asm)

    def post_visit_Index(self, node: ASTIndex):
        self.TCODE.extend(node.asm)
        
    def post_visit_Initializer(self, node: ASTInitializer):
        self.TCODE.extend(node.asm)

    def post_visit_MaybeArgumentList(self, node: ASTMaybeArgumentList):
        self.TCODE.extend(node.asm)

    def post_visit_MaybeExpression(self, node: ASTMaybeExpression):
        self.TCODE.extend(node.asm)

    def post_visit_MaybeInitializer(self, node: ASTMaybeInitializer):
        self.TCODE.extend(node.asm)

    def post_visit_MaybeParamList(self, node: ASTMaybeParamList):
        self.TCODE.extend(node.asm)

    def post_visit_MethodBody(self, node: ASTMethodBody):
        self.TCODE.extend(node.asm)

    def post_visit_MethodDeclaration(self, node: ASTMethodDeclaration):
        self.TCODE.extend(node.asm)

    def post_visit_MethodSuffix(self, node: ASTMethodSuffix):
        self.TCODE.extend(node.asm)

    def post_visit_MultipleCase(self, node: ASTMultipleCase):
        self.TCODE.extend(node.asm)

    def post_visit_MultipleClassDefinition(self, node: ASTMultipleClassDefinition):
        self.TCODE.extend(node.asm)
                
    def post_visit_MultipleClassMemberDefinition(self, node: ASTMultipleClassMemberDefinition):
        self.TCODE.extend(node.asm)

    def post_visit_MultipleCommaExpression(self, node: ASTMultipleCommaExpression):
        self.TCODE.extend(node.asm)

    def post_visit_MultipleCommaParameter(self, node: ASTMultipleCommaParameter):
        self.TCODE.extend(node.asm)

    def post_visit_MultipleStatement(self, node: ASTMultipleStatement):
        self.TCODE.extend(node.asm)

    def post_visit_Parameter(self, node: ASTParameter):
        self.TCODE.extend(node.asm)

    def post_visit_ParameterList(self, node: ASTParameterList):
        self.TCODE.extend(node.asm)

    def post_visit_StatementBreak(self, node: ASTStatementBreak):
        self.TCODE.extend(node.asm)

    def pre_visit_StatementCIN(self, node: ASTStatementCIN):
        self.TCODE.extend(node.asm_pre)

    def post_visit_StatementCIN(self, node: ASTStatementCIN):
        self.TCODE.extend(node.asm_post)

    def pre_visit_StatementCOUT(self, node: ASTStatementCOUT):
        self.TCODE.extend(node.asm_pre)

    def post_visit_StatementCOUT(self, node: ASTStatementCOUT):
        self.TCODE.extend(node.asm_post)

    def pre_visit_StatementExpression(self, node: ASTStatementExpression):
        self.TCODE.extend(node.asm_pre)

    def post_visit_StatementExpression(self, node: ASTStatementExpression):
        self.TCODE.extend(node.asm_post)

    def pre_visit_StatementIF(self, node: ASTStatementIF):
        self.TCODE.extend(node.asm_pre)

    def mid_visit_StatementIF(self, node: ASTStatementIF):
        self.TCODE.extend(node.asm_mid)

    def post_visit_StatementIF(self, node: ASTStatementIF):
        self.TCODE.extend(node.asm)

    def after_exp_visit_StatementIFELSE(self, node: ASTStatementIFELSE):
        self.TCODE.extend(node.asm_after_exp)

    def after_statement_one_visit_StatementIFELSE(self, node: ASTStatementIFELSE):
        self.TCODE.extend(node.asm_after_statement1)

    def post_visit_StatementIFELSE(self, node: ASTStatementIFELSE):
        self.TCODE.extend(node.asm)

    def pre_visit_StatementMultipleStatement(self, node: ASTStatementMultipleStatement):
        self.TCODE.extend(node.asm)

    def pre_visit_StatementToVariableDeclaration(self, node: ASTStatementToVariableDeclaration):
        self.TCODE.extend(node.asm_pre)

    def post_visit_StatementToVariableDeclaration(self, node: ASTStatementToVariableDeclaration):
        self.TCODE.extend(node.asm)

    def post_visit_StatementReturn(self, node: ASTStatementReturn):
        self.TCODE.extend(node.asm)

    def post_visit_StatementSwitch(self, node: ASTStatementSwitch):
        self.TCODE.extend(node.asm)

    def pre_visit_StatementWhile(self, node: ASTStatementWhile):
        self.TCODE.extend(node.asm_pre)

    def mid_visit_StatementWhile(self, node: ASTStatementWhile):
        self.TCODE.extend(node.asm_mid)

    def post_visit_StatementWhile(self, node: ASTStatementWhile):
        self.TCODE.extend(node.asm)

    def post_visit_VariableDeclaration(self, node: ASTVariableDeclaration):
        self.TCODE.extend(node.asm)

    def post_visit_Terminal(self, node: ASTTerminal):
        self.TCODE.extend(node.asm)


