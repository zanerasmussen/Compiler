import ply.yacc as yacc
from theLexer import tokens
import pydot

#This class creates the AST. Each node has children, a type and then a unique ID
#The unique ID is to create the pretty printer DOT graph as to not create any cyclical edges
class Node:
    def __init__(self, type, children=None, id=None):
        self.type = type
        self.children = children or []  # ensure that children is always a list
        self.id = id

#This class is to have an 'outside of recursion' type that adds a unique ID to each node with the help of UniqueID. 
class Unique:
    def __init__(self) -> None:
        self.id = 0

    def getID(self):
        self.id += 1
        return self.id

def UniqueID(node, Uid):
    id = Uid.getID()
    node.id = '$' + str(id)
    for child in node.children:
        UniqueID(child, Uid)
    return node        
  
#This function is to help with debugging at first. May not include in the final project
def print_tree(node, indent=0):
    print(' ' * indent + f'- [{node.type}]')
    for child in node.children:
        print_tree(child, indent + 2)


#The next few methods are for the DOT graph. It calls to functions such as 'add_nodes', 'add_edges' and 'add_leafs'
def pydot_printer(graph, node, first):
    if len(node.children) != 0:
        graph = add_nodes(graph, node)
        if first == True:
            first = False 
            start = pydot.Node('Start$0', shape='diamond', style='filled', fillcolor='cyan')
            graph.add_node(start)
            edge = pydot.Edge("Start$0", node.type+node.id)
            graph.add_edge(edge)
    else:
        graph = add_leafs(graph, node)

    for child in node.children:
        pydot_printer(graph, child, first)
        add_edges(graph, node, child)
    return graph

def add_nodes(graph, node):
    x = pydot.Node(node.type+node.id, style="filled", fillcolor="#47E21A")
    graph.add_node(x)
    return graph

def add_leafs(graph, node):
    x = pydot.Node(str(node.type)+node.id, shape='octagon', style="filled", fillcolor="#F62020")
    graph.add_node(x)
    return graph

def add_edges(graph, parent, child):
    edge = pydot.Edge(str(parent.type)+parent.id, str(child.type)+child.id)
    graph.add_edge(edge)
    return graph




     

# GRAMMAR
###########################

def p_Arguments(p):
    """Arguments : LPAREN RPAREN
                    | LPAREN ArgumentList RPAREN"""
    if len(p) == 3:
        p[0] = Node("Arguments", children=[Node(p[1]), Node(p[2])])
    else:
        p[0] = Node("Arguments", children=[Node(p[1]), p[2], Node(p[3])])
    
def p_ArgumentList(p):
    """ArgumentList : Expression ExpressionComma"""
    p[0] = Node("Argument List", children=[p[1], p[2]])

def p_Case(p):
    """Case :  
                | CASE INT COLON Statement
                | CASE CHAR COLON Statement"""
    if len(p) == 1:
        p[0] = Node("None")
    else:
        p[0] = Node("Case", children=[Node(p[1]), Node(p[2]), Node(p[3]), p[4]])

def p_CaseBlock(p):
    """CaseBlock : LCURLY Case DEFAULT COLON Statement RCURLY"""
    p[0] = Node("Case Block", children=[Node(p[1]), p[2], Node(p[3]), Node(p[4]), p[5], Node(p[6])])


def p_ClassDefinition(p):
    """ClassDefinition : 
                            | CLASS ID LCURLY ClassMemberDefinition RCURLY ClassDefinition
    """
    if len(p) == 1:
        p[0] = Node("None")
    else:
        p[0] = Node("Class Definition", children=[Node(p[1]), Node(p[2]), Node(p[3]), p[4], Node(p[5]), p[6]])

# def p_ClassDefinition_error(p):
#     """ClassDefinition : error ID LCURLY ClassMemberDefinition RCURLY ClassDefinition"""
#     if p[1] == "error":
#         print("Syntax error: Expected CLASS")

def p_ClassMemberDefinition(p):
    """ClassMemberDefinition : 
                                | MethodDeclaration ClassMemberDefinition
                                | DataMemberDeclaration ClassMemberDefinition
                                | ConstructorDeclaration ClassMemberDefinition"""
    if len(p) == 1:
        p[0] = Node("None")
    else:
        p[0] = Node("Class Member Definition", children=[p[1], p[2]])   

