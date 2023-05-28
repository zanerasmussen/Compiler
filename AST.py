from AbstractNode import ASTBASENODE

class ASTArgument(ASTBASENODE):
    def __init__(self, lineno, LPAREN, MaybeArgumentList, RPAREN):
        self.lineno = lineno
        self.LPAREN = LPAREN
        self.MaybeArgumentList = MaybeArgumentList
        self.RPAREN = RPAREN
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_Argument(self)
        if self.MaybeArgumentList != None:
            self.MaybeArgumentList.accept(visitor)
        visitor.post_visit_Argument(self)

class ASTArgOrIdx(ASTBASENODE):
    def __init__(self, Arg_Idx):
        self.Arg_Idx = Arg_Idx
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_ArgOrIdx(self)
        self.Arg_Idx.accept(visitor)
        visitor.post_visit_ArgOrIdx(self)

class ASTArgumentList(ASTBASENODE):
    def __init__(self, Expression, MultipleCommaExpression):
        self.Expression = Expression
        self.MultipleCommaExpression = MultipleCommaExpression 
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_ArgumentList(self)
        if self.Expression != None:
            self.Expression.accept(visitor)
        if self.MultipleCommaExpression != None:
            self.MultipleCommaExpression.accept(visitor)
        visitor.post_visit_ArgumentList(self)

class ASTCase(ASTBASENODE):
    def __init__(self, lineno, CASE, NumOrChar, COLON, MultipleStatement):
        self.lineno = lineno
        self.CASE = CASE
        self.NumOrChar = NumOrChar
        self.COLON = COLON
        self.MultipleStatement = MultipleStatement
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_Case(self)
        if self.MultipleStatement != None:
            self.MultipleStatement.accept(visitor)
        visitor.post_visit_Case(self)

class ASTCaseBlock(ASTBASENODE):
    def __init__(self, lineno, LCURLY, MultipleCase, DEFAULT, COLON, MultipleStatement, RCURLY):
        self.lineno = lineno
        self.LCURLY = LCURLY
        self.MultipleCase = MultipleCase
        self.DEFAULT = DEFAULT
        self.COLON = COLON
        self.MultipleStatement = MultipleStatement
        self.RCURLY = RCURLY
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_CaseBlock(self)
        if self.MultipleCase != None:
            self.MultipleCase.accept(visitor)
        if self.MultipleStatement != None:
            self.MultipleStatement.accept(visitor)
        visitor.post_visit_CaseBlock(self)

class ASTClassDefinition(ASTBASENODE):
    def __init__(self, lineno, Class, ID, LCURLY, MultipleClassMemberDefinition, RCURLY):
        self.lineno = lineno
        self.Class = Class
        self.ID = ID
        self.LCURLY = LCURLY
        self.MultipleClassMemberDefinition = MultipleClassMemberDefinition
        self.RCURLY = RCURLY
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_ClassDefinition(self)
        if self.MultipleClassMemberDefinition != None:
            self.MultipleClassMemberDefinition.accept(visitor)
        if self.MultipleClassMemberDefinition != None:
            visitor.post_visit_ClassDefinition(self)

class ASTClassMemberDefinition(ASTBASENODE):
    def __init__(self, Method_DataMember_Constructor):
        self.Method_DataMember_Constructor = Method_DataMember_Constructor
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_ClassMemberDefinition(self)
        self.Method_DataMember_Constructor.accept(visitor)
        visitor.post_visit_ClassMemberDefinition(self)

class ASTCompilationUnit(ASTBASENODE):
    def __init__(self, lineno, MultipleClassDefinition, void, kxi2023, main, LPAREN, RPAREN, MethodBody):
        self.lineno = lineno
        self.MultipleClassDefinition = MultipleClassDefinition
        self.void = void
        self.kxi2023 = kxi2023
        self.main = main
        self.LPAREN = LPAREN
        self.RPAREN = RPAREN
        self.MethodBody = MethodBody
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_CompilationUnit(self)
        if self.MultipleClassDefinition != None:
            self.MultipleClassDefinition.accept(visitor)
        if self.MethodBody != None:
            self.MethodBody.accept(visitor)
        if self.MultipleClassDefinition != None and self.MethodBody != None:
            visitor.post_visit_CompilationUnit(self)
  
