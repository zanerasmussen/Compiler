from AbstractNode import ASTBASENODE


class ASTArgument(ASTBASENODE):
    def __init__(self, LPAREN, MaybeArgumentList, RPAREN):
        self.LPAREN = LPAREN
        self.MaybeArgumentList = MaybeArgumentList
        self.RPAREN = RPAREN

    def accept(self, visitor):
        return visitor.visit_Argument(self)

class ASTArgumentList(ASTBASENODE):
    def __init__(self, Expression, MultipleCommaExpression):
        self.Expression = Expression
        self.MultipleCommaExpression = MultipleCommaExpression 

    def accept(self, visitor):
        return visitor.visit_ArgumentList(self)

class ASTArgOrIdx(ASTBASENODE):
    def __init__(self, Arg_Idx):
        self.Arg_Idx = Arg_Idx

    def accept(self, visitor):
        return visitor.visit_ArgOrIdx(self)

class ASTCase(ASTBASENODE):
    def __init__(self, CASE, NumOrChar, COLON, MultipleStatement):
        self.CASE = CASE
        self.NumOrChar = NumOrChar
        self.COLON = COLON
        self.MultipleStatement = MultipleStatement

    def accept(self, visitor):
        return visitor.visit_Case(self)

class ASTCaseBlock(ASTBASENODE):
    def __init__(self, LCURLY, MultipleCase, DEFAULT, COLON, MultipleStatement, RCURLY):
        self.LCURLY = LCURLY
        self.MultipleCase = MultipleCase
        self.DEFAULT = DEFAULT
        self.COLON = COLON
        self.MultipleStatement = MultipleStatement
        self.RCURLY = RCURLY

    def accept(self, visitor):
        return visitor.visit_CaseBlock(self)

class ASTClassDefinition(ASTBASENODE):
    def __init__(self, Class, ID, LCURLY, MultipleClassMemberDefinition, RCURLY):
        self.Class = Class
        self.ID = ID
        self.LCURLY = LCURLY
        self.MultipleClassMemberDefinition = MultipleClassMemberDefinition
        self.RCURLY = RCURLY

    def accept(self, visitor):
        return visitor.visit_ClassDefinition(self)

class ASTClassMemberDefinition(ASTBASENODE):
    def __init__(self, Method_DataMember_Constructor):
        self.Method_DataMember_Constructor = Method_DataMember_Constructor

    def accept(self, visitor):
        return visitor.visit_ClassMemberDefinition(self)

class ASTCompilationUnit(ASTBASENODE):
    def __init__(self, MultipleClassDefinition, void, kxi2023, main, LPAREN, RPAREN, MethodBody):
        self.MultipleClassDefinition = MultipleClassDefinition
        self.void = void
        self.kxi2023 = kxi2023
        self.main = main
        self.LPAREN = LPAREN
        self.RPAREN = RPAREN
        self.MethodBody = MethodBody

    def accept(self, visitor):
        return visitor.visit_CompilationUnit(self)
  
class ASTConstructorDeclaration(ASTBASENODE):
    def __init__(self, ID, MethodSuffix):
        self.ID = ID
        self.MethodSuffix = MethodSuffix

    def accept(self, visitor):
        return visitor.visit_ConstructorDeclaration(self)

class ASTDataMemberDeclaration(ASTBASENODE):
    def __init__(self, Modifier, VariableDeclaration):
        self.Modifier = Modifier
        self.VariableDeclaration = VariableDeclaration

    def accept(self, visitor):
        return visitor.visit_DataMemberDeclaration(self)

class ASTExpressionArgIdx(ASTBASENODE):
    def __init__(self, Expression, ArgOrIdx):
        self.Expression = Expression
        self.ArgOrIdx = ArgOrIdx

    def accept(self, visitor):
        return visitor.visit_ExpressionArgIdx(self)

class ASTExpressionDotID(ASTBASENODE):
    def __init__(self, Expression, PERIOD, ID):
        self.Expression = Expression
        self.PERIOD = PERIOD
        self.ID = ID

    def accept(self, visitor):
        return visitor.visit_ExpressionDotID(self)

