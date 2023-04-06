from abc import ABCMeta, abstractmethod
from AST import *

class ASTVisitor(metaclass=ABCMeta):
    @abstractmethod
    def visit_Argument(self, node: ASTArgument):
        pass

    @abstractmethod
    def visit_ArgumentList(self, node: ASTArgumentList):
        pass
    
    @abstractmethod
    def visit_ArgOrIdx(self, node: ASTArgOrIdx):
        pass

    @abstractmethod
    def visit_Case(self, node: ASTCase):
        pass

    @abstractmethod
    def visit_CaseBlock(self, node: ASTCaseBlock):
        pass

    @abstractmethod
    def visit_ClassDefinition(self, node: ASTClassDefinition):
        pass

    @abstractmethod
    def visit_ClassMemberDefinition(self, node: ASTClassMemberDefinition):
        pass

    @abstractmethod
    def visit_CompilationUnit(self, node: ASTCompilationUnit):
        pass

    @abstractmethod
    def visit_ConstructorDeclaration(self, node: ASTConstructorDeclaration):
        pass

    @abstractmethod
    def visit_DataMemberDeclaration(self, node: ASTDataMemberDeclaration):
        pass

    @abstractmethod
    def visit_ExpressionArgIdx(self, node: ASTExpressionArgIdx):
        pass

    @abstractmethod
    def visit_ExpressionDotID(self, node: ASTExpressionDotID):
        pass

    @abstractmethod
    def visit_ExpressionMinus(self, node: ASTExpressionMinus):
        pass

    @abstractmethod
    def visit_ExpressionNew(self, node: ASTExpressionNew):
        pass

    @abstractmethod
    def visit_ExpressionNot(self, node: ASTExpressionNot):
        pass

    @abstractmethod
    def visit_ExpressionPlus(self, node: ASTExpressionPlus):
        pass

    @abstractmethod
    def visit_ExpressionPAREN(self, node: ASTExpressionPAREN):
        pass

    @abstractmethod
    def visit_ExpressionEAANDE(self, node: ASTExpressionEAANDE):
        pass

    @abstractmethod
    def visit_ExpresssionECEqualE(self, node: ASTExpressionECEqualE):
        pass

    @abstractmethod
    def visit_ExpressionEDivideE(self, node: ASTExpressionEDivideE):
        pass

    @abstractmethod
    def visit_ExpressionEDivideEqualE(self, node: ASTExpressionEDivideEqualE):
        pass

    @abstractmethod
    def visit_ExpressionEEqualE(self, node: ASTExpressionEEqualE):
        pass

    @abstractmethod
    def visit_ExpressionEGreaterE(self, node: ASTExpressionEGreaterE):
        pass

    @abstractmethod
    def visit_ExpressionEGreaterEqualE(self, node: ASTExpressionEGreaterEqualE):
        pass

    @abstractmethod
    def visit_ExpressionELessE(self, node: ASTExpressionELessE):
        pass

    @abstractmethod
    def visit_ExpressionELessEqualE(self, node: ASTExpressionELessEqualE):
        pass

    @abstractmethod
    def visit_ExpressionEMinusE(self, node: ASTExpressionEMinusE):
        pass

    @abstractmethod
    def visit_ExpressionEMinusEqualE(self, node: ASTExpressionEMinusEqualE):
        pass

    @abstractmethod
    def visit_ExpressionENotEqualE(self, node: ASTExpressionENotEqualE):
        pass

    @abstractmethod
    def visit_ExpressionEOORE(self, node: ASTExpressionEOORE):
        pass

    @abstractmethod
    def visit_ExpressionEPlusE(self, node: ASTExpressionEPlusE):
        pass

    @abstractmethod
    def visit_ExpressionEPlusEqualE(self, node: ASTExpressionEPlusEqualE):
        pass

    @abstractmethod
    def visit_ExpressionETimesE(self, node: ASTExpressionETimesE):
        pass

    @abstractmethod
    def visit_ExpressionETimesEqualE(self, node: ASTExpressionETimesEqualE):
        pass

    @abstractmethod
    def visit_Index(self, node: ASTIndex):
        pass

    @abstractmethod
    def visit_Initializer(self, node: ASTInitializer):
        pass

    @abstractmethod
    def visit_MaybeArgumentList(self, node: ASTMaybeArgumentList):
        pass

    @abstractmethod
    def visit_MaybeExpression(self, node: ASTMaybeExpression):
        pass

    @abstractmethod
    def visit_MaybeInitializer(self, node: ASTMaybeInitializer):
        pass

    @abstractmethod
    def visit_MaybeParamList(self, node: ASTMaybeParamList):
        pass

    @abstractmethod
    def visit_MethodBody(self, node: ASTMethodBody):
        pass

    @abstractmethod
    def visit_MethodDeclaration(self, node: ASTMethodDeclaration):
        pass

    @abstractmethod
    def visit_MethodSuffix(self, node: ASTMethodSuffix):
        pass

    @abstractmethod
    def visit_MultipleCase(self, node: ASTMultipleCase):
        pass

    @abstractmethod
    def visit_MultipleClassDefinition(self, node: ASTMultipleClassDefinition):
        pass

    @abstractmethod
    def visit_MultipleClassMemberDefinition(self, node: ASTMultipleClassMemberDefinition):
        pass

    @abstractmethod
    def visit_MultipleCommaExpression(self, node: ASTMultipleCommaExpression):
        pass

    @abstractmethod
    def visit_MultipleCommaParameter(self, node: ASTMultipleCommaParameter):
        pass

    @abstractmethod
    def visit_MultipleStatement(self, node: ASTMultipleStatement):
        pass

    @abstractmethod
    def visit_Parameter(self, node: ASTParameter):
        pass

    @abstractmethod
    def visit_ParameterList(self, node: ASTParameterList):
        pass

    @abstractmethod
    def visit_StatementBreak(self, node: ASTStatementBreak):
        pass

    @abstractmethod
    def visit_StatementCIN(self, node: ASTStatementCIN):
        pass

    @abstractmethod
    def visit_StatementCOUT(self, node: ASTStatementCOUT):
        pass

    @abstractmethod
    def visit_StatementExpression(self, node: ASTStatementExpression):
        pass

    @abstractmethod
    def visit_StatementIF(self, node: ASTStatementIF):
        pass

    @abstractmethod
    def visit_StatementIFELSE(self, node: ASTStatementIFELSE):
        pass

    @abstractmethod
    def visit_StatementMultipleStatement(self, node: ASTStatementMultipleStatement):
        pass

    @abstractmethod
    def visit_StatementToVariableDeclaration(self, node: ASTStatementToVariableDeclaration):
        pass

    @abstractmethod
    def visit_StatementReturn(self, node: ASTStatementReturn):
        pass

    @abstractmethod
    def visit_StatementSwitch(self, node: ASTStatementSwitch):
        pass

    @abstractmethod
    def visit_StatementWhile(self, node: ASTStatementWhile):
        pass

    @abstractmethod
    def visit_VariableDeclaration(self, node: ASTVariableDeclaration):
        pass

    @abstractmethod
    def visit_Terminal(self, node: ASTTerminal):
        pass