class ASTConstructorDeclaration(ASTBASENODE):
    def __init__(self, lineno, ID, MethodSuffix):
        self.lineno = lineno
        self.ID = ID
        self.MethodSuffix = MethodSuffix
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_ConstructorDeclaration(self)
        if self.MethodSuffix != None:
            self.MethodSuffix.accept(visitor)
        visitor.post_visit_ConstructorDeclaration(self)

class ASTDataMemberDeclaration(ASTBASENODE):
    def __init__(self, Modifier, VariableDeclaration):
        self.Modifier = Modifier
        self.VariableDeclaration = VariableDeclaration
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_DataMemberDeclaration(self)
        if self.VariableDeclaration != None:
            self.VariableDeclaration.accept(visitor)
        visitor.post_visit_DataMemberDeclaration(self)

class ASTExpressionArgIdx(ASTBASENODE):
    def __init__(self, Expression, ArgOrIdx):
        self.Expression = Expression
        self.ArgOrIdx = ArgOrIdx
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_ExpressionArgIdx(self)
        if self.Expression != None:
            self.Expression.accept(visitor)
        if self.ArgOrIdx != None:
            self.ArgOrIdx.accept(visitor)
        visitor.post_visit_ExpressionArgIdx(self)

class ASTExpressionDotID(ASTBASENODE):
    def __init__(self, lineno, Expression, PERIOD, ID):
        self.lineno = lineno
        self.Expression = Expression
        self.PERIOD = PERIOD
        self.ID = ID
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_ExpressionDotID(self)
        if self.Expression != None:
            self.Expression.accept(visitor)
        visitor.post_visit_ExpressionDotID(self)

class ASTExpressionMinus(ASTBASENODE):
    def __init__(self, lineno, MINUS, Expression):
        self.lineno = lineno
        self.MINUS = MINUS
        self.Expression = Expression
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_ExpressionMinus(self)
        if self.Expression != None:
            self.Expression.accept(visitor)
        visitor.post_visit_ExpressionMinus(self)

class ASTExpressionNew(ASTBASENODE):
    def __init__(self, lineno, NEW, Type, ArgOrIdx):
        self.lineno = lineno
        self.NEW = NEW
        self.Type = Type
        self.ArgOrIdx = ArgOrIdx
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_ExpressionNew(self)
        if self.ArgOrIdx != None:
            self.ArgOrIdx.accept(visitor)
        visitor.post_visit_ExpressionNew(self)

class ASTExpressionNot(ASTBASENODE):
    def __init__(self, lineno, NOT, Expression):
        self.lineno = lineno
        self.NOT = NOT
        self.Expression = Expression
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_ExpressionNot(self)
        if self.Expression != None:
            self.Expression.accept(visitor)
        visitor.post_visit_ExpressionNot(self)

class ASTExpressionPlus(ASTBASENODE):
    def __init__(self, lineno, PLUS, Expression):
        self.lineno = lineno
        self.PLUS = PLUS
        self.Expression = Expression
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_ExpressionPlus(self)
        if self.Expression != None:
            self.Expression.accept(visitor)
        visitor.post_visit_ExpressionPlus(self)

class ASTExpressionPAREN(ASTBASENODE):
    def __init__(self, lineno, LPAREN, Expression, RPAREN):
        self.lineno = lineno
        self.LPAREN = LPAREN
        self.Expression = Expression
        self.RPAREN = RPAREN
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_ExpressionPAREN(self)
        if self.Expression != None:
            self.Expression.accept(visitor)
        visitor.post_visit_ExpressionPAREN(self)

class ASTExpressionEAANDE(ASTBASENODE):
    def __init__(self, lineno, Expression, AAND, Expression2):
        self.lineno = lineno
        self.Expression = Expression
        self.AAND = AAND
        self.Expression2 = Expression2
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_ExpressionEAANDE(self)
        if self.Expression != None:
            self.Expression.accept(visitor)
        if self.Expression2 != None:
            self.Expression2.accept(visitor)
        visitor.post_visit_ExpressionEAANDE(self)

class ASTExpressionECEqualE(ASTBASENODE):
    def __init__(self, lineno, Expression, CEQUAL, Expression2):
        self.lineno = lineno
        self.Expression = Expression
        self.CEQUAL = CEQUAL
        self.Expression2 = Expression2
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_ExpresssionECEqualE(self)
        if self.Expression != None:
            self.Expression.accept(visitor)
        if self.Expression2 != None:
            self.Expression2.accept(visitor)
        visitor.post_visit_ExpresssionECEqualE(self)