class ASTExpressionMinus(ASTBASENODE):
    def __init__(self, MINUS, Expression):
        self.MINUS = MINUS
        self.Expression = Expression

    def accept(self, visitor):
        return visitor.visit_ExpressionMinus(self)

class ASTExpressionNew(ASTBASENODE):
    def __init__(self, NEW, Type, ArgOrIdx):
        self.NEW = NEW
        self.Type = Type
        self.ArgOrIdx = ArgOrIdx

    def accept(self, visitor):
        return visitor.visit_ExpressionNew(self)

class ASTExpressionNot(ASTBASENODE):
    def __init__(self, NOT, Expression):
        self.NOT = NOT
        self.Expression = Expression

    def accept(self, visitor):
        return visitor.visit_ExpressionNot(self)

class ASTExpressionPlus(ASTBASENODE):
    def __init__(self, PLUS, Expression):
        self.PLUS = PLUS
        self.Expression = Expression

    def accept(self, visitor):
        return visitor.visit_ExpressionPlus(self)

class ASTExpressionPAREN(ASTBASENODE):
    def __init__(self, LPAREN, Expression, RPAREN):
        self.LPAREN = LPAREN
        self.Expression = Expression
        self.RPAREN = RPAREN

    def accept(self, visitor):
        return visitor.visit_ExpressionPAREN(self)

class ASTExpressionEAANDE(ASTBASENODE):
    def __init__(self, Expression, AAND, Expression2):
        self.Expression = Expression
        self.AAND = AAND
        self.Expression2 = Expression2

    def accept(self, visitor):
        return visitor.visit_ExpressionEAANDE(self)

class ASTExpressionECEqualE(ASTBASENODE):
    def __init__(self, Expression, CEQUAL, Expression2):
        self.Expression = Expression
        self.CEQUAL = CEQUAL
        self.Expression2 = Expression2

    def accept(self, visitor):
        return visitor.visit_ExpresssionECEqualE(self)

class ASTExpressionEDivideE(ASTBASENODE):
    def __init__(self, Expression, DIVIDE, Expression2):
        self.Expression = Expression
        self.DIVIDE = DIVIDE
        self.Expression2 = Expression2

    def accept(self, visitor):
        return visitor.visit_ExpressionEDivideE(self)

class ASTExpressionEDivideEqualE(ASTBASENODE):
    def __init__(self, Expression, DIVIDEEQUAL, Expression2):
        self.Expression = Expression
        self.DIVIDEEQUAL = DIVIDEEQUAL
        self.Expression2 = Expression2

    def accept(self, visitor):
        return visitor.visit_ExpressionEDivideEqualE(self)

class ASTExpressionEEqualE(ASTBASENODE):
    def __init__(self, Expression, EQUAL, Expression2):
        self.Expression = Expression
        self.EQUAL = EQUAL
        self.Expression2 = Expression2

    def accept(self, visitor):
        return visitor.visit_ExpressionEEqualE(self)

class ASTExpressionEGreaterE(ASTBASENODE):
    def __init__(self, Expression, GREATER, Expression2):
        self.Expression = Expression
        self.GREATER = GREATER
        self.Expression2 = Expression2

    def accept(self, visitor):
        return visitor.visit_ExpressionEGreaterE(self)

class ASTExpressionEGreaterEqualE(ASTBASENODE):
    def __init__(self, Expression, GREATEQUAL, Expression2):
        self.Expression = Expression
        self.GREATEQUAL = GREATEQUAL
        self.Expression2 = Expression2

    def accept(self, visitor):
        return visitor.visit_ExpressionEGreaterEqualE(self)

class ASTExpressionELessE(ASTBASENODE):
    def __init__(self, Expression, LESS, Expression2):
        self.Expression = Expression
        self.LESS = LESS
        self.Expression2 = Expression2

    def accept(self, visitor):
        return visitor.visit_ExpressionELessE(self)

