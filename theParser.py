import ply.yacc as yacc
from theLexer import tokens
import AST as AST
from PrintVisitor import PrintDotVisitor

# GRAMMAR
###########################
def p_Arguments(p):
    """Arguments : LPAREN MaybeArgumentList RPAREN"""
    p[0] = AST.ASTArgument(p[1], p[2], p[3])

# def p_Arguments_error(p):
#     """Arguments : error MaybeArgumentList RPAREN
#                     | LPAREN error RPAREN
#                     | LPAREN MaybeArgumentList error"""
#     print("Error in Arguments. Should be: ( <MaybeArgumentList> )")
#     raise SyntaxError("error")

def p_ArgumentList(p):
    """ArgumentList : Expression MultipleCommaExpression"""
    p[0] = AST.ASTArgumentList(p[1], p[2])

# def p_ArgumentList_error(p):
#     """ArgumentList : error MultipleCommaExpression
#                         | Expression error"""
#     print("Argument List error: Should be <expression> <MultipleCommaExpression>")
#     raise SyntaxError("Error")
    
def p_Case(p):
    """Case : CASE NumOrChar COLON MultipleStatement"""
    p[0] = AST.ASTCase(p[1], p[2], p[3], p[4])

# def p_Case_error(p):
#     """Case : error NumOrChar COLON MultipleStatement
#                 | CASE error COLON MultipleStatement
#                 | CASE NumOrChar error MultipleStatement
#                 | CASE NumOrChar COLON error"""
#     print("Error in Case. Should be 'case' <num>|<char> : <Multiple Statement>")
#     raise SyntaxError("Error in Case")

def p_CaseBlock(p):
    """CaseBlock : LCURLY MultipleCase DEFAULT COLON MultipleStatement RCURLY"""
    p[0] = AST.ASTCaseBlock(p[1], p[2], p[3], p[4], p[5], p[6])

def p_ClassDefinition(p):
    """ClassDefinition : CLASS ID LCURLY MultipleClassMemberDefinition RCURLY"""
    p[0] = AST.ASTClassDefinition(p[1], p[2], p[3], p[4], p[5])

# def p_ClassDefinition_error(p):
#     """ClassDefinition : error ID LCURLY MultipleClassMemberDefinition RCURLY
#                             | CLASS error LCURLY MultipleClassMemberDefinition RCURLY
#                             | CLASS ID error MultipleClassMemberDefinition RCURLY
#                             | CLASS ID LCURLY error RCURLY
#                             | CLASS ID LCURLY MultipleClassMemberDefinition error"""
#     print("Error in ClassDefinition. Should be: 'class' <id> { <ClassMemberDefinition>* }")
#     raise SyntaxError("error")

def p_ClassMemberDefinition(p):
    """ClassMemberDefinition : MethodDeclaration
                                | DataMemberDeclaration
                                | ConstructorDeclaration"""
    p[0] = AST.ASTClassMemberDefinition(p[1])
   
def p_CompilationUnit(p):
    """CompilationUnit : MultipleClassDefinition VOID KXI2023 Main LPAREN RPAREN MethodBody"""
    p[0] = AST.ASTCompilationUnit(p[1], p[2], p[3], p[4], p[5], p[6], p[7])

def p_CompilationUnit_error(p):
    """CompilationUnit : error VOID KXI2023 Main LPAREN RPAREN MethodBody"""
    print("Error with compilation Unit")

def p_ConstructorDeclaration(p):
    """ConstructorDeclaration : ID MethodSuffix"""
    p[0] = AST.ASTConstructorDeclaration(p[1], p[2])

def p_DataMemberDeclaration(p): 
    """DataMemberDeclaration : Modifier VariableDeclaration"""
    p[0] = AST.ASTDataMemberDeclaration(p[1], p[2])

