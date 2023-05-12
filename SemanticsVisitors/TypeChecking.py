from abc import ABCMeta, abstractmethod
from AbstractVisitor import ASTVisitor
from SupportFiles.theLexer import theLexerTester
from AST import *

class Unique:
    def __init__(self):
        self.id = -1

    def getID(self):
        self.id += 1
        return self.id
    
class TypeChecking(ASTVisitor):
    def __init__(self):
        self.UID = Unique()
        self.paramList = []
        self.errors = []
        self.stack = []
        self.scope_stack = []
        self.symbol_tables = []
        self.current_class = ""
        self.arguments = []
        self.returnType = ""
        self.returnFound = False

    def enter_scope(self):
        new_scope = self.UID.getID()
        self.scope_stack.append(new_scope)

    def exit_scope(self):
        self.scope_stack.pop()


    def get_type(self, node):

        if isinstance(node, ASTArgument):
            pass
        
        elif isinstance(node, ASTArgumentList):
            return self.get_type(node.Expression)
 
        elif isinstance(node, ASTArgOrIdx):
            pass
                      
        elif isinstance(node, ASTCase):
            pass
                 
        elif isinstance(node, ASTCaseBlock):
            pass
                 
        elif isinstance(node, ASTClassDefinition):
            pass
                 
        elif isinstance(node, ASTClassMemberDefinition):
            pass
                 
        elif isinstance(node, ASTCompilationUnit):
            pass
                 
        elif isinstance(node, ASTConstructorDeclaration):
            pass
                 
        elif isinstance(node, ASTDataMemberDeclaration):
            pass
 
        elif isinstance(node, ASTExpressionArgIdx):
            type = self.get_type(node.Expression)
            if isinstance(node.ArgOrIdx, ASTIndex) and type[-2:]== '[]':
                return type[:-2]
            else:
                return type
                 
        elif isinstance(node, ASTExpressionDotID):
            left_side = self.get_type(node.Expression)
            if left_side == 'this':
                left_side = self.current_class
    
            for x in range(len(self.symbol_tables)):
                inClass = False
                for key, value in self.symbol_tables[x].items():
                    if (key[0] == left_side and key[1] == 'class'):
                        inClass = True
                    if inClass == True:
                        if key[0] == node.ID and (key[1] == 'constructor' or key[1] == 'method' or key[1] == 'dataMember'):
                            symbol = value['symbol']
                            return symbol.Type
            self.errors.append(f"Error: Illegal call. {left_side} has no method/dataStructure called {node.ID}. Around line {node.lineno}")

        elif isinstance(node, ASTExpressionMinus):
            return self.get_type(node.Expression)
        
        elif isinstance(node, ASTExpressionNew):
            type = node.Type
            
            if isinstance (node.ArgOrIdx.Arg_Idx, ASTIndex):
                return (str(type) + '[]')
            else:
                return str(type)
                 
        elif isinstance(node, ASTExpressionNot):
            return self.get_type(node.Expression)
                 
        elif isinstance(node, ASTExpressionPlus):
            return self.get_type(node.Expression)
                 
        elif isinstance(node, ASTExpressionPAREN):
            return self.get_type(node.Expression)
        
        elif isinstance(node, ASTExpressionEAANDE):
            left_side = self.get_type(node.Expression)
            right_side = self.get_type(node.Expression2)
            if (left_side == 'bool' or left_side == 'true' or left_side == 'false') and (right_side == 'bool' or right_side == 'true' or right_side == 'false'):
                return ("bool")

        elif isinstance(node, ASTExpressionECEqualE):
            left_side = self.get_type(node.Expression)
            right_side = self.get_type(node.Expression2)
            if ((left_side == 'bool' or left_side == 'true' or left_side == 'false') and (right_side == 'bool' or right_side == 'true' or right_side == 'false')) or (left_side == right_side):
                return ("bool")

        elif isinstance(node, ASTExpressionEDivideE):
            left_side = self.get_type(node.Expression)
            right_side = self.get_type(node.Expression2)
            if left_side == right_side and left_side == 'int':
                return('int')
            
        elif isinstance(node, ASTExpressionEDivideEqualE):
            left_side = self.get_type(node.Expression)
            right_side = self.get_type(node.Expression2)
            if left_side == right_side and left_side == 'int':
                return('int')

        elif isinstance(node, ASTExpressionEEqualE):
            left_side = self.get_type(node.Expression)
            right_side = self.get_type(node.Expression2)
            if left_side == right_side:
                return str(left_side)
            
        elif isinstance(node, ASTExpressionEGreaterE):
            left_side = self.get_type(node.Expression)
            right_side = self.get_type(node.Expression2)
            if left_side == 'int' or left_side == 'char' and (left_side == right_side):
                return ("bool")

        elif isinstance(node, ASTExpressionEGreaterEqualE):
            left_side = self.get_type(node.Expression)
            right_side = self.get_type(node.Expression2)
            if left_side == 'int' or left_side == 'char' and (left_side == right_side):
                return ("bool")

        elif isinstance(node, ASTExpressionELessE):
            left_side = self.get_type(node.Expression)
            right_side = self.get_type(node.Expression2)
            if left_side == 'int' or left_side == 'char' and (left_side == right_side):
                return ("bool")

        elif isinstance(node, ASTExpressionELessEqualE):
            left_side = self.get_type(node.Expression)
            right_side = self.get_type(node.Expression2)
            if left_side == 'int' or left_side == 'char' and (left_side == right_side):
                return ("bool")

        elif isinstance(node, ASTExpressionEMinusE):
            left_side = self.get_type(node.Expression)
            right_side = self.get_type(node.Expression2)
            if left_side == right_side and left_side == 'int':
                return('int')       
                      
        elif isinstance(node, ASTExpressionEMinusEqualE):
            left_side = self.get_type(node.Expression)
            right_side = self.get_type(node.Expression2)
            if left_side == right_side and left_side == 'int':
                return('int')                 

        elif isinstance(node, ASTExpressionENotEqualE):
            left_side = self.get_type(node.Expression)
            right_side = self.get_type(node.Expression2)
            if ((left_side == 'bool' or left_side == 'true' or left_side == 'false') and (right_side == 'bool' or right_side == 'true' or right_side == 'false')) or (left_side == right_side):
                return ("bool")

        elif isinstance(node, ASTExpressionEOORE):
            left_side = self.get_type(node.Expression)
            right_side = self.get_type(node.Expression2)
            if ((left_side == 'bool' or left_side == 'true' or left_side == 'false') and (right_side == 'bool' or right_side == 'true' or right_side == 'false')):
                return ("bool")

        elif isinstance(node, ASTExpressionEPlusE):
            left_side = self.get_type(node.Expression)
            right_side = self.get_type(node.Expression2)
            if left_side == right_side and left_side == 'int':
                return ("int")
        
        elif isinstance(node, ASTExpressionEPlusEqualE):
            left_side = self.get_type(node.Expression)
            right_side = self.get_type(node.Expression2)
            if left_side == right_side and left_side == 'int':
                return ("int")

        elif isinstance(node, ASTExpressionETimesE):
            left_side = self.get_type(node.Expression)
            right_side = self.get_type(node.Expression2)
            if left_side == right_side and left_side == 'int':
                return ("int")
        
        elif isinstance(node, ASTExpressionETimesEqualE):
            left_side = self.get_type(node.Expression)
            right_side = self.get_type(node.Expression2)
            if left_side == right_side and left_side == 'int':
                return ("int")
            
        elif isinstance(node, ASTIndex):
            idx = self.get_type(node.Expression)
            if idx == 'int':
                return ("int")
            
        elif isinstance(node, ASTInitializer):
            type = self.get_type(node.Expression)
            return type
                 
        elif isinstance(node, ASTMaybeArgumentList):
            pass
                 
        elif isinstance(node, ASTMaybeExpression):
            return self.get_type(node.Expression)
                 
        elif isinstance(node, ASTMaybeInitializer):
            if node.Initializer == None:
                return ("null")
                 
        elif isinstance(node, ASTMaybeParamList):
            pass
                 
        elif isinstance(node, ASTMethodBody):
            pass
                 
        elif isinstance(node, ASTMethodDeclaration):
            pass
                 
        elif isinstance(node, ASTMethodSuffix):
            pass
                 
        elif isinstance(node, ASTMultipleCase):
            pass
                 
        elif isinstance(node, ASTMultipleClassDefinition):
            pass
                 
        elif isinstance(node, ASTMultipleClassMemberDefinition):
            pass
                 
        elif isinstance(node, ASTMultipleCommaExpression):
            pass
                 
        elif isinstance(node, ASTMultipleCommaParameter):
            pass
                 
        elif isinstance(node, ASTMultipleStatement):
            pass
                 
        elif isinstance(node, ASTParameter):
            pass
                 
        elif isinstance(node, ASTParameterList):
            pass
                 
        elif isinstance(node, ASTStatementBreak):
            pass
                 
        elif isinstance(node, ASTStatementCIN):
            return self.get_type(node.Expression)
                 
        elif isinstance(node, ASTStatementCOUT):
            return self.get_type(node.Expression)
                 
        elif isinstance(node, ASTStatementExpression):
            return self.get_type(node.Expression)
                 
        elif isinstance(node, ASTStatementIF):
            return self.get_type(node.Expression)
                 
        elif isinstance(node, ASTStatementIFELSE):
            return self.get_type(node.Expression)
                 
        elif isinstance(node, ASTStatementMultipleStatement):
            pass
                 
        elif isinstance(node, ASTStatementToVariableDeclaration):
            pass
                 
        elif isinstance(node, ASTStatementReturn):
            return self.get_type(node.MaybeExpression)
                 
        elif isinstance(node, ASTStatementSwitch):
            return self.get_type(node.Expression)
                 
        elif isinstance(node, ASTStatementWhile):
            return self.get_type(node.Expression)
                 
        elif isinstance(node, ASTVariableDeclaration):
            type = node.Type
            if node.LRSquare != None:
                type = type + '[]'
            return str(type)
 
        elif isinstance(node, ASTTerminal):
            tokType = theLexerTester(str(node.Terminal))
            if tokType.type != 'ID' and tokType.type != 'char':
                return(str(tokType.type).lower())
            else:
                for x in reversed(self.scope_stack):
                    for key, value in self.symbol_tables[x].items():
                        if key[0] == str(node.Terminal):
                            symbol = value['symbol']
                            return(str(symbol.Type))




    def pre_visit_Argument(self, node: ASTArgument):
        pass

    def post_visit_Argument(self, node: ASTArgument):
        pass

    def pre_visit_ArgumentList(self, node: ASTArgumentList):
        type = self.get_type(node.Expression)
        self.arguments.append(type)

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
        self.current_class = str(node.ID)
    
    def post_visit_ClassDefinition(self, node: ASTClassDefinition):
        self.exit_scope()
        self.current_class = ""

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
        expressionType = self.get_type(node.Expression)
        if isinstance(node.ArgOrIdx, ASTIndex):
            if expressionType != None:
                idxType = self.get_type(node.ArgOrIdx)
                if idxType != "int":
                    self.errors.append(f"Error: attempting to access an index and the index value is not an int.")
                if len(expressionType) > 2:
                    if expressionType[-2:] != '[]':
                        self.errors.append(f"Error: attempting to get an index when variable is not an array.")
                else:
                    self.errors.append(f"Error: attempting to get an index when variable is not an array.")
         
        else:
            if isinstance(node.Expression, ASTExpressionDotID):
                theClass = self.get_type(node.Expression.Expression)
                if theClass == 'this':
                    theClass = self.current_class
                method = node.Expression.ID
                for x in self.paramList:
                    if x['className'] == theClass and x['methodName'] == method:
                        if len(self.arguments) != len(x['paramTypes']):
                            self.errors.append(f"Error: When calling a method {method}. {len(x['paramTypes'])} were expected and {len(self.arguments)} was given.")
                        else:
                            for i in range(len(x['paramTypes'])):
                                if x['paramTypes'][i] != self.arguments[i]:
                                    if (x['paramTypes'][i] == 'bool' and (self.arguments[i] == 'false' or self.arguments[i] == 'true')) or (self.arguments[i] == 'bool' and (x['paramTypes'][i] == 'true' or x['paramTypes'][i] == 'false')):
                                        pass
                                    else:
                                        self.errors.append(f"Error: attempting to call method {method}. Argument {x['paramTypes'][i]} was expected and {self.arguments[i]} was given.")
            
            elif isinstance(node.Expression, ASTTerminal):
                theClass = self.current_class
                method = node.Expression.Terminal
                for x in self.paramList:
                    if x['className'] == theClass and x['methodName'] == method:
                        if len(self.arguments) != len(x['paramTypes']):
                            self.errors.append(f"Error: When calling a method {method}. {len(x['paramTypes'])} were expected and {len(self.arguments)} was given.")
                        else:
                            for i in range(len(x['paramTypes'])):
                                if x['paramTypes'][i] != self.arguments[i]:
                                    self.errors.append(f"Error: attempting to call method {method}. Argument {x['paramTypes'][i]} was expected and {self.arguments[i]} was given.")
            
            self.arguments = []
        #find what method is being called and check argument stack with parameters

    def pre_visit_ExpressionDotID(self, node: ASTExpressionDotID):
        pass

    def post_visit_ExpressionDotID(self, node: ASTExpressionDotID):
        isValid = False
        left_side = self.get_type(node.Expression)
        if left_side == 'this':
            left_side = self.current_class
  
        for x in range(len(self.symbol_tables)):
            inClass = False
            for key, value in self.symbol_tables[x].items():
                if [key[0] == left_side and key[1] == 'class']:
                    inClass = True
                if inClass == True:
                    if key[0] == node.ID and (key[1] == 'constructor' or key[1] == 'method' or key[1] == 'dataMember'):
                        isValid = True

        if isValid == False:
            self.errors.append(f"Error: Invalid expression at line {node.lineno}. {left_side}.{node.ID} is not a valid method or dataMember")

    def pre_visit_ExpressionMinus(self, node: ASTExpressionMinus):
        pass

    def post_visit_ExpressionMinus(self, node: ASTExpressionMinus):
        right_side = self.get_type(node.Expression)
        if right_side != 'int':
            self.errors.append(f"Error: Attempting to '-' an invalid type. '{right_side}'. Need to be an 'int'. Around line {node.lineno}")

    def pre_visit_ExpressionNew(self, node: ASTExpressionNew):
        pass

    def post_visit_ExpressionNew(self, node: ASTExpressionNew):
        type = self.get_type(node)
        if type == 'int' or type == 'char' or type == 'bool' or type == 'string':
            pass
        else:
            if len(type) > 2:
                if type[-2:] == '[]':
                    pass
            
                else: 
                    #object with arguments
                    constructExists = False
                    for x in range(len(self.symbol_tables)):
                        for key, value in self.symbol_tables[x].items():
                            if key[0] == type and key[1] == 'constructor':
                                constructExists = True
                    if constructExists == False:
                        self.errors.append(f"Error: Attempting to initialize an object {type} and there is no constructor of that type. Around line {node.lineno}")

                    for x in self.paramList:
                        if x['className'] == type and x['methodName'] == type:
                            if len(self.arguments) != len(x['paramTypes']):
                                self.errors.append(f"Error: When initializing an object of type {type}. {len(x['paramTypes'])} were expected and {len(self.arguments)} was given. around line {node.lineno}")
                            else:
                                for i in range(len(x['paramTypes'])):
                                    if x['paramTypes'][i] != self.arguments[i]:
                                        self.errors.append(f"Error: attempting to initialize an object of type '{type}'. Argument {x['paramTypes'][i]} was expected and {self.arguments[i]} was given. Around line {node.lineno}")
        self.arguments = []

    def pre_visit_ExpressionNot(self, node: ASTExpressionNot):
        pass

    def post_visit_ExpressionNot(self, node: ASTExpressionNot):
        left_side = self.get_type(node.Expression)
        if left_side != 'bool':
            self.errors.append(f"Error: Attempting to '!' an invalid type. '{left_side}' Needs to be an 'bool'. Around line {node.lineno}")

    def pre_visit_ExpressionPlus(self, node: ASTExpressionPlus):
        pass

    def post_visit_ExpressionPlus(self, node: ASTExpressionPlus):
        right_side = self.get_type(node.Expression)
        if right_side != 'int':
            self.errors.append(f"Error: Attempting to '+' an invalid type. '{right_side}'. Need to be an 'int'. Around line {node.lineno}")

    def pre_visit_ExpressionPAREN(self, node: ASTExpressionPAREN):
        pass
    
    def post_visit_ExpressionPAREN(self, node: ASTExpressionPAREN):
        pass

    def pre_visit_ExpressionEAANDE(self, node: ASTExpressionEAANDE):
        pass

    def post_visit_ExpressionEAANDE(self, node: ASTExpressionEAANDE):
        left_side = self.get_type(node.Expression)
        right_side = self.get_type(node.Expression2)
        isValid = False
        if ((left_side == 'bool' or left_side == 'true' or left_side == 'bool') and (right_side == 'true' or right_side == 'false')) or ((right_side == 'bool' or right_side == 'true' or right_side == 'false') and (left_side == 'true' or left_side == 'false')):
            isValid = True
        if left_side != right_side and isValid == False:
            self.errors.append(f"Error: Attempting to '&&'' different types. {left_side} and {right_side}. Around line {node.lineno}")

    def pre_visit_ExpresssionECEqualE(self, node: ASTExpressionECEqualE):
        pass

    def post_visit_ExpresssionECEqualE(self, node: ASTExpressionECEqualE):
        left_side = self.get_type(node.Expression)
        right_side = self.get_type(node.Expression2)
        isValid = False
        if ((left_side == 'bool' or left_side == 'true' or left_side == 'false') and (right_side == 'true' or right_side == 'false')) or ((right_side == 'bool' or right_side == 'true' or right_side == 'false') and (left_side == 'true' or left_side == 'false')):
            isValid = True
        if left_side != right_side and isValid == False:
            self.errors.append(f"Error: Attempting to compare different types. {left_side} and {right_side}. Around line {node.lineno}")

    def pre_visit_ExpressionEDivideE(self, node: ASTExpressionEDivideE):
        pass

    def post_visit_ExpressionEDivideE(self, node: ASTExpressionEDivideE):
        left_side = self.get_type(node.Expression)
        right_side = self.get_type(node.Expression2)
        if left_side != right_side:
            self.errors.append(f"Error: Attempting to '/' a variable of type {left_side} with {right_side}. Around line {node.lineno}")
        else:
            if left_side != "int":
                self.errors.append(f"Error: Attempting to '/' a variable of type {left_side} Only 'int' is able to be divided. Around line {node.lineno}")

    def pre_visit_ExpressionEDivideEqualE(self, node: ASTExpressionEDivideEqualE):
        pass

    def post_visit_ExpressionEDivideEqualE(self, node: ASTExpressionEDivideEqualE):
        left_side = self.get_type(node.Expression)
        right_side = self.get_type(node.Expression2)
        if left_side != right_side:
            self.errors.append(f"Error: Attempting to '/=' a variable of type {left_side} with {right_side}. Around line {node.lineno}")
        else:
            if left_side != "int":
                self.errors.append(f"Error: Attempting to '/=' a variable of type {left_side} Only 'int' is able to be divided. Around line {node.lineno}")

    def pre_visit_ExpressionEEqualE(self, node: ASTExpressionEEqualE):
        pass

    def post_visit_ExpressionEEqualE(self, node: ASTExpressionEEqualE):
        left_side = self.get_type(node.Expression)
        right_side = self.get_type(node.Expression2)
        isValid = False
        if left_side != right_side:
            isValid = False
        else:
            isValid = True
        if len(left_side) > 2:
            if left_side[-2:] == '[]':
                if right_side == 'null':
                    isValid = True
        if right_side == 'null' and (left_side == 'int[]' or left_side == 'char[]' or left_side == 'bool[]' or left_side == 'string[]'):
            isValid = True
        else:
            if right_side == 'null' and (left_side == 'int' or left_side == 'char' or left_side == 'bool' or left_side == 'string'):
                self.errors.append(f"Error: null can only be assigned to a class or array type not {left_side}. Around line {node.lineno}")
            else:
                if right_side == 'null':
                    isValid = True
        if (left_side == 'bool' and (right_side == 'true' or right_side == 'false')) or (right_side == 'bool' and (left_side == 'true' or left_side == 'false')):
            isValid = True
        if left_side == 'true' or left_side == 'false':
            isValid = False
        if isValid == False:
            self.errors.append(f"Error: Attempting to assign different types. {left_side} and {right_side}. Around line {node.lineno}")

    def pre_visit_ExpressionEGreaterE(self, node: ASTExpressionEGreaterE):
        pass

    def post_visit_ExpressionEGreaterE(self, node: ASTExpressionEGreaterE):
        left_side = self.get_type(node.Expression)
        right_side = self.get_type(node.Expression2)
        if left_side != right_side:
            self.errors.append(f"Error: Attempting to compare different types. {left_side} and {right_side}. Around line {node.lineno}")
        if left_side != 'int' and left_side != 'char':
            self.errors.append(f"Error: Attempting to compare an invalid type. '{left_side}' Needs to be an 'int' or 'char'. Around line {node.lineno}")

    def pre_visit_ExpressionEGreaterEqualE(self, node: ASTExpressionEGreaterEqualE):
        pass

    def post_visit_ExpressionEGreaterEqualE(self, node: ASTExpressionEGreaterEqualE):
        left_side = self.get_type(node.Expression)
        right_side = self.get_type(node.Expression2)
        if left_side != right_side:
            self.errors.append(f"Error: Attempting to compare different types. {left_side} and {right_side}. Around line {node.lineno}")
        if left_side != 'int' and left_side != 'char':
            self.errors.append(f"Error: Attempting to compare an invalid type. '{left_side}' Needs to be an 'int' or 'char'. Around line {node.lineno}")

    def pre_visit_ExpressionELessE(self, node: ASTExpressionELessE):
        pass

    def post_visit_ExpressionELessE(self, node: ASTExpressionELessE):
        left_side = self.get_type(node.Expression)
        right_side = self.get_type(node.Expression2)
        if left_side != right_side:
            self.errors.append(f"Error: Attempting to compare different types. {left_side} and {right_side}. Around line {node.lineno}")
        if left_side != 'int' and left_side != 'char':
            self.errors.append(f"Error: Attempting to compare an invalid type. '{left_side}' Needs to be an 'int' or 'char'. Around line {node.lineno}")

    def pre_visit_ExpressionELessEqualE(self, node: ASTExpressionELessEqualE):
        pass

    def post_visit_ExpressionELessEqualE(self, node: ASTExpressionELessEqualE):
        left_side = self.get_type(node.Expression)
        right_side = self.get_type(node.Expression2)
        if left_side != right_side:
            self.errors.append(f"Error: Attempting to compare different types. {left_side} and {right_side}. Around line {node.lineno}")
        if left_side != 'int' and left_side != 'char':
            self.errors.append(f"Error: Attempting to compare an invalid type. '{left_side}' Needs to be an 'int' or 'char'. Around line {node.lineno}")

    def pre_visit_ExpressionEMinusE(self, node: ASTExpressionEMinusE):
        pass

    def post_visit_ExpressionEMinusE(self, node: ASTExpressionEMinusE):
        left_side = self.get_type(node.Expression)
        right_side = self.get_type(node.Expression2)
        if left_side != right_side:
            self.errors.append(f"Error: Attempting to '-' a variable of type {left_side} with {right_side}. Around line {node.lineno}")
        else:
            if left_side != "int":
                self.errors.append(f"Error: Attempting to '-' a variable of type {left_side} Only 'int' is able to be subtracted. Around line {node.lineno}")

    def pre_visit_ExpressionEMinusEqualE(self, node: ASTExpressionEMinusEqualE):
        pass

    def post_visit_ExpressionEMinusEqualE(self, node: ASTExpressionEMinusEqualE):
        left_side = self.get_type(node.Expression)
        right_side = self.get_type(node.Expression2)
        if left_side != right_side:
            self.errors.append(f"Error: Attempting to '-=' a variable of type {left_side} with {right_side}. Around line {node.lineno}")
        else:
            if left_side != "int":
                self.errors.append(f"Error: Attempting to '-=' a variable of type {left_side} Only 'int' is able to be subtracted. Around line {node.lineno}")

    def pre_visit_ExpressionENotEqualE(self, node: ASTExpressionENotEqualE):
        pass

    def post_visit_ExpressionENotEqualE(self, node: ASTExpressionENotEqualE):
        left_side = self.get_type(node.Expression)
        right_side = self.get_type(node.Expression2) 
        isValid = False
        if (left_side == 'bool' or left_side == 'true' or left_side=='false' and (right_side == 'true' or right_side == 'false')) or (right_side == 'bool' and (left_side == 'true' or left_side == 'false')):
            isValid = True
        if left_side != right_side and isValid == False:
            self.errors.append(f"Error: Attempting to compare different types. {left_side} and {right_side}. Around line {node.lineno}")

    def pre_visit_ExpressionEOORE(self, node: ASTExpressionEOORE):
        pass

    def post_visit_ExpressionEOORE(self, node: ASTExpressionEOORE):
        left_side = self.get_type(node.Expression)
        right_side = self.get_type(node.Expression2)
        isValid = False
        if (left_side == 'bool' and (right_side == 'true' or right_side == 'false')) or (right_side == 'bool' and (left_side == 'true' or left_side == 'false')):
            isValid = True
        if left_side != right_side and isValid == False:
            self.errors.append(f"Error: Attempting to '||' different types. {left_side} and {right_side}. Around line {node.lineno}")

    def pre_visit_ExpressionEPlusE(self, node: ASTExpressionEPlusE):
        pass
    
    def post_visit_ExpressionEPlusE(self, node: ASTExpressionEPlusE):
        left_side = self.get_type(node.Expression)
        right_side = self.get_type(node.Expression2)
        if left_side != right_side:
            self.errors.append(f"Error: Attempting to '+' a variable of type {left_side} with {right_side}. Around line {node.lineno}")
        else:
            if left_side != "int":
                self.errors.append(f"Error: Attempting to '+' a variable of type {left_side} Only 'int' is able to be added. Around line {node.lineno}")

    def pre_visit_ExpressionEPlusEqualE(self, node: ASTExpressionEPlusEqualE):
        pass

    def post_visit_ExpressionEPlusEqualE(self, node: ASTExpressionEPlusEqualE):
        left_side = self.get_type(node.Expression)
        right_side = self.get_type(node.Expression2)
        if left_side != right_side:
            self.errors.append(f"Error: Attempting to '+=' a variable of type {left_side} with {right_side}. Around line {node.lineno}")
        else:
            if left_side != "int":
                self.errors.append(f"Error: Attempting to '+=' a variable of type {left_side} Only 'int' is able to be added. Around line {node.lineno}")

    def pre_visit_ExpressionETimesE(self, node: ASTExpressionETimesE):
        pass

    def post_visit_ExpressionETimesE(self, node: ASTExpressionETimesE):
        left_side = self.get_type(node.Expression)
        right_side = self.get_type(node.Expression2)
        if left_side != right_side:
            self.errors.append(f"Error: Attempting to '*' a variable of type {left_side} with {right_side}. Around line {node.lineno}")
        else:
            if left_side != "int":
                self.errors.append(f"Error: Attempting to '*' a variable of type {left_side} Only 'int' is able to be multiplied. Around line {node.lineno}")

    def pre_visit_ExpressionETimesEqualE(self, node: ASTExpressionETimesEqualE):
        pass

    def post_visit_ExpressionETimesEqualE(self, node: ASTExpressionETimesEqualE):
        left_side = self.get_type(node.Expression)
        right_side = self.get_type(node.Expression2)
        if left_side != right_side:
            self.errors.append(f"Error: Attempting to '*=' a variable of type {left_side} with {right_side}. Around line {node.lineno}")
        else:
            if left_side != "int":
                self.errors.append(f"Error: Attempting to '*=' a variable of type {left_side} Only 'int' is able to be multiplied. Around line {node.lineno}")

    def pre_visit_Index(self, node: ASTIndex):
        pass

    def post_visit_Index(self, node: ASTIndex):
        idx = self.get_type(node.Expression)
        if idx != 'int':
            self.errors.append(f"Error: attempting to access index and 'int' was not given. {idx} was given. Around line {node.lineno}")
    
    def pre_visit_Initializer(self, node: ASTInitializer):
        pass

    def post_visit_Initializer(self, node: ASTInitializer):
        pass

    def pre_visit_MaybeArgumentList(self, node: ASTMaybeArgumentList):
        self.arguments.append(None)
            
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
        self.enter_scope()
        self.returnType = node.Type
        if node.LRSquare != None:
            self.returnType = str(node.Type) + '[]'

    def post_visit_MethodDeclaration(self, node: ASTMethodDeclaration):
        self.exit_scope()
        if self.returnType == 'void':
            pass
        else:
            if self.returnFound == False:
                self.errors.append(f"Error: Method doesn't have any return statements. Only 'void' can have no return statement")
        self.returnType = ""

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
        if node.Expression != None:
            type = self.get_type(node.Expression)
            self.arguments.append(type)

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
        messageType = self.get_type(node.Expression)
        if messageType  != "int" and messageType !='char':
            self.errors.append(f"Error: Can not CIN {messageType}. Around line {node.lineno}")

    def pre_visit_StatementCOUT(self, node: ASTStatementCOUT):
        pass

    def post_visit_StatementCOUT(self, node: ASTStatementCOUT):
        messageType = self.get_type(node.Expression)
        if messageType  != "int" and messageType !='char' and messageType != 'string':
            self.errors.append(f"Error: Can not COUT {messageType}. Around line {node.lineno}")

    def pre_visit_StatementExpression(self, node: ASTStatementExpression):
        pass

    def post_visit_StatementExpression(self, node: ASTStatementExpression):
        pass

    def pre_visit_StatementIF(self, node: ASTStatementIF):
        pass

    def post_visit_StatementIF(self, node: ASTStatementIF):
        ifType = self.get_type(node.Expression)
        if ifType != 'bool'  and ifType != 'true' and ifType != 'false':
            self.errors.append(f"Error: A bool is required after an if statement. {ifType} was given. Around line {node.lineno}")

    def pre_visit_StatementIFELSE(self, node: ASTStatementIFELSE):
        pass

    def post_visit_StatementIFELSE(self, node: ASTStatementIFELSE):
        ifType = self.get_type(node.Expression)
        if ifType != 'bool'  and ifType != 'true' and ifType != 'false':
            self.errors.append(f"Error: A bool is required after an if statement. {ifType} was given. Around line {node.lineno}")

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
        self.returnFound = True
        type = self.get_type(node.MaybeExpression)
        if type == None and self.returnType == 'void':
            pass
        elif type == self.returnType or (self.returnType == 'bool' and (type == 'true' or type == 'false')):
            pass
        else:
            self.errors.append(f"Error: return type {type} doesn't match method return type {self.returnType}. Around line {node.lineno}")

    def pre_visit_StatementSwitch(self, node: ASTStatementSwitch):
        pass

    def post_visit_StatementSwitch(self, node: ASTStatementSwitch):
        type = self.get_type(node.Expression)
        if type != 'int' and type != 'char':
            self.errors.append(f"Error: Switch statement must be a 'char' or an 'int'. {type} was given. ")

    def pre_visit_StatementWhile(self, node: ASTStatementWhile):
        pass

    def post_visit_StatementWhile(self, node: ASTStatementWhile):
        ifType = self.get_type(node.Expression)
        if ifType != 'bool':
            self.errors.append(f"Error: A bool is required after a while statement. {ifType} was given. Around line {node.lineno}")

    def pre_visit_VariableDeclaration(self, node: ASTVariableDeclaration):
        pass

    def post_visit_VariableDeclaration(self, node: ASTVariableDeclaration):
        type = node.Type
        if node.LRSquare != None:
            type = type + '[]'
        
        if node.Initializer.Initializer != None:
            done = False
            initalType = self.get_type(node.Initializer.Initializer)
            if node.LRSquare != None:
                if initalType == 'null':
                    done = True

            if initalType == 'null' and (type == 'int[]' or type == 'char[]' or type == 'bool[]' or type == 'string[]'):
                done= True
            else:
                if initalType == 'null' and (type == 'int' or type == 'char' or type == 'bool' or type == 'string'):
                    self.errors.append(f"Error: null can only be assigned to a class or array type not {type}. Around line {node.lineno}")
                else:
                    if initalType == 'null':
                        done = True

            if type == 'bool' and (initalType == 'false' or initalType == 'true'):
                done = True
            elif type == initalType:
                done = True
            if done == False:
                self.errors.append(f"Error: attempting to initalize a variable of type {type} and is getting set to {initalType}. Around line {node.lineno}")

    def pre_visit_Terminal(self, node: ASTTerminal):
        pass

    def post_visit_Terminal(self, node: ASTTerminal):
        pass