class ASTExpressionELessEqualE(ASTBASENODE):
    def __init__(self, Expression, LESSEQUAL, Expression2):
        self.Expression = Expression
        self.LESSEQUAL = LESSEQUAL
        self.Expression2 = Expression2

    def accept(self, visitor):
        return visitor.visit_ExpressionELessEqualE(self)

class ASTExpressionEMinusE(ASTBASENODE):
    def __init__(self, Expression, MINUS, Expression2):
        self.Expression = Expression
        self.MINUS = MINUS
        self.Expression2 = Expression2

    def accept(self, visitor):
        return visitor.visit_ExpressionEMinusE(self)

class ASTExpressionEMinusEqualE(ASTBASENODE):
    def __init__(self, Expression, MINUSEQUAL, Expression2):
        self.Expression = Expression
        self.MINUSEQUAL = MINUSEQUAL
        self.Expression2 = Expression2

    def accept(self, visitor):
        return visitor.visit_ExpressionEMinusEqualE(self)

class ASTExpressionENotEqualE(ASTBASENODE):
    def __init__(self, Expression, NEQUAL, Expression2):
        self.Expression = Expression
        self.NEQUAL = NEQUAL
        self.Expression2 = Expression2

    def accept(self, visitor):
        return visitor.visit_ExpressionENotEqualE(self)

class ASTExpressionEOORE(ASTBASENODE):
    def __init__(self, Expression, OOR, Expression2):
        self.Expression = Expression
        self.OOR = OOR
        self.Expression2 = Expression2

    def accept(self, visitor):
        return visitor.visit_ExpressionEOORE(self)

class ASTExpressionEPlusE(ASTBASENODE):
    def __init__(self, Expression, PLUS, Expression2):
        self.Expression = Expression
        self.PLUS = PLUS
        self.Expression2 = Expression2

    def accept(self, visitor):
        return visitor.visit_ExpressionEPlusE(self)

class ASTExpressionEPlusEqualE(ASTBASENODE):
    def __init__(self, Expression, PLUSEQUAL, Expression2):
        self.Expression = Expression
        self.PLUSEQUAL = PLUSEQUAL
        self.Expression2 = Expression2

    def accept(self, visitor):
        return visitor.visit_ExpressionEPlusEqualE(self)

class ASTExpressionETimesE(ASTBASENODE):
    def __init__(self, Expression, TIMES, Expression2):
        self.Expression = Expression
        self.TIMES = TIMES
        self.Expression2 = Expression2

    def accept(self, visitor):
        return visitor.visit_ExpressionETimesE(self)

class ASTExpressionETimesEqualE(ASTBASENODE):
    def __init__(self, Expression, TIMESEQUAL, Expression2):
        self.Expression = Expression
        self.TIMESEQUAL = TIMESEQUAL
        self.Expression2 = Expression2

    def accept(self, visitor):
        return visitor.visit_ExpressionETimesEqualE(self)

class ASTIndex(ASTBASENODE):
    def __init__(self, LSQUARE, Expression, RSQUARE):
        self.LSQUARE = LSQUARE
        self.Expression = Expression
        self.RSQUARE = RSQUARE

    def accept(self, visitor):
        return visitor.visit_Index(self)

class ASTInitializer(ASTBASENODE):
    def __init__(self, EQUAL, Expression):
        self.EQUAL = EQUAL
        self.Expression = Expression

    def accept(self, visitor):
        return visitor.visit_Initializer(self)

class ASTMaybeArgumentList(ASTBASENODE):
    def __init__(self, ArgumentList):
        self.ArgumentList = ArgumentList

    def accept(self, visitor):
        return visitor.visit_MaybeArgumentList(self)

class ASTMaybeExpression(ASTBASENODE):
    def __init__(self, Expression):
        self.Expression = Expression

    def accept(self, visitor):
        return visitor.visit_MaybeExpression(self)

class ASTMaybeInitializer(ASTBASENODE):
    def __init__(self, Initializer):
        self.Initializer = Initializer

    def accept(self, visitor):
        return visitor.visit_MaybeInitializer(self)

