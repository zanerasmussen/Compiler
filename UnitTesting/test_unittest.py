import unittest
import theLexer

class Test_Lexer(unittest.TestCase):

#base case examples. One for each token type
    def test_bool(self):
        tok = theLexer.theLexerTester('''bool''')
        self.assertEqual(tok.type, "BOOL" )
        self.assertEqual(tok.value, 'bool')

    def test_break(self):
        tok = theLexer.theLexerTester('''break''')
        self.assertEqual(tok.type, "BREAK" )
        self.assertEqual(tok.value, 'break')

    def test_case(self):
        tok = theLexer.theLexerTester('''case''')
        self.assertEqual(tok.type, "CASE" )
        self.assertEqual(tok.value, 'case')

    def test_class(self):
        tok = theLexer.theLexerTester('''class''')
        self.assertEqual(tok.type, "CLASS" )
        self.assertEqual(tok.value, 'class') 

    def test_cin(self):
        tok = theLexer.theLexerTester('''cin''')
        self.assertEqual(tok.type, "CIN" )
        self.assertEqual(tok.value, 'cin')

    def test_cout(self):
        tok = theLexer.theLexerTester('''cout''')
        self.assertEqual(tok.type, "COUT" )
        self.assertEqual(tok.value, 'cout')

    def test_default(self):
        tok = theLexer.theLexerTester('''default''')
        self.assertEqual(tok.type, "DEFAULT" )
        self.assertEqual(tok.value, 'default') 

    def test_else(self):
        tok = theLexer.theLexerTester('''else''')
        self.assertEqual(tok.type, "ELSE" )
        self.assertEqual(tok.value, 'else')

    def test_false(self):
        tok = theLexer.theLexerTester('''false''')
        self.assertEqual(tok.type, "FALSE" )
        self.assertEqual(tok.value, 'false')

    def test_if(self):
        tok = theLexer.theLexerTester('''if''')
        self.assertEqual(tok.type, "IF" )
        self.assertEqual(tok.value, 'if') 

    def test_kxi2023(self):
        tok = theLexer.theLexerTester('''kxi2023''')
        self.assertEqual(tok.type, "KXI2023" )
        self.assertEqual(tok.value, 'kxi2023')

    def test_new(self):
        tok = theLexer.theLexerTester('''new''')
        self.assertEqual(tok.type, "NEW" )
        self.assertEqual(tok.value, 'new')

    def test_null(self):
        tok = theLexer.theLexerTester('''null''')
        self.assertEqual(tok.type, "NULL" )
        self.assertEqual(tok.value, 'null') 

    def test_public(self):
        tok = theLexer.theLexerTester('''public''')
        self.assertEqual(tok.type, "PUBLIC" )
        self.assertEqual(tok.value, 'public')

    def test_private(self):
        tok = theLexer.theLexerTester('''private''')
        self.assertEqual(tok.type, "PRIVATE" )
        self.assertEqual(tok.value, 'private')

    def test_return(self):
        tok = theLexer.theLexerTester('''return''')
        self.assertEqual(tok.type, "RETURN" )
        self.assertEqual(tok.value, 'return') 

    def test_switch(self):
        tok = theLexer.theLexerTester('''switch''')
        self.assertEqual(tok.type, "SWITCH" )
        self.assertEqual(tok.value, 'switch')

    def test_this(self):
        tok = theLexer.theLexerTester('''this''')
        self.assertEqual(tok.type, "THIS" )
        self.assertEqual(tok.value, 'this')

    def test_true(self):
        tok = theLexer.theLexerTester('''true''')
        self.assertEqual(tok.type, "TRUE" )
        self.assertEqual(tok.value, 'true') 

    def test_void(self):
        tok = theLexer.theLexerTester('''void''')
        self.assertEqual(tok.type, "VOID" )
        self.assertEqual(tok.value, 'void')

    def test_while(self):
        tok = theLexer.theLexerTester('''while''')
        self.assertEqual(tok.type, "WHILE" )
        self.assertEqual(tok.value, 'while')             

    def test_colon(self):
        tok = theLexer.theLexerTester(''':''')
        self.assertEqual(tok.type, "COLON" )
        self.assertEqual(tok.value, ':')

    def test_semicolon(self):
        tok = theLexer.theLexerTester(''';''')
        self.assertEqual(tok.type, "SEMICOLON" )
        self.assertEqual(tok.value, ';')

    def test_lcurly(self):
        tok = theLexer.theLexerTester('''{''')
        self.assertEqual(tok.type, "LCURLY" )
        self.assertEqual(tok.value, '{')

    def test_rcurly(self):
        tok = theLexer.theLexerTester('''}''')
        self.assertEqual(tok.type, "RCURLY" )
        self.assertEqual(tok.value, '}')

    def test_lparen(self):
        tok = theLexer.theLexerTester('''(''')
        self.assertEqual(tok.type, "LPAREN" )
        self.assertEqual(tok.value, '(')

    def test_rparen(self):
        tok = theLexer.theLexerTester(''')''')
        self.assertEqual(tok.type, "RPAREN" )
        self.assertEqual(tok.value, ')')

    def test_lsquare(self):
        tok = theLexer.theLexerTester('''[''')
        self.assertEqual(tok.type, "LSQUARE" )
        self.assertEqual(tok.value, '[')

    def test_rsquare(self):
        tok = theLexer.theLexerTester(''']''')
        self.assertEqual(tok.type, "RSQUARE" )
        self.assertEqual(tok.value, ']')

    def test_equal(self):
        tok = theLexer.theLexerTester('''=''')
        self.assertEqual(tok.type, "EQUAL" )
        self.assertEqual(tok.value, '=')

    def test_nequal(self):
        tok = theLexer.theLexerTester('''!=''')
        self.assertEqual(tok.type, "NEQUAL" )
        self.assertEqual(tok.value, '!=')        

    def test_greatequal(self):
        tok = theLexer.theLexerTester('''>=''')
        self.assertEqual(tok.type, "GREATEQUAL" )
        self.assertEqual(tok.value, '>=')

    def test_lessequal(self):
        tok = theLexer.theLexerTester('''<=''')
        self.assertEqual(tok.type, "LESSEQUAL" )
        self.assertEqual(tok.value, '<=')

    def test_greater(self):
        tok = theLexer.theLexerTester('''>''')
        self.assertEqual(tok.type, "GREATER" )
        self.assertEqual(tok.value, '>')  

    def test_less(self):
        tok = theLexer.theLexerTester('''<''')
        self.assertEqual(tok.type, "LESS" )
        self.assertEqual(tok.value, '<')   

    def test_aand(self):
        tok = theLexer.theLexerTester('''&&''')
        self.assertEqual(tok.type, "AAND" )
        self.assertEqual(tok.value, '&&')   

    def test_oor(self):
        tok = theLexer.theLexerTester('''||''')
        self.assertEqual(tok.type, "OOR" )
        self.assertEqual(tok.value, '||')  

    def test_not(self):
        tok = theLexer.theLexerTester('''!''')
        self.assertEqual(tok.type, "NOT" )
        self.assertEqual(tok.value, '!')   

    def test_minus(self):
        tok = theLexer.theLexerTester('''-''')
        self.assertEqual(tok.type, "MINUS" )
        self.assertEqual(tok.value, '-')   

    def test_plus(self):
        tok = theLexer.theLexerTester('''+''')
        self.assertEqual(tok.type, "PLUS" )
        self.assertEqual(tok.value, '+')  

    def test_times(self):
        tok = theLexer.theLexerTester('''*''')
        self.assertEqual(tok.type, "TIMES" )
        self.assertEqual(tok.value, '*')   

    def test_divide(self):
        tok = theLexer.theLexerTester('''/''')
        self.assertEqual(tok.type, "DIVIDE" )
        self.assertEqual(tok.value, '/')   

    def test_plusequal(self):
        tok = theLexer.theLexerTester('''+=''')
        self.assertEqual(tok.type, "PLUSEQUAL" )
        self.assertEqual(tok.value, '+=')  

    def test_minusequal(self):
        tok = theLexer.theLexerTester('''-=''')
        self.assertEqual(tok.type, "MINUSEQUAL" )
        self.assertEqual(tok.value, '-=')   

    def test_timesequal(self):
        tok = theLexer.theLexerTester('''*=''')
        self.assertEqual(tok.type, "TIMESEQUAL" )
        self.assertEqual(tok.value, '*=')   

    def test_divideequal(self):
        tok = theLexer.theLexerTester('''/=''')
        self.assertEqual(tok.type, "DIVIDEEQUAL" )
        self.assertEqual(tok.value, '/=')  

    def test_leftshift(self):
        tok = theLexer.theLexerTester('''<<''')
        self.assertEqual(tok.type, "LEFTSHIFT" )
        self.assertEqual(tok.value, '<<')   

    def test_rightshift(self):
        tok = theLexer.theLexerTester('''>>''')
        self.assertEqual(tok.type, "RIGHTSHIFT" )
        self.assertEqual(tok.value, '>>')     

    def test_int(self):
        tok = theLexer.theLexerTester('''123455''')
        self.assertEqual(tok.type, "INT")
        self.assertEqual(tok.value, 123455)      

    def test_id(self):
        tok = theLexer.theLexerTester('''ThisIsID_A__''')
        self.assertEqual(tok.type, "ID")
        self.assertEqual(tok.value, 'ThisIsID_A__')    

    def test_char(self):
        tok = theLexer.theLexerTester(''' 't' ''')
        self.assertEqual(tok.type, "CHAR")
        self.assertEqual(tok.value, "'t'")              

    def test_string(self):
        tok = theLexer.theLexerTester(''' "This whole thing is a striung #$#@#$__" ''')
        self.assertEqual(tok.type, "STRING")
        self.assertEqual(tok.value, '"This whole thing is a striung #$#@#$__"')     

    def test_lineending(self):
        tok = theLexer.theLexerTester('''


        ''')
        self.assertEqual(tok, None)

    def test_whitespace(self):
        tok = theLexer.theLexerTester('''   ''')
        self.assertEqual(tok, None)    

    def test_comment(self):
        tok = theLexer.theLexerTester('''//This is a comment 434$3499 bool !@##%T@$%& 't 't' ''')
        self.assertEqual(tok.type, "COMMENTS" )
        self.assertEqual(tok.value, "//This is a comment 434$3499 bool !@##%T@$%& 't 't' ")    

    def test_unknown(self):
        tok = theLexer.theLexerTester(''' ' ''')
        self.assertEqual(tok.type, "UNKNOWN" )
        self.assertEqual(tok.value, "'")  

