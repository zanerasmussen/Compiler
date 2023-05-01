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
                            return (symbol.Type, str(symbol.isInitialized).lower())

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

        elif isinstance(node, ASTExpressionECEqualE):
            left_side = self.get_type(node.Expression)
            left_side_init = left_side[1]
            right_side = self.get_type(node.Expression2)
            right_side_init = right_side[1]
            if left_side_init != "false" and right_side_init != "false":
                return ("bool", "true")

        elif isinstance(node, ASTExpressionEDivideE):
            left_side = self.get_type(node.Expression)
            left_side_init = left_side[1]
            right_side = self.get_type(node.Expression2)
            right_side_init = right_side[1]
            if left_side_init == "true" and right_side_init != "false":
                return ("int", "true")
            else:
                self.errors.append(f"Error: Attemping to use {left_side[0]} and {right_side[0]}. May not be initialized or 'terminal'. Around line {node.lineno}")
            
        elif isinstance(node, ASTExpressionEDivideEqualE):
            left_side = self.get_type(node.Expression)
            left_side_init = left_side[1]
            right_side = self.get_type(node.Expression2)
            right_side_init = right_side[1]
            if left_side_init != "terminal" and right_side_init != "false":
                return ("int", "true")
            else:
                self.errors.append(f"Error: Attemping to use {left_side[0]} and {right_side[0]}. May not be initialized or 'terminal'. Around line {node.lineno}")
             
        elif isinstance(node, ASTExpressionEEqualE):
            left_side = self.get_type(node.Expression)
            left_side_init = left_side[1]
            right_side = self.get_type(node.Expression2)
            right_side_init = right_side[1]
            if left_side_init != "terminal" and right_side_init != "false":
                return (str(left_side[0]), "true")
            else:
                self.errors.append(f"Error: Attemping to use {left_side[0]} and {right_side[0]}. May not be initialized or 'terminal'. Around line {node.lineno}")
   
        elif isinstance(node, ASTExpressionEGreaterE):
            left_side = self.get_type(node.Expression)
            left_side_init = left_side[1]
            right_side = self.get_type(node.Expression2)
            right_side_init = right_side[1]
            if right_side_init != "false" and left_side_init != "false":
                return ("bool", "true")
            else:
                self.errors.append(f"Error: Attemping to use {left_side[0]} and {right_side[0]}. May not be initialized or 'terminal'. Around line {node.lineno}")

        elif isinstance(node, ASTExpressionEGreaterEqualE):
            left_side = self.get_type(node.Expression)
            left_side_init = left_side[1]
            right_side = self.get_type(node.Expression2)
            right_side_init = right_side[1]
            if right_side_init != "false" and left_side_init != "terminal":
                return ("bool", "true")
            else:
                self.errors.append(f"Error: Attemping to use {left_side[0]} and {right_side[0]}. May not be initialized or 'terminal'. Around line {node.lineno}")

        elif isinstance(node, ASTExpressionELessE):
            left_side = self.get_type(node.Expression)
            left_side_init = left_side[1]
            right_side = self.get_type(node.Expression2)
            right_side_init = right_side[1]
            if right_side_init != "false" and left_side_init != "false":
                return ("bool", "true")
            else:
                self.errors.append(f"Error: Attemping to use {left_side[0]} and {right_side[0]}. May not be initialized or 'terminal'. Around line {node.lineno}")

        elif isinstance(node, ASTExpressionELessEqualE):
            left_side = self.get_type(node.Expression)
            left_side_init = left_side[1]
            right_side = self.get_type(node.Expression2)
            right_side_init = right_side[1]
            if right_side_init != "false" and left_side_init != "terminal":
                return ("bool", "true")
            else:
                self.errors.append(f"Error: Attemping to use {left_side[0]} and {right_side[0]}. May not be initialized or 'terminal'. Around line {node.lineno}")

        elif isinstance(node, ASTExpressionEMinusE):
            left_side = self.get_type(node.Expression)
            left_side_init = left_side[1]
            right_side = self.get_type(node.Expression2)
            right_side_init = right_side[1]
            if left_side_init == "true" and right_side_init != "false":
                return ("int", "true")
            else:
                self.errors.append(f"Error: Attemping to use {left_side[0]} and {right_side[0]}. May not be initialized or 'terminal'. Around line {node.lineno}")   
                      
        elif isinstance(node, ASTExpressionEMinusEqualE):
            left_side = self.get_type(node.Expression)
            left_side_init = left_side[1]
            right_side = self.get_type(node.Expression2)
            right_side_init = right_side[1]
            if left_side_init != "terminal" and right_side_init != "false":
                return ("int", "true")
            else:
                self.errors.append(f"Error: Attemping to use {left_side[0]} and {right_side[0]}. May not be initialized or 'terminal'. Around line {node.lineno}")
             
        elif isinstance(node, ASTExpressionENotEqualE):
            left_side = self.get_type(node.Expression)
            left_side_init = left_side[1]
            right_side = self.get_type(node.Expression2)
            right_side_init = right_side[1]
            if right_side_init != "false" and left_side_init != "terminal":
                return ("bool", "true")
            else:
                self.errors.append(f"Error: Attemping to use {left_side[0]} and {right_side[0]}. May not be initialized or 'terminal'. Around line {node.lineno}")

        elif isinstance(node, ASTExpressionEOORE):
            left_side = self.get_type(node.Expression)
            left_side_init = left_side[1]
            right_side = self.get_type(node.Expression2)
            right_side_init = right_side[1]
            if left_side_init != "false" and right_side_init != "false":
                return ("bool", "true")
            else:
                self.errors.append(f"Error: Attemping to use {left_side[0]} and {right_side[0]}. May not be initialized or 'terminal'. Around line {node.lineno}")

        elif isinstance(node, ASTExpressionEPlusE):
            left_side = self.get_type(node.Expression)
            left_side_init = left_side[1]
            right_side = self.get_type(node.Expression2)
            right_side_init = right_side[1]
            if left_side_init == "true" and right_side_init != "false":
                return ("int", "true")
            else:
                self.errors.append(f"Error: Attemping to use {left_side[0]} and {right_side[0]}. May not be initialized or 'terminal'. Around line {node.lineno}")
                
        elif isinstance(node, ASTExpressionEPlusEqualE):
            left_side = self.get_type(node.Expression)
            left_side_init = left_side[1]
            right_side = self.get_type(node.Expression2)
            right_side_init = right_side[1]
            if left_side_init != "terminal" and right_side_init != "false":
                return ("int", "true")
            else:
                self.errors.append(f"Error: Attemping to use {left_side[0]} and {right_side[0]}. May not be initialized or 'terminal'. Around line {node.lineno}")
            
        elif isinstance(node, ASTExpressionETimesE):
            left_side = self.get_type(node.Expression)
            left_side_init = left_side[1]
            right_side = self.get_type(node.Expression2)
            right_side_init = right_side[1]
            if left_side_init == "true" and right_side_init != "false":
                return ("int", "true")
            else:
                self.errors.append(f"Error: Attemping to use {left_side[0] } and {right_side[0]}. May not be initialized or 'terminal'. Around line {node.lineno}")
            
        elif isinstance(node, ASTExpressionETimesEqualE):
            left_side = self.get_type(node.Expression)
            left_side_init = left_side[1]
            right_side = self.get_type(node.Expression2)
            right_side_init = right_side[1]
            if left_side_init != "terminal" and right_side_init != "false":
                return ("int", "true")
            else:
                self.errors.append(f"Error: Attemping to use {left_side[0] } and {right_side[0]}. May not be initialized or 'terminal'. Around line {node.lineno}")
            
        elif isinstance(node, ASTIndex):
            idx = self.get_type(node.Expression)
            idx_init = idx[1]
            if idx_init != 'false':
                return ("int", "true")
            else:
                self.errors.append(f"Error: Attemping to use an index {idx[0]} that is not initialied. Around line {node.lineno}")
            
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
                for x in (self.scope_stack):
                    for key, value in self.symbol_tables[x].items():
                        if key[0] == str(node.Terminal):
                            symbol = value['symbol']
                            return(str(symbol.Type), str(symbol.isInitialized).lower())

        else:
            self.errors.append("didn't find expression")


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
        if expressionType != None:
            if expressionType[1] != "true":
                self.errors.append(f"Error: attemping to call on an expression that hasn't been initialized.")

    def pre_visit_ExpressionDotID(self, node: ASTExpressionDotID):
        pass

    def post_visit_ExpressionDotID(self, node: ASTExpressionDotID):
        left_side = self.get_type(node.Expression)
        if left_side[1] != "true":
            self.errors.append(f"Error: Attempting to use an object {left_side[0]} that hasn't been initialized")

    def pre_visit_ExpressionMinus(self, node: ASTExpressionMinus):
        pass

    def post_visit_ExpressionMinus(self, node: ASTExpressionMinus):
        right_side = self.get_type(node.Expression)
        if right_side[1] == "false":
            self.errors.append(f"Error: Attemping to uniary '-' and it hasn't been initialized. Around line {node.lineno}")

    def pre_visit_ExpressionNew(self, node: ASTExpressionNew):
        pass

    def post_visit_ExpressionNew(self, node: ASTExpressionNew):
        pass

    def pre_visit_ExpressionNot(self, node: ASTExpressionNot):
        pass

    def post_visit_ExpressionNot(self, node: ASTExpressionNot):
        right_side = self.get_type(node.Expression)
        if right_side[1] == 'false':
            self.errors.append(f"Error: Attemping to '!' that hasn't been initialized. Around line {node.lineno}")

    def pre_visit_ExpressionPlus(self, node: ASTExpressionPlus):
        pass

    def post_visit_ExpressionPlus(self, node: ASTExpressionPlus):
        right_side = self.get_type(node.Expression)
        if right_side[1] == 'false':
            self.errors.append(f"Error: Attemping to '+' that hasn't been initialized. Around line {node.lineno}")

    def pre_visit_ExpressionPAREN(self, node: ASTExpressionPAREN):
        pass
    
    def post_visit_ExpressionPAREN(self, node: ASTExpressionPAREN):
        pass

    def pre_visit_ExpressionEAANDE(self, node: ASTExpressionEAANDE):
        pass

    def post_visit_ExpressionEAANDE(self, node: ASTExpressionEAANDE):
        left_side = self.get_type(node.Expression)
        right_side = self.get_type(node.Expression2)
        if left_side[1] == 'false' or right_side[1] == 'false':
            self.errors.append(f"Error: Attempting to '&&' something that hasn't been initialized yet. Around line {node.lineno}")

    def pre_visit_ExpresssionECEqualE(self, node: ASTExpressionECEqualE):
        pass

    def post_visit_ExpresssionECEqualE(self, node: ASTExpressionECEqualE):
        left_side = self.get_type(node.Expression)
        right_side = self.get_type(node.Expression2)
        if left_side[1] == 'false' or right_side[1] == 'false':
            self.errors.append(f"Error: Attempting to '&&' something that hasn't been initialized yet. Around line {node.lineno}")

    def pre_visit_ExpressionEDivideE(self, node: ASTExpressionEDivideE):
        pass

    def post_visit_ExpressionEDivideE(self, node: ASTExpressionEDivideE):
        left_side = self.get_type(node.Expression)
        right_side = self.get_type(node.Expression2)
        if left_side[1] == 'false' or right_side[1] == 'false':
            self.errors.append(f"Error: Attempting to '/' something that hasn't been initialized yet. Around line {node.lineno}")

    def pre_visit_ExpressionEDivideEqualE(self, node: ASTExpressionEDivideEqualE):
        pass

    def post_visit_ExpressionEDivideEqualE(self, node: ASTExpressionEDivideEqualE):
        left_side = self.get_type(node.Expression)
        right_side = self.get_type(node.Expression2)
        if left_side[1] != 'true' or right_side[1] == 'false':
            self.errors.append(f"Error: Attempting to '/=' something that hasn't been initialized yet. Around line {node.lineno}")

    def pre_visit_ExpressionEEqualE(self, node: ASTExpressionEEqualE):
        pass

    def post_visit_ExpressionEEqualE(self, node: ASTExpressionEEqualE):
        left_side = self.get_type(node.Expression)
        right_side = self.get_type(node.Expression2)
        if left_side[1] == 'terminal' or right_side[1] == 'false':
            self.errors.append(f"Error: Attempting to '=' something that hasn't been initialized yet. Around line {node.lineno}")

    def pre_visit_ExpressionEGreaterE(self, node: ASTExpressionEGreaterE):
        pass

    def post_visit_ExpressionEGreaterE(self, node: ASTExpressionEGreaterE):
        left_side = self.get_type(node.Expression)
        right_side = self.get_type(node.Expression2)
        if left_side[1] == 'false' or right_side[1] == 'false':
            self.errors.append(f"Error: Attempting to '<' something that hasn't been initialized yet. Around line {node.lineno}")

    def pre_visit_ExpressionEGreaterEqualE(self, node: ASTExpressionEGreaterEqualE):
        pass

    def post_visit_ExpressionEGreaterEqualE(self, node: ASTExpressionEGreaterEqualE):
        left_side = self.get_type(node.Expression)
        right_side = self.get_type(node.Expression2)
        if left_side[1] != 'true' or right_side[1] == 'false':
            self.errors.append(f"Error: Attempting to '<' something that hasn't been initialized yet. Around line {node.lineno}")

    def pre_visit_ExpressionELessE(self, node: ASTExpressionELessE):
        pass

    def post_visit_ExpressionELessE(self, node: ASTExpressionELessE):
        left_side = self.get_type(node.Expression)
        right_side = self.get_type(node.Expression2)
        if left_side[1] == 'false' or right_side[1] == 'false':
            self.errors.append(f"Error: Attempting to '<' something that hasn't been initialized yet. Around line {node.lineno}")

    def pre_visit_ExpressionELessEqualE(self, node: ASTExpressionELessEqualE):
        pass

    def post_visit_ExpressionELessEqualE(self, node: ASTExpressionELessEqualE):
        left_side = self.get_type(node.Expression)
        right_side = self.get_type(node.Expression2)
        if left_side[1] != 'true' or right_side[1] == 'false':
            self.errors.append(f"Error: Attempting to '<' something that hasn't been initialized yet. Around line {node.lineno}")

    def pre_visit_ExpressionEMinusE(self, node: ASTExpressionEMinusE):
        pass

    def post_visit_ExpressionEMinusE(self, node: ASTExpressionEMinusE):
        left_side = self.get_type(node.Expression)
        right_side = self.get_type(node.Expression2)
        if left_side[1] == 'false' or right_side[1] == 'false':
            self.errors.append(f"Error: Attempting to '-' something that hasn't been initialized yet. Around line {node.lineno}")

    def pre_visit_ExpressionEMinusEqualE(self, node: ASTExpressionEMinusEqualE):
        pass

    def post_visit_ExpressionEMinusEqualE(self, node: ASTExpressionEMinusEqualE):
        left_side = self.get_type(node.Expression)
        right_side = self.get_type(node.Expression2)
        if left_side[1] != 'true' or right_side[1] == 'false':
            self.errors.append(f"Error: Attempting to '<' something that hasn't been initialized yet. Around line {node.lineno}")

    def pre_visit_ExpressionENotEqualE(self, node: ASTExpressionENotEqualE):
        pass

    def post_visit_ExpressionENotEqualE(self, node: ASTExpressionENotEqualE):
        left_side = self.get_type(node.Expression)
        right_side = self.get_type(node.Expression2) 
        if left_side[1] != 'true' or right_side[1] == 'false':
            self.errors.append(f"Error: Attempting to '!=' something that hasn't been initialized yet. Around line {node.lineno}")

    def pre_visit_ExpressionEOORE(self, node: ASTExpressionEOORE):
        pass

    def post_visit_ExpressionEOORE(self, node: ASTExpressionEOORE):
        left_side = self.get_type(node.Expression)
        right_side = self.get_type(node.Expression2)
        if left_side[1] == 'false' or right_side[1] == 'false':
            self.errors.append(f"Error: Attempting to '&&' something that hasn't been initialized yet. Around line {node.lineno}")

    def pre_visit_ExpressionEPlusE(self, node: ASTExpressionEPlusE):
        pass
    
    def post_visit_ExpressionEPlusE(self, node: ASTExpressionEPlusE):
        left_side = self.get_type(node.Expression)
        right_side = self.get_type(node.Expression2)
        if left_side[1] == 'false' or right_side[1] == 'false':
            self.errors.append(f"Error: Attempting to '+' something that hasn't been initialized yet. Around line {node.lineno}")

    def pre_visit_ExpressionEPlusEqualE(self, node: ASTExpressionEPlusEqualE):
        pass

    def post_visit_ExpressionEPlusEqualE(self, node: ASTExpressionEPlusEqualE):
        left_side = self.get_type(node.Expression)
        right_side = self.get_type(node.Expression2)
        if left_side[1] != 'true' or right_side[1] == 'false':
            self.errors.append(f"Error: Attempting to '<' something that hasn't been initialized yet. Around line {node.lineno}")

    def pre_visit_ExpressionETimesE(self, node: ASTExpressionETimesE):
        pass

    def post_visit_ExpressionETimesE(self, node: ASTExpressionETimesE):
        left_side = self.get_type(node.Expression)
        right_side = self.get_type(node.Expression2)
        if left_side[1] == 'false' or right_side[1] == 'false':
            self.errors.append(f"Error: Attempting to '*' something that hasn't been initialized yet. Around line {node.lineno}")

    def pre_visit_ExpressionETimesEqualE(self, node: ASTExpressionETimesEqualE):
        pass

    def post_visit_ExpressionETimesEqualE(self, node: ASTExpressionETimesEqualE):
        left_side = self.get_type(node.Expression)
        right_side = self.get_type(node.Expression2)
        if left_side[1] != 'true' or right_side[1] == 'false':
            self.errors.append(f"Error: Attempting to '<' something that hasn't been initialized yet. Around line {node.lineno}")

    def pre_visit_Index(self, node: ASTIndex):
        pass

    def post_visit_Index(self, node: ASTIndex):
        idx = self.get_type(node.Expression)
        if idx[1] == False:
            self.errrors.append(f"Error: index value is not initialized. Around line {node.lineno}")
    
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
        self.enter_scope()

    def post_visit_MethodDeclaration(self, node: ASTMethodDeclaration):
        self.exit_scope()

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
        messageType = self.get_type(node.Expression)
        if messageType  != "int" and messageType !='char':
            self.errors.append(f"Error: Can not CIN {messageType}. Around line {node.lineno}")

    def pre_visit_StatementCOUT(self, node: ASTStatementCOUT):
        pass

    def post_visit_StatementCOUT(self, node: ASTStatementCOUT):
        messageType = self.get_type(node.Expression)
        if messageType  != "int" and messageType !='char' and messageType != 'bool' and messageType != 'true'and messageType != 'false' and messageType != 'string':
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
        pass

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
            self.errors.append(f"Error: A bool is required after an if statement. {ifType} was given. Around line {node.lineno}")

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