class ASTExpressionEDivideE(ASTBASENODE):
    def __init__(self, lineno, Expression, DIVIDE, Expression2):
        self.lineno = lineno
        self.Expression = Expression
        self.DIVIDE = DIVIDE
        self.Expression2 = Expression2
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_ExpressionEDivideE(self)
        if self.Expression != None:
            self.Expression.accept(visitor)
        if self.Expression2 != None:
            self.Expression2.accept(visitor)
        visitor.post_visit_ExpressionEDivideE(self)

class ASTExpressionEDivideEqualE(ASTBASENODE):
    def __init__(self, lineno, Expression, DIVIDEEQUAL, Expression2):
        self.lineno = lineno
        self.Expression = Expression
        self.DIVIDEEQUAL = DIVIDEEQUAL
        self.Expression2 = Expression2
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_ExpressionEDivideEqualE(self)
        if self.Expression != None:
            self.Expression.accept(visitor)
        if self.Expression2 != None:
            self.Expression2.accept(visitor)
        visitor.post_visit_ExpressionEDivideEqualE(self)

class ASTExpressionEEqualE(ASTBASENODE):
    def __init__(self, lineno, Expression, EQUAL, Expression2):
        self.lineno = lineno
        self.Expression = Expression
        self.EQUAL = EQUAL
        self.Expression2 = Expression2
        self.type = ""
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_ExpressionEEqualE(self)
        if self.Expression != None:
            self.Expression.accept(visitor)
        if self.Expression2 != None:
            self.Expression2.accept(visitor)
        visitor.post_visit_ExpressionEEqualE(self)

class ASTExpressionEGreaterE(ASTBASENODE):
    def __init__(self, lineno, Expression, GREATER, Expression2):
        self.lineno = lineno
        self.Expression = Expression
        self.GREATER = GREATER
        self.Expression2 = Expression2
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_ExpressionEGreaterE(self)
        if self.Expression != None:
            self.Expression.accept(visitor)
        if self.Expression2 != None:
            self.Expression2.accept(visitor)
        visitor.post_visit_ExpressionEGreaterE(self)

class ASTExpressionEGreaterEqualE(ASTBASENODE):
    def __init__(self, lineno, Expression, GREATEQUAL, Expression2):
        self.lineno = lineno
        self.Expression = Expression
        self.GREATEQUAL = GREATEQUAL
        self.Expression2 = Expression2
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_ExpressionEGreaterEqualE(self)
        if self.Expression != None:
            self.Expression.accept(visitor)
        if self.Expression2 != None:
            self.Expression2.accept(visitor)
        visitor.post_visit_ExpressionEGreaterEqualE(self)

class ASTExpressionELessE(ASTBASENODE):
    def __init__(self, lineno, Expression, LESS, Expression2):
        self.lineno = lineno
        self.Expression = Expression
        self.LESS = LESS
        self.Expression2 = Expression2
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_ExpressionELessE(self)
        if self.Expression != None:
            self.Expression.accept(visitor)
        if self.Expression2 != None:
            self.Expression2.accept(visitor)
        visitor.post_visit_ExpressionELessE(self)

class ASTExpressionELessEqualE(ASTBASENODE):
    def __init__(self, lineno, Expression, LESSEQUAL, Expression2):
        self.lineno = lineno
        self.Expression = Expression
        self.LESSEQUAL = LESSEQUAL
        self.Expression2 = Expression2
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_ExpressionELessEqualE(self)
        if self.Expression != None:
            self.Expression.accept(visitor)
        if self.Expression2 != None:
            self.Expression2.accept(visitor)
        visitor.post_visit_ExpressionELessEqualE(self)

class ASTExpressionEMinusE(ASTBASENODE):
    def __init__(self, lineno, Expression, MINUS, Expression2):
        self.lineno = lineno
        self.Expression = Expression
        self.MINUS = MINUS
        self.Expression2 = Expression2
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_ExpressionEMinusE(self)
        if self.Expression != None:
            self.Expression.accept(visitor)
        if self.Expression2 != None:
            self.Expression2.accept(visitor)
        visitor.post_visit_ExpressionEMinusE(self)

