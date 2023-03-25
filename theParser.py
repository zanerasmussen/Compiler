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

def print_tree(node, indent=0):
    print(' ' * indent + f'- [{node}]')
    for child in node.children:
        print_tree(child, indent + 2)

# def print_tree(node, indent=0):
#     print(' ' * indent + f'- [{node.type}] {node.leaf}')
#     for child in node.children:
#         print_tree(child, indent + 2)        
          

# GRAMMAR
###########################

def p_Arguments(p):
    """Arguments : LPAREN RPAREN
                    | LPAREN ArgumentList RPAREN"""
    if len(p) == 3:
        p[0] = Node("Arguments", leaf=[p[1], p[2]])
    else:
        p[0] = Node("Arguments", [p[2]], [p[1], p[3]])
    
def p_ArgumentList(p):
    """ArgumentList : Expression ExpressionComma"""
    p[0] = Node("Argument List", [p[1], p[2]])

def p_Case(p):
    """Case :  
                | CASE INT COLON Statement
                | CASE CHAR COLON Statement"""
    if len(p) == 1:
        p[0] = Node("None")
    else:
        p[0] = Node("Case", [p[4]], [p[1], p[2], p[3]])

def p_CaseBlock(p):
    """CaseBlock : LCURLY Case DEFAULT COLON Statement RCURLY"""
    p[0] = Node("Case Block", [p[2], p[5]], [p[1], p[3], p[4], p[6]])

def p_ClassDefinition(p):
    """ClassDefinition : 
                            | CLASS ID LCURLY ClassMemberDefinition RCURLY ClassDefinition
    """
    if len(p) == 1:
        p[0] = Node("None")
    else:
        p[0] = Node("Class Definition", [p[3], p[4], p[5], p[6]], [p[1], p[2]])

def p_ClassMemberDefinition(p):
    """ClassMemberDefinition : 
                                | MethodDeclaration ClassMemberDefinition
                                | DataMemberDeclaration ClassMemberDefinition
                                | ConstructorDeclaration ClassMemberDefinition"""
    if len(p) == 1:
        p[0] = Node("None")
    else:
        p[0] = Node("Class Member Definition", [p[1], p[2]])    

def p_CompilationUnit(p):
    """CompilationUnit : ClassDefinition VOID KXI2023 MAIN LPAREN RPAREN MethodBody"""
    #p[0] = Node("Compilation Unit", [p[1], p[7]], [p[2], p[3], p[4], p[5], p[6]]) #with leaf
    p[0] = Node("Compilation Unit", [p[1], p[7], p[2], p[3], p[4], p[5], p[6]]) #without leaf

def p_ConstructorDeclaration(p):
    """ConstructorDeclaration : ID MethodSuffix"""
    #p[0] = Node("Constructor Declaration", [p[2]], [p[1]])
    p[0] = Node("Constructor Declaration", [p[2], p[1]])

def p_ContinueStatement(p):
    """ContinueStatement : ELSE Statement
                            | """
    if len(p) == 1:
        p[0] = Node("None")
    else:
        p[0] = Node("Continue Statement", [p[2]], [p[1]])

def p_DataMemberDeclaration(p):
    """DataMemberDeclaration : Modifier VariableDeclaration"""
    p[0] = Node("Data Member Declaration", [p[1], p[2]])

def p_Expression(p):
    """Expression : Type
                    | TRUE
                    | FALSE
                    | NULL
                    | THIS
                    | PLUS Expression
                    | NOT Expression
                    | MINUS Expression
                    | Expression Index
                    | Expression Arguments
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
                    | LPAREN Expression RPAREN
                    | NEW Type Arguments
                    | NEW Type Index
                    | Expression PERIOD ID"""
    if len(p) == 2:
        p[0] = Node("Expression", leaf=[p[1]])
    elif len(p) == 3 and ((p[1] == '+') or (p[1] == '!') or (p[1] == '-')):
        p[0] = Node("Expression", [p[2]], [p[1]])
    elif len(p) == 3:
        p[0] = Node("Expression", [p[1], p[2]])
    elif len(p) == 4 and ((p[2] == '=') or (p[2] == '+=') or (p[2] == '-=') or (p[2] == '*=') or (p[2] == '/=') or (p[2] == '+') or (p[2] == '-') or (p[2] == '*') 
                          or (p[2] == '/') or (p[2] == '==') or (p[2] == '!=') or (p[2] == '<') or (p[2] == '>') or (p[2] == '>=') or (p[2] == '<=') or (p[2] == '&&') or (p[2] == '||')):
        p[0] = Node("Expression", [p[1], p[3]], [p[2]])
    elif len(p) == 4 and p[1] == '(':
        p[0] = Node("Expression", [p[2]], [p[1], p[3]])
    elif len(p) == 4 and p[1] == 'new':
        p[0] = Node("Expression", [p[2], p[3]], [p[1]])
    else:
        p[0] = Node("Expression", [p[1]], [p[2], p[3]])

def p_ExpressionComma(p):
    """ExpressionComma : 
                        | COMMA Expression ExpressionComma"""
    if len(p) == 1:
        p[0] = Node("None")
    else:
        p[0] = Node("Expression Comma", [p[2], p[3]], [p[1]])