class ASTMaybeParamList(ASTBASENODE):
    def __init__(self, ParameterList):
        self.ParameterList = ParameterList

    def accept(self, visitor):
        return visitor.visit_MaybeParamList(self)

class ASTMethodBody(ASTBASENODE):
    def __init__(self, LCURLY, MultipleStatement, RCURLY):
        self.LCURLY = LCURLY
        self.MultipleStatement = MultipleStatement
        self.RCURLY = RCURLY

    def accept(self, visitor):
        return visitor.visit_MethodBody(self)

class ASTMethodDeclaration(ASTBASENODE):
    def __init__(self, Modifier, Type, LRSquare, ID, MethodSuffix):
        self.Modifier = Modifier
        self.Type = Type
        self.LRSquare = LRSquare
        self.ID = ID
        self.MethodSuffix = MethodSuffix

    def accept(self, visitor):
        return visitor.visit_MethodDeclaration(self)

class ASTMethodSuffix(ASTBASENODE):
    def __init__(self, LPAREN, MaybeParameterList, RPAREN, MethodBody):
        self.LPAREN = LPAREN
        self.MaybeParameterList = MaybeParameterList
        self.RPAREN = RPAREN
        self.MethodBody = MethodBody

    def accept(self, visitor):
        return visitor.visit_MethodSuffix(self)

class ASTMultipleCase(ASTBASENODE):
    def __init__(self, Case):
        self.Case = Case

    def accept(self, visitor):
        return visitor.visit_MultipleCase(self)

class ASTMultipleClassDefinition(ASTBASENODE):
    def __init__(self, ClassDefinition):
        self.ClassDefinition = ClassDefinition

    def accept(self, visitor):
        return visitor.visit_MultipleClassDefinition(self)

class ASTMultipleClassMemberDefinition(ASTBASENODE):
    def __init__(self, ClassMemberDefinition):
        self.ClassMemberDefinition = ClassMemberDefinition

    def accept(self, visitor):
        return visitor.visit_MultipleClassMemberDefinition(self)

class ASTMultipleCommaExpression(ASTBASENODE):
    def __init__(self, COMMA, Expression, MultipleCommaExpression):
        self.COMMA = COMMA
        self.Expression = Expression
        self.MultipleCommaExpression = MultipleCommaExpression

    def accept(self, visitor):
        return visitor.visit_MultipleCommaExpression(self)

class ASTMultipleCommaParameter(ASTBASENODE):
    def __init__(self, COMMA, Expression, MultipleCommaParameter):
        self.COMMA = COMMA
        self.Expression = Expression
        self.MultipleCommaParameter = MultipleCommaParameter

    def accept(self, visitor):
        return visitor.visit_MultipleCommaParameter(self)

class ASTMultipleStatement(ASTBASENODE):
    def __init__(self, Statement):
        self.Statement = Statement

    def accept(self, visitor):
        return visitor.visit_MultipleStatement(self)

class ASTParameter(ASTBASENODE):
    def __init__(self, Type, LRSquare, ID):
        self.Type = Type
        self.LRSquare = LRSquare
        self.ID = ID

    def accept(self, visitor):
        return visitor.visit_Parameter(self)

class ASTParameterList(ASTBASENODE):
    def __init__(self, Parameter, MultipleCommaParameter):
        self.Parameter = Parameter
        self.MultipleCommaParameter = MultipleCommaParameter

    def accept(self, visitor):
        return visitor.visit_ParameterList(self)

class ASTStatementBreak(ASTBASENODE):
    def __init__(self, BREAK, SEMICOLON):
        self.BREAK = BREAK
        self.SEMICOLON = SEMICOLON

    def accept(self, visitor):
        return visitor.visit_StatementBreak(self)

