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

tokens = [
    'COLON', 'SEMICOLON', 'LCURLY', 'RCURLY', 'LPAREN', 'RPAREN', 'LSQUARE', 'RSQUARE', 'EQUAL', 'CEQUAL', 'NEQUAL', 'GREATEQUAL', 'LESSEQUAL',
    'GREATER', 'LESS', 'AAND', 'OOR', 'NOT', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'PLUSEQUAL', 'MINUSEQUAL', 'TIMESEQUAL', 'DIVIDEEQUAL', 'LEFTSHIFT', 'RIGHTSHIFT',
    'PERIOD', 'COMMA',
    'INT', 'ID', 'CHAR','STRING', 'LINEENDING', 'WHITESPACE', 'COMMENTS', 
    'UNKONWN', 
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

def t_INT(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t


#note there is not _ in ID
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

def t_CHAR(t):
    r'\'[a-zA-Z_ !#$%&()*+,.-/:;<=>?@[\]^`{\}~]\''
    return t

def t_STRING(t):
    r'"[a-zA-Z_ 0-9][a-zA-Z_ 0-9]*"'
    return t

def t_WHITESPACE(t):
    r' [ \t]+ '

def t_NEWLINE(t):
    r'[\n\r]+'
    t.lexer.lineno += len(t.value)

def t_COMMENTS(t):
    r'//[^\r\n]*'
    return t

def t_error(t):
    t.type = 'UNKNOWN'
    t.value = t.value[0]
    x = t.lexer.skip(1)
    return t


# Test it out
data = '''
bool
break
case
class
cin
cout
default
else
false
if
kxi2023
new
null
public
private
return
switch
this
true
void
while
ifelse
classes
//'bool'    //Unknown
"bool"
BOOL
IF
:
;
{
}
()
[] 
= 
== 
!= 
<=
>=
> <
&& ||
!   'r'
+-*/
+= -= *= /=
<< >>
. ,

123
5555
1513513515313513599999999
"123"

ThisIsId
ThisIs__ID
'test'
't'
'!'
'"'
'$4'


'''




import ply.lex as lex
lexer = lex.lex()

 
# Give the lexer some input
lexer.input(data)
 
print('{:15}'.format('TAG'), '{:<10}'.format("Line #"), 'LEXEME')
print('{:-<35}'.format('-'))
# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print('{:<15}'.format(tok.type), '{:<10}'.format(tok.lineno), tok.value)