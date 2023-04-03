class ASTClassDefinition:
    def __init__(self, Class, ID, LCURLY, MultipleClassMemberDefinition, RCURLY):
        self.A_Class = Class
        self.B_ID = ID
        self.C_LCURLY = LCURLY
        self.D_MultipleClassMemberDefinition = MultipleClassMemberDefinition or []
        self.E_RCURLY = RCURLY

class ASTClassMemberDefinition:
    def __init__(self, MethodDeclaration, DataMemberDeclaration, ConstructorDeclaration):
        self.A_MethodDeclaration = MethodDeclaration
        self.B_DataMemberDeclaration = DataMemberDeclaration
        self.C_ConstructorDeclaration = ConstructorDeclaration

class ASTCompilationUnit:
    def __init__(self, MultipleClassDefinition, void, kxi2023, main, LPAREN, RPAREN, MethodBody):
        self.A_MultipleClassDefinition = MultipleClassDefinition or []
        self.B_void = void
        self.C_kxi2023 = kxi2023
        self.D_main = main
        self.E_LPAREN = LPAREN
        self.F_RPAREN = RPAREN
        self.G_MethodBody = MethodBody

class ASTConstructorDeclaration:
    def __init__(self, ID, MethodSuffix):
        self.ID = ID
        self.MethodSuffix = MethodSuffix

class ASTDataMemberDeclaration:
    def __init__(self, Modifier, VariableDeclaration):
        self.Modifier = Modifier
        self.VariableDeclaration = VariableDeclaration

class ASTInitializer:
    def __init__(self, EQUAL, Expression):
        self.EQUAL = EQUAL
        self.Expression = Expression

class ASTMethodBody:
    def __init__(self, LCURLY, MultipleStatement, RCURLY):
        self.LCURLY = LCURLY
        self.MultipleStatement = MultipleStatement
        self.RCURLY = RCURLY

class ASTMethodDeclaration:
    def __init__(self, Modifier, Type, LRSquare, ID, MethodSuffix):
        self.Modifier = Modifier
        self.Type = Type
        self.LRSquare = LRSquare
        self.ID = ID
        self.MethodSuffix = MethodSuffix

class ASTMethodSuffix:
    def __init__(self, LPAREN, MaybeParameterList, RPAREN, MethodBody):
        self.LPAREN = LPAREN
        self.MaybeParameterList = MaybeParameterList
        self.RPAREN = RPAREN
        self.MethodBody = MethodBody

class ASTMultipleClassDefinition:
    def __init__(self, ClassDefinition):
        self.ClassDefinition = ClassDefinition or []

class ASTMultipleClassMemberDefinition:
    def __init__(self, ClassMemberDefinition):
        self.ClassMemberDefinition = ClassMemberDefinition or []

class ASTMultipleCommaParameter:
    def __init__(self, COMMA, Expression, MultipleCommaExpression):
        self.COMMA = COMMA
        self.Expression = Expression
        self.MultipleCommaExpression = MultipleCommaExpression or []

class ASTParameter:
    def __init__(self, Type, LRSquare, ID):
        self.Type = Type
        self.LRSquare = LRSquare
        self.ID = ID

class ASTParameterList:
    def __init__(self, Parameter, MultipleCommaParameter):
        self.Parameter = Parameter
        self.MultipleCommaParameter = MultipleCommaParameter

class ASTStatementBreak:
    def __init__(self, BREAK, SEMICOLON):
        self.BREAK = BREAK
        self.SEMICOLON = SEMICOLON

class ASTStatementCIN:
    def __init__(self, CIN, RIGHTSHIFT, Expression, SEMICOLON):
        self.CIN = CIN
        self.RIGHTSHIFT = RIGHTSHIFT
        self.Expression = Expression
        self.SEMICOLON = SEMICOLON

class ASTStatementCOUT:
    def __init__(self, COUT, LEFTSHIFT, Expression, SEMICOLON):
        self.COUT = COUT
        self.LEFTSHIFT = LEFTSHIFT
        self.Expression = Expression
        self.SEMICOLON = SEMICOLON

class ASTStatementExpression:
    def __init__(self, Expression, SEMICOLON):
        self.Expression = Expression
        self.SEMICOLON = SEMICOLON

class ASTStatementMultipleStatement:
    def __init__(self, LCURLY, MultipleStatement, RCURLY):
        self.LCURLY = LCURLY
        self.MultipleStatement = MultipleStatement
        self.RCURLY = RCURLY

class ASTStatementToVariableDeclaration:
    def __init__(self, VariableDeclaration):
        self.VariableDeclaration = VariableDeclaration

class ASTStatementReturn:
    def __init__(self, RETURN, MaybeExpression, SEMICOLON):
        self.RETURN = RETURN
        self.MaybeExpression = MaybeExpression
        self.SEMICOLON = SEMICOLON

class ASTVariableDeclaration:
    def __init__(self, Type, LRSquare, ID, Initializer, SEMICOLON):
        self.Type = Type
        self.LRSquare = LRSquare
        self.ID = ID
        self.Initializer = Initializer
        self.SEMICOLON = SEMICOLON