class ASTExpressionEMinusEqualE(ASTBASENODE):
    def __init__(self, lineno, Expression, MINUSEQUAL, Expression2):
        self.lineno = lineno
        self.Expression = Expression
        self.MINUSEQUAL = MINUSEQUAL
        self.Expression2 = Expression2
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_ExpressionEMinusEqualE(self)
        if self.Expression != None:
            self.Expression.accept(visitor)
        if self.Expression2 != None:
            self.Expression2.accept(visitor)
        visitor.post_visit_ExpressionEMinusEqualE(self)

class ASTExpressionENotEqualE(ASTBASENODE):
    def __init__(self, lineno, Expression, NEQUAL, Expression2):
        self.lineno = lineno
        self.Expression = Expression
        self.NEQUAL = NEQUAL
        self.Expression2 = Expression2
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_ExpressionENotEqualE(self)
        if self.Expression != None:
            self.Expression.accept(visitor)
        if self.Expression2 != None:
            self.Expression2.accept(visitor)
        visitor.post_visit_ExpressionENotEqualE(self)

class ASTExpressionEOORE(ASTBASENODE):
    def __init__(self, lineno, Expression, OOR, Expression2):
        self.lineno = lineno
        self.Expression = Expression
        self.OOR = OOR
        self.Expression2 = Expression2
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_ExpressionEOORE(self)
        if self.Expression != None:
            self.Expression.accept(visitor)
        if self.Expression2 != None:
            self.Expression2.accept(visitor)
        visitor.post_visit_ExpressionEOORE(self)

class ASTExpressionEPlusE(ASTBASENODE):
    def __init__(self, lineno, Expression, PLUS, Expression2):
        self.lineno = lineno
        self.Expression = Expression
        self.PLUS = PLUS
        self.Expression2 = Expression2
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_ExpressionEPlusE(self)
        if self.Expression != None:
            self.Expression.accept(visitor)
        if self.Expression2 != None:
            self.Expression2.accept(visitor)
        visitor.post_visit_ExpressionEPlusE(self)

class ASTExpressionEPlusEqualE(ASTBASENODE):
    def __init__(self, lineno, Expression, PLUSEQUAL, Expression2):
        self.lineno = lineno
        self.Expression = Expression
        self.PLUSEQUAL = PLUSEQUAL
        self.Expression2 = Expression2
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_ExpressionEPlusEqualE(self)
        if self.Expression != None:
            self.Expression.accept(visitor)
        if self.Expression2 != None:
            self.Expression2.accept(visitor)
        visitor.post_visit_ExpressionEPlusEqualE(self)

class ASTExpressionETimesE(ASTBASENODE):
    def __init__(self, lineno, Expression, TIMES, Expression2):
        self.lineno = lineno
        self.Expression = Expression
        self.TIMES = TIMES
        self.Expression2 = Expression2
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_ExpressionETimesE(self)
        if self.Expression != None:
            self.Expression.accept(visitor)
        if self.Expression2 != None:
            self.Expression2.accept(visitor)
        visitor.post_visit_ExpressionETimesE(self)

class ASTExpressionETimesEqualE(ASTBASENODE):
    def __init__(self, lineno, Expression, TIMESEQUAL, Expression2):
        self.lineno = lineno
        self.Expression = Expression
        self.TIMESEQUAL = TIMESEQUAL
        self.Expression2 = Expression2
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_ExpressionETimesEqualE(self)
        if self.Expression != None:
            self.Expression.accept(visitor)
        if self.Expression2 != None:
            self.Expression2.accept(visitor)
        visitor.post_visit_ExpressionETimesEqualE(self)

class ASTIndex(ASTBASENODE):
    def __init__(self, lineno, LSQUARE, Expression, RSQUARE):
        self.lineno = lineno
        self.LSQUARE = LSQUARE
        self.Expression = Expression
        self.RSQUARE = RSQUARE
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_Index(self)
        if self.Expression != None:
            self.Expression.accept(visitor)
        visitor.post_visit_Index(self)

class ASTInitializer(ASTBASENODE):
    def __init__(self, lineno, EQUAL, Expression):
        self.lineno = lineno
        self.EQUAL = EQUAL
        self.Expression = Expression
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_Initializer(self)
        if self.Expression != None:
            self.Expression.accept(visitor)
        visitor.post_visit_Initializer(self)