def p_Expression(p):
    """Expression : THIS
                    | INT
                    | CHAR
                    | STRING
                    | TRUE
                    | FALSE
                    | NULL
                    | ID
                    | Expression Index
                    | Expression Arguments
                    | PLUS Expression
                    | NOT Expression
                    | MINUS Expression
                    | Expression PERIOD ID
                    | LPAREN Expression RPAREN
                    | Expression AAND Expression
                    | Expression CEQUAL Expression
                    | Expression DIVIDE Expression
                    | Expression DIVIDEEQUAL Expression
                    | Expression EQUAL Expression
                    | Expression GREATER Expression
                    | Expression GREATEQUAL Expression
                    | Expression LESS Expression
                    | Expression LESSEQUAL Expression
                    | Expression MINUS Expression
                    | Expression MINUSEQUAL Expression
                    | Expression NEQUAL Expression
                    | Expression OOR Expression
                    | Expression PLUS Expression
                    | Expression PLUSEQUAL Expression
                    | Expression TIMES Expression
                    | Expression TIMESEQUAL Expression
                    | NEW VOID Index
                    | NEW VOID Arguments
                    | NEW INT Index
                    | NEW INT Arguments
                    | NEW CHAR Index
                    | NEW CHAR Arguments
                    | NEW BOOL Index
                    | NEW BOOL Arguments
                    | NEW STRING Index
                    | NEW STRING Arguments
                    | NEW ID Index
                    | NEW ID Arguments"""

    if len(p) == 2:
        p[0] = AST.ASTTerminal(p[1])
    elif len(p) == 3 and p[1] == '-':
        p[0] = AST.ASTExpressionMinus(p[1], p[2])
    elif len(p) == 3 and p[1] == '!':
        p[0] = AST.ASTExpressionNot(p[1], p[2])     
    elif len(p) == 3 and p[1] == '+':
        p[0] = AST.ASTExpressionNot(p[1], p[2])   
    elif len(p) == 3:
        p[0] = AST.ASTExpressionArgIdx(p[1], p[2])
    elif len(p) == 4 and p[2] == '.':
        p[0] = AST.ASTExpressionDotID(p[1], p[2], p[3])
    elif len(p) == 4 and p[1] == "new":
        p[0] = AST.ASTExpressionNew(p[1], p[2], p[3])   
    elif len(p) == 4 and p[2] == "*=":
        p[0] = AST.ASTExpressionETimesEqualE(p[1], p[2], p[3])   
    elif len(p) == 4 and p[2] == "*":
        p[0] = AST.ASTExpressionETimesE(p[1], p[2], p[3])      
    elif len(p) == 4 and p[2] == "+=":
        p[0] = AST.ASTExpressionEPlusEqualE(p[1], p[2], p[3])    
    elif len(p) == 4 and p[2] == "+":
        p[0] = AST.ASTExpressionEPlusE(p[1], p[2], p[3])
    elif len(p) == 4 and p[2] == "||":
        p[0] = AST.ASTExpressionEOORE(p[1], p[2], p[3])
    elif len(p) == 4 and p[2] == "!=":
        p[0] = AST.ASTExpressionENotEqualE(p[1], p[2], p[3])
    elif len(p) == 4 and p[2] == "-=":
        p[0] = AST.ASTExpressionEMinusEqualE(p[1], p[2], p[3])
    elif len(p) == 4 and p[2] == "-":
        p[0] = AST.ASTExpressionEMinusE(p[1], p[2], p[3])
    elif len(p) == 4 and p[2] == "<=":
        p[0] = AST.ASTExpressionELessEqualE(p[1], p[2], p[3])
    elif len(p) == 4 and p[2] == "<":
        p[0] = AST.ASTExpressionELessE(p[1], p[2], p[3])    
    elif len(p) == 4 and p[2] == ">=":
        p[0] = AST.ASTExpressionEGreaterEqualE(p[1], p[2], p[3])
    elif len(p) == 4 and p[2] == ">":
        p[0] = AST.ASTExpressionEGreaterE(p[1], p[2], p[3])
    elif len(p) == 4 and p[2] == "=":
        p[0] = AST.ASTExpressionEEqualE(p[1], p[2], p[3])
    elif len(p) == 4 and p[2] == "/=":
        p[0] = AST.ASTExpressionEDivideEqualE(p[1], p[2], p[3])
    elif len(p) == 4 and p[2] == "/":
        p[0] = AST.ASTExpressionEDivideE(p[1], p[2], p[3])
    elif len(p) == 4 and p[2] == "==":
        p[0] = AST.ASTExpressionECEqualE(p[1], p[2], p[3])
    elif len(p) == 4 and p[2] == "&&":
        p[0] = AST.ASTExpressionEAANDE(p[1], p[2], p[3])
    else:
        p[0] = AST.ASTExpressionPAREN(p[1], p[2], p[3])

def p_Index(p):
    """Index : LSQUARE Expression RSQUARE"""
    p[0] = AST.ASTIndex(p[1], p[2], p[3])

def p_Initializer(p):
    """Initializer : EQUAL Expression"""
    p[0] = AST.ASTInitializer(p[1], p[2])

def p_Main(p):
    """Main : ID"""
    if p[1] != "main":
        print("expected main and got " + p[1])
    else:
        p[0] = "main"

def p_MaybeArgumentList(p):
    """MaybeArgumentList : 
                            | ArgumentList"""
    if len(p) == 1:
        p[0] = AST.ASTMaybeArgumentList(None)
    else:
        p[0] = AST.ASTMaybeArgumentList(p[1])