#Edge case scenarios. 

    def test_StringBool(self):
        tok = theLexer.theLexerTester('''"bool"''')
        self.assertEqual(tok.type, "STRING" )
        self.assertEqual(tok.value, '"bool"')        

    def test_BOOL(self):
        tok = theLexer.theLexerTester('''BOOL''')
        self.assertEqual(tok.type, "ID" )
        self.assertEqual(tok.value, 'BOOL') 

    def test__while(self):
        tok = theLexer.theLexerTester('''_while''')
        self.assertEqual(tok.type, "ID" )
        self.assertEqual(tok.value, '_while')    

    def test_false_(self):
        tok = theLexer.theLexerTester('''false_''')
        self.assertEqual(tok.type, "ID" )
        self.assertEqual(tok.value, 'false_')       

    def test_falsetimes(self):
        tok = theLexer.theLexerTester('''false*''')
        self.assertEqual(tok.type, "FALSE" )
        self.assertEqual(tok.value, 'false') 

    def test_minusEqualEqual(self):
        tok = theLexer.theLexerTester('''-==''')
        self.assertEqual(tok.type, "MINUSEQUAL" )
        self.assertEqual(tok.value, '-=')         

    def test_IDquote(self):
        tok = theLexer.theLexerTester('''ThisIsAID"''')
        self.assertEqual(tok.type, "ID" )
        self.assertEqual(tok.value, 'ThisIsAID') 