class ASTMaybeArgumentList(ASTBASENODE):
    def __init__(self, ArgumentList):
        self.ArgumentList = ArgumentList
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_MaybeArgumentList(self)
        if self.ArgumentList != None:
            self.ArgumentList.accept(visitor)
        if self.ArgumentList != None:
            visitor.post_visit_MaybeArgumentList(self)

class ASTMaybeExpression(ASTBASENODE):
    def __init__(self, Expression):
        self.Expression = Expression
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_MaybeExpression(self)
        if self.Expression != None:
            self.Expression.accept(visitor)
        if self.Expression != None:
            visitor.post_visit_MaybeExpression(self)

class ASTMaybeInitializer(ASTBASENODE):
    def __init__(self, Initializer):
        self.Initializer = Initializer
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_MaybeInitializer(self)
        if self.Initializer != None:
            self.Initializer.accept(visitor)
        if self.Initializer != None:
            visitor.post_visit_MaybeInitializer(self)

class ASTMaybeParamList(ASTBASENODE):
    def __init__(self, ParameterList):
        self.ParameterList = ParameterList
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_MaybeParamList(self)
        if self.ParameterList != None:
            self.ParameterList.accept(visitor)
        if self.ParameterList != None:
            visitor.post_visit_MaybeParamList(self)

class ASTMethodBody(ASTBASENODE):
    def __init__(self, lineno, LCURLY, MultipleStatement, RCURLY):
        self.lineno = lineno
        self.LCURLY = LCURLY
        self.MultipleStatement = MultipleStatement
        self.RCURLY = RCURLY
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_MethodBody(self)
        if self.MultipleStatement != None:
            self.MultipleStatement.accept(visitor)
        if self.MultipleStatement != None:
            visitor.post_visit_MethodBody(self)

class ASTMethodDeclaration(ASTBASENODE):
    def __init__(self, lineno, Modifier, Type, LRSquare, ID, MethodSuffix):
        self.lineno = lineno
        self.Modifier = Modifier
        self.Type = Type
        self.LRSquare = LRSquare
        self.ID = ID
        self.MethodSuffix = MethodSuffix
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_MethodDeclaration(self)
        if self.MethodSuffix != None:
            self.MethodSuffix.accept(visitor)
            visitor.post_visit_MethodDeclaration(self)

class ASTMethodSuffix(ASTBASENODE):
    def __init__(self, lineno, LPAREN, MaybeParameterList, RPAREN, MethodBody):
        self.lineno = lineno
        self.LPAREN = LPAREN
        self.MaybeParameterList = MaybeParameterList
        self.RPAREN = RPAREN
        self.MethodBody = MethodBody
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_MethodSuffix(self)
        if self.MaybeParameterList != None:
            self.MaybeParameterList.accept(visitor)
        if self.MethodBody != None:
            self.MethodBody.accept(visitor)
        visitor.post_visit_MethodSuffix(self)

class ASTMultipleCase(ASTBASENODE):
    def __init__(self, Case, MultipleCase):
        self.Case = Case
        self.MultipleCase = MultipleCase
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_MultipleCase(self)
        if self.Case != None:
            self.Case.accept(visitor)
        if self.MultipleCase != None:
            self.MultipleCase.accept(visitor)
        if self.MultipleCase != None and self.Case != None:
            visitor.post_visit_MultipleCase(self)

class ASTMultipleClassDefinition(ASTBASENODE):
    def __init__(self, ClassDefinition, MultipleClassDefinition):
        self.ClassDefinition = ClassDefinition
        self.MultipleClassDefinition = MultipleClassDefinition
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_MultipleClassDefinition(self)
        if self.ClassDefinition != None:
            self.ClassDefinition.accept(visitor)
        if self.MultipleClassDefinition != None:
            self.MultipleClassDefinition.accept(visitor)  
        if self.ClassDefinition != None and self.MultipleClassDefinition != None:
            visitor.post_visit_MultipleClassDefinition(self)

class ASTMultipleClassMemberDefinition(ASTBASENODE):
    def __init__(self, ClassMemberDefinition, MultipleClassMemberDefinition):
        self.ClassMemberDefinition = ClassMemberDefinition
        self.MultipleClassMemberDefinition = MultipleClassMemberDefinition
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_MultipleClassMemberDefinition(self)
        if self.ClassMemberDefinition != None:
            self.ClassMemberDefinition.accept(visitor)
        if self.MultipleClassMemberDefinition != None:
            self.MultipleClassMemberDefinition.accept(visitor)
        if self.ClassMemberDefinition != None and self.MultipleClassMemberDefinition != None:
            visitor.post_visit_MultipleClassMemberDefinition(self)