def p_MaybeExpression(p):
    """MaybeExpression : 
                            | Expression"""
    if len(p) == 1:
        p[0] = AST.ASTMaybeExpression(None)
    else:
        p[0] = AST.ASTMaybeExpression(p[1])

def p_MaybeInitializer(p):
    """MaybeInitializer : 
                            | Initializer"""
    if len(p) == 1:
        p[0] = AST.ASTMaybeInitializer(None)
    else:
        p[0] = AST.ASTMaybeInitializer(p[1])    
    
def p_MaybeLRSquare(p):
    """MaybeLRSquare : 
                        | LSQUARE RSQUARE"""
    if len(p) == 1:
        p[0] = None
    else:
        p[0] = "[]"

def p_MaybeParamList(p):
    """MaybeParamList : 
                        | ParameterList"""
    if len(p) == 1:
        p[0] = AST.ASTMaybeParamList(None)
    else:
        p[0] = AST.ASTMaybeParamList(p[1])       

def p_MethodBody(p):
    """MethodBody : LCURLY MultipleStatement RCURLY"""
    p[0] = AST.ASTMethodBody(p[1], p[2], p[3])

def p_MethodDeclaration(p):
    """MethodDeclaration : Modifier VOID MaybeLRSquare ID MethodSuffix
                            | Modifier INT MaybeLRSquare ID MethodSuffix
                            | Modifier CHAR MaybeLRSquare ID MethodSuffix
                            | Modifier BOOL MaybeLRSquare ID MethodSuffix
                            | Modifier STRING MaybeLRSquare ID MethodSuffix
                            | Modifier ID MaybeLRSquare ID MethodSuffix"""
    p[0] = AST.ASTMethodDeclaration(p[1], p[2], p[3], p[4], p[5])

def p_MethodSuffix(p):
    """MethodSuffix : LPAREN MaybeParamList RPAREN MethodBody"""
    p[0] = AST.ASTMethodSuffix(p[1], p[2], p[3], p[4])

def p_Modifier(p):
    """Modifier : PUBLIC
                    | PRIVATE"""
    if p[1] == "public":
        p[0] = "PUBLIC"
    else:
        p[0] = "PRIVATE"
    
def p_MultipleCase(p):
    """MultipleCase : 
                        | Case MultipleCase"""
    if len(p) == 1:
        p[0] = AST.ASTMultipleCase(None)
    else:
        p[0] = AST.ASTMultipleCase(Case=[p[1], p[2]])

def p_MultipleClassDefinition(p):
    """MultipleClassDefinition : 
                                    | ClassDefinition MultipleClassDefinition"""
    if len(p) == 1:
        p[0] = AST.ASTMultipleClassDefinition(None)
    else:
        p[0] = AST.ASTMultipleClassDefinition(ClassDefinition=[p[1], p[2]])

def p_MultipleClassMemberDefinition(p):
    """MultipleClassMemberDefinition : 
                                        | ClassMemberDefinition MultipleClassMemberDefinition"""    
    if len(p) == 1:
        p[0] = AST.ASTMultipleClassMemberDefinition(None)
    else:
        p[0] = AST.ASTMultipleClassMemberDefinition(ClassMemberDefinition=[p[1], p[2]])

def p_MultipleCommaExpression(p):
    """MultipleCommaExpression : 
                                    | COMMA Expression MultipleCommaExpression"""
    if len(p) == 1:
        p[0] = AST.ASTMultipleCommaExpression(None, None, None)
    else:
        p[0] = AST.ASTMultipleCommaExpression(p[1], p[2], p[3])

def p_MultipleCommaParameter(p):
    """MultipleCommaParameter : 
                        | COMMA Parameter MultipleCommaParameter"""
    if len(p) == 1:
        p[0] = AST.ASTMultipleCommaParameter(None, None, None)
    else:
        p[0] = AST.ASTMultipleCommaParameter(p[1], p[2], p[3])

def p_MultipleStatement(p):
    """MultipleStatement :
                            | Statement MultipleStatement"""
    if len(p) == 1:
        p[0] = AST.ASTMultipleStatement(None)
    else:
        p[0] = AST.ASTMultipleStatement(Statement=[p[1], p[2]])

def p_NumOrChar(p):
    """NumOrChar : INT
                    | CHAR"""
    p[0] = p[1]

def p_Parameter(p):
    """Parameter : VOID MaybeLRSquare ID
                    | INT MaybeLRSquare ID
                    | CHAR MaybeLRSquare ID
                    | BOOL MaybeLRSquare ID
                    | STRING MaybeLRSquare ID
                    | ID MaybeLRSquare ID"""
    p[0] = AST.ASTParameter(p[1], p[2], p[3])

