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
    'this' : 'THIS',
    'true' : 'TRUE', 
    'void' : 'VOID', 
    'while' : 'WHILE',
}

tokens = (
    'COLON', 
    'SEMICOLON', 
    'LCURLY',
    'RCURLY', 
    'LPAREN', 
    'RPAREN', 
    'LSQUARE', 
    'RSQUARE', 
    'EQUAL', 
    'CEQUAL', 
    'NEQUAL', 
    'GREATEQUAL', 
    'LESSEQUAL',
    'GREATER', 
    'LESS', 
    'AAND', 
    'OOR', 
    'NOT', 
    'PLUS', 
    'MINUS', 
    'TIMES', 
    'DIVIDE', 
    'PLUSEQUAL', 
    'MINUSEQUAL', 
    'TIMESEQUAL', 
    'DIVIDEEQUAL', 
    'LEFTSHIFT', 
    'RIGHTSHIFT',
    'PERIOD', 
    'COMMA',
    'INT', 
    'ID', 
    'CHAR',
    'STRING', 
    'UNKONWN', 
    'BOOL',
    'BREAK',
    'CASE',
    'CLASS',
    'CIN',
    'COUT', 
    'DEFAULT', 
    'ELSE', 
    'FALSE', 
    'IF', 
    'KXI2023',
    'NEW',
    'NULL', 
    'PUBLIC', 
    'PRIVATE', 
    'RETURN', 
    'SWITCH', 
    'THIS',
    'TRUE', 
    'VOID', 
    'WHILE',
    'LRSQUARE'
)

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
t_LSQUARE = r'\['
t_RSQUARE = r'\]'
t_EQUAL = r'='
t_NOT = r'!'
t_GREATER = r'>'
t_LESS = r'<'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_PERIOD = r'\.'
t_COMMA = r','

 #REGULAR EXPRESSIONS WITH RULES

def t_LRSQUARE(t):
    r'\[ ([ ]||(\\n)|(\\r)|(\n)|(\t)|(\\t)|(//[^\r\n]*))*\]'
    #r'(\[( \n\r\t)*(//[a-zA-Z_ 0-9!#$%&()*+,.-/:;<=>?@[\]^`{\}~\\r\\n\\t\\\\]*)*\])'
    t.value = '[]'
    return t

def t_INT(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

def t_CHAR(t):
    r'\'([a-zA-Z_ 0-9!#$%&()*+,\-.-/:|;<=>?@[\]^`{\}~"]|(\\n)|(\\\')|(\\r)|(\\t)|(\\\\))\' '
    return t

def t_STRING(t):
    r'\"([a-zA-Z_ 0-9!#$%&()*+,.\-/:;<=>?@[\]^`{\}~]|(\\")|(\\r)|(\\n)|(\\t)|(\\\\))*\"'
    return t

def t_ignore_WHITESPACE(t):
    r' [ \t]+'

def t_ignore_NEWLINE(t):
    r'[\n\r]+'
    t.lexer.lineno += len(t.value)

def t_ignore_COMMENTS(t):
    r'//[^\r\n]*'


def t_error(t):
    t.type = 'UNKNOWN'
    t.value = t.value[0]
    x = t.lexer.skip(1)
    return t

def t_eof(t):
    return None

def theLexerReturnFucntion(stuff):
    import ply.lex as lex
    lexer = lex.lex()
    lexer.input(stuff)
    return lexer

def theLexerPrintFunction(stuff):
    import ply.lex as lex
    lexer = lex.lex()
    lexer.input(stuff)
    clone = lexer
    print('{:15}'.format('TAG'), '{:<10}'.format("Line #"), 'LEXEME')
    print('{:-<35}'.format('-'))

    while True:
        tok = clone.token()
        if not tok: 
            break       # No more input
        print('{:<15}'.format(tok.type), '{:<10}'.format(tok.lineno), tok.value)

    return lexer

def theLexerTester(stuff):
    import ply.lex as lex
    lexer = lex.lex()
    lexer.input(stuff)
    tok = lexer.token()
    return tok

def tokenChecker(stuff):
    import sys
    clone = stuff
    while True:
        tok = clone.token()
        if not tok:
            break
        elif tok.type == 'UNKNOWN':
            print("Unknown token " + str(tok.value) + " reached on line #" + str(tok.lineno))
            print("Caution when parsing with unknown tokens")
