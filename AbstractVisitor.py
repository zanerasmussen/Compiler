from abc import ABCMeta, abstractmethod
from AST import *

class ASTVisitor(metaclass=ABCMeta):
    @abstractmethod
    def pre_visit_Argument(self, node: ASTArgument):
        pass

    @abstractmethod
    def post_visit_Argument(self, node: ASTArgument):
        pass

    @abstractmethod
    def pre_visit_ArgumentList(self, node: ASTArgumentList):
        pass

    @abstractmethod
    def post_visit_ArgumentList(self, node: ASTArgumentList):
        pass
    
    @abstractmethod
    def pre_visit_ArgOrIdx(self, node: ASTArgOrIdx):
        pass
    
    @abstractmethod
    def post_visit_ArgOrIdx(self, node: ASTArgOrIdx):
        pass

    @abstractmethod
    def pre_visit_Case(self, node: ASTCase):
        pass

    @abstractmethod
    def post_visit_Case(self, node: ASTCase):
        pass

    @abstractmethod
    def pre_visit_CaseBlock(self, node: ASTCaseBlock):
        pass

    @abstractmethod
    def post_visit_CaseBlock(self, node: ASTCaseBlock):
        pass

    @abstractmethod
    def pre_visit_ClassDefinition(self, node: ASTClassDefinition):
        pass
    
    @abstractmethod
    def post_visit_ClassDefinition(self, node: ASTClassDefinition):
        pass

    @abstractmethod
    def pre_visit_ClassMemberDefinition(self, node: ASTClassMemberDefinition):
        pass

    @abstractmethod
    def post_visit_ClassMemberDefinition(self, node: ASTClassMemberDefinition):
        pass

    @abstractmethod
    def pre_visit_CompilationUnit(self, node: ASTCompilationUnit):
        pass

    @abstractmethod
    def post_visit_CompilationUnit(self, node: ASTCompilationUnit):
        pass

    @abstractmethod
    def pre_visit_ConstructorDeclaration(self, node: ASTConstructorDeclaration):
        pass

    @abstractmethod
    def post_visit_ConstructorDeclaration(self, node: ASTConstructorDeclaration):
        pass

    @abstractmethod
    def pre_visit_DataMemberDeclaration(self, node: ASTDataMemberDeclaration):
        pass

    @abstractmethod
    def post_visit_DataMemberDeclaration(self, node: ASTDataMemberDeclaration):
        pass

    @abstractmethod
    def pre_visit_ExpressionArgIdx(self, node: ASTExpressionArgIdx):
        pass

    @abstractmethod
    def post_visit_ExpressionArgIdx(self, node: ASTExpressionArgIdx):
        pass

    @abstractmethod
    def pre_visit_ExpressionDotID(self, node: ASTExpressionDotID):
        pass

    @abstractmethod
    def post_visit_ExpressionDotID(self, node: ASTExpressionDotID):
        pass

    @abstractmethod
    def pre_visit_ExpressionMinus(self, node: ASTExpressionMinus):
        pass

    @abstractmethod
    def post_visit_ExpressionMinus(self, node: ASTExpressionMinus):
        pass

    @abstractmethod
    def pre_visit_ExpressionNew(self, node: ASTExpressionNew):
        pass

    @abstractmethod
    def post_visit_ExpressionNew(self, node: ASTExpressionNew):
        pass

    @abstractmethod
    def pre_visit_ExpressionNot(self, node: ASTExpressionNot):
        pass

    @abstractmethod
    def post_visit_ExpressionNot(self, node: ASTExpressionNot):
        pass

    @abstractmethod
    def pre_visit_ExpressionPlus(self, node: ASTExpressionPlus):
        pass

    @abstractmethod
    def post_visit_ExpressionPlus(self, node: ASTExpressionPlus):
        pass

    @abstractmethod
    def pre_visit_ExpressionPAREN(self, node: ASTExpressionPAREN):
        pass
    
    @abstractmethod
    def post_visit_ExpressionPAREN(self, node: ASTExpressionPAREN):
        pass

    @abstractmethod
    def pre_visit_ExpressionEAANDE(self, node: ASTExpressionEAANDE):
        pass

    @abstractmethod
    def post_visit_ExpressionEAANDE(self, node: ASTExpressionEAANDE):
        pass

    @abstractmethod
    def pre_visit_ExpresssionECEqualE(self, node: ASTExpressionECEqualE):
        pass

    @abstractmethod
    def post_visit_ExpresssionECEqualE(self, node: ASTExpressionECEqualE):
        pass

    @abstractmethod
    def pre_visit_ExpressionEDivideE(self, node: ASTExpressionEDivideE):
        pass

    @abstractmethod
    def post_visit_ExpressionEDivideE(self, node: ASTExpressionEDivideE):
        pass

    @abstractmethod
    def pre_visit_ExpressionEDivideEqualE(self, node: ASTExpressionEDivideEqualE):
        pass

    @abstractmethod
    def post_visit_ExpressionEDivideEqualE(self, node: ASTExpressionEDivideEqualE):
        pass
    
    @abstractmethod
    def pre_visit_ExpressionEEqualE(self, node: ASTExpressionEEqualE):
        pass

    @abstractmethod
    def post_visit_ExpressionEEqualE(self, node: ASTExpressionEEqualE):
        pass

    @abstractmethod
    def pre_visit_ExpressionEGreaterE(self, node: ASTExpressionEGreaterE):
        pass

    @abstractmethod
    def post_visit_ExpressionEGreaterE(self, node: ASTExpressionEGreaterE):
        pass

    @abstractmethod
    def pre_visit_ExpressionEGreaterEqualE(self, node: ASTExpressionEGreaterEqualE):
        pass

    @abstractmethod
    def post_visit_ExpressionEGreaterEqualE(self, node: ASTExpressionEGreaterEqualE):
        pass

    @abstractmethod
    def pre_visit_ExpressionELessE(self, node: ASTExpressionELessE):
        pass

    @abstractmethod
    def post_visit_ExpressionELessE(self, node: ASTExpressionELessE):
        pass

    @abstractmethod
    def pre_visit_ExpressionELessEqualE(self, node: ASTExpressionELessEqualE):
        pass

    @abstractmethod
    def post_visit_ExpressionELessEqualE(self, node: ASTExpressionELessEqualE):
        pass

    @abstractmethod
    def pre_visit_ExpressionEMinusE(self, node: ASTExpressionEMinusE):
        pass

    @abstractmethod
    def post_visit_ExpressionEMinusE(self, node: ASTExpressionEMinusE):
        pass

    @abstractmethod
    def pre_visit_ExpressionEMinusEqualE(self, node: ASTExpressionEMinusEqualE):
        pass

    @abstractmethod
    def post_visit_ExpressionEMinusEqualE(self, node: ASTExpressionEMinusEqualE):
        pass

    @abstractmethod
    def pre_visit_ExpressionENotEqualE(self, node: ASTExpressionENotEqualE):
        pass

    @abstractmethod
    def post_visit_ExpressionENotEqualE(self, node: ASTExpressionENotEqualE):
        pass

    @abstractmethod
    def pre_visit_ExpressionEOORE(self, node: ASTExpressionEOORE):
        pass

    @abstractmethod
    def post_visit_ExpressionEOORE(self, node: ASTExpressionEOORE):
        pass

    @abstractmethod
    def pre_visit_ExpressionEPlusE(self, node: ASTExpressionEPlusE):
        pass
    
    @abstractmethod
    def post_visit_ExpressionEPlusE(self, node: ASTExpressionEPlusE):
        pass

    @abstractmethod
    def pre_visit_ExpressionEPlusEqualE(self, node: ASTExpressionEPlusEqualE):
        pass

    @abstractmethod
    def post_visit_ExpressionEPlusEqualE(self, node: ASTExpressionEPlusEqualE):
        pass

    @abstractmethod
    def pre_visit_ExpressionETimesE(self, node: ASTExpressionETimesE):
        pass

    @abstractmethod
    def post_visit_ExpressionETimesE(self, node: ASTExpressionETimesE):
        pass

    @abstractmethod
    def pre_visit_ExpressionETimesEqualE(self, node: ASTExpressionETimesEqualE):
        pass

    @abstractmethod
    def post_visit_ExpressionETimesEqualE(self, node: ASTExpressionETimesEqualE):
        pass

    @abstractmethod
    def pre_visit_Index(self, node: ASTIndex):
        pass

    @abstractmethod
    def post_visit_Index(self, node: ASTIndex):
        pass
        
    @abstractmethod
    def pre_visit_Initializer(self, node: ASTInitializer):
        pass

    @abstractmethod
    def post_visit_Initializer(self, node: ASTInitializer):
        pass

    @abstractmethod
    def pre_visit_MaybeArgumentList(self, node: ASTMaybeArgumentList):
        pass

    @abstractmethod
    def post_visit_MaybeArgumentList(self, node: ASTMaybeArgumentList):
        pass

    @abstractmethod
    def pre_visit_MaybeExpression(self, node: ASTMaybeExpression):
        pass

    @abstractmethod
    def post_visit_MaybeExpression(self, node: ASTMaybeExpression):
        pass

    @abstractmethod
    def pre_visit_MaybeInitializer(self, node: ASTMaybeInitializer):
        pass

    @abstractmethod
    def post_visit_MaybeInitializer(self, node: ASTMaybeInitializer):
        pass

    @abstractmethod
    def pre_visit_MaybeParamList(self, node: ASTMaybeParamList):
        pass

    @abstractmethod
    def post_visit_MaybeParamList(self, node: ASTMaybeParamList):
        pass

    @abstractmethod
    def pre_visit_MethodBody(self, node: ASTMethodBody):
        pass

    @abstractmethod
    def post_visit_MethodBody(self, node: ASTMethodBody):
        pass

    @abstractmethod
    def pre_visit_MethodDeclaration(self, node: ASTMethodDeclaration):
        pass

    @abstractmethod
    def post_visit_MethodDeclaration(self, node: ASTMethodDeclaration):
        pass

    @abstractmethod
    def pre_visit_MethodSuffix(self, node: ASTMethodSuffix):
        pass

    @abstractmethod
    def post_visit_MethodSuffix(self, node: ASTMethodSuffix):
        pass

    @abstractmethod
    def pre_visit_MultipleCase(self, node: ASTMultipleCase):
        pass

    @abstractmethod
    def post_visit_MultipleCase(self, node: ASTMultipleCase):
        pass

    @abstractmethod
    def pre_visit_MultipleClassDefinition(self, node: ASTMultipleClassDefinition):
        pass

    @abstractmethod
    def post_visit_MultipleClassDefinition(self, node: ASTMultipleClassDefinition):
        pass
                
    @abstractmethod
    def pre_visit_MultipleClassMemberDefinition(self, node: ASTMultipleClassMemberDefinition):
        pass

    @abstractmethod
    def post_visit_MultipleClassMemberDefinition(self, node: ASTMultipleClassMemberDefinition):
        pass

    @abstractmethod
    def pre_visit_MultipleCommaExpression(self, node: ASTMultipleCommaExpression):
        pass

    @abstractmethod
    def post_visit_MultipleCommaExpression(self, node: ASTMultipleCommaExpression):
        pass

    @abstractmethod
    def pre_visit_MultipleCommaParameter(self, node: ASTMultipleCommaParameter):
        pass

    @abstractmethod
    def post_visit_MultipleCommaParameter(self, node: ASTMultipleCommaParameter):
        pass

    @abstractmethod
    def pre_visit_MultipleStatement(self, node: ASTMultipleStatement):
        pass

    @abstractmethod
    def post_visit_MultipleStatement(self, node: ASTMultipleStatement):
        pass

    @abstractmethod
    def pre_visit_Parameter(self, node: ASTParameter):
        pass

    @abstractmethod
    def post_visit_Parameter(self, node: ASTParameter):
        pass

    @abstractmethod
    def pre_visit_ParameterList(self, node: ASTParameterList):
        pass

    @abstractmethod
    def post_visit_ParameterList(self, node: ASTParameterList):
        pass

    @abstractmethod
    def pre_visit_StatementBreak(self, node: ASTStatementBreak):
        pass

    @abstractmethod
    def post_visit_StatementBreak(self, node: ASTStatementBreak):
        pass    

    @abstractmethod
    def pre_visit_StatementCIN(self, node: ASTStatementCIN):
        pass

    @abstractmethod
    def post_visit_StatementCIN(self, node: ASTStatementCIN):
        pass

    @abstractmethod
    def pre_visit_StatementCOUT(self, node: ASTStatementCOUT):
        pass

    @abstractmethod
    def post_visit_StatementCOUT(self, node: ASTStatementCOUT):
        pass

    @abstractmethod
    def pre_visit_StatementExpression(self, node: ASTStatementExpression):
        pass

    @abstractmethod
    def post_visit_StatementExpression(self, node: ASTStatementExpression):
        pass

    @abstractmethod
    def pre_visit_StatementIF(self, node: ASTStatementIF):
        pass

    @abstractmethod
    def post_visit_StatementIF(self, node: ASTStatementIF):
        pass

    @abstractmethod
    def pre_visit_StatementIFELSE(self, node: ASTStatementIFELSE):
        pass

    @abstractmethod
    def post_visit_StatementIFELSE(self, node: ASTStatementIFELSE):
       pass

    @abstractmethod
    def pre_visit_StatementMultipleStatement(self, node: ASTStatementMultipleStatement):
        pass

    @abstractmethod
    def post_visit_StatementMultipleStatement(self, node: ASTStatementMultipleStatement):
        pass

    @abstractmethod
    def pre_visit_StatementToVariableDeclaration(self, node: ASTStatementToVariableDeclaration):
        pass

    @abstractmethod
    def post_visit_StatementToVariableDeclaration(self, node: ASTStatementToVariableDeclaration):
        pass

    @abstractmethod
    def pre_visit_StatementReturn(self, node: ASTStatementReturn):
        pass

    @abstractmethod
    def post_visit_StatementReturn(self, node: ASTStatementReturn):
        pass

    @abstractmethod
    def pre_visit_StatementSwitch(self, node: ASTStatementSwitch):
        pass

    @abstractmethod
    def post_visit_StatementSwitch(self, node: ASTStatementSwitch):
        pass

    @abstractmethod
    def pre_visit_StatementWhile(self, node: ASTStatementWhile):
        pass

    @abstractmethod
    def post_visit_StatementWhile(self, node: ASTStatementWhile):
        pass

    @abstractmethod
    def pre_visit_VariableDeclaration(self, node: ASTVariableDeclaration):
        pass

    @abstractmethod
    def post_visit_VariableDeclaration(self, node: ASTVariableDeclaration):
        pass

    @abstractmethod
    def pre_visit_Terminal(self, node: ASTTerminal):
        pass

    @abstractmethod
    def post_visit_Terminal(self, node: ASTTerminal):
        pass