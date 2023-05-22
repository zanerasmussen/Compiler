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
    
class AssignmentVisitor(ASTVisitor):
    def __init__(self):
        self.UID = Unique()
        self.paramList = []
        self.errors = []
        self.stack = []
        self.scope_stack = []
        self.symbol_tables = []
        self.current_class = ""
        self.isMethod = False

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
            # if left_side[0] == 'this':
            #     left_side[0] = self.current_class
    
            for x in range(len(self.symbol_tables)):
                inClass = False
                for key, value in self.symbol_tables[x].items():
                    if left_side[0] == 'this':
                        if (key[0] == self.current_class and key[1] == 'class'):
                            inClass = True
                    else:
                        if (key[0] == left_side[0] and key[1] == 'class'):
                            inClass = True
                    if inClass == True:
                        if key[0] == node.ID and (key[1] == 'constructor' or key[1] == 'method' or key[1] == 'dataMember'):
                            if key[1] == 'method':
                                self.isMethod = True
                            else:
                                self.isMethod = False
                            symbol = value['symbol']
                            return (symbol.Type,'true')

        elif isinstance(node, ASTExpressionMinus):
            return self.get_type(node.Expression)
        
        elif isinstance(node, ASTExpressionNew):
            type = node.Type
            if isinstance (node.ArgOrIdx.Arg_Idx, ASTIndex):
                return (str(type) + '[]', "true")
            else:
                return (str(type), "true")
                 
        elif isinstance(node, ASTExpressionNot):
            return self.get_type(node.Expression)
                 
        elif isinstance(node, ASTExpressionPlus):
            return self.get_type(node.Expression)
                 
        elif isinstance(node, ASTExpressionPAREN):
            return self.get_type(node.Expression)
        
        elif isinstance(node, ASTExpressionEAANDE):
            left_side = self.get_type(node.Expression)
            left_side_init = left_side[1]
            right_side = self.get_type(node.Expression2)
            right_side_init = right_side[1]
            if left_side_init != "false" and right_side_init != "false":
                return ("bool", "true")
            else:
                self.errors.append(f"Error: Attemping to use {left_side[0]} and {right_side[0]}. May not be initialized or 'terminal'. Around line {node.lineno}")
                return ("bool", "true")

        elif isinstance(node, ASTExpressionECEqualE):
            left_side = self.get_type(node.Expression)
            left_side_init = left_side[1]
            right_side = self.get_type(node.Expression2)
            right_side_init = right_side[1]
            if left_side_init != "false" and right_side_init != "false":
                return ("bool", "true")
            else:
                self.errors.append(f"Error: Attemping to '==' two objects that haven't been initialized. Around line {node.lineno}")
                return("bool", "true")

        elif isinstance(node, ASTExpressionEDivideE):
            left_side = self.get_type(node.Expression)
            left_side_init = left_side[1]
            right_side = self.get_type(node.Expression2)
            right_side_init = right_side[1]
            if left_side_init != "false" and right_side_init != "false":
                return ("int", "true")
            else:
                self.errors.append(f"Error: Attemping to use {left_side[0]} and {right_side[0]}. May not be initialized or 'terminal'. Around line {node.lineno}")
                return ("int", "true")
                
        elif isinstance(node, ASTExpressionEDivideEqualE):
            left_side = self.get_type(node.Expression)
            left_side_init = left_side[1]
            right_side = self.get_type(node.Expression2)
            right_side_init = right_side[1]
            if left_side_init != "terminal" and right_side_init != "false":
                return ("int", "true")
            else:
                self.errors.append(f"Error: Attemping to use {left_side[0]} and {right_side[0]}. May not be initialized or 'terminal'. Around line {node.lineno}")
                return ("int", "true")
             
        elif isinstance(node, ASTExpressionEEqualE):
            left_side = self.get_type(node.Expression)
            left_side_init = left_side[1]
            right_side = self.get_type(node.Expression2)
            right_side_init = right_side[1]
            if left_side_init != "terminal" and right_side_init != "false":
                return (str(left_side[0]), "true")
            else:
                self.errors.append(f"Error: Attemping to use {left_side[0]} and {right_side[0]}. May not be initialized or 'terminal'. Around line {node.lineno}")
                return (str(left_side[0]), "true")
   
        elif isinstance(node, ASTExpressionEGreaterE):
            left_side = self.get_type(node.Expression)
            left_side_init = left_side[1]
            right_side = self.get_type(node.Expression2)
            right_side_init = right_side[1]
            if right_side_init != "false" and left_side_init != "false":
                return ("bool", "true")
            else:
                self.errors.append(f"Error: Attemping to use {left_side[0]} and {right_side[0]}. May not be initialized or 'terminal'. Around line {node.lineno}")
                return ("bool", "true")

        elif isinstance(node, ASTExpressionEGreaterEqualE):
            left_side = self.get_type(node.Expression)
            left_side_init = left_side[1]
            right_side = self.get_type(node.Expression2)
            right_side_init = right_side[1]
            if right_side_init != "false" and left_side_init != "false":
                return ("bool", "true")
            else:
                self.errors.append(f"Error: Attemping to use {left_side[0]} and {right_side[0]}. May not be initialized or 'terminal'. Around line {node.lineno}")
                return ("bool", "true")

        elif isinstance(node, ASTExpressionELessE):
            left_side = self.get_type(node.Expression)
            left_side_init = left_side[1]
            right_side = self.get_type(node.Expression2)
            right_side_init = right_side[1]
            if right_side_init != "false" and left_side_init != "false":
                return ("bool", "true")
            else:
                self.errors.append(f"Error: Attemping to use {left_side[0]} and {right_side[0]}. May not be initialized or 'terminal'. Around line {node.lineno}")
                return ("bool", "true")

        elif isinstance(node, ASTExpressionELessEqualE):
            left_side = self.get_type(node.Expression)
            left_side_init = left_side[1]
            right_side = self.get_type(node.Expression2)
            right_side_init = right_side[1]
            if right_side_init != "false" and left_side_init != "false":
                return ("bool", "true")
            else:
                self.errors.append(f"Error: Attemping to use {left_side[0]} and {right_side[0]}. May not be initialized or 'terminal'. Around line {node.lineno}")
                return ("bool", "true")

        elif isinstance(node, ASTExpressionEMinusE):
            left_side = self.get_type(node.Expression)
            left_side_init = left_side[1]
            right_side = self.get_type(node.Expression2)
            right_side_init = right_side[1]
            if left_side_init != "false" and right_side_init != "false":
                return ("int", "true")
            else:
                self.errors.append(f"Error: Attemping to use {left_side[0]} and {right_side[0]}. May not be initialized or 'terminal'. Around line {node.lineno}") 
                return ("int", "true")  
                      
        elif isinstance(node, ASTExpressionEMinusEqualE):
            left_side = self.get_type(node.Expression)
            left_side_init = left_side[1]
            right_side = self.get_type(node.Expression2)
            right_side_init = right_side[1]
            if left_side_init != "terminal" and right_side_init != "false":
                return ("int", "true")
            else:
                self.errors.append(f"Error: Attemping to use {left_side[0]} and {right_side[0]}. May not be initialized or 'terminal'. Around line {node.lineno}")
                return ("int", "true")
             
        elif isinstance(node, ASTExpressionENotEqualE):
            left_side = self.get_type(node.Expression)
            left_side_init = left_side[1]
            right_side = self.get_type(node.Expression2)
            right_side_init = right_side[1]
            if right_side_init != "false" and left_side_init != "false":
                return ("bool", "true")
            else:
                self.errors.append(f"Error: Attemping to use {left_side[0]} and {right_side[0]}. May not be initialized or 'terminal'. Around line {node.lineno}")
                return ("bool", "true")

        elif isinstance(node, ASTExpressionEOORE):
            left_side = self.get_type(node.Expression)
            left_side_init = left_side[1]
            right_side = self.get_type(node.Expression2)
            right_side_init = right_side[1]
            if left_side_init != "false" and right_side_init != "false":
                return ("bool", "true")
            else:
                self.errors.append(f"Error: Attemping to use {left_side[0]} and {right_side[0]}. May not be initialized or 'terminal'. Around line {node.lineno}")
                return ("bool", "true")

        elif isinstance(node, ASTExpressionEPlusE):
            left_side = self.get_type(node.Expression)
            left_side_init = left_side[1]
            right_side = self.get_type(node.Expression2)
            right_side_init = right_side[1]
            if left_side_init != "false" and right_side_init != "false":
                return ("int", "true")
            else:
                self.errors.append(f"Error: Attemping to use {left_side[0]} and {right_side[0]}. May not be initialized or 'terminal'. Around line {node.lineno}")
                return ("int", "true")
                
        elif isinstance(node, ASTExpressionEPlusEqualE):
            left_side = self.get_type(node.Expression)
            left_side_init = left_side[1]
            right_side = self.get_type(node.Expression2)
            right_side_init = right_side[1]
            if left_side_init != "terminal" and right_side_init != "false":
                return ("int", "true")
            else:
                self.errors.append(f"Error: Attemping to use {left_side[0]} and {right_side[0]}. May not be initialized or 'terminal'. Around line {node.lineno}")
                return ("int", "true")
            
        elif isinstance(node, ASTExpressionETimesE):
            left_side = self.get_type(node.Expression)
            left_side_init = left_side[1]
            right_side = self.get_type(node.Expression2)
            right_side_init = right_side[1]
            if left_side_init != "false" and right_side_init != "false":
                return ("int", "true")
            else:
                self.errors.append(f"Error: Attemping to use {left_side[0] } and {right_side[0]}. May not be initialized or 'terminal'. Around line {node.lineno}")
                return ("int", "true")
            
        elif isinstance(node, ASTExpressionETimesEqualE):
            left_side = self.get_type(node.Expression)
            left_side_init = left_side[1]
            right_side = self.get_type(node.Expression2)
            right_side_init = right_side[1]
            if left_side_init != "terminal" and right_side_init != "false":
                return ("int", "true")
            else:
                self.errors.append(f"Error: Attemping to use {left_side[0] } and {right_side[0]}. May not be initialized or 'terminal'. Around line {node.lineno}")
                return ("int", "true")
            
        elif isinstance(node, ASTIndex):
            idx = self.get_type(node.Expression)
            idx_init = idx[1]
            if idx_init != 'false':
                return ("int", "true")
            else:
                self.errors.append(f"Error: Attemping to use an index {idx[0]} that is not initialied. Around line {node.lineno}")
                return ("int", "true")
            
        elif isinstance(node, ASTInitializer):
            return self.get_type(node.Expression)
                 
        elif isinstance(node, ASTMaybeArgumentList):
            pass
                 
        elif isinstance(node, ASTMaybeExpression):
            return self.get_type(node.Expression)
                 
        elif isinstance(node, ASTMaybeInitializer):
            if node.Initializer == None:
                return ("null", "false")
                 
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
            pass
                 
        elif isinstance(node, ASTStatementSwitch):
            return self.get_type(node.Expression)
                 
        elif isinstance(node, ASTStatementWhile):
            return self.get_type(node.Expression)
                 
        elif isinstance(node, ASTVariableDeclaration):
            type = node.Type
            if node.LRSquare != None:
                type = type + '[]'
            if node.Initializer.Initializer == None:
                return (str(type), "false")
            return (str(type), "true")
        
        elif isinstance(node, ASTTerminal):
            tokType = theLexerTester(str(node.Terminal))
            if tokType.type != 'ID':
                return(str(tokType.type).lower(), "terminal")
            else:
                for x in reversed(self.scope_stack):
                    for key, value in self.symbol_tables[x].items():
                        if key[0] == str(node.Terminal):
                            symbol = value['symbol']
                            return(str(symbol.Type), str(symbol.isInitialized).lower())

        else:
            self.errors.append("didn't find expression")

    def set_true(self, node):

        if isinstance(node, ASTArgument):
            pass
        
        elif isinstance(node, ASTArgumentList):
            pass
 
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
            pass
                 
        elif isinstance(node, ASTExpressionDotID):
            left_side = self.get_type(node.Expression)
            if left_side[0] == 'this':
                left_side[0] = self.current_class
    
            for x in range(len(self.symbol_tables)):
                inClass = False
                for key, value in self.symbol_tables[x].items():
                    if (key[0] == left_side[0] and key[1] == 'class'):
                        inClass = True
                    if inClass == True:
                        if key[0] == node.ID and (key[1] == 'constructor' or key[1] == 'method' or key[1] == 'dataMember'):
                            symbol = value['symbol']
                            return (symbol.Type,'true')

        elif isinstance(node, ASTExpressionMinus):
            pass
        
        elif isinstance(node, ASTExpressionNew):
            pass
                 
        elif isinstance(node, ASTExpressionNot):
            pass
                 
        elif isinstance(node, ASTExpressionPlus):
            pass
                 
        elif isinstance(node, ASTExpressionPAREN):
            pass
        
        elif isinstance(node, ASTExpressionEAANDE):
            pass

        elif isinstance(node, ASTExpressionECEqualE):
            pass

        elif isinstance(node, ASTExpressionEDivideE):
            pass

        elif isinstance(node, ASTExpressionEDivideEqualE):
            pass

        elif isinstance(node, ASTExpressionEEqualE):
            pass

        elif isinstance(node, ASTExpressionEGreaterE):
            pass

        elif isinstance(node, ASTExpressionEGreaterEqualE):
            pass

        elif isinstance(node, ASTExpressionELessE):
            pass

        elif isinstance(node, ASTExpressionELessEqualE):
            pass

        elif isinstance(node, ASTExpressionEMinusE):
            pass

        elif isinstance(node, ASTExpressionEMinusEqualE):
            pass

        elif isinstance(node, ASTExpressionENotEqualE):
            pass

        elif isinstance(node, ASTExpressionEOORE):
            pass

        elif isinstance(node, ASTExpressionEPlusE):
            pass

        elif isinstance(node, ASTExpressionEPlusEqualE):
            pass

        elif isinstance(node, ASTExpressionETimesE):
            pass

        elif isinstance(node, ASTExpressionETimesEqualE):
            pass

        elif isinstance(node, ASTIndex):
            pass

        elif isinstance(node, ASTInitializer):
            pass
                 
        elif isinstance(node, ASTMaybeArgumentList):
            pass
                 
        elif isinstance(node, ASTMaybeExpression):
            pass
                 
        elif isinstance(node, ASTMaybeInitializer):
            pass

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
            pass
                 
        elif isinstance(node, ASTStatementCOUT):
            pass

        elif isinstance(node, ASTStatementExpression):
            pass
                 
        elif isinstance(node, ASTStatementIF):
            pass

        elif isinstance(node, ASTStatementIFELSE):
            pass
                 
        elif isinstance(node, ASTStatementMultipleStatement):
            pass
                 
        elif isinstance(node, ASTStatementToVariableDeclaration):
            pass
                 
        elif isinstance(node, ASTStatementReturn):
            pass
                 
        elif isinstance(node, ASTStatementSwitch):
            pass
                 
        elif isinstance(node, ASTStatementWhile):
            pass
                 
        elif isinstance(node, ASTVariableDeclaration):
            pass
        
        elif isinstance(node, ASTTerminal):
            tokType = theLexerTester(str(node.Terminal))
            if tokType.type != 'ID':
                pass
            else:
                for x in reversed(self.scope_stack):
                    for key, value in self.symbol_tables[x].items():
                        if key[0] == str(node.Terminal):
                            symbol = value['symbol']
                            symbol.isInitialized = True

        else:
            self.errors.append("didn't find expression")


    def pre_visit_ClassDefinition(self, node: ASTClassDefinition):
        self.enter_scope()
        self.current_class = str(node.ID)
    
    def post_visit_ClassDefinition(self, node: ASTClassDefinition):
        self.exit_scope()
        self.current_class = ""

    def pre_visit_CompilationUnit(self, node: ASTCompilationUnit):
        self.enter_scope()

    def post_visit_CompilationUnit(self, node: ASTCompilationUnit):
        self.exit_scope()

    def post_visit_ExpressionArgIdx(self, node: ASTExpressionArgIdx):
        expressionType = self.get_type(node.Expression)
        if expressionType != None:
            if expressionType[1] != "true":
                self.errors.append(f"Error: attemping to call on an expression that hasn't been initialized.")

    def post_visit_ExpressionDotID(self, node: ASTExpressionDotID):
        left_side = self.get_type(node.Expression)
        isValid = True
        if left_side[1] != "true":
            isValid = False
        if left_side[0] == 'this':
            isValid = True
        if isValid == False:
            self.errors.append(f"Error: Attempting to use an object {left_side[0]} that hasn't been initialized. Around line {node.lineno}")

    def post_visit_ExpressionMinus(self, node: ASTExpressionMinus):
        right_side = self.get_type(node.Expression)
        if right_side[1] == "false":
            self.errors.append(f"Error: Attemping to uniary '-' and it hasn't been initialized. Around line {node.lineno}")

    def post_visit_ExpressionNot(self, node: ASTExpressionNot):
        right_side = self.get_type(node.Expression)
        if right_side[1] == 'false':
            self.errors.append(f"Error: Attemping to '!' that hasn't been initialized. Around line {node.lineno}")

    def post_visit_ExpressionPlus(self, node: ASTExpressionPlus):
        right_side = self.get_type(node.Expression)
        if right_side[1] == 'false':
            self.errors.append(f"Error: Attemping to '+' that hasn't been initialized. Around line {node.lineno}")

    def post_visit_ExpressionEAANDE(self, node: ASTExpressionEAANDE):
        left_side = self.get_type(node.Expression)
        right_side = self.get_type(node.Expression2)
        if left_side[1] == 'false' or right_side[1] == 'false':
            self.errors.append(f"Error: Attempting to '&&' something that hasn't been initialized yet. Around line {node.lineno}")

    def post_visit_ExpresssionECEqualE(self, node: ASTExpressionECEqualE):
        left_side = self.get_type(node.Expression)
        right_side = self.get_type(node.Expression2)
        isValid = False
        if right_side[1] == 'false':
            isValid = False
        elif left_side[1] == 'false':
            isValid = False
        else:
            isValid = True

        if (right_side[0] not in ('int', 'char', 'string',  'bool')) and left_side[0] == 'null':
            isValid = True
        elif (left_side[0] not in ('int', 'char', 'string',  'bool')) and right_side[0] == 'null':
            isValid = True
        if (right_side[0] not in ('int[]', 'char[]', 'string[]',  'bool[]')) and right_side[1] == 'false' and left_side[0] == 'null':
            isValid = True
        elif (left_side[0] not in ('int[]', 'char[]', 'string[]',  'bool[]')) and left_side[1] == 'false' and right_side[0] == 'null':
            isValid = True

        if isValid == False:
            self.errors.append(f"Error: Attempting to '==' {left_side[0]} and {right_side[0]} that hasn't been initialized yet. Around line {node.lineno}")

    def post_visit_ExpressionEDivideE(self, node: ASTExpressionEDivideE):
        left_side = self.get_type(node.Expression)
        right_side = self.get_type(node.Expression2)
        isValid = False
        if right_side[1] == 'false':
            isValid = False
        elif left_side[1] == 'false':
            isValid = False
        else:
            isValid = True
        if isValid == False:
            self.errors.append(f"Error: Attempting to '/' {left_side[0]} and {right_side[0]} that hasn't been initialized yet. Around line {node.lineno}")

    def post_visit_ExpressionEDivideEqualE(self, node: ASTExpressionEDivideEqualE):
        left_side = self.get_type(node.Expression)
        right_side = self.get_type(node.Expression2)
        isValid = False
        if right_side[1] == 'false':
            isValid = False
        elif left_side[1] == 'terminal':
            isValid = False
        elif left_side[1] == 'false':
            self.set_true(node.Expression)
            isValid = True
        else:
            isValid = True
        if isValid == False:
            self.errors.append(f"Error: Attempting to '/=' {left_side[0]} that hasn't been initialized yet. Around line {node.lineno}")

    def post_visit_ExpressionEEqualE(self, node: ASTExpressionEEqualE):
        left_side = self.get_type(node.Expression)
        right_side = self.get_type(node.Expression2)
        isValid = False
        if left_side[1] == 'terminal':
            isValid = False
        elif right_side[1] == 'false':
            isValid == False
        elif isinstance(node.Expression, ASTExpressionNew):
            isValid = False
        elif (right_side[1] == 'terminal' or right_side[1] == 'true') and (left_side[1] != 'terminal'):
            isValid = True
            if isinstance(node.Expression, ASTTerminal):
                tokType = theLexerTester(str(node.Expression.Terminal))
                if tokType.type != 'ID':
                    pass
                else:
                    for x in reversed(self.scope_stack):
                        for key, value in self.symbol_tables[x].items():
                            if key[0] == str(node.Expression.Terminal):
                                symbol = value['symbol']
                                symbol.isInitialized = True
                                break
        elif isinstance(node.Expression2, ASTExpressionNew):
            isValid = True
            if isinstance(node.Expression, ASTTerminal):
                tokType = theLexerTester(str(node.Expression.Terminal))
                if tokType.type != 'ID':
                    pass
                else:
                    for x in reversed(self.scope_stack):
                        for key, value in self.symbol_tables[x].items():
                            if key[0] == str(node.Expression.Terminal):
                                symbol = value['symbol']
                                symbol.isInitialized = True
        if isValid == False:
            self.errors.append(f"Error: Attempting to '=' something that hasn't been initialized yet. Around line {node.lineno}")
        if self.isMethod == True and isinstance(node.Expression2, ASTExpressionArgIdx):
            self.errors.append(f"Error: Attempting to assign a function to a variable. Around line {node.lineno}")
        self.isMethod = False

    def post_visit_ExpressionEGreaterE(self, node: ASTExpressionEGreaterE):
        left_side = self.get_type(node.Expression)
        right_side = self.get_type(node.Expression2)
        if left_side[1] == 'false' or right_side[1] == 'false':
            self.errors.append(f"Error: Attempting to '>' something that hasn't been initialized yet. Around line {node.lineno}")

    def post_visit_ExpressionEGreaterEqualE(self, node: ASTExpressionEGreaterEqualE):
        left_side = self.get_type(node.Expression)
        right_side = self.get_type(node.Expression2)
        if left_side[1] == 'false' or right_side[1] == 'false':
            self.errors.append(f"Error: Attempting to '>=' something that hasn't been initialized yet. Around line {node.lineno}")

    def post_visit_ExpressionELessE(self, node: ASTExpressionELessE):
        left_side = self.get_type(node.Expression)
        right_side = self.get_type(node.Expression2)
        if left_side[1] == 'false' or right_side[1] == 'false':
            self.errors.append(f"Error: Attempting to '<' something that hasn't been initialized yet. Around line {node.lineno}")

    def post_visit_ExpressionELessEqualE(self, node: ASTExpressionELessEqualE):
        left_side = self.get_type(node.Expression)
        right_side = self.get_type(node.Expression2)
        if left_side[1] == 'false' or right_side[1] == 'false':
            self.errors.append(f"Error: Attempting to '<=' something that hasn't been initialized yet. Around line {node.lineno}")

    def post_visit_ExpressionEMinusE(self, node: ASTExpressionEMinusE):
        left_side = self.get_type(node.Expression)
        right_side = self.get_type(node.Expression2)
        isValid = False
        if right_side[1] == 'false':
            isValid = False
        elif left_side[1] == 'false':
            isValid = False
        else:
            isValid = True
        if isValid == False:
            self.errors.append(f"Error: Attempting to '-' {left_side[0]} and {right_side[0]} that hasn't been initialized yet. Around line {node.lineno}")

    def post_visit_ExpressionEMinusEqualE(self, node: ASTExpressionEMinusEqualE):
        left_side = self.get_type(node.Expression)
        right_side = self.get_type(node.Expression2)
        isValid = False
        if right_side[1] == 'false':
            isValid = False
        elif left_side[1] == 'terminal':
            isValid = False
        elif left_side[1] == 'false':
            self.set_true(node.Expression)
            isValid = True
        else:
            isValid = True
        if isValid == False:
            self.errors.append(f"Error: Attempting to -= {left_side[0]} that hasn't been initialized yet. Around line {node.lineno}")

    def post_visit_ExpressionENotEqualE(self, node: ASTExpressionENotEqualE):
        left_side = self.get_type(node.Expression)
        right_side = self.get_type(node.Expression2)
        isValid = False
        if right_side[1] == 'false':
            isValid = False
        elif left_side[1] == 'false':
            isValid = False
        else:
            isValid = True

        if (right_side[0] not in ('int', 'char', 'string',  'bool')) and left_side[0] == 'null':
            isValid = True
        elif (left_side[0] not in ('int', 'char', 'string',  'bool')) and right_side[0] == 'null':
            isValid = True
        if (right_side[0] not in ('int[]', 'char[]', 'string[]',  'bool[]')) and right_side[1] == 'false' and left_side[0] == 'null':
            isValid = True
        elif (left_side[0] not in ('int[]', 'char[]', 'string[]',  'bool[]')) and left_side[1] == 'false' and right_side[0] == 'null':
            isValid = True
            
        if isValid == False:
            self.errors.append(f"Error: Attempting to '!=' {left_side[0]} and {right_side[0]} that hasn't been initialized yet. Around line {node.lineno}")

    def post_visit_ExpressionEOORE(self, node: ASTExpressionEOORE):
        left_side = self.get_type(node.Expression)
        right_side = self.get_type(node.Expression2)
        if left_side[1] == 'false' or right_side[1] == 'false':
            self.errors.append(f"Error: Attempting to '||' something that hasn't been initialized yet. Around line {node.lineno}")

    def post_visit_ExpressionEPlusE(self, node: ASTExpressionEPlusE):        
        left_side = self.get_type(node.Expression)
        right_side = self.get_type(node.Expression2)
        isValid = False
        if right_side[1] == 'false':
            isValid = False
        elif left_side[1] == 'false':
            isValid = False
        else:
            isValid = True
        if isValid == False:
            self.errors.append(f"Error: Attempting to '+' {left_side[0]} and {right_side[0]} that hasn't been initialized yet. Around line {node.lineno}")

    def post_visit_ExpressionEPlusEqualE(self, node: ASTExpressionEPlusEqualE):
        left_side = self.get_type(node.Expression)
        right_side = self.get_type(node.Expression2)
        isValid = False
        if right_side[1] == 'false':
            isValid = False
        elif left_side[1] == 'terminal':
            isValid = False
        elif left_side[1] == 'false':
            self.set_true(node.Expression)
            isValid = True
        else:
            isValid = True
        if isValid == False:
            self.errors.append(f"Error: Attempting to '+=' {left_side[0]} that hasn't been initialized yet. Around line {node.lineno}")

    def post_visit_ExpressionETimesE(self, node: ASTExpressionETimesE):
        left_side = self.get_type(node.Expression)
        right_side = self.get_type(node.Expression2)
        isValid = False
        if right_side[1] == 'false':
            isValid = False
        elif left_side[1] == 'false':
            isValid = False
        else:
            isValid = True
        if isValid == False:
            self.errors.append(f"Error: Attempting to '*' {left_side[0]} and {right_side[0]} that hasn't been initialized yet. Around line {node.lineno}")

    def post_visit_ExpressionETimesEqualE(self, node: ASTExpressionETimesEqualE):
        left_side = self.get_type(node.Expression)
        right_side = self.get_type(node.Expression2)
        isValid = False
        if right_side[1] == 'false':
            isValid = False
        elif left_side[1] == 'terminal':
            isValid = False
        elif left_side[1] == 'false':
            self.set_true(node.Expression)
            isValid = True
        else:
            isValid = True
        if isValid == False:
            self.errors.append(f"Error: Attempting to '*=' {left_side[0]} that hasn't been initialized yet. Around line {node.lineno}")

    def post_visit_Index(self, node: ASTIndex):
        idx = self.get_type(node.Expression)
        if idx[1] == False:
            self.errrors.append(f"Error: index value is not initialized. Around line {node.lineno}")
    
    def pre_visit_MethodDeclaration(self, node: ASTMethodDeclaration):
        self.enter_scope()

    def post_visit_MethodDeclaration(self, node: ASTMethodDeclaration):
        self.exit_scope()

    def post_visit_StatementCIN(self, node: ASTStatementCIN):
        messageType = self.get_type(node.Expression)
        if messageType[1] == 'terminal':
            self.errors.append(f"Error: Can not CIN {messageType[0]} that is a terminal. Around line {node.lineno}")
        else:
            self.set_true(node.Expression)

    def post_visit_StatementCOUT(self, node: ASTStatementCOUT):
        messageType = self.get_type(node.Expression)
        if messageType[1] != 'true' and messageType[1] != 'terminal':
            self.errors.append(f"Error: Can not COUT {messageType[0]} that hasn't been initialized. Around line {node.lineno}")

    def post_visit_StatementIF(self, node: ASTStatementIF):
        ifType = self.get_type(node.Expression)
        if ifType[1] != 'true' and (ifType[0] != 'true' and ifType[0] != 'false'): 
            self.errors.append(f"Error: The given expressiong for an 'if' statement {ifType[0]} is not initialized. Around line {node.lineno}")

    def post_visit_StatementIFELSE(self, node: ASTStatementIFELSE):
        ifType = self.get_type(node.Expression)
        if ifType[1] != 'true' and (ifType[0] != 'true' and ifType[0] != 'false'): 
            self.errors.append(f"Error: The given expressiong for an 'if/else' statement {ifType[0]} is not initialized. Around line {node.lineno}")

    def post_visit_StatementReturn(self, node: ASTStatementReturn):
        if node.MaybeExpression.Expression != None:
            returnType = self.get_type(node.MaybeExpression.Expression)
            if returnType[1] != 'terminal' and returnType[1] != 'true':
                self.errors.append(f"Error: Attempting to return a variable {returnType} that hasn't been initialized. Around line {node.lineno}")

    def post_visit_StatementSwitch(self, node: ASTStatementSwitch):
        type = self.get_type(node.Expression)
        if type[1] == 'false':
            self.errors.append(f"Error: Switch statement expression is not initialized. {type[0]} was not initialized. Around line {node.lineno}")

    def post_visit_StatementWhile(self, node: ASTStatementWhile):
        ifType = self.get_type(node.Expression)
        if ifType[1] != 'true' and (ifType[0] != 'true' and ifType[0] != 'false'): 
            self.errors.append(f"Error: The given expressiong for an 'while' statement is not initialized. Around line {node.lineno}")

    def post_visit_VariableDeclaration(self, node: ASTVariableDeclaration):
        type = node.Type
        if node.LRSquare != None:
            type = str(type) + '[]'
        
        if node.Initializer.Initializer != None:
            done = False
            initalType = self.get_type(node.Initializer.Initializer)
            if node.LRSquare != None:
                if initalType[0] == 'null':
                    done = True

            if initalType[0] == 'null':
                done= True
            else:
                if initalType[0] == 'null' and (type == 'int' or type == 'char' or type == 'bool' or type == 'string'):
                    self.errors.append(f"Error: null can only be assigned to a class or array type not {type}. Around line {node.lineno}")
                else:
                    if initalType == 'null':
                        done = True

            if type == 'bool' and (initalType[0] == 'false' or initalType[0] == 'true'):
                done = True
            elif type == initalType[0]:
                done = True
            if done == False:
                self.errors.append(f"Error: attempting to initalize a variable of type {type} and is getting set to {initalType[0]}. Around line {node.lineno}")
