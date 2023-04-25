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


 #REGULAR EXPRESSIONS WITH RULES

def t_LRSQUARE(t):
    r'\[ ([ ]||(\\n)|(\\r)|(\n)|(\t)|(\\t)|(//[^\r\n]*))*\]'
    #r'(\[( \n\r\t)*(//[a-zA-Z_ 0-9!#$%&()*+,.-/:;<=>?@[\]^`{\}~\\r\\n\\t\\\\]*)*\])'
    t.value = '[]'
    t.lineno = t.lexer.lineno
    return t

def t_INT(t):
    r'[0-9]+'
    t.value = int(t.value)
    t.lineno = t.lexer.lineno
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    t.lineno = t.lexer.lineno
    return t

def t_CHAR(t):
    r'\'([a-zA-Z_ 0-9!#$%&()*+,\-.-/:|;<=>?@[\]^`{\}~"]|(\\n)|(\\\')|(\\r)|(\\t)|(\\\\))\' '
    t.lineno = t.lexer.lineno
    return t

def t_STRING(t):
    r'\"([a-zA-Z_ 0-9!#$%&()*+,.\-/:;<=>?@[\]^`{\}~]|(\\")|(\\r)|(\\n)|(\\t)|(\\\\))*\"'
    t.lineno = t.lexer.lineno
    return t

def t_ignore_WHITESPACE(t):
    r' [ \t]+'

def t_ignore_NEWLINE(t):
    r'[\n\r]+'
    t.lexer.lineno += len(t.value)

def t_ignore_COMMENTS(t):
    r'//[^\r\n]*'

#LIST OF REGULAR EXPRESSION RULES
def t_CEQUAL(t):
    r'=='
    t.lineno = t.lexer.lineno
    return t

def t_NEQUAL(t):
    r'!='
    t.lineno = t.lexer.lineno
    return t

def t_GREATEQUAL(t):
    r'>='
    t.lineno = t.lexer.lineno
    return t
def t_LESSEQUAL(t): 
    r'<='
    t.lineno = t.lexer.lineno
    return t

def t_AAND(t):
    r'&&'
    t.lineno = t.lexer.lineno
    return t

def t_OOR(t):
    r'\|\|'
    t.lineno = t.lexer.lineno
    return t
 
def t_PLUSEQUAL(t):
    r'\+='
    t.lineno = t.lexer.lineno
    return t
 
def t_MINUSEQUAL(t):
    r'\-='
    t.lineno = t.lexer.lineno
    return t
 
def t_TIMESEQUAL(t):
    r'\*='
    t.lineno = t.lexer.lineno
    return t
 
def t_DIVIDEEQUAL(t):
    r'/='
    t.lineno = t.lexer.lineno
    return t
 
def t_LEFTSHIFT(t):
    r'<<'
    t.lineno = t.lexer.lineno
    return t
 
def t_RIGHTSHIFT(t):
    r'>>'
    t.lineno = t.lexer.lineno
    return t
 
def t_LPAREN (t):
    r'\('
    t.lineno = t.lexer.lineno
    return t

def t_RPAREN(t):
    r'\)'
    t.lineno = t.lexer.lineno
    return t
 
def t_COLON(t):
    r':'
    t.lineno = t.lexer.lineno
    return t
 
def t_SEMICOLON(t):
    r';'
    t.lineno = t.lexer.lineno
    return t
 
def t_LCURLY(t):
    r'{'
    t.lineno = t.lexer.lineno
    return t
 
def t_RCURLY(t):
    r'}'
    t.lineno = t.lexer.lineno
    return t
 
def t_LSQUARE(t):
    r'\['
    t.lineno = t.lexer.lineno
    return t
 
def t_RSQUARE(t):
    r'\]'
    t.lineno = t.lexer.lineno
    return t
 
def t_EQUAL(t):
    r'='
    t.lineno = t.lexer.lineno
    return t
 
def t_NOT(t):
    r'!'
    t.lineno = t.lexer.lineno
    return t
 
def t_GREATER(t):
    r'>'
    t.lineno = t.lexer.lineno
    return t
 
def t_LESS(t):
    r'<'
    t.lineno = t.lexer.lineno
    return t
 
def t_PLUS(t):
    r'\+'
    t.lineno = t.lexer.lineno
    return t
 
def t_MINUS(t):
    r'\-'
    t.lineno = t.lexer.lineno
    return t
 
def t_TIMES(t):
    r'\*'
    t.lineno = t.lexer.lineno
    return t
 
def t_DIVIDE(t):
    r'/'
    t.lineno = t.lexer.lineno
    return t
 
def t_PERIOD(t):
    r'\.'
    t.lineno = t.lexer.lineno
    return t
 
def t_COMMA(t):
    r','
    t.lineno = t.lexer.lineno
    return t
 

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
