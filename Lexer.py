reserved = {
    'bool' : 'BOOL',
    'break' : 'BREAK',
    'case' : 'CASE',
    'class' : 'CLASS',
    'cin' : 'CIN',
    'cout' : 'COUT', 
    'default' : 'DEFAULT', 
    'else' : 'ELSE', 
    'false' : 'FALSE', 
    'if' : 'IF', 
    'kxi2023' : 'KXI2023',
    'new' : 'NEW',
    'null' : 'NULL', 
    'public' : 'PUBLIC', 
    'private' : 'PRIVATE', 
    'return' : 'RETURN', 
    'switch' :  'SWITCH', 
    'true' : 'TRUE', 
    'void' : 'VOID', 
    'while' : 'WHILE',
}

tokens = [
    'COLON', 'SEMICOLON', 'LCURLY', 'RCURLY', 'LPAREN', 'RPAREN', 'LSQUARE', 'RSQUARE', 'EQUAL', 'CEQUAL', 'NEQUAL', 'GREATEQUAL', 'LESSEQUAL',
    'GREATER', 'LESS', 'AAND', 'OOR', 'NOT', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'PLUSEQUAL', 'MINUSEQUAL', 'TIMESEQUAL', 'DIVIDEEQUAL', 'LEFTSHIFT', 'RIGHTSHIFT',
    'PERIOD', 'COMMA',
    'INT', 'ID',
#    'CHAR','STRING',
#    'UNKONWN', 'WHITESPACE', 'COMMENTS', 'NEWLINE',
] + list(reserved.values())

#LIST OF REGULAR EXPRESSION RULES
t_CEQUAL = r'=='
t_NEQUAL = r'!='
t_GREATEQUAL = r'>='
t_LESSEQUAL = r'<='
t_AAND = r'&&'
t_OOR = r'\|\|'   
t_PLUSEQUAL = r'\+='
t_MINUSEQUAL = r'\-='
t_TIMESEQUAL = r'\*='
t_DIVIDEEQUAL = r'/='
t_LEFTSHIFT = r'<<'
t_RIGHTSHIFT = r'>>'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_COLON = r':'
t_SEMICOLON = r';'
t_LCURLY = r'{'
t_RCURLY = r'}'
t_LSQUARE = r'['
t_RSQUARE = r']'
t_EQUAL = r'='
t_NOT = r'!'
t_GREATER = r'>'
t_LESS = r'<'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_PERIOD = r'.'
t_COMMA = r','

 #REGULAR EXPRESSIONS WITH RULES

def t_INT(t):
    r'\d+'
    t.value = int(t.value)    
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

def t_CHAR(t):
    r'[a-zA-Z_]'
    return t