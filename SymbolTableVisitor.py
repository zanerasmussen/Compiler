from AST import *
from SupportFiles.theLexer import theLexerTester
from AbstractVisitor import ASTVisitor

class Unique:
    def __init__(self):
        self.id = -1

    def getID(self):
        self.id += 1
        return self.id

class Symbol:
    def __init__(self, whatAmI: str, name: str, type, offset: int, isPrivate: bool, isPublic: bool, hasIndex: bool, isInitialized: bool):
        self.whatAmI = whatAmI
        self.Name = name
        self.Type = type
        self.Offset = offset
        self.isPrivate = isPrivate
        self.isPublic = isPublic
        self.hasIndex = hasIndex
        self.isInitialized = isInitialized

class SymbolTableVisitor(ASTVisitor):
    def __init__(self):
        self.UID = Unique()
        self.symbol_tables = []
        self.scope_stack = []
        self.has_Error = False
        self.errors = [] 
        self.paramList = []
        self.current_class = ""
        self.current_method = ""
        self.current_constructor = ""


    def enter_scope(self):
        new_scope = self.UID.getID()
        self.scope_stack.append(new_scope)
        self.symbol_tables.append({})

    def exit_scope(self):
        self.scope_stack.pop()

    def create_symbol(self, whatAmI: str, name: str, type: str, offset: int, isPrivate: bool, isPublic: bool, hasIndex: bool, isInitialized: bool) -> Symbol:
        return Symbol(whatAmI = whatAmI, name=name, type=type, offset=offset, isPrivate=isPrivate, isPublic=isPublic, hasIndex=hasIndex, isInitialized=isInitialized)


    def add_to_symbol_table(self, symbol: Symbol, lineno: int):
        current_scope = self.scope_stack[-1]
        name = symbol.Name
        whatAmI = symbol.whatAmI
        
        if whatAmI == 'constructor':
            if(name,'class') in self.symbol_tables[current_scope]:
                pass
            else:
                self.errors.append(f"Error: Constructor {name} is being called in a class with a different name. Names must be the same for a constructor. Around line {lineno}")
                self.has_Error = True

        if whatAmI == 'object':
            classExist = False
            className = symbol.Type
            for i in range(len(self.symbol_tables)-2, -1, -1):
                if (className, 'class') in self.symbol_tables[i]:
                    classExist = True
            if classExist == False:
                self.errors.append(f"Error: symbol {name} tried to create an object of {className} which doesn't exist. Around line {lineno}")
                self.has_Error = True
            if(name,'variable') in self.symbol_tables[current_scope]:
                self.errors.append(f"Error: {name} is already defined as an object. Around line {lineno}")
                self.has_Error = True

        #Data Members and Methods can not be the same name
        if whatAmI == 'dataMember':
            if(name,'method') in self.symbol_tables[current_scope]:
                self.errors.append(f"Error: symbol {name} already defined as a method. Around line {lineno}")
                self.has_Error = True
            if(name,'class') in self.symbol_tables[current_scope]:
                self.errors.append(f"Error: dataMember {name} is defined in class with the same name. Around line {lineno}")
                self.has_Error = True

        elif whatAmI == 'variable':
            if(name,'object') in self.symbol_tables[current_scope]:
                self.errors.append(f"Error: {name} is already defined as a variable. Around line {lineno}")
                self.has_Error = True

        elif whatAmI == 'method':
            if(name,'dataMember') in self.symbol_tables[current_scope]:
                self.errors.append(f"Error: symbol {name} already defined as a dataMember. Around line {lineno}")
                self.has_Error = True
            if(name,'class') in self.symbol_tables[current_scope]:
                self.errors.append(f"Error: method {name} is defined in class with the same name. Around line {lineno}")
                self.has_Error = True

        elif whatAmI == 'class':
            for i in range(len(self.symbol_tables)-2, -1, -1):
                if (name, 'class') in self.symbol_tables[i]:
                    self.errors.append(f"Error: class {name} is already as a class. Around line {lineno}")
                    self.has_Error = True

        if (name, whatAmI) in self.symbol_tables[current_scope]:
            #can have more than one constructor but must have the same name as the class defining it. 
            if whatAmI == 'constructor':
                self.errors.append(f"Error: Only one constructor is allowed. {name} is duplicated. Around line {lineno}")
                self.has_Error = True
            else:
                self.errors.append(f"Error: symbol {name} already defined. Around line {lineno}")
                self.has_Error = True
        
        if symbol.isPrivate == True:
            self.symbol_tables[current_scope][(name, whatAmI)] = {
                "symbol": symbol,
                "can_access_scopes": [current_scope]
            }
        else:
            self.symbol_tables[current_scope][(name, whatAmI)] = {
                "symbol": symbol,
                "can_access_scopes": self.scope_stack.copy(),
            }

    def add_Param(self, class_name: str, method_name: str, param_type: str, hasIndex: bool):
        method_found = False
        for param in self.paramList:
            if param['className'] == class_name and param['methodName'] == method_name:
                method_found = True
                param['numberOfParams'] += 1
                if param_type:
                    param['paramTypes'].append((param_type, hasIndex))
                else:
                    param['paramTypes'].append(())
                break
        if not method_found:
            new_method = {'className': class_name, 'methodName': method_name,
                        'numberOfParams': 1, 'paramTypes': [(param_type, hasIndex)]}
            self.paramList.append(new_method)

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
        if not (type.type == 'INT' or type.type == 'CHAR'):
            self.has_Error = True
            self.errors.append(f"Error: case can only be followed by an int or char. You gave case {type.value} {type.type}. Around line {node.lineno}")
        symbol = self.create_symbol(str("case"), str(node.NumOrChar), str(type.type), 12, False, False, False, True)
        lineno = node.lineno
        self.add_to_symbol_table(symbol, lineno)

    def post_visit_Case(self, node: ASTCase):
        pass

    def pre_visit_CaseBlock(self, node: ASTCaseBlock):
        pass

    def post_visit_CaseBlock(self, node: ASTCaseBlock):
        pass

    def pre_visit_ClassDefinition(self, node: ASTClassDefinition):
        self.current_class = str(node.ID)
        self.enter_scope()
        symbol = self.create_symbol(str("class"), str(node.ID), str(node.Class), 12, False, True, False, True)
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
        symbol = self.create_symbol(str("function"), str(node.main), str(node.void), 12, False, True, False, True)
        lineno = node.lineno
        self.add_to_symbol_table(symbol, lineno)

    def post_visit_CompilationUnit(self, node: ASTCompilationUnit):
        self.exit_scope()
        
    def pre_visit_ConstructorDeclaration(self, node: ASTConstructorDeclaration):
        self.current_constructor = str(node.ID)
        symbol = self.create_symbol(str("constructor"), str(node.ID), "ID", 4, False, False, False, True)
        lineno = node.lineno
        self.add_to_symbol_table(symbol, lineno)

    def post_visit_ConstructorDeclaration(self, node: ASTConstructorDeclaration):
        self.current_constructor = ""

    def pre_visit_DataMemberDeclaration(self, node: ASTDataMemberDeclaration):
        isPrivate = False
        isPublic = False
        hasIndex = False
        isInitialized = False
        if node.VariableDeclaration.Type == "void":
            self.has_Error = True
            self.errors.append(f"Error: DataMember can not have the type VOID. Near Class {self.current_class}")
        if node.Modifier == 'PRIVATE':
            isPrivate = True
        if node.Modifier == 'PUBLIC':
            isPublic = True
        if node.VariableDeclaration.LRSquare is not None:
            hasIndex = True
        if node.VariableDeclaration.Initializer.Initializer is not None:
            isInitialized = True
        symbol = self.create_symbol(str("dataMember"), str(node.VariableDeclaration.ID), str(node.VariableDeclaration.Type), 12, isPrivate, isPublic, hasIndex, isInitialized)
        lineno = node.VariableDeclaration.lineno
        self.add_to_symbol_table(symbol, lineno)

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
        if (self.current_class != "" and self.current_constructor!= ""):
            self.add_Param(str(self.current_class), str(self.current_constructor), None, False)
        if (self.current_class != "" and self.current_method!= ""):
            self.add_Param(str(self.current_class), str(self.current_method), None, False)


    def post_visit_MaybeParamList(self, node: ASTMaybeParamList):
        pass

    def pre_visit_MethodBody(self, node: ASTMethodBody):
        pass

    def post_visit_MethodBody(self, node: ASTMethodBody):
        pass

    def pre_visit_MethodDeclaration(self, node: ASTMethodDeclaration):
        self.current_method = str(node.ID)
        isPrivate = False
        isPublic = False
        hasIndex = False
        if node.Modifier == 'PRIVATE':
            isPrivate = True
        if node.Modifier == 'PUBLIC':
            isPublic = True
        if node.LRSquare is not None:
            hasIndex = True
        symbol = self.create_symbol(str("method"), str(node.ID), str(node.Type), 12, isPrivate, isPublic, hasIndex, True)
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
        if node.Type == 'void':
            self.has_Error = True
            self.errors.append(f"Error: Parameter {node.ID} can not be of type void. Around line {node.lineno}")

        hasIndex = False
        if node.LRSquare is not None:
            hasIndex = True
        symbol = self.create_symbol("variable", str(node.ID), str(node.Type), 12, False, False, hasIndex, True)
        lineno = node.lineno
        self.add_to_symbol_table(symbol, lineno)
        
        hasIndex = True
        if node.LRSquare is None:
            hasIndex = False
        if self.current_class == self.current_constructor and str(node.Type) == self.current_class:
            self.has_Error = True
            self.errors.append(f"Error: Since only one constructor is allowed, it is illegal to have a parameter {node.Type} {node.ID} be of the same type as the class {self.current_class}. Around line {node.lineno}")
        else:
            if self.current_constructor != "":
                self.add_Param(str(self.current_class), str(self.current_constructor), str(node.Type), hasIndex)
            else:
                self.add_Param(str(self.current_class), str(self.current_method), str(node.Type), hasIndex)

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
        if node.VariableDeclaration.Type == 'void':
            self.has_Error = True
            self.errors.append(f"Error: Parameter {node.VariableDeclaration.ID} can not be of type void. Around line {node.VariableDeclaration.lineno}")
        hasIndex = False
        isInitialized = False
        if node.VariableDeclaration.LRSquare is not None:
            hasIndex = True
        if node.VariableDeclaration.Initializer.Initializer is not None:
            isInitialized = True
        if node.VariableDeclaration.Type != 'void' and node.VariableDeclaration.Type != 'int' and node.VariableDeclaration.Type != 'char' and node.VariableDeclaration.Type != 'bool' and node.VariableDeclaration.Type != 'string':
            symbol = self.create_symbol("object", str(node.VariableDeclaration.ID), str(node.VariableDeclaration.Type), 12, False, False, hasIndex, isInitialized)
        else:
            symbol = self.create_symbol("variable", str(node.VariableDeclaration.ID), str(node.VariableDeclaration.Type), 12, False, False, hasIndex, isInitialized)

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
        pass

    def post_visit_Terminal(self, node: ASTTerminal):
        pass