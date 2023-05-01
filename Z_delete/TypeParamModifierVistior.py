from abc import ABCMeta, abstractmethod
from AbstractVisitor import ASTVisitor
from AST import *
from SupportFiles.theLexer import theLexerTester

class Unique:
    def __init__(self):
        self.id = -1

    def getID(self):
        self.id += 1
        return self.id

class TypeParamModifierVistior(ASTVisitor):
    def __init__(self):
        self.UID = Unique()
        self.symbolTable = []
        self.scope_stack = []
        self.paramList = []
        self.has_Error = False
        self.errors = []
        self.Terminal_stack = []
        #('ID'/'Terminal', 'isInitialized', 'name', 'Type', 'HasIndex', 'AccessingIndex')

    def enter_scope(self):
        new_scope = self.UID.getID()
        self.scope_stack.append(new_scope)

    def exit_scope(self):
        self.scope_stack.pop()

    def assignmentChecking(self, E1, E2, lineno):
        if ((E1[4] == True and E1[5] == True and E2[4] == True and E2[5] == True) or (E1[4] == True and E1[5] == True and E2[4] == False and E2[5] == False) or (E1[4] == True and E1[5] == False and E2[4] == True and E2[5] == False) or (E1[4] == False and E1[5] == False and E2[4] == True and E2[5] == True) or (E1[4] == False and E1[5] == False and E2[4] == False and E2[5] == False)):
            pass
        else:
            self.has_Error = True
            self.errors.append(f"Error: There is an error with assinging arrays with pointers or with no indexes. Around line {lineno}")

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
        self.enter_scope()
    
    def post_visit_ClassDefinition(self, node: ASTClassDefinition):
        self.exit_scope()

    def pre_visit_ClassMemberDefinition(self, node: ASTClassMemberDefinition):
        pass

    def post_visit_ClassMemberDefinition(self, node: ASTClassMemberDefinition):
        pass

    def pre_visit_CompilationUnit(self, node: ASTCompilationUnit):
        self.enter_scope()

    def post_visit_CompilationUnit(self, node: ASTCompilationUnit):
        self.exit_scope()

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
        pass

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
        #pop E2
        # is initialized

        #pop e1
        #is initialized sets to true

        #type check e1 and e2
        #if e2
        # E2 = self.Terminal_stack.pop()
        # if E2[1] == False:
        #     self.has_Error = True
        #     self.errors.append(f"Error: attempting to use {E2[2]} and it has not been initialized. Around line {node.lineno}")


        # E1 = self.Terminal_stack.pop()
        # E1[1] = True

        # if E1[3] != E2[3]:
        #     self.has_Error = True
        #     self.errors.append(f"Error: attempting to divide {E1[2]} to {E2[2]} and they are not of the same type. Around line {node.lineno}")

        # if E2[3] != "INT" or E1[3] != "INT":
        #     self.has_Error = True
        #     self.errors.append(f"Error: attempting to divide {E1[2]} to {E2[2]} and they must be of type 'int' to divide. Around line {node.lineno}")
        
        # self.Terminal_stack.append(('terminal', True, '$CUSTOM', E1[3], False, False))

    def pre_visit_ExpressionEDivideE(self, node: ASTExpressionEDivideE):
        pass

    def post_visit_ExpressionEDivideE(self, node: ASTExpressionEDivideE):
        pass
        # E2 = self.Terminal_stack.pop()
        # if E2[1] == False:
        #     self.has_Error = True
        #     self.errors.append(f"Error: attempting to use {E2[2]} and it has not been initialized. Around line {node.lineno}")
        # if E2[4] != E2[5]:
        #     self.has_Error = True
        #     self.errors.append(f"Error: attempting to use {E2[2]}. Index reference is needed. Around line {node.lineno}")

        # E1 = self.Terminal_stack.pop()
        # if E1[1] == False:
        #     self.has_Error = True
        #     self.errors.append(f"Error: attempting to use {E1[2]} and it has not been initialized. Around line {node.lineno}")
        # if E1[4] != E1[5]:
        #     self.has_Error = True
        #     self.errors.append(f"Error: attempting to use {E1[2]}. Index reference is needed. Around line {node.lineno}")

        # if E1[3] != E2[3]:
        #     self.has_Error = True
        #     self.errors.append(f"Error: attempting to divide {E1[2]} to {E2[2]} and they are not of the same type. Around line {node.lineno}")

        # if E2[3] != "INT" or E1[3] != "INT":
        #     self.has_Error = True
        #     self.errors.append(f"Error: attempting to divide {E1[2]} to {E2[2]} and they must be of type 'int' to divide. Around line {node.lineno}")
        
        # self.Terminal_stack.append(('terminal', True, '$CUSTOM', E1[3], False, False))

    def pre_visit_ExpressionEDivideEqualE(self, node: ASTExpressionEDivideEqualE):
        pass

    def post_visit_ExpressionEDivideEqualE(self, node: ASTExpressionEDivideEqualE):
        pass
    
    def pre_visit_ExpressionEEqualE(self, node: ASTExpressionEEqualE):
        pass

    def post_visit_ExpressionEEqualE(self, node: ASTExpressionEEqualE):
        E2 = self.Terminal_stack.pop()
        if E2[1] == False:
            self.has_Error = True
            self.errors.append(f"Error: attempting to use {E2[2]} and it has not been initialized. Around line {node.lineno}")

        E1 = self.Terminal_stack.pop()
        tempList = list(E1)
        tempList[1] = True
        E1 = tuple(tempList)
        if (E1[0] == 'terminal' and (E1[3] == "INT" or E1[3] == "CHAR" or E1[3] == 'TRUE' or E1[3] == 'FALSE' or E1[3] == 'STRING')):
            self.has_Error = True
            self.errors.append(f"Error: {E1[2]} can not be assigned a value. Around line {node.lineno}")
        
        if (E1[0] != 'terminal' and E2[0] != 'terminal'):
            pass

        if E1[3] == 'null':
            self.has_Error = True
            self.errors.append(f"Error: {E1[2]} is of type null. Can not assign 'null' to a value. Around line {node.lineno}")

        if E1[3] == 'this':
            self.has_Error = True
            self.errors.append(f"Error: {E1[2]} is of type this. Can not assign 'this' to a value. Around line {node.lineno}")

        
        if E2[3] != 'null':
            if E1[3] != E2[3]:
                self.has_Error = True
                self.errors.append(f"Error: {E1[2]} and {E2[2]} need to be of the same type. '{E1[3]}' and '{E2[3]}' were given. Around line {node.lineno}")

        else:
            tempList = list(E1)
            tempList[1] = False
            E1 = tuple(tempList)
            
        self.assignmentChecking(E1, E2, node.lineno)

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
        # E2 = self.Terminal_stack.pop()
        # if E2[1] == False:
        #     self.has_Error = True
        #     self.errors.append(f"Error: attempting to use {E2[2]} and it has not been initialized. Around line {node.lineno}")
        # if E2[4] != E2[5]:
        #     self.has_Error = True
        #     self.errors.append(f"Error: attempting to use {E2[2]}. Index reference is needed. Around line {node.lineno}")

        # E1 = self.Terminal_stack.pop()
        # if E1[1] == False:
        #     self.has_Error = True
        #     self.errors.append(f"Error: attempting to use {E1[2]} and it has not been initialized. Around line {node.lineno}")
        # if E1[4] != E1[5]:
        #     self.has_Error = True
        #     self.errors.append(f"Error: attempting to use {E1[2]}. Index reference is needed. Around line {node.lineno}")

        # if E1[3] != E2[3]:
        #     self.has_Error = True
        #     self.errors.append(f"Error: attempting to subtract {E1[2]} to {E2[2]} and they are not of the same type. Around line {node.lineno}")

        # if E2[3] != "INT" or E1[3] != "INT":
        #     self.has_Error = True
        #     self.errors.append(f"Error: attempting to subtract {E1[2]} to {E2[2]} and they must be of type 'int' to subtract. Around line {node.lineno}")
        
        # self.Terminal_stack.append(('terminal', True, '$CUSTOM', E1[3], False, False))

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
        # E2 = self.Terminal_stack.pop()
        # if E2[1] == False:
        #     self.has_Error = True
        #     self.errors.append(f"Error: attempting to use {E2[2]} and it has not been initialized. Around line {node.lineno}")
        # if E2[4] != E2[5]:
        #     self.has_Error = True
        #     self.errors.append(f"Error: attempting to use {E2[2]}. Index reference is needed. Around line {node.lineno}")

        # E1 = self.Terminal_stack.pop()
        # if E1[1] == False:
        #     self.has_Error = True
        #     self.errors.append(f"Error: attempting to use {E1[2]} and it has not been initialized. Around line {node.lineno}")
        # if E1[4] != E1[5]:
        #     self.has_Error = True
        #     self.errors.append(f"Error: attempting to use {E1[2]}. Index reference is needed. Around line {node.lineno}")

        # if E1[3] != E2[3]:
        #     self.has_Error = True
        #     self.errors.append(f"Error: attempting to add {E1[2]} to {E2[2]} and they are not of the same type. Around line {node.lineno}")

        # if E2[3] != "INT" or E1[3] != "INT":
        #     self.has_Error = True
        #     self.errors.append(f"Error: attempting to add {E1[2]} to {E2[2]} and they must be of type 'int' to add. Around line {node.lineno}")
        
        # self.Terminal_stack.append(('terminal', True, '$CUSTOM', E1[3], False, False))

    def pre_visit_ExpressionEPlusEqualE(self, node: ASTExpressionEPlusEqualE):
        pass

    def post_visit_ExpressionEPlusEqualE(self, node: ASTExpressionEPlusEqualE):
        pass

    def pre_visit_ExpressionETimesE(self, node: ASTExpressionETimesE):
        pass

    def post_visit_ExpressionETimesE(self, node: ASTExpressionETimesE):
        pass
        # E2 = self.Terminal_stack.pop()
        # if E2[1] == False:
        #     self.has_Error = True
        #     self.errors.append(f"Error: attempting to use {E2[2]} and it has not been initialized. Around line {node.lineno}")
        # if E2[4] != E2[5]:
        #     self.has_Error = True
        #     self.errors.append(f"Error: attempting to use {E2[2]}. Index reference is needed. Around line {node.lineno}")

        # E1 = self.Terminal_stack.pop()
        # if E1[1] == False:
        #     self.has_Error = True
        #     self.errors.append(f"Error: attempting to use {E1[2]} and it has not been initialized. Around line {node.lineno}")
        # if E1[4] != E1[5]:
        #     self.has_Error = True
        #     self.errors.append(f"Error: attempting to use {E1[2]}. Index reference is needed. Around line {node.lineno}")

        # if E1[3] != E2[3]:
        #     self.has_Error = True
        #     self.errors.append(f"Error: attempting to multiply {E1[2]} to {E2[2]} and they are not of the same type. Around line {node.lineno}")

        # if E2[3] != "INT" or E1[3] != "INT":
        #     self.has_Error = True
        #     self.errors.append(f"Error: attempting to multiply {E1[2]} to {E2[2]} and they must be of type 'int' to multiply. Around line {node.lineno}")
        
        # self.Terminal_stack.append(('terminal', True, '$CUSTOM', E1[3], False, False))

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
        pass

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
        pass

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
        pass
        # if node.Initializer.Initializer == None:
        #     pass
        # else:
        #     self.Terminal_stack.append(("ID", True, node.ID, node.Type, False))

    def post_visit_VariableDeclaration(self, node: ASTVariableDeclaration):
        pass
        #pop Initializer
        #   check if initialized
        #   check if index is needed

    def pre_visit_Terminal(self, node: ASTTerminal):
        tokType = theLexerTester(str(node.Terminal))
        if tokType.type != 'ID':
            self.Terminal_stack.append(("terminal", True, str(node.Terminal), str(tokType.type).upper(), False, False))
        else:
            for x in self.scope_stack:
                for key, value in self.symbolTable[x].items():
                    if key[0] == str(node.Terminal):
                        symbol = value['symbol']
                        self.Terminal_stack.append((str(symbol.whatAmI), symbol.isInitialized, symbol.Name, str(symbol.Type).upper(), symbol.hasIndex, False))

    def post_visit_Terminal(self, node: ASTTerminal):
        pass