import ply.yacc as yacc
from theLexer import tokens


class Node:
    def __init__(self,type,children=None,leaf=None):
         self.type = type
         if children:
              self.children = children
         else:
              self.children = [ ]
         self.leaf = leaf
# GRAMMAR
###########################
def p_CompilationUnit(p):
    """CompilationUnit : ClassDefinition VOID KXI2023 MAIN LPAREN RPAREN MethodBody"""

def p_ClassDefinition(p):
    """ClassDefinition : 
                            | CLASS ID LCURLY ClassMemberDefinition RCURLY ClassDefinition
    """
    
def p_Type(p):
    """Type : VOID
                | INT
                | CHAR
                | BOOL
                | STRING
                | ID"""
    
def p_Modifier(p):
    """Modifier : PUBLIC
                    | PRIVATE"""
    
def p_ClassMemberDefinition(p):
    """ClassMemberDefinition : 
                                | MethodDeclaration ClassMemberDefinition
                                | DataMemberDeclaration ClassMemberDefinition
                                | ConstructorDeclaration ClassMemberDefinition"""

def p_DataMemberDeclaration(p):
    """DataMemberDeclaration : Modifier VariableDeclaration"""

def p_MethodDeclaration(p):
    """MethodDeclaration : Modifier Type LSQUARE RSQUARE ID MethodSuffix
                            | Modifier Type ID MethodSuffix"""
    
def p_ConstructorDeclaration(p):
    """ConstructorDeclaration : ID MethodSuffix"""

def p_Initializer(p):
    """Initializer : Expression"""

def p_MethodSuffix(p):
    """MethodSuffix : LPAREN ParameterList RPAREN MethodBody
                        | LPAREN RPAREN MethodBody"""

def p_MethodBody(p):
    """MethodBody : LCURLY Statement RCURLY"""

def p_ParameterList(p):
    """ParameterList : Parameter ParameterComma"""

def p_ParameterComma(p):
    """ParameterComma : 
                        | COMMA Parameter ParameterComma"""

def p_Parameter(p):
    """Parameter : Type LSQUARE RSQUARE ID
                    | Type ID"""

def p_VariableDeclaration(p):
    """VariableDeclaration : Type LSQUARE RSQUARE ID Initializer SEMICOLON
                            | Type ID Initializer SEMICOLON
                            | Type LSQUARE RSQUARE ID SEMICOLON
                            | Type ID SEMICOLON"""

def p_Statement(p):
    """Statement : 
                    | LCURLY Statement RCURLY
                    | Expression SEMICOLON
                    | IF LPAREN Expression RPAREN Statement ELSE Statement
                    | IF LPAREN Expression RPAREN Statement
                    | WHILE LPAREN Expression RPAREN Statement
                    | RETURN Expression SEMICOLON
                    | RETURN SEMICOLON
                    | COUT LEFTSHIFT Expression SEMICOLON
                    | CIN RIGHTSHIFT Expression SEMICOLON
                    | SWITCH LPAREN Expression RPAREN CaseBlock
                    | BREAK SEMICOLON
                    | VariableDeclaration"""
    
def p_CaseBlock(p):
    """CaseBlock : LCURLY Case DEFAULT COLON Statement RCURLY"""

def p_Case(p):
    """Case :  
                | CASE INT COLON Statement
                | CASE CHAR COLON Statement"""
    
def p_Expression(p):
    """Expression : LPAREN Expression RPAREN
                    | Expression EQUAL Expression
                    | Expression PLUSEQUAL Expression
                    | Expression MINUSEQUAL Expression
                    | Expression TIMESEQUAL Expression
                    | Expression DIVIDEEQUAL Expression
                    | Expression PLUS Expression
                    | Expression MINUS Expression
                    | Expression TIMES Expression
                    | Expression DIVIDE Expression
                    | Expression CEQUAL Expression
                    | Expression NEQUAL Expression
                    | Expression LESS Expression
                    | Expression GREATER Expression
                    | Expression GREATEQUAL Expression
                    | Expression LESSEQUAL Expression
                    | Expression AAND Expression
                    | Expression OOR Expression
                    | NOT Expression
                    | PLUS Expression
                    | MINUS Expression
                    | INT
                    | CHAR
                    | STRING
                    | TRUE
                    | FALSE
                    | NULL
                    | ID
                    | NEW Type Arguments
                    | NEW Type Index
                    | THIS
                    | Expression PERIOD ID
                    | Expression Index
                    | Expression Arguments"""
    
def p_Arguments(p):
    """Arguments : LPAREN RPAREN
                    | LPAREN ArgumentList RPAREN"""
    
def p_ArgumentList(p):
    """ArgumentList : Expression ExpressionComma"""

def p_ExpressionComma(p):
    """ExpressionComma : 
                        | COMMA Expression ExpressionComma"""
    
def p_Index(p):
    """Index : LSQUARE Expression RSQUARE"""

def p_error(p):
    print("Syntax error in input!")

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
)

def Parse(lex):
    parser = yacc.yacc(start="CompilationUnit", debug=True, tracking=True)

    # import ast
    # import pprint

    # tree = ast.parse(parser)
    # pprint.pprint(ast.dump(tree, indent=4))
    # print(parser)