class ASTMultipleCommaExpression(ASTBASENODE):
    def __init__(self, COMMA, Expression, MultipleCommaExpression):
        self.COMMA = COMMA
        self.Expression = Expression
        self.MultipleCommaExpression = MultipleCommaExpression
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_MultipleCommaExpression(self)
        if self.Expression != None:
            self.Expression.accept(visitor)
        if self.MultipleCommaExpression != None:
            self.MultipleCommaExpression.accept(visitor)
        visitor.post_visit_MultipleCommaExpression(self)

class ASTMultipleCommaParameter(ASTBASENODE):
    def __init__(self, COMMA, Parameter, MultipleCommaParameter):
        self.COMMA = COMMA
        self.Parameter = Parameter
        self.MultipleCommaParameter = MultipleCommaParameter
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_MultipleCommaParameter(self)
        if self.Parameter != None:
            self.Parameter.accept(visitor)
        if self.MultipleCommaParameter != None:
            self.MultipleCommaParameter.accept(visitor)
        visitor.post_visit_MultipleCommaParameter(self)

class ASTMultipleStatement(ASTBASENODE):
    def __init__(self, Statement, MultipleStatement):
        self.Statement = Statement
        self.MultipleStatement = MultipleStatement
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_MultipleStatement(self)
        if self.Statement != None:
            self.Statement.accept(visitor)
        if self.MultipleStatement != None:
            self.MultipleStatement.accept(visitor)
        if self.MultipleStatement != None and self.Statement != None:
            visitor.post_visit_MultipleStatement(self)

class ASTParameter(ASTBASENODE):
    def __init__(self, lineno, Type, LRSquare, ID):
        self.lineno = lineno
        self.Type = Type
        self.LRSquare = LRSquare
        self.ID = ID
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_Parameter(self)
        visitor.post_visit_Parameter(self)

class ASTParameterList(ASTBASENODE):
    def __init__(self, Parameter, MultipleCommaParameter):
        self.Parameter = Parameter
        self.MultipleCommaParameter = MultipleCommaParameter
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_ParameterList(self)
        if self.Parameter != None:
            self.Parameter.accept(visitor)
        if self.MultipleCommaParameter != None:
            self.MultipleCommaParameter.accept(visitor)
        visitor.post_visit_ParameterList(self)

class ASTStatementBreak(ASTBASENODE):
    def __init__(self, lineno, BREAK, SEMICOLON):
        self.lineno = lineno
        self.BREAK = BREAK
        self.SEMICOLON = SEMICOLON
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_StatementBreak(self)
        visitor.post_visit_StatementBreak(self)

class ASTStatementCIN(ASTBASENODE):
    def __init__(self, lineno, CIN, RIGHTSHIFT, Expression, SEMICOLON):
        self.lineno = lineno
        self.CIN = CIN
        self.RIGHTSHIFT = RIGHTSHIFT
        self.Expression = Expression
        self.SEMICOLON = SEMICOLON
        self.type = ""
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_StatementCIN(self)
        if self.Expression != None:
            self.Expression.accept(visitor)
        visitor.post_visit_StatementCIN(self)

class ASTStatementCOUT(ASTBASENODE):
    def __init__(self, lineno, COUT, LEFTSHIFT, Expression, SEMICOLON):
        self.lineno = lineno
        self.COUT = COUT
        self.LEFTSHIFT = LEFTSHIFT
        self.Expression = Expression
        self.SEMICOLON = SEMICOLON
        self.type = ""
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_StatementCOUT(self)
        if self.Expression != None:
            self.Expression.accept(visitor)
        visitor.post_visit_StatementCOUT(self)

class ASTStatementExpression(ASTBASENODE):
    def __init__(self, lineno, Expression, SEMICOLON):
        self.lineno = lineno
        self.Expression = Expression
        self.SEMICOLON = SEMICOLON
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_StatementExpression(self)
        if self.Expression != None:
            self.Expression.accept(visitor)
        visitor.post_visit_StatementExpression(self)