class ASTStatementCIN(ASTBASENODE):
    def __init__(self, CIN, RIGHTSHIFT, Expression, SEMICOLON):
        self.CIN = CIN
        self.RIGHTSHIFT = RIGHTSHIFT
        self.Expression = Expression
        self.SEMICOLON = SEMICOLON

    def accept(self, visitor):
        return visitor.visit_StatementCIN(self)

class ASTStatementCOUT(ASTBASENODE):
    def __init__(self, COUT, LEFTSHIFT, Expression, SEMICOLON):
        self.COUT = COUT
        self.LEFTSHIFT = LEFTSHIFT
        self.Expression = Expression
        self.SEMICOLON = SEMICOLON

    def accept(self, visitor):
        return visitor.visit_StatementCOUT(self)

class ASTStatementExpression(ASTBASENODE):
    def __init__(self, Expression, SEMICOLON):
        self.Expression = Expression
        self.SEMICOLON = SEMICOLON

    def accept(self, visitor):
        return visitor.visit_StatementExpression(self)

class ASTStatementIF(ASTBASENODE):
    def __init__(self, IF, LPAREN, Expression, RPAREN, Statement):
        self.IF = IF
        self.LPAREN = LPAREN
        self.Expression = Expression
        self.RPAREN = RPAREN
        self.Statement = Statement

    def accept(self, visitor):
        return visitor.visit_StatementIF(self)

class ASTStatementIFELSE(ASTBASENODE):
    def __init__(self, IF, LPAREN, Expression, RPAREN, Statement, ELSE, Statement2):
        self.IF = IF
        self.LPAREN = LPAREN
        self.Expression = Expression
        self.RPAREN = RPAREN
        self.Statement = Statement
        self.ELSE = ELSE
        self.Statement2 = Statement2

    def accept(self, visitor):
        return visitor.visit_StatementIFELSE(self)

class ASTStatementMultipleStatement(ASTBASENODE):
    def __init__(self, LCURLY, MultipleStatement, RCURLY):
        self.LCURLY = LCURLY
        self.MultipleStatement = MultipleStatement
        self.RCURLY = RCURLY

    def accept(self, visitor):
        return visitor.visit_StatementMultipleStatement(self)

class ASTStatementToVariableDeclaration(ASTBASENODE):
    def __init__(self, VariableDeclaration):
        self.VariableDeclaration = VariableDeclaration

    def accept(self, visitor):
        return visitor.visit_StatementToVariableDeclaration(self)

class ASTStatementReturn(ASTBASENODE):
    def __init__(self, RETURN, MaybeExpression, SEMICOLON):
        self.RETURN = RETURN
        self.MaybeExpression = MaybeExpression
        self.SEMICOLON = SEMICOLON

    def accept(self, visitor):
        return visitor.visit_StatementReturn(self)

class ASTStatementSwitch(ASTBASENODE):
    def __init__(self, SWITCH, LPAREN, Expression, RPAREN, CaseBlock):
        self.SWITCH = SWITCH
        self.LPAREN = LPAREN
        self.Expression = Expression
        self.RPAREN = RPAREN
        self.CaseBlock = CaseBlock

    def accept(self, visitor):
        return visitor.visit_StatementSwitch(self)

class ASTStatementWhile(ASTBASENODE):
    def __init__(self, WHILE, LPAREN, Expression, RPAREN, Statement):
        self.WHILE = WHILE
        self.LPAREN = LPAREN
        self.Expression = Expression
        self.RPAREN = RPAREN
        self.Statement = Statement

    def accept(self, visitor):
        return visitor.visit_StatementWhile(self)

class ASTVariableDeclaration(ASTBASENODE):
    def __init__(self, Type, LRSquare, ID, Initializer, SEMICOLON):
        self.Type = Type
        self.LRSquare = LRSquare
        self.ID = ID
        self.Initializer = Initializer
        self.SEMICOLON = SEMICOLON

    def accept(self, visitor):
        return visitor.visit_VariableDeclaration(self)

class ASTTerminal(ASTBASENODE):
    def __init__(self, Terminal):
        self.Terminal = Terminal

    def accept(self, visitor):
        return visitor.visit_Terminal(self)