def p_Index(p):
    """Index : LSQUARE Expression RSQUARE"""
    p[0] = Node("Index", [p[2]], [p[1], p[3]] )

def p_Initializer(p):
    """Initializer : EQUAL Expression"""
    p[0] = Node("Initializer", [p[2]], [p[1]])

def p_MethodBody(p):
    """MethodBody : LCURLY Statement RCURLY"""
    p[0] = Node("Method Body", [p[2]], [p[1], p[3]])

def p_MethodDeclaration(p):
    """MethodDeclaration : Modifier Type LSQUARE RSQUARE ID MethodSuffix
                            | Modifier Type ID MethodSuffix"""
    if len(p) == 7:
        p[0] = Node("Method Declaration", [p[1], p[2], p[6]], [p[3], p[4], p[5]])
    else:
        p[0] = Node("Method Declaration", [p[1], p[2], p[4]], [p[3]])

def p_MethodSuffix(p):
    """MethodSuffix : LPAREN ParameterList RPAREN MethodBody
                        | LPAREN RPAREN MethodBody"""
    if len(p) == 5:
        p[0] = Node("Method Suffix", [p[2], p[4]], [p[1], p[3] ])
    else:
        p[0] = Node("Method Suffix", [p[3] ], [p[1], p[2] ])

def p_Modifier(p):
    """Modifier : PUBLIC
                    | PRIVATE"""
    p[0] = Node("Modifier", leaf=p[1])

def p_Parameter(p):
    """Parameter : Type LSQUARE RSQUARE ID
                    | Type ID"""
    if len(p) == 5:
        p[0] = Node("Parameter", [p[1]], [p[2], p[3], p[4]])
    else:
        p[0] = Node("Parameter", [p[1]], [p[2]])

def p_ParameterComma(p):
    """ParameterComma : 
                        | COMMA Parameter ParameterComma"""
    if len(p) == 1:
        p[0] = Node("None")
    else:
        p[0] = Node("Parameter Comma", [p[2], p[3]], [p[1]])

def p_ParameterList(p):
    """ParameterList : Parameter ParameterComma"""
    p[0] = Node("Parameter List", [p[1], p[2]])

def p_Statement(p):
    """Statement : 
                    | VariableDeclaration Statement
                    | RETURN SEMICOLON Statement
                    | BREAK SEMICOLON Statement
                    | Expression SEMICOLON Statement
                    | RETURN Expression SEMICOLON Statement
                    | LCURLY Statement RCURLY Statement
                    | COUT LEFTSHIFT Expression SEMICOLON Statement
                    | CIN RIGHTSHIFT Expression SEMICOLON Statement
                    | WHILE LPAREN Expression RPAREN Statement
                    | SWITCH LPAREN Expression RPAREN CaseBlock Statement
                    | IF LPAREN Expression RPAREN Statement ContinueStatement Statement"""
    if len(p) == 1:
        p[0] = Node("None")
    elif len(p) == 3:
        p[0] = Node("Statement", [[p[1]], p[2]])
    elif len(p) == 4 and ((p[1] == 'return') or (p[1] == 'break')):
        p[0] = Node("Statement", [p[1]], [p[1], p[2]])
    elif len(p) == 4:
        p[0] = Node("Statement", [p[1], p[3]], [p[2]])
    elif len(p) == 5:
        p[0] = Node("Statement", [p[2], p[4]], [p[1], p[3]])
    elif len(p) == 6:
        p[0] = Node("Statement", [p[3], p[5]], [p[1], p[2], p[4]])

    elif len(p) == 7:
        p[0] = Node("Statement", [p[3], p[5], p[6]], [p[1], p[2], p[4]]) 
    else:
        p[0] = Node("Statement", [p[3], p[5], p[6], p[7]], [p[1], p[2], p[4]]) 

def p_Type(p):
    """Type : VOID
                | INT
                | CHAR
                | BOOL
                | STRING
                | ID"""
    p[0] = Node("Type", p[1])

def p_VariableDeclaration(p):
    """VariableDeclaration : Type ID SEMICOLON
                            | Type ID Initializer SEMICOLON
                            | Type LSQUARE RSQUARE ID SEMICOLON
                            | Type LSQUARE RSQUARE ID Initializer SEMICOLON"""
    if len(p) == 4:
        p[0] = Node("Variable Declaration", [p[1]], [p[2], p[3]])
    elif len(p) == 5:
        p[0] = Node("Variable Declaration", [p[1], p[3]], [p[2], p[4]])
    elif len(p) == 6:
        p[0] = Node("Variable Declaration", [p[1]], [p[2], p[3], p[4], p[5]])
    else:
        p[0] = Node("Variable Declaration", [p[1], p[5]], [p[2], p[3], p[4], p[6]])

def p_error(p):
    print("Syntax error in input! " + p.type + "/ " + p.value + " was given. This is found on line #" + str(p.lineno))

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

def Parse(file):
    parser = yacc.yacc(start="CompilationUnit", debug=True)
    parsed_output = parser.parse(file)
    print_tree(parsed_output)