def p_ParameterList(p):
    """ParameterList : Parameter MultipleCommaParameter"""
    p[0] = AST.ASTParameterList(p[1], p[2])

def p_Statement(p):
    """Statement : VariableDeclaration
                    | BREAK SEMICOLON
                    | Expression SEMICOLON
                    | LCURLY MultipleStatement RCURLY
                    | RETURN MaybeExpression SEMICOLON
                    | COUT LEFTSHIFT Expression SEMICOLON
                    | CIN RIGHTSHIFT Expression SEMICOLON
                    | WHILE LPAREN Expression RPAREN Statement
                    | SWITCH LPAREN Expression RPAREN CaseBlock
                    | IF LPAREN Expression RPAREN Statement
                    | IF LPAREN Expression RPAREN Statement ELSE Statement"""
    if len(p) == 2:
        p[0] = AST.ASTStatementToVariableDeclaration(p[1])
    elif len(p) == 3 and p[1] == 'break':
        p[0] = AST.ASTStatementBreak(p[1], p[2])
    elif len(p) == 3:
        p[0] = AST.ASTStatementExpression(p[1], p[2])
    elif p[1] == '{':
        p[0] = AST.ASTStatementMultipleStatement(p[1], p[2], p[3])
    elif p[1] == 'return':
        p[0] = AST.ASTStatementReturn(p[1], p[2], p[3])
    elif p[1] == 'cout':
        p[0] = AST.ASTStatementCOUT(p[1], p[2], p[3], p[4])
    elif p[1] == 'cin':
        p[0] = AST.ASTStatementCIN(p[1], p[2], p[3], p[4])
    elif p[1] == 'while':
        p[0] = AST.ASTStatementWhile(p[1], p[2], p[3], p[4], p[5])
    elif p[1] == 'switch':
        p[0] = AST.ASTStatementSwitch(p[1], p[2], p[3], p[4], p[5])
    elif p[1] == 'if' and len(p) == 5:
        p[0] = AST.ASTStatementIF(p[1], p[2], p[3], p[4], p[5])
    else:
        p[0] = AST.ASTStatementIFELSE(p[1], p[2], p[3], p[4], p[5], p[6], p[7])

def p_VariableDeclaration(p):
    """VariableDeclaration : VOID MaybeLRSquare ID MaybeInitializer SEMICOLON
                                | INT MaybeLRSquare ID MaybeInitializer SEMICOLON
                                | CHAR MaybeLRSquare ID MaybeInitializer SEMICOLON
                                | BOOL MaybeLRSquare ID MaybeInitializer SEMICOLON
                                | STRING MaybeLRSquare ID MaybeInitializer SEMICOLON
                                | ID MaybeLRSquare ID MaybeInitializer SEMICOLON"""
    p[0] = AST.ASTVariableDeclaration(p[1], p[2], p[3], p[4], p[5])

def p_error(p):
    if p != None:
        print("Syntax error in input! " + str(p.type) + " / " + str(p.value) + " was given. This is found on line #" + str(p.lineno))
    else:
        print("None Object")

precedence = (
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'PLUS', 'MINUS'),
    ('right', 'RIGHTSHIFT', 'LEFTSHIFT'),
    ('right', 'GREATER', 'LESS', 'LESSEQUAL', 'GREATEQUAL'),
    ('right', 'CEQUAL', 'NEQUAL'),
    ('right', 'NOT'),
    ('right', 'AAND'),
    ('right', 'OOR'),
    ('right', 'EQUAL', 'PLUSEQUAL', 'MINUSEQUAL', 'TIMESEQUAL', 'DIVIDEEQUAL'),
    ('right', 'LCURLY', 'LSQUARE', 'LPAREN'),
)


def Parse(file):
    parser = yacc.yacc(start="CompilationUnit", debug=True)
    # parser.error = p_error
    # parser.error = p_error

    # parser._errok = lambda: errorok() # define errorok
    # parser.productions.append(('error', ('ClassDefiniton',), p_ClassDefinition_error))
    # parser.productions.append(('error', ('Arguments',), p_Arguments_error))
    # parser.productions.append(('error', ('ArgumentList',), p_ArgumentList_error))
    parsed_output = parser.parse(file)
    if parsed_output != None:
        print("parsed")
        print_Visitor = PrintDotVisitor()
        parsed_output.accept(print_Visitor)

    else:
        print("No parsed tree generated")

def ParseDotPrinter(file):
    parser = yacc.yacc(start="CompilationUnit")
    parsed_output = parser.parse(file)
    if parsed_output != None:
        print_Visitor = PrintDotVisitor()
        parsed_output.accept(print_Visitor)
    else:
        print("No parsed tree generated")