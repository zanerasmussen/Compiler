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

    def pre_visit_Case(self, node: ASTCase):
        type = theLexerTester(str(node.NumOrChar))

    def pre_visit_ClassDefinition(self, node: ASTClassDefinition):
        self.current_class = str(node.ID)
        self.enter_scope()
        symbol = self.create_symbol(str("class"), str(node.ID), str(node.Class), 12, False, True)
        lineno = node.lineno
        self.add_to_symbol_table(symbol, lineno)
        
    def post_visit_ClassDefinition(self, node: ASTClassDefinition):
        self.current_class = ""
        self.exit_scope()

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

    def pre_visit_Parameter(self, node: ASTParameter):
        type = str(node.Type)
        if node.LRSquare is not None:
            type = str(node.Type) + "[]"
        symbol = self.create_symbol("variable", str(node.ID), type, 12, False, True)
        lineno = node.lineno
        self.add_to_symbol_table(symbol, lineno)

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