def p_CompilationUnit(p):
    """CompilationUnit : ClassDefinition VOID KXI2023 MAIN LPAREN RPAREN MethodBody"""
    p[0] = Node("Compilation Unit", children=[p[1], Node(p[2]), Node(p[3]), Node(p[4]), Node(p[5]), Node(p[6]), p[7]])

# def p_CompilationUnit_error(p):
#     """CompilationUnit : error VOID KXI2023 MAIN LPAREN RPAREN MethodBody
#                         | ClassDefinition error KXI2023 MAIN LPAREN RPAREN MethodBody"""
#     print(p[1])
#     if p[1] == "error":
#         print("Syntax error with compilationUnit. Expected a Compilation Unit Grammar Rule")
#     elif p[2] == "error":
#         print("Syntax error: Expected VOID")

def p_ConstructorDeclaration(p):
    """ConstructorDeclaration : ID MethodSuffix"""
    p[0] = Node("Constructor Declaration", children=[Node(p[1]), p[2]])

def p_ContinueStatement(p):
    """ContinueStatement : ELSE Statement
                            | """
    if len(p) == 1:
        p[0] = Node("None")
    else:
        p[0] = Node("Continue Statement", children=[Node(p[1]), p[2]])

def p_DataMemberDeclaration(p):
    """DataMemberDeclaration : Modifier VariableDeclaration"""
    p[0] = Node("Data Member Declaration", children=[p[1], p[2]])

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
    if len(p) == 2 and ((p[1] == 'true') or (p[1] == 'false') or (p[1] == 'null') or (p[1] == 'this')):
        p[0] = Node("Expression", children=[Node(p[1])])
    elif len(p) == 2:
        p[0] = Node("Expression", children=[p[1]])
    elif len(p) == 3 and ((p[1] == '+') or (p[1] == '!') or (p[1] == '-')):
        p[0] = Node("Expression", children=[Node(p[1]), p[2]])
    elif len(p) == 3:
        p[0] = Node("Expression", children=[p[1], p[2]])
    elif len(p) == 4 and ((p[2] == '=') or (p[2] == '+=') or (p[2] == '-=') or (p[2] == '*=') or (p[2] == '/=') or (p[2] == '+') or (p[2] == '-') or (p[2] == '*') 
                          or (p[2] == '/') or (p[2] == '==') or (p[2] == '!=') or (p[2] == '<') or (p[2] == '>') or (p[2] == '>=') or (p[2] == '<=') or (p[2] == '&&') or (p[2] == '||')):
        p[0] = Node("Expression", children=[p[1], Node(p[2]), p[3]])
    elif len(p) == 4 and p[1] == '(':
        p[0] = Node("Expression", children=[Node(p[1]), p[2], Node(p[3])])
    elif len(p) == 4 and p[1] == 'new':
        p[0] = Node("Expression", children=[Node(p[1]), p[2], p[3]])
    else:
        p[0] = Node("Expression", children=[p[1], Node(p[2]), Node(p[3])])

def p_ExpressionComma(p):
    """ExpressionComma : 
                        | COMMA Expression ExpressionComma"""
    if len(p) == 1:
        p[0] = Node("None")
    else:
        p[0] = Node("Expression Comma", children=[Node(p[1]), p[2], p[3]])

def p_Index(p):
    """Index : LSQUARE Expression RSQUARE"""
    p[0] = Node("Index", children=[Node(p[1]), p[2], Node(p[3])])

def p_Initializer(p):
    """Initializer : EQUAL Expression"""
    p[0] = Node("Initializer", children=[Node(p[1]), p[2]])

def p_MethodBody(p):
    """MethodBody : LCURLY Statement RCURLY"""
    p[0] = Node("Method Body", children=[Node(p[1]), p[2], Node(p[3])])

def p_MethodDeclaration(p):
    """MethodDeclaration : Modifier Type LSQUARE RSQUARE ID MethodSuffix
                            | Modifier Type ID MethodSuffix"""
    if len(p) == 7:
        p[0] = Node("Method Declaration", children=[p[1], p[2], Node(p[3]), Node(p[4]), Node(p[5]), p[6]])
    else:
        p[0] = Node("Method Declaration", children=[p[1], p[2], Node(p[3]), p[4]])

def p_MethodSuffix(p):
    """MethodSuffix : LPAREN ParameterList RPAREN MethodBody
                        | LPAREN RPAREN MethodBody"""
    if len(p) == 5:
        p[0] = Node("Method Suffix", children=[Node(p[1]), p[2], Node(p[3]), p[4]])
    else:
        p[0] = Node("Method Suffix", children=[Node(p[1]), Node(p[2]), p[3]])

