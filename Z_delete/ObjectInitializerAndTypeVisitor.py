from abc import ABCMeta, abstractmethod
from AbstractVisitor import ASTVisitor
from AST import *


class ObjectInitializerAndTypeVisitor(ASTVisitor):
    def __init__(self):
        self.symbol_tables = []
        self.has_Error = False
        self.errors = []

    def checkNew(self, node: ASTVariableDeclaration):
        #make sure New is of right type
        if node.Type != node.Initializer.Initializer.Expression.Type:
            self.has_Error = True
            self.errors.append(f"Error: Attempting to initalize object {node.Type} {node.ID} with invalid type of {node.Initializer.Initializer.Expression.Type}. Around line {node.lineno}")
                    
        #make sure NEW isn't of invalid type
        if node.Initializer.Initializer.Expression.Type == "void":
            self.has_Error = True
            self.errors.append(f"Error: Can not use void to declare a variable. Around line {node.lineno}")

        if ((node.Initializer.Initializer.Expression.Type == "int") or (node.Initializer.Initializer.Expression.Type == "char") or (node.Initializer.Initializer.Expression.Type == "bool") or (node.Initializer.Initializer.Expression.Type == "string")):
            if node.LRSquare== None:
                self.has_Error = True
                self.errors.append(f"Error : can not use 'NEW' with type {node.Initializer.Initializer.Expression.Type} without it setting variable {node.ID} to be an array. Around line {node.lineno}")
            else:
                if str(node.Initializer.Initializer.Expression.ArgOrIdx.Arg_Idx.__class__) == "<class 'AST.ASTIndex'>":
                    pass
                else:
                    self.has_Error = True
                    self.errors.append(f"Error : can not use 'NEW' with type {node.Initializer.Initializer.Expression.Type} when {node.ID} is an array type. Around line {node.lineno}")
        else:       
            if (node.LRSquare != None and str(node.Initializer.Initializer.Expression.ArgOrIdx.Arg_Idx.__class__) == "<class 'AST.ASTIndex'>") or (node.LRSquare == None and str(node.Initializer.Initializer.Expression.ArgOrIdx.Arg_Idx.__class__) == "<class 'AST.ASTArgument'>"):
                pass
            else:
                self.has_Error = True
                self.errors.append(f"Error: error when attempting to initialize object {node.Type} {node.ID}. Around line {node.lineno}")

    def checkType(self, type: str):
        if (type == 'void') or (type == 'int') or (type == 'char') or (type == 'bool') or (type == 'string'):
            pass
        else:
            doesClassExist = False
            for table in self.symbol_tables:
                for key, value in table.items():
                    symbol = value["symbol"]
                    if symbol.whatAmI == 'class' and symbol.Name== type:
                        doesClassExist = True
            if doesClassExist == False:
                self.has_Error = True
                self.errors.append(f"Error: there is no class '{type}'. Attempting to use a variable of that type is illegal")

    def pre_visit_Argument(self, node: ASTArgument):
        pass

    def post_visit_Argument(self, node: ASTArgument):
        pass

    def pre_visit_ArgumentList(self, node: ASTArgumentList):
        pass

    def post_visit_ArgumentList(self, node: ASTArgumentList):
        pass
    
    def pre_visit_ArgOrIdx(self, node: ASTArgOrIdx):
        pass
    
    def post_visit_ArgOrIdx(self, node: ASTArgOrIdx):
        pass

    def pre_visit_Case(self, node: ASTCase):
        pass

    def post_visit_Case(self, node: ASTCase):
        pass

    def pre_visit_CaseBlock(self, node: ASTCaseBlock):
        pass

    def post_visit_CaseBlock(self, node: ASTCaseBlock):
        pass

    def pre_visit_ClassDefinition(self, node: ASTClassDefinition):
        pass

    def post_visit_ClassDefinition(self, node: ASTClassDefinition):
        pass

    def pre_visit_ClassMemberDefinition(self, node: ASTClassMemberDefinition):
        pass

    def post_visit_ClassMemberDefinition(self, node: ASTClassMemberDefinition):
        pass

    def pre_visit_CompilationUnit(self, node: ASTCompilationUnit):
        pass

    def post_visit_CompilationUnit(self, node: ASTCompilationUnit):
        pass
        
    def pre_visit_ConstructorDeclaration(self, node: ASTConstructorDeclaration):
        pass

    def post_visit_ConstructorDeclaration(self, node: ASTConstructorDeclaration):
        pass

    def pre_visit_DataMemberDeclaration(self, node: ASTDataMemberDeclaration):
        pass

    def post_visit_DataMemberDeclaration(self, node: ASTDataMemberDeclaration):
        pass

    def pre_visit_ExpressionArgIdx(self, node: ASTExpressionArgIdx):
        pass

    def post_visit_ExpressionArgIdx(self, node: ASTExpressionArgIdx):
        pass

    def pre_visit_ExpressionDotID(self, node: ASTExpressionDotID):
        pass

    def post_visit_ExpressionDotID(self, node: ASTExpressionDotID):
        pass

    def pre_visit_ExpressionMinus(self, node: ASTExpressionMinus):
        pass

    def post_visit_ExpressionMinus(self, node: ASTExpressionMinus):
        pass

    def pre_visit_ExpressionNew(self, node: ASTExpressionNew):
        self.checkType(node.Type)
    
    def post_visit_ExpressionNew(self, node: ASTExpressionNew):
        pass

    def pre_visit_ExpressionNot(self, node: ASTExpressionNot):
        pass

    def post_visit_ExpressionNot(self, node: ASTExpressionNot):
        pass

    def pre_visit_ExpressionPlus(self, node: ASTExpressionPlus):
        pass

    def post_visit_ExpressionPlus(self, node: ASTExpressionPlus):
        pass

    def pre_visit_ExpressionPAREN(self, node: ASTExpressionPAREN):
        pass
    
    def post_visit_ExpressionPAREN(self, node: ASTExpressionPAREN):
        pass

    def pre_visit_ExpressionEAANDE(self, node: ASTExpressionEAANDE):
        pass

    def post_visit_ExpressionEAANDE(self, node: ASTExpressionEAANDE):
        pass

    def pre_visit_ExpresssionECEqualE(self, node: ASTExpressionECEqualE):
        pass

    def post_visit_ExpresssionECEqualE(self, node: ASTExpressionECEqualE):
        pass

    def pre_visit_ExpressionEDivideE(self, node: ASTExpressionEDivideE):
        pass

    def post_visit_ExpressionEDivideE(self, node: ASTExpressionEDivideE):
        pass

    def pre_visit_ExpressionEDivideEqualE(self, node: ASTExpressionEDivideEqualE):
        pass

    def post_visit_ExpressionEDivideEqualE(self, node: ASTExpressionEDivideEqualE):
        pass
    
    def pre_visit_ExpressionEEqualE(self, node: ASTExpressionEEqualE):
        pass

    def post_visit_ExpressionEEqualE(self, node: ASTExpressionEEqualE):
        pass

    def pre_visit_ExpressionEGreaterE(self, node: ASTExpressionEGreaterE):
        pass

    def post_visit_ExpressionEGreaterE(self, node: ASTExpressionEGreaterE):
        pass

    def pre_visit_ExpressionEGreaterEqualE(self, node: ASTExpressionEGreaterEqualE):
        pass

    def post_visit_ExpressionEGreaterEqualE(self, node: ASTExpressionEGreaterEqualE):
        pass

    def pre_visit_ExpressionELessE(self, node: ASTExpressionELessE):
        pass

    def post_visit_ExpressionELessE(self, node: ASTExpressionELessE):
        pass

    def pre_visit_ExpressionELessEqualE(self, node: ASTExpressionELessEqualE):
        pass

    def post_visit_ExpressionELessEqualE(self, node: ASTExpressionELessEqualE):
        pass

    def pre_visit_ExpressionEMinusE(self, node: ASTExpressionEMinusE):
        pass

    def post_visit_ExpressionEMinusE(self, node: ASTExpressionEMinusE):
        pass

    def pre_visit_ExpressionEMinusEqualE(self, node: ASTExpressionEMinusEqualE):
        pass

    def post_visit_ExpressionEMinusEqualE(self, node: ASTExpressionEMinusEqualE):
        pass

    def pre_visit_ExpressionENotEqualE(self, node: ASTExpressionENotEqualE):
        pass

    def post_visit_ExpressionENotEqualE(self, node: ASTExpressionENotEqualE):
        pass

    def pre_visit_ExpressionEOORE(self, node: ASTExpressionEOORE):
        pass

    def post_visit_ExpressionEOORE(self, node: ASTExpressionEOORE):
        pass

    def pre_visit_ExpressionEPlusE(self, node: ASTExpressionEPlusE):
        pass
    
    def post_visit_ExpressionEPlusE(self, node: ASTExpressionEPlusE):
        pass

    def pre_visit_ExpressionEPlusEqualE(self, node: ASTExpressionEPlusEqualE):
        pass

    def post_visit_ExpressionEPlusEqualE(self, node: ASTExpressionEPlusEqualE):
        pass

    def pre_visit_ExpressionETimesE(self, node: ASTExpressionETimesE):
        pass

    def post_visit_ExpressionETimesE(self, node: ASTExpressionETimesE):
        pass

    def pre_visit_ExpressionETimesEqualE(self, node: ASTExpressionETimesEqualE):
        pass

    def post_visit_ExpressionETimesEqualE(self, node: ASTExpressionETimesEqualE):
        pass

    def pre_visit_Index(self, node: ASTIndex):
        pass

    def post_visit_Index(self, node: ASTIndex):
        pass
        
    def pre_visit_Initializer(self, node: ASTInitializer):
        pass

    def post_visit_Initializer(self, node: ASTInitializer):
        pass

    def pre_visit_MaybeArgumentList(self, node: ASTMaybeArgumentList):
        pass

    def post_visit_MaybeArgumentList(self, node: ASTMaybeArgumentList):
        pass

    def pre_visit_MaybeExpression(self, node: ASTMaybeExpression):
        pass

    def post_visit_MaybeExpression(self, node: ASTMaybeExpression):
        pass

    def pre_visit_MaybeInitializer(self, node: ASTMaybeInitializer):
        pass

    def post_visit_MaybeInitializer(self, node: ASTMaybeInitializer):
        pass

    def pre_visit_MaybeParamList(self, node: ASTMaybeParamList):
        pass

    def post_visit_MaybeParamList(self, node: ASTMaybeParamList):
        pass

    def pre_visit_MethodBody(self, node: ASTMethodBody):
        pass

    def post_visit_MethodBody(self, node: ASTMethodBody):
        pass

    def pre_visit_MethodDeclaration(self, node: ASTMethodDeclaration):
        self.checkType(node.Type)

    def post_visit_MethodDeclaration(self, node: ASTMethodDeclaration):
        pass

    def pre_visit_MethodSuffix(self, node: ASTMethodSuffix):
        pass

    def post_visit_MethodSuffix(self, node: ASTMethodSuffix):
        pass

    def pre_visit_MultipleCase(self, node: ASTMultipleCase):
        pass

    def post_visit_MultipleCase(self, node: ASTMultipleCase):
        pass

    def pre_visit_MultipleClassDefinition(self, node: ASTMultipleClassDefinition):
        pass

    def post_visit_MultipleClassDefinition(self, node: ASTMultipleClassDefinition):
        pass
                
    def pre_visit_MultipleClassMemberDefinition(self, node: ASTMultipleClassMemberDefinition):
        pass

    def post_visit_MultipleClassMemberDefinition(self, node: ASTMultipleClassMemberDefinition):
        pass

    def pre_visit_MultipleCommaExpression(self, node: ASTMultipleCommaExpression):
        pass

    def post_visit_MultipleCommaExpression(self, node: ASTMultipleCommaExpression):
        pass

    def pre_visit_MultipleCommaParameter(self, node: ASTMultipleCommaParameter):
        pass

    def post_visit_MultipleCommaParameter(self, node: ASTMultipleCommaParameter):
        pass

    def pre_visit_MultipleStatement(self, node: ASTMultipleStatement):
        pass

    def post_visit_MultipleStatement(self, node: ASTMultipleStatement):
        pass

    def pre_visit_Parameter(self, node: ASTParameter):
        self.checkType(node.Type)

    def post_visit_Parameter(self, node: ASTParameter):
        pass

    def pre_visit_ParameterList(self, node: ASTParameterList):
        pass

    def post_visit_ParameterList(self, node: ASTParameterList):
        pass

    def pre_visit_StatementBreak(self, node: ASTStatementBreak):
        pass

    def post_visit_StatementBreak(self, node: ASTStatementBreak):
        pass    

    def pre_visit_StatementCIN(self, node: ASTStatementCIN):
        pass

    def post_visit_StatementCIN(self, node: ASTStatementCIN):
        pass

    def pre_visit_StatementCOUT(self, node: ASTStatementCOUT):
        pass

    def post_visit_StatementCOUT(self, node: ASTStatementCOUT):
        pass

    def pre_visit_StatementExpression(self, node: ASTStatementExpression):
        pass

    def post_visit_StatementExpression(self, node: ASTStatementExpression):
        pass

    def pre_visit_StatementIF(self, node: ASTStatementIF):
        pass

    def post_visit_StatementIF(self, node: ASTStatementIF):
        pass

    def pre_visit_StatementIFELSE(self, node: ASTStatementIFELSE):
        pass

    def post_visit_StatementIFELSE(self, node: ASTStatementIFELSE):
        pass

    def pre_visit_StatementMultipleStatement(self, node: ASTStatementMultipleStatement):
        pass

    def post_visit_StatementMultipleStatement(self, node: ASTStatementMultipleStatement):
        pass

    def pre_visit_StatementToVariableDeclaration(self, node: ASTStatementToVariableDeclaration):
        pass

    def post_visit_StatementToVariableDeclaration(self, node: ASTStatementToVariableDeclaration):
        pass

    def pre_visit_StatementReturn(self, node: ASTStatementReturn):
        pass

    def post_visit_StatementReturn(self, node: ASTStatementReturn):
        pass

    def pre_visit_StatementSwitch(self, node: ASTStatementSwitch):
        pass

    def post_visit_StatementSwitch(self, node: ASTStatementSwitch):
        pass

    def pre_visit_StatementWhile(self, node: ASTStatementWhile):
        pass

    def post_visit_StatementWhile(self, node: ASTStatementWhile):
        pass

    def pre_visit_VariableDeclaration(self, node: ASTVariableDeclaration):
        self.checkType(node.Type)
        if node.Initializer.Initializer != None:
            if str(node.Initializer.Initializer.Expression.__class__) == "<class 'AST.ASTExpressionNew'>":
                self.checkNew(node)

    def post_visit_VariableDeclaration(self, node: ASTVariableDeclaration):
        pass

    def pre_visit_Terminal(self, node: ASTTerminal):
        pass

    def post_visit_Terminal(self, node: ASTTerminal):
        pass