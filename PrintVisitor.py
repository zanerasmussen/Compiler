from AbstractVisitor import ASTVisitor
from AST import *
import pydot

class PrintVisitor(ASTVisitor):
    
    def visit_Argument(self, node: ASTArgument):
        pass

    def visit_ArgumentList(self, node: ASTArgumentList):
        pass
    
    def visit_ArgOrIdx(self, node: ASTArgOrIdx):
        pass

    def visit_Case(self, node: ASTCase):
        pass

    def visit_CaseBlock(self, node: ASTCaseBlock):
        pass

    def visit_ClassDefinition(self, node: ASTClassDefinition):
        print("visited Class Definition: " + str(node.Class) + " " + str(node.ID) + " " + str(node.LCURLY) + " " + str(node.MultipleClassMemberDefinition) + " " + str(node.RCURLY))
        node.MultipleClassMemberDefinition.accept(self)

    def visit_ClassMemberDefinition(self, node: ASTClassMemberDefinition):
        pass

    def visit_CompilationUnit(self, node: ASTCompilationUnit):
        print("Visited Compilation Unit: " + str(node.MultipleClassDefinition) + " " + str(node.void) + " " + str(node.kxi2023) + " " + 
              str(node.main) + " " + str(node.LPAREN) + " " + str(node.RPAREN) + " " + str(node.MethodBody))
        node.MultipleClassDefinition.accept(self)
        node.MethodBody.accept(self)

    def visit_ConstructorDeclaration(self, node: ASTConstructorDeclaration):
        pass

    def visit_DataMemberDeclaration(self, node: ASTDataMemberDeclaration):
        pass

    def visit_ExpressionArgIdx(self, node: ASTExpressionArgIdx):
        pass

    def visit_ExpressionDotID(self, node: ASTExpressionDotID):
        pass

    def visit_ExpressionMinus(self, node: ASTExpressionMinus):
        pass

    def visit_ExpressionNew(self, node: ASTExpressionNew):
        pass

    def visit_ExpressionNot(self, node: ASTExpressionNot):
        pass

    def visit_ExpressionPlus(self, node: ASTExpressionPlus):
        pass

    def visit_ExpressionPAREN(self, node: ASTExpressionPAREN):
        pass

    def visit_ExpressionEAANDE(self, node: ASTExpressionEAANDE):
        pass

    def visit_ExpresssionECEqualE(self, node: ASTExpressionECEqualE):
        pass

    def visit_ExpressionEDivideE(self, node: ASTExpressionEDivideE):
        pass

    def visit_ExpressionEDivideEqualE(self, node: ASTExpressionEDivideEqualE):
        pass
    
    def visit_ExpressionEEqualE(self, node: ASTExpressionEEqualE):
        pass

    def visit_ExpressionEGreaterE(self, node: ASTExpressionEGreaterE):
        pass

    def visit_ExpressionEGreaterEqualE(self, node: ASTExpressionEGreaterEqualE):
        pass

    def visit_ExpressionELessE(self, node: ASTExpressionELessE):
        pass

    def visit_ExpressionELessEqualE(self, node: ASTExpressionELessEqualE):
        pass

    def visit_ExpressionEMinusE(self, node: ASTExpressionEMinusE):
        pass

    def visit_ExpressionEMinusEqualE(self, node: ASTExpressionEMinusEqualE):
        pass

    def visit_ExpressionENotEqualE(self, node: ASTExpressionENotEqualE):
        pass

    def visit_ExpressionEOORE(self, node: ASTExpressionEOORE):
        pass

    def visit_ExpressionEPlusE(self, node: ASTExpressionEPlusE):
        pass

    def visit_ExpressionEPlusEqualE(self, node: ASTExpressionEPlusEqualE):
        pass

    def visit_ExpressionETimesE(self, node: ASTExpressionETimesE):
        pass

    def visit_ExpressionETimesEqualE(self, node: ASTExpressionETimesEqualE):
        pass

    def visit_Index(self, node: ASTIndex):
        pass

    def visit_Initializer(self, node: ASTInitializer):
        pass

    def visit_MaybeArgumentList(self, node: ASTMaybeArgumentList):
        pass

    def visit_MaybeExpression(self, node: ASTMaybeExpression):
        pass

    def visit_MaybeInitializer(self, node: ASTMaybeInitializer):
        pass

    def visit_MaybeParamList(self, node: ASTMaybeParamList):
        pass

    def visit_MethodBody(self, node: ASTMethodBody):
        pass

    def visit_MethodDeclaration(self, node: ASTMethodDeclaration):
        pass

    def visit_MethodSuffix(self, node: ASTMethodSuffix):
        pass

    def visit_MultipleCase(self, node: ASTMultipleCase):
        pass

    def visit_MultipleClassDefinition(self, node: ASTMultipleClassDefinition):
        print("visited Multiple Class Definition: " + str(node.ClassDefinition))
        if (node.ClassDefinition != None):
            for classDef in node.ClassDefinition:
                classDef.accept(self)

    def visit_MultipleClassMemberDefinition(self, node: ASTMultipleClassMemberDefinition):
        pass

    def visit_MultipleCommaExpression(self, node: ASTMultipleCommaExpression):
        pass

    def visit_MultipleCommaParameter(self, node: ASTMultipleCommaParameter):
        pass

    def visit_MultipleStatement(self, node: ASTMultipleStatement):
        pass

    def visit_Parameter(self, node: ASTParameter):
        pass

    def visit_ParameterList(self, node: ASTParameterList):
        pass

    def visit_StatementBreak(self, node: ASTStatementBreak):
        pass

    def visit_StatementCIN(self, node: ASTStatementCIN):
        pass

    def visit_StatementCOUT(self, node: ASTStatementCOUT):
        pass

    def visit_StatementExpression(self, node: ASTStatementExpression):
        pass

    def visit_StatementIF(self, node: ASTStatementIF):
        pass

    def visit_StatementIFELSE(self, node: ASTStatementIFELSE):
        pass

    def visit_StatementMultipleStatement(self, node: ASTStatementMultipleStatement):
        pass

    def visit_StatementToVariableDeclaration(self, node: ASTStatementToVariableDeclaration):
        pass

    def visit_StatementReturn(self, node: ASTStatementReturn):
        pass

    def visit_StatementSwitch(self, node: ASTStatementSwitch):
        pass

    def visit_StatementWhile(self, node: ASTStatementWhile):
        pass

    def visit_VariableDeclaration(self, node: ASTVariableDeclaration):
        pass