def p_Modifier(p):
    """Modifier : PUBLIC
                    | PRIVATE"""
    p[0] = Node("Modifier", children=[Node(p[1])])

def p_Parameter(p):
    """Parameter : Type LSQUARE RSQUARE ID
                    | Type ID"""
    if len(p) == 5:
        p[0] = Node("Parameter", children=[p[1], Node(p[2]), Node(p[3]), Node(p[4])])
    else:
        p[0] = Node("Parameter", children=[p[1], Node(p[2])])

def p_ParameterComma(p):
    """ParameterComma : 
                        | COMMA Parameter ParameterComma"""
    if len(p) == 1:
        p[0] = Node("None")
    else:
        p[0] = Node("Parameter Comma", children=[Node(p[1]), p[2], p[3]])

def p_ParameterList(p):
    """ParameterList : Parameter ParameterComma"""
    p[0] = Node("Parameter List", children=[p[1], p[2]])

def p_Statement(p):
    """Statement : 
                    | VariableDeclaration
                    | RETURN SEMICOLON 
                    | BREAK SEMICOLON 
                    | Expression SEMICOLON 
                    | RETURN Expression SEMICOLON 
                    | LCURLY Statement RCURLY 
                    | COUT LEFTSHIFT Expression SEMICOLON 
                    | CIN RIGHTSHIFT Expression SEMICOLON 
                    | WHILE LPAREN Expression RPAREN 
                    | SWITCH LPAREN Expression RPAREN CaseBlock 
                    | IF LPAREN Expression RPAREN Statement ContinueStatement """
    if len(p) == 1:
        p[0] = Node("None")
    elif len(p) == 2:
        p[0] = Node("Statement", children=[p[1]])
    elif len(p) == 3 and ((p[1] == 'return') or (p[1] == 'break')):
        p[0] = Node("Statement", children=[Node(p[1]), Node(p[2])])
    elif len(p) == 4:
        p[0] = Node("Statement", children=[p[1], Node(p[2])])
    elif len(p) == 5:
        p[0] = Node("Statement", children=[Node(p[1]), p[2], Node(p[3])])
    elif len(p) == 6:
        p[0] = Node("Statement", children=[Node(p[1]), Node(p[2]), p[3], Node(p[4])])
    elif len(p) == 7:
        p[0] = Node("Statement", children=[Node(p[1]), Node(p[2]), p[3], Node(p[4]), p[5]])
    else:
        p[0] = Node("Statement", children=[Node(p[1]), Node(p[2]), p[3], Node(p[4]), p[5], p[6]])

def p_Type(p):
    """Type : VOID
                | INT
                | CHAR
                | BOOL
                | STRING
                | ID"""
    p[0] = Node("Type", children=[Node(p[1])])

def p_VariableDeclaration(p):
    """VariableDeclaration : Type ID SEMICOLON
                            | Type ID Initializer SEMICOLON
                            | Type LSQUARE RSQUARE ID SEMICOLON
                            | Type LSQUARE RSQUARE ID Initializer SEMICOLON"""
    if len(p) == 4:
        p[0] = Node("Variable Declaration", children=[p[1], Node(p[2]), Node(p[3])])
    elif len(p) == 5:
        p[0] = Node("Variable Declaration", children=[p[1], Node(p[2]), p[3], Node(p[4])])
    elif len(p) == 6:
        p[0] = Node("Variable Declaration", children=[p[1], Node(p[2]), Node(p[3]), Node(p[4]), Node(p[5])])
    else:
        p[0] = Node("Variable Declaration", children=[p[1], Node(p[2]), Node(p[3]), Node(p[4]), p[5], Node(p[6])])

def p_error(p):
    print("Syntax error in input! " + p.type + " / " + p.value + " was given. This is found on line #" + str(p.lineno))

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
    if parsed_output != None:
        #print_tree(parsed_output)
        parsed_output1 = parsed_output
        Uid = Unique()
        parsed_output1= UniqueID(parsed_output1, Uid)

        graph = pydot.Dot('my_graph', graph_type='graph')
        first = True
        graph = pydot_printer(graph, parsed_output1, first)
        graph.write_png('output.png')
    else:
        print("No parsed tree generated")



    # pydot_Graph = pydot_printer(pydot_Graph, parsed_output)
