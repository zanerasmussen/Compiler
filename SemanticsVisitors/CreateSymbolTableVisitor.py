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
    def __init__(self, whatAmI: str, name: str, type, offset: int, isPrivate: bool, isInitialized: bool):
        self.whatAmI = whatAmI
        self.Name = name
        self.Type = type
        self.Offset = offset
        self.isPrivate = isPrivate
        self.isInitialized = isInitialized

class SymbolTableVisitor(ASTVisitor):
    def __init__(self):
        self.UID = Unique()
        self.symbol_tables = []
        self.scope_stack = []
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

    def create_symbol(self, whatAmI: str, name: str, type: str, offset: int, isPrivate: bool, isInitialized: bool) -> Symbol:
        return Symbol(whatAmI = whatAmI, name=name, type=type, offset=offset, isPrivate=isPrivate, isInitialized=isInitialized)

    def add_to_symbol_table(self, symbol: Symbol, lineno: int):
        current_scope = self.scope_stack[-1]
        name = symbol.Name
        whatAmI = symbol.whatAmI
        
        if whatAmI == 'constructor':
            if(name,'class') in self.symbol_tables[current_scope]:
                pass
            else:
                self.errors.append(f"Error: Constructor {name} is being called in a class with a different name. Names must be the same for a constructor. Around line {lineno}")

        if whatAmI == 'object':
            if(name,'variable') in self.symbol_tables[current_scope]:
                self.errors.append(f"Error: {name} is already defined as an object. Around line {lineno}")

        #Data Members and Methods can not be the same name
        if whatAmI == 'dataMember':
            if(name,'method') in self.symbol_tables[current_scope]:
                self.errors.append(f"Error: symbol {name} already defined as a method. Around line {lineno}")
            if(name,'class') in self.symbol_tables[current_scope]:
                self.errors.append(f"Error: dataMember {name} is defined in class with the same name. Around line {lineno}")

        elif whatAmI == 'variable':
            if(name,'object') in self.symbol_tables[current_scope]:
                self.errors.append(f"Error: {name} is already defined as a variable. Around line {lineno}")


        elif whatAmI == 'method':
            if(name,'dataMember') in self.symbol_tables[current_scope]:
                self.errors.append(f"Error: symbol {name} already defined as a dataMember. Around line {lineno}")
            if(name,'class') in self.symbol_tables[current_scope]:
                self.errors.append(f"Error: method {name} is defined in class with the same name. Around line {lineno}")

        elif whatAmI == 'class':
            for i in range(len(self.symbol_tables)-2, -1, -1):
                if (name, 'class') in self.symbol_tables[i]:
                    self.errors.append(f"Error: class {name} is already as a class. Around line {lineno}")

        if (name, whatAmI) in self.symbol_tables[current_scope]:
            #can have more than one constructor but must have the same name as the class defining it. 
            if whatAmI == 'constructor':
                self.errors.append(f"Error: Only one constructor is allowed. {name} is duplicated. Around line {lineno}")
            else:
                self.errors.append(f"Error: symbol {name} already defined. Around line {lineno}")
        

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

    def add_Param(self, class_name: str, method_name: str, param_type: str):
        method_found = False
        for param in self.paramList:
            if param['className'] == class_name and param['methodName'] == method_name:
                method_found = True
                param['numberOfParams'] += 1
                if param_type:
                    param['paramTypes'].append((param_type))
                else:
                    param['paramTypes'].append(())
                break
        if not method_found:
            new_method = {'className': class_name, 'methodName': method_name,
                        'numberOfParams': 1, 'paramTypes': [(param_type)]}
            self.paramList.append(new_method)

    def checkParamTypes(self):
        for x in range(len(self.paramList)):
            for i in range(len(self.paramList[x]['paramTypes'])):      
                typeExists = False
                type = self.paramList[x]['paramTypes'][i]
                if type!= "void" and type != None and type != "int" and type != "int[]" and type != "char" and type != "char[]" and type != "string" and type != "string[]" and type != "bool" and type != "bool[]":
                    for symbol_table in self.symbol_tables:
                        for key in symbol_table.keys():
                            if key[0] == type and key[1] == 'class':
                                typeExists = True
                            if str(key[0])+"[]" == type and key[1] == 'class':
                                typeExists = True
                else:
                    typeExists = True
                if typeExists == False:
                    self.errors.append(f"Error: {type} is not a valid class or type for KXI. Param checking")
                           

    def checkSymbolTableTypes(self):
        for s in self.symbol_tables:
            for k, v in s.items():
                typeExists = False
                type = v['symbol'].Type
                if k[1] == "class" or k[1] == "constructor":
                    typeExists = True
                elif type!= "void" and type != None and type != "int" and type != "int[]" and type != "char" and type != "char[]" and type != "string" and type != "string[]" and type != "bool" and type != "bool[]":
                    for symbol_table in self.symbol_tables:
                        for key in symbol_table.keys():
                            if key[0] == type and key[1] == 'class':
                                typeExists = True
                            if str(key[0])+"[]" == type and key[1] == 'class':
                                typeExists = True
                else:
                    typeExists = True
                if typeExists == False:
                    self.errors.append(f"Error: {type} is not a valid class or type for KXI. Symbol checking")


    def pre_visit_Case(self, node: ASTCase):
        type = theLexerTester(str(node.NumOrChar))
        if not (type.type == 'INT' or type.type == 'CHAR'):
            self.errors.append(f"Error: case can only be followed by an int or char. You gave case {type.value} {type.type}. Around line {node.lineno}")
            
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
        self.checkParamTypes()
        self.checkSymbolTableTypes()

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
        if node.VariableDeclaration.Type == "void":
            self.errors.append(f"Error: DataMember can not have the type VOID. Near Class {self.current_class}")
        if node.Modifier == 'PRIVATE':
            isPrivate = True
        if node.VariableDeclaration.LRSquare is not None:
            type = str(node.VariableDeclaration.Type) + "[]"
        if node.VariableDeclaration.Initializer.Initializer is not None:
            isInitialized = True
        symbol = self.create_symbol(str("dataMember"), str(node.VariableDeclaration.ID), type, 12, isPrivate, isInitialized)
        lineno = node.VariableDeclaration.lineno
        self.add_to_symbol_table(symbol, lineno)

    def pre_visit_MaybeParamList(self, node: ASTMaybeParamList):
        if (self.current_class != "" and self.current_constructor!= ""):
            self.add_Param(str(self.current_class), str(self.current_constructor), None)
        if (self.current_class != "" and self.current_method!= ""):
            self.add_Param(str(self.current_class), str(self.current_method), None)

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
        if node.Type == 'void':
            self.errors.append(f"Error: Parameter {node.ID} can not be of type void. Around line {node.lineno}")

        type = str(node.Type)
        if node.LRSquare is not None:
            type = str(node.Type) + "[]"
        symbol = self.create_symbol("variable", str(node.ID), type, 12, False, True)
        lineno = node.lineno
        self.add_to_symbol_table(symbol, lineno)
        
        hasIndex = True
        if node.LRSquare is None:
            hasIndex = False
        if self.current_class == self.current_constructor and str(node.Type) == self.current_class:
            self.errors.append(f"Error: Since only one constructor is allowed, it is illegal to have a parameter {node.Type} {node.ID} be of the same type as the class {self.current_class}. Around line {node.lineno}")
        else:
            if self.current_constructor != "":
                self.add_Param(str(self.current_class), str(self.current_constructor), type)
            else:
                self.add_Param(str(self.current_class), str(self.current_method), type)

    def pre_visit_StatementToVariableDeclaration(self, node: ASTStatementToVariableDeclaration):
        if node.VariableDeclaration.Type == 'void':
            self.errors.append(f"Error: Parameter {node.VariableDeclaration.ID} can not be of type void. Around line {node.VariableDeclaration.lineno}")
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