from abc import ABCMeta, abstractmethod
from AbstractVisitor import ASTVisitor
from AST import *
from SupportFiles.theLexer import theLexerTester

#check for undeclared variable and for objects calling invalid method names. 
class Unique:
    def __init__(self):
        self.id = -1

    def getID(self):
        self.id += 1
        return self.id
    
class Symbol:
    def __init__(self, whatAmI: str, name: str, type, offset: int, isPrivate: bool, isInitialized: bool):
        self.whatAmI = whatAmI
        self.Name = name
        self.Type = type
        self.Offset = offset
        self.isPrivate = isPrivate
        self.isInitialized = isInitialized

class UndeclaredVisitor(ASTVisitor):
    def __init__(self):
        self.UID = Unique()
        self.oldSymbols = []
        self.symbol_tables = []
        self.scope_stack = []
        self.errors = []
        self.objects = []
        self.paramList = []
        self.current_class = ""

    def enter_scope(self):
        new_scope = self.UID.getID()
        self.scope_stack.append(new_scope)
        self.symbol_tables.append({})

    def exit_scope(self):
        self.scope_stack.pop()    

    def create_symbol(self, whatAmI: str, name: str, type: str, offset: int, isPrivate: bool, isInitialized: bool) -> Symbol:
        return Symbol(whatAmI = whatAmI, name=name, type=type, offset=offset, isPrivate=isPrivate, isInitialized=isInitialized)
    
    def add_to_symbol_table(self, symbol: Symbol, lineno: int):
        current_scope = self.scope_stack[-1]
        name = symbol.Name
        whatAmI = symbol.whatAmI
    
        self.symbol_tables[current_scope][(name, whatAmI)] = {
            "symbol": symbol,
            "can_access_scopes": self.scope_stack.copy(),
        }

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
        type = theLexerTester(str(node.NumOrChar))

    def post_visit_Case(self, node: ASTCase):
        pass

    def pre_visit_CaseBlock(self, node: ASTCaseBlock):
        pass

    def post_visit_CaseBlock(self, node: ASTCaseBlock):
        pass

    def pre_visit_ClassDefinition(self, node: ASTClassDefinition):
        self.current_class = str(node.ID)
        self.enter_scope()
        symbol = self.create_symbol(str("class"), str(node.ID), str(node.Class), 12, False, True)
        lineno = node.lineno
        self.add_to_symbol_table(symbol, lineno)
        
    def post_visit_ClassDefinition(self, node: ASTClassDefinition):
        self.current_class = ""
        self.exit_scope()

    def pre_visit_ClassMemberDefinition(self, node: ASTClassMemberDefinition):
        pass

    def post_visit_ClassMemberDefinition(self, node: ASTClassMemberDefinition):
        pass

    def pre_visit_CompilationUnit(self, node: ASTCompilationUnit):
        self.enter_scope()
        symbol = self.create_symbol(str("function"), str(node.main), str(node.void), 12, False, True)
        lineno = node.lineno
        self.add_to_symbol_table(symbol, lineno)

    def post_visit_CompilationUnit(self, node: ASTCompilationUnit):
        self.exit_scope()
        
    def pre_visit_ConstructorDeclaration(self, node: ASTConstructorDeclaration):
        self.current_constructor = str(node.ID)
        symbol = self.create_symbol(str("constructor"), str(node.ID), "ID", 4, False, True)
        lineno = node.lineno
        self.add_to_symbol_table(symbol, lineno)

    def post_visit_ConstructorDeclaration(self, node: ASTConstructorDeclaration):
        self.current_constructor = ""

    def pre_visit_DataMemberDeclaration(self, node: ASTDataMemberDeclaration):
        isPrivate = False
        isInitialized = False
        type = str(node.VariableDeclaration.Type) 
        if node.Modifier == 'PRIVATE':
            isPrivate = True
        if node.VariableDeclaration.LRSquare is not None:
            type = str(node.VariableDeclaration.Type) + "[]"
        if node.VariableDeclaration.Initializer.Initializer is not None:
            isInitialized = True
        symbol = self.create_symbol(str("dataMember"), str(node.VariableDeclaration.ID), type, 12, isPrivate, isInitialized)
        lineno = node.VariableDeclaration.lineno
        self.add_to_symbol_table(symbol, lineno)

    def post_visit_DataMemberDeclaration(self, node: ASTDataMemberDeclaration):
        pass

    def pre_visit_ExpressionArgIdx(self, node: ASTExpressionArgIdx):
        pass

    def post_visit_ExpressionArgIdx(self, node: ASTExpressionArgIdx):
        pass

    def pre_visit_ExpressionDotID(self, node: ASTExpressionDotID):
        isDataMeth = False
        for x in range(len(self.oldSymbols)):
            scope_class = ""
            for key, value in self.oldSymbols[x].items():    
                if key[1] == 'class':
                    scope_class = key[0]
                if key[0] == str(node.ID):
                    if key[1] == 'method' or key[1] == 'dataMember':
                        isDataMeth = True
                        symbol = value['symbol']
                        if symbol.isPrivate == True:
                            errorAdded = False
                            if scope_class != self.current_class:
                                errorAdded = True
                                self.errors.append(f"Error: Attempting to use '.'{node.ID}. This is a private method/datamember and can only be access in the class. Around line {node.lineno}")
                            if str(node.Expression.__class__) == "<class 'AST.ASTTerminal'>":
                                if node.Expression.Terminal != 'this' and errorAdded == False:
                                    self.errors.append(f"Error: Attempting to use '.'{node.ID}. This is a private method/datamember and can only be access in the class. Around line {node.lineno}")

        if isDataMeth == False:          
            self.errors.append(f"Error: Attempting to use '.'{node.ID}. Must be a dataMember or a method. Around line {node.lineno}")
        


    def post_visit_ExpressionDotID(self, node: ASTExpressionDotID):
        pass

    def pre_visit_ExpressionMinus(self, node: ASTExpressionMinus):
        pass

    def post_visit_ExpressionMinus(self, node: ASTExpressionMinus):
        pass

    def pre_visit_ExpressionNew(self, node: ASTExpressionNew):
        classExists = False
        if (node.Type == 'char' or node.Type == 'int'or node.Type == 'string' or node.Type == 'bool') and str(node.ArgOrIdx.Arg_Idx.__class__) == "<class 'AST.ASTIndex'>":
            classExists = True
        for x in range(len(self.oldSymbols)):
            for key, value in self.oldSymbols[x].items():
                if key[1] == 'class' and key[0] == str(node.Type):
                    classExists = True
        if classExists == False:
            self.errors.append(f"Error: Attempting to initialize an object of type {node.Type} and no such class exists. Around line {node.lineno}")

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
        self.current_method = str(node.ID)
        isPrivate = False
        type = str(node.Type)
        if node.Modifier == 'PRIVATE':
            isPrivate = True
        if node.LRSquare is not None:
            type = str(node.Type) + "[]"
        symbol = self.create_symbol(str("method"), str(node.ID), type, 12, isPrivate, True)
        lineno = node.lineno
        self.add_to_symbol_table(symbol, lineno)
        self.enter_scope()

    def post_visit_MethodDeclaration(self, node: ASTMethodDeclaration):
        self.exit_scope()
        self.current_method = ""

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
        type = str(node.Type)
        if node.LRSquare is not None:
            type = str(node.Type) + "[]"
        symbol = self.create_symbol("variable", str(node.ID), type, 12, False, True)
        lineno = node.lineno
        self.add_to_symbol_table(symbol, lineno)
    
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
        hasIndex = False
        isInitialized = False
        type = str(node.VariableDeclaration.Type)
        if node.VariableDeclaration.LRSquare is not None:
            type = str(node.VariableDeclaration.Type) + "[]"
        if node.VariableDeclaration.Initializer.Initializer is not None:
            isInitialized = True
        if node.VariableDeclaration.Type != 'void' and node.VariableDeclaration.Type != 'int' and node.VariableDeclaration.Type != 'char' and node.VariableDeclaration.Type != 'bool' and node.VariableDeclaration.Type != 'string':
            symbol = self.create_symbol("object", str(node.VariableDeclaration.ID), type, 12, False,  isInitialized)
        else:
            symbol = self.create_symbol("variable", str(node.VariableDeclaration.ID), type, 12, False, isInitialized)

        lineno = node.VariableDeclaration.lineno
        self.add_to_symbol_table(symbol, lineno)


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

    def post_visit_VariableDeclaration(self, node: ASTVariableDeclaration):
        pass

    def pre_visit_Terminal(self, node: ASTTerminal):
        tokType = theLexerTester(str(node.Terminal))
        varName = tokType.value
        varType = tokType.type
        varExists = False
        if varType == 'ID':
            for x in self.scope_stack:
                for item in self.symbol_tables[x]:
                     if item[0] == varName:
                         varExists = True
            if varExists == False:
                needError = True
                # for x in range(len(self.oldSymbols)):
                #     for key, value in self.oldSymbols[x].items():
                #         if key[0] == str(node.Terminal):
                #             if key[1] == 'method' or key[1] == 'dataMember':
                #                 needError = False
                if needError == True:
                    self.errors.append(f"Error: {varName} is used but never declared or used before it is declared. Around line {node.lineno}")
            else:
                for x in self.objects:
                    pass
        else:
            pass


        if varType == 'THIS':
            if self.current_class == '':
                self.errors.append(f"Error: 'this' is used and 'this' can not be used outside of a class. Around line {node.lineno}")

    def post_visit_Terminal(self, node: ASTTerminal):
        pass