class ASTStatementIF(ASTBASENODE):
    def __init__(self, lineno, IF, LPAREN, Expression, RPAREN, Statement):
        self.lineno = lineno
        self.IF = IF
        self.LPAREN = LPAREN
        self.Expression = Expression
        self.RPAREN = RPAREN
        self.Statement = Statement
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_StatementIF(self)
        if self.Expression != None:
            self.Expression.accept(visitor)
        if self.Statement != None:
            self.Statement.accept(visitor)
        visitor.post_visit_StatementIF(self)

class ASTStatementIFELSE(ASTBASENODE):
    def __init__(self, lineno, IF, LPAREN, Expression, RPAREN, Statement, ELSE, Statement2):
        self.lineno = lineno
        self.IF = IF
        self.LPAREN = LPAREN
        self.Expression = Expression
        self.RPAREN = RPAREN
        self.Statement = Statement
        self.ELSE = ELSE
        self.Statement2 = Statement2
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_StatementIFELSE(self)
        if self.Expression != None:
            self.Expression.accept(visitor)
        if self.Statement != None:
            self.Statement.accept(visitor)
        if self.Statement2 != None:
            self.Statement2.accept(visitor)
        visitor.post_visit_StatementIFELSE(self)

class ASTStatementMultipleStatement(ASTBASENODE):
    def __init__(self, lineno, LCURLY, MultipleStatement, RCURLY):
        self.lineno = lineno
        self.LCURLY = LCURLY
        self.MultipleStatement = MultipleStatement
        self.RCURLY = RCURLY
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_StatementMultipleStatement(self)
        if self.MultipleStatement != None:
            self.MultipleStatement.accept(visitor)
        visitor.post_visit_StatementMultipleStatement(self)

class ASTStatementToVariableDeclaration(ASTBASENODE):
    def __init__(self, VariableDeclaration):
        self.VariableDeclaration = VariableDeclaration
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_StatementToVariableDeclaration(self)
        if self.VariableDeclaration != None:
            self.VariableDeclaration.accept(visitor)
        visitor.post_visit_StatementToVariableDeclaration(self)

class ASTStatementReturn(ASTBASENODE):
    def __init__(self, lineno, RETURN, MaybeExpression, SEMICOLON):
        self.lineno = lineno
        self.RETURN = RETURN
        self.MaybeExpression = MaybeExpression
        self.SEMICOLON = SEMICOLON
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_StatementReturn(self)
        if self.MaybeExpression != None:
            self.MaybeExpression.accept(visitor)
        visitor.post_visit_StatementReturn(self)

class ASTStatementSwitch(ASTBASENODE):
    def __init__(self, lineno, SWITCH, LPAREN, Expression, RPAREN, CaseBlock):
        self.lineno = lineno
        self.SWITCH = SWITCH
        self.LPAREN = LPAREN
        self.Expression = Expression
        self.RPAREN = RPAREN
        self.CaseBlock = CaseBlock
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_StatementSwitch(self)
        if self.Expression != None:
            self.Expression.accept(visitor)
        if self.CaseBlock != None:
            self.CaseBlock.accept(visitor)
        visitor.post_visit_StatementSwitch(self)

class ASTStatementWhile(ASTBASENODE):
    def __init__(self, lineno, WHILE, LPAREN, Expression, RPAREN, Statement):
        self.lineno = lineno
        self.WHILE = WHILE
        self.LPAREN = LPAREN
        self.Expression = Expression
        self.RPAREN = RPAREN
        self.Statement = Statement
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_StatementWhile(self)
        if self.Expression != None:
            self.Expression.accept(visitor)
        if self.Statement != None:
            self.Statement.accept(visitor)
        visitor.post_visit_StatementWhile(self)

class ASTVariableDeclaration(ASTBASENODE):
    def __init__(self, lineno, Type, LRSquare, ID, Initializer, SEMICOLON):
        self.lineno = lineno
        self.Type = Type
        self.LRSquare = LRSquare
        self.ID = ID
        self.Initializer = Initializer
        self.SEMICOLON = SEMICOLON
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_VariableDeclaration(self)
        if self.Initializer != None:
            self.Initializer.accept(visitor)
        visitor.post_visit_VariableDeclaration(self)

class ASTTerminal(ASTBASENODE):
    def __init__(self, lineno, Terminal):
        self.lineno = lineno
        self.Terminal = Terminal
        self.asm = []

    def accept(self, visitor):
        visitor.pre_visit_Terminal(self)
        visitor.post_visit_Terminal(self)