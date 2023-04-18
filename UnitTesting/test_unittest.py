import unittest
import theLexer
import theParser
from SymbolTableVisitor import SymbolTableVisitor
from UndeclaredVarVistitor import UndeclaredVisitor
from ObjectInitializerAndTypeVisitor import ObjectInitializerAndTypeVisitor

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
        self.assertEqual(tok, None) 

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

class Test_parser(unittest.TestCase):

    def test_Arguments_empty(self):
        data = """()"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Arguments", data)
        self.assertEqual(parsed.LPAREN, '(')
        self.assertEqual(parsed.MaybeArgumentList.ArgumentList, None)
        self.assertEqual(parsed.RPAREN, ')')

    def test_Arguments_withList(self):
        data = """(a == b)"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Arguments", data)
        self.assertEqual(parsed.LPAREN, '(')
        self.assertEqual(hasattr(parsed.MaybeArgumentList.ArgumentList, 'Expression'), True)
        self.assertEqual(parsed.RPAREN, ')')

    def test_Argument_Invalid(self):
        data = """ ( test"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Arguments", data)
        self.assertEqual(parsed, None)
        
    def test_ArgumentList_single(self):
        data = """a == b"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("ArgumentList", data)
        self.assertEqual(hasattr(parsed.MultipleCommaExpression, 'COMMA'), True)
        self.assertEqual(parsed.MultipleCommaExpression.COMMA, None)
        self.assertEqual(parsed.MultipleCommaExpression.Expression, None)

    def test_ArgumentList_Multiple(self):
        data = """123,new void ()"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("ArgumentList", data)
        self.assertEqual(parsed.Expression.Terminal, 123)
        self.assertEqual(parsed.MultipleCommaExpression.MultipleCommaExpression.Expression, None)
        self.assertEqual(parsed.MultipleCommaExpression.COMMA, ',')
        self.assertNotEqual(parsed.MultipleCommaExpression.Expression, None)    

    def test_ArgumentList_Invalid(self):
        data = """break ;"""

    def test_Case_Num_none(self):
        data = """case 12345 : """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Case", data)
        self.assertEqual(parsed.CASE, 'case')
        self.assertEqual(parsed.COLON, ':')
        self.assertEqual(parsed.NumOrChar, 12345)
        self.assertEqual(parsed.MultipleStatement.Statement, None)

    def test_Case_Char_none(self):
        data = """case 'a' : """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Case", data)
        self.assertEqual(parsed.CASE, 'case')
        self.assertEqual(parsed.COLON, ':')
        self.assertEqual(parsed.NumOrChar, "'a'")
        self.assertEqual(parsed.MultipleStatement.Statement, None)

    def test_Case_Num_Statement(self):
        data = """case 1 : cout <<"hello";"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Case", data)
        self.assertEqual(parsed.CASE, 'case')
        self.assertEqual(parsed.COLON, ':')
        self.assertEqual(parsed.NumOrChar, 1)
        self.assertNotEqual(parsed.MultipleStatement.Statement, None)

    def test_Case_Char_Statement(self):
        data = """case 'x' : break;"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Case", data)
        self.assertEqual(parsed.CASE, 'case')
        self.assertEqual(parsed.COLON, ':')
        self.assertEqual(parsed.NumOrChar, "'x'")
        self.assertNotEqual(parsed.MultipleStatement.Statement, None)        

    def test_Case_Invalid(self):
        data = """case ab : a == b"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Case", data)
        self.assertEqual(parsed, None)

    def test_CaseBlock_none(self):
        data = """{ default : }"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("CaseBlock", data)
        self.assertEqual(parsed.LCURLY, '{')
        self.assertEqual(parsed.RCURLY, '}')
        self.assertEqual(parsed.DEFAULT, 'default')
        self.assertEqual(parsed.COLON, ':')
        self.assertEqual(parsed.MultipleCase.Case, None)
        self.assertEqual(parsed.MultipleStatement.Statement, None)

    def test_CaseBlock_Case(self):
        data = """{ case 1 : default : }"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("CaseBlock", data)
        self.assertEqual(parsed.LCURLY, '{')
        self.assertEqual(parsed.RCURLY, '}')
        self.assertEqual(parsed.DEFAULT, 'default')
        self.assertEqual(parsed.COLON, ':')
        self.assertNotEqual(parsed.MultipleCase.Case, None)
        self.assertEqual(parsed.MultipleStatement.Statement, None)

    def test_CaseBlock_Statement(self):
        data = """{ default : return;}"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("CaseBlock", data)
        self.assertEqual(parsed.LCURLY, '{')
        self.assertEqual(parsed.RCURLY, '}')
        self.assertEqual(parsed.DEFAULT, 'default')
        self.assertEqual(parsed.COLON, ':')
        self.assertEqual(parsed.MultipleCase.Case, None)
        self.assertNotEqual(parsed.MultipleStatement.Statement, None)

    def test_CaseBlock_Case_Statement(self):
        data = """{ case 'x' : break; default : return;}"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("CaseBlock", data)
        self.assertEqual(parsed.LCURLY, '{')
        self.assertEqual(parsed.RCURLY, '}')
        self.assertEqual(parsed.DEFAULT, 'default')
        self.assertEqual(parsed.COLON, ':')
        self.assertNotEqual(parsed.MultipleCase.Case, None)
        self.assertNotEqual(parsed.MultipleStatement.Statement, None)

    def test_CaseBlock_Invalid(self):
        data = """{ default }"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("CaseBlock", data)
        self.assertEqual(parsed, None)

    def test_ClassDefinition_None(self):
        data = """class test {}"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("ClassDefinition", data)
        self.assertEqual(parsed.Class, 'class')
        self.assertEqual(parsed.ID, 'test')
        self.assertEqual(parsed.LCURLY, '{')
        self.assertEqual(parsed.RCURLY, '}')
        self.assertEqual(parsed.MultipleClassMemberDefinition.ClassMemberDefinition, None)

    def test_ClassDefinition_Class(self):
        data = """class test { private void [] ident ; }"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("ClassDefinition", data)
        self.assertEqual(parsed.Class, 'class')
        self.assertEqual(parsed.ID, 'test')
        self.assertEqual(parsed.LCURLY, '{')
        self.assertEqual(parsed.RCURLY, '}')
        self.assertNotEqual(parsed.MultipleClassMemberDefinition.ClassMemberDefinition, None)

    def test_ClassDefinition_Invalid(self):
        data = """class test { """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("ClassDefinition", data)
        self.assertEqual(parsed, None)

    def test_ClassDefinition_Invalid_NoID(self):
        data = """class { }"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("ClassDefinition", data)
        self.assertEqual(parsed, None)

    def test_ClassDefinition_Invalid_NoClass(self):
        data = """cla test { }"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("ClassDefinition", data)
        self.assertEqual(parsed, None)

    def test_CompilationUnit_basic(self):
        data = """void kxi2023 main (){}"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("CompilationUnit", data)
        self.assertEqual(parsed.MultipleClassDefinition.ClassDefinition, None)
        self.assertEqual(parsed.void, 'void')
        self.assertEqual(parsed.kxi2023, 'kxi2023')
        self.assertEqual(parsed.main, 'main')
        self.assertEqual(parsed.LPAREN, '(')
        self.assertEqual(parsed.RPAREN, ')')
        self.assertEqual(parsed.MethodBody.MultipleStatement.Statement, None)

    def test_CompilationUnit_Class(self):
        data = """class test {} void kxi2023 main (){}"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("CompilationUnit", data)
        self.assertNotEqual(parsed.MultipleClassDefinition.ClassDefinition, None)
        self.assertEqual(parsed.void, 'void')
        self.assertEqual(parsed.kxi2023, 'kxi2023')
        self.assertEqual(parsed.main, 'main')
        self.assertEqual(parsed.LPAREN, '(')
        self.assertEqual(parsed.RPAREN, ')')
        self.assertEqual(parsed.MethodBody.MultipleStatement.Statement, None)

    def test_CompilationUnit_Method(self):
        data = """void kxi2023 main (){
            cout << "Test";
        }"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("CompilationUnit", data)
        self.assertEqual(parsed.MultipleClassDefinition.ClassDefinition, None)
        self.assertEqual(parsed.void, 'void')
        self.assertEqual(parsed.kxi2023, 'kxi2023')
        self.assertEqual(parsed.main, 'main')
        self.assertEqual(parsed.LPAREN, '(')
        self.assertEqual(parsed.RPAREN, ')')
        self.assertNotEqual(parsed.MethodBody.MultipleStatement.Statement, None)

    def test_CompilationUnit_Class_Method(self):
        data = """class test {
        
        } 
        void kxi2023 main (){
            cout << "Test";
        }"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("CompilationUnit", data)
        self.assertNotEqual(parsed.MultipleClassDefinition.ClassDefinition, None)
        self.assertEqual(parsed.void, 'void')
        self.assertEqual(parsed.kxi2023, 'kxi2023')
        self.assertEqual(parsed.main, 'main')
        self.assertEqual(parsed.LPAREN, '(')
        self.assertEqual(parsed.RPAREN, ')')
        self.assertNotEqual(parsed.MethodBody.MultipleStatement.Statement, None)

    def test_CompilationUnit_Invalid(self):
        data = """voikxi2023 main (){}"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("CompilationUnit", data)
        self.assertEqual(parsed, None)

    def test_ConstructionDeclaration(self):
        data = """ id (){}"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("ConstructorDeclaration", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTConstructorDeclaration'>")
        self.assertEqual(parsed.ID, 'id')
        self.assertEqual(str(parsed.MethodSuffix.__class__), "<class 'AST.ASTMethodSuffix'>")

    def test_ConstructionDeclaration_Invalid(self):
        data = """ "string" (){}"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("ConstructorDeclaration", data)
        self.assertEqual(parsed, None)

    def test_DataMemberDeclaration(self):
        data = """ private bool [] test1;"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("DataMemberDeclaration", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTDataMemberDeclaration'>")
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTVariableDeclaration'>")
        self.assertNotEqual(parsed.VariabledDeclartion, None)
        self.assertEqual(parsed.Modifier, "private")
        
    def test_DataMemberDeclaration(self):
        data = """ privt bool [] test1;"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("DataMemberDeclaration", data)
        self.assertEqual(parsed, None)
        
    def test_Expression_Terminal_This(self):
        data = """this"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Expression", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTTerminal'>")
        self.assertEqual(parsed.Terminal, "this")

    def test_Expression_Terminal_INT(self):
        data = """1234"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Expression", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTTerminal'>")
        self.assertEqual(parsed.Terminal, 1234)

    def test_Expression_Terminal_CHAR(self):
        data = """'a'"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Expression", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTTerminal'>")
        self.assertEqual(parsed.Terminal, "'a'")

    def test_Expression_Terminal_STRING(self):
        data = '"This is a string"'
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Expression", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTTerminal'>")
        self.assertEqual(parsed.Terminal, '"This is a string"')

    def test_Expression_Terminal_TRUE(self):
        data = """true"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Expression", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTTerminal'>")
        self.assertEqual(parsed.Terminal, "true")

    def test_Expression_Terminal_FALSE(self):
        data = """false"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Expression", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTTerminal'>")
        self.assertEqual(parsed.Terminal, "false")

    def test_Expression_Terminal_NULL(self):
        data = """null"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Expression", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTTerminal'>")
        self.assertEqual(parsed.Terminal, "null")

    def test_Expression_Terminal_ID(self):
        data = """TestID1"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Expression", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTTerminal'>")
        self.assertEqual(parsed.Terminal, "TestID1")

    def test_Expression_Terminal_invalid1(self):
        data = """void"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Expression", data)
        self.assertEqual(parsed, None)

    def test_Expression_Terminal_invalid2(self):
        data = """true true"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Expression", data)
        self.assertEqual(parsed, None)

    def test_Expression_Expression_Index(self):    
        data = """array[0]"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Expression", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTExpressionArgIdx'>")

    def test_Expression_Expression_Index_Invalid(self):
        data = """array[0"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Expression", data)
        self.assertEqual(parsed, None)

    def test_Expression_Expression_Argument(self):    
        data = """array()"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Expression", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTExpressionArgIdx'>")

    def test_Expression_Expression_Argument_Invalid(self):
        data = """array("""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Expression", data)
        self.assertEqual(parsed, None)

    def test_Expression_PLUS_Expression(self):    
        data = """+ (a<b)"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Expression", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTExpressionPlus'>")
        self.assertEqual(parsed.PLUS, '+')
        self.assertNotEqual(parsed.Expression, None)

    def test_Expression_PLUS_Expression_Invalid(self):
        data = """+ (a b)"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Expression", data)
        self.assertEqual(parsed, None)

    def test_Expression_NOT_Expression(self):    
        data = """!(a<b)"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Expression", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTExpressionNot'>")
        self.assertEqual(parsed.NOT, '!')
        self.assertNotEqual(parsed.Expression, None)

    def test_Expression_NOT_Expression_Invalid(self):
        data = """!(a b)"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Expression", data)
        self.assertEqual(parsed, None)

    def test_Expression_MINUS_Expression(self):    
        data = """-(a||b)"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Expression", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTExpressionMinus'>")
        self.assertEqual(parsed.MINUS, '-')
        self.assertNotEqual(parsed.Expression, None)

    def test_Expression_MINUS_Expression_Invalid(self):
        data = """-(a | b)"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Expression", data)
        self.assertEqual(parsed, None)

    def test_Expression_PERIOD_ID(self):
        data = """test.test1"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Expression", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTExpressionDotID'>")
        self.assertEqual(parsed.PERIOD, '.')
        self.assertEqual(parsed.ID, 'test1')
        self.assertNotEqual(parsed.Expression, None)

    def test_Expression_LP_Expression_RP(self):
        data = """(a+2)"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Expression", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTExpressionPAREN'>")
        self.assertEqual(parsed.LPAREN, '(')
        self.assertEqual(parsed.RPAREN, ')')
        self.assertNotEqual(parsed.Expression, None)

    def test_Expression_NEW_Void_index(self):
        data = """new void [ this ]"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Expression", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTExpressionNew'>")
        self.assertEqual(parsed.NEW, 'new')
        self.assertEqual(parsed.Type, 'void')
        self.assertEqual(str(parsed.ArgOrIdx.Arg_Idx.__class__), "<class 'AST.ASTIndex'>")

    def test_Expression_NEW_Void_Argument(self):
        data = """new void ()"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Expression", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTExpressionNew'>")
        self.assertEqual(parsed.NEW, 'new')
        self.assertEqual(parsed.Type, 'void')
        self.assertEqual(str(parsed.ArgOrIdx.Arg_Idx.__class__), "<class 'AST.ASTArgument'>")

    def test_Expression_NEW_Int_index(self):
        data = """new int [ this ]"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Expression", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTExpressionNew'>")
        self.assertEqual(parsed.NEW, 'new')
        self.assertEqual(parsed.Type, 'int')
        self.assertEqual(str(parsed.ArgOrIdx.Arg_Idx.__class__), "<class 'AST.ASTIndex'>")

    def test_Expression_NEW_Int_Argument(self):
        data = """new int ()"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Expression", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTExpressionNew'>")
        self.assertEqual(parsed.NEW, 'new')
        self.assertEqual(parsed.Type, 'int')
        self.assertEqual(str(parsed.ArgOrIdx.Arg_Idx.__class__), "<class 'AST.ASTArgument'>")

    def test_Expression_NEW_CHAR_index(self):
        data = """new char [ this ]"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Expression", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTExpressionNew'>")
        self.assertEqual(parsed.NEW, 'new')
        self.assertEqual(parsed.Type, 'char')
        self.assertEqual(str(parsed.ArgOrIdx.Arg_Idx.__class__), "<class 'AST.ASTIndex'>")

    def test_Expression_NEW_CHAR_Argument(self):
        data = """new char ()"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Expression", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTExpressionNew'>")
        self.assertEqual(parsed.NEW, 'new')
        self.assertEqual(parsed.Type, 'char')
        self.assertEqual(str(parsed.ArgOrIdx.Arg_Idx.__class__), "<class 'AST.ASTArgument'>")

    def test_Expression_NEW_BOOL_index(self):
        data = """new bool [ this ]"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Expression", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTExpressionNew'>")
        self.assertEqual(parsed.NEW, 'new')
        self.assertEqual(parsed.Type, 'bool')
        self.assertEqual(str(parsed.ArgOrIdx.Arg_Idx.__class__), "<class 'AST.ASTIndex'>")

    def test_Expression_NEW_BOOL_Argument(self):
        data = """new bool ()"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Expression", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTExpressionNew'>")
        self.assertEqual(parsed.NEW, 'new')
        self.assertEqual(parsed.Type, 'bool')
        self.assertEqual(str(parsed.ArgOrIdx.Arg_Idx.__class__), "<class 'AST.ASTArgument'>")

    def test_Expression_NEW_STRING_index(self):
        data = """new string [ this ]"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Expression", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTExpressionNew'>")
        self.assertEqual(parsed.NEW, 'new')
        self.assertEqual(parsed.Type, 'string')
        self.assertEqual(str(parsed.ArgOrIdx.Arg_Idx.__class__), "<class 'AST.ASTIndex'>")

    def test_Expression_NEW_STRING_Argument(self):
        data = """new string ()"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Expression", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTExpressionNew'>")
        self.assertEqual(parsed.NEW, 'new')
        self.assertEqual(parsed.Type, 'string')
        self.assertEqual(str(parsed.ArgOrIdx.Arg_Idx.__class__), "<class 'AST.ASTArgument'>")

    def test_Expression_NEW_ID_index(self):
        data = """new id [ this ]"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Expression", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTExpressionNew'>")
        self.assertEqual(parsed.NEW, 'new')
        self.assertEqual(parsed.Type, 'id')
        self.assertEqual(str(parsed.ArgOrIdx.Arg_Idx.__class__), "<class 'AST.ASTIndex'>")

    def test_Expression_NEW_ID_Argument(self):
        data = """new id ()"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Expression", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTExpressionNew'>")
        self.assertEqual(parsed.NEW, 'new')
        self.assertEqual(parsed.Type, 'id')
        self.assertEqual(str(parsed.ArgOrIdx.Arg_Idx.__class__), "<class 'AST.ASTArgument'>")

    def test_Expression_ETimesEqualE(self):
        data = """(5 *= 3) *= (a*true)"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Expression", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTExpressionETimesEqualE'>")
        self.assertEqual(parsed.TIMESEQUAL, '*=')
        self.assertEqual(str(parsed.Expression.__class__), "<class 'AST.ASTExpressionPAREN'>")
        self.assertEqual(str(parsed.Expression2.__class__), "<class 'AST.ASTExpressionPAREN'>")

    def test_Expression_ETimesE(self):
        data = """(5 *= 3) * this"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Expression", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTExpressionETimesE'>")
        self.assertEqual(parsed.TIMES, '*')
        self.assertEqual(str(parsed.Expression.__class__), "<class 'AST.ASTExpressionPAREN'>")
        self.assertEqual(str(parsed.Expression2.__class__), "<class 'AST.ASTTerminal'>")

    def test_Expression_EPlusEqualsE(self):
        data = """(5 *= 3) += 123 """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Expression", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTExpressionEPlusEqualE'>")
        self.assertEqual(parsed.PLUSEQUAL, '+=')
        self.assertEqual(str(parsed.Expression.__class__), "<class 'AST.ASTExpressionPAREN'>")
        self.assertEqual(str(parsed.Expression2.__class__), "<class 'AST.ASTTerminal'>")

    def test_Expression_EPlusE(self):
        data = """(5 *= 3) + ids"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Expression", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTExpressionEPlusE'>")
        self.assertEqual(parsed.PLUS, '+')
        self.assertEqual(str(parsed.Expression.__class__), "<class 'AST.ASTExpressionPAREN'>")
        self.assertEqual(str(parsed.Expression2.__class__), "<class 'AST.ASTTerminal'>")

    def test_Expression_EOORE(self):
        data = """(5 *= 3) || null"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Expression", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTExpressionEOORE'>")
        self.assertEqual(parsed.OOR, '||')
        self.assertEqual(str(parsed.Expression.__class__), "<class 'AST.ASTExpressionPAREN'>")
        self.assertEqual(str(parsed.Expression2.__class__), "<class 'AST.ASTTerminal'>")

    def test_Expression_ENotEqualE(self):
        data = """(5 *= 3) != (test.test1)"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Expression", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTExpressionENotEqualE'>")
        self.assertEqual(parsed.NEQUAL, '!=')
        self.assertEqual(str(parsed.Expression.__class__), "<class 'AST.ASTExpressionPAREN'>")
        self.assertEqual(str(parsed.Expression2.__class__), "<class 'AST.ASTExpressionPAREN'>")

    def test_Expression_EMinusEqualE(self):
        data = """(5 *= 3) -= (+ test)"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Expression", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTExpressionEMinusEqualE'>")
        self.assertEqual(parsed.MINUSEQUAL, '-=')
        self.assertEqual(str(parsed.Expression.__class__), "<class 'AST.ASTExpressionPAREN'>")
        self.assertEqual(str(parsed.Expression2.__class__), "<class 'AST.ASTExpressionPAREN'>")

    def test_Expression_EMinusE(self):
        data = """(5 *= 3) - 'a' """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Expression", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTExpressionEMinusE'>")
        self.assertEqual(parsed.MINUS, '-')
        self.assertEqual(str(parsed.Expression.__class__), "<class 'AST.ASTExpressionPAREN'>")
        self.assertEqual(str(parsed.Expression2.__class__), "<class 'AST.ASTTerminal'>")

    def test_Expression_ELessEqualE(self):
        data = """(5 *= 3) <= 'a' """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Expression", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTExpressionELessEqualE'>")
        self.assertEqual(parsed.LESSEQUAL, '<=')
        self.assertEqual(str(parsed.Expression.__class__), "<class 'AST.ASTExpressionPAREN'>")
        self.assertEqual(str(parsed.Expression2.__class__), "<class 'AST.ASTTerminal'>")

    def test_Expression_ELessE(self):
        data = """(5 *= 3) < 'a' """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Expression", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTExpressionELessE'>")
        self.assertEqual(parsed.LESS, '<')
        self.assertEqual(str(parsed.Expression.__class__), "<class 'AST.ASTExpressionPAREN'>")
        self.assertEqual(str(parsed.Expression2.__class__), "<class 'AST.ASTTerminal'>")

    def test_Expression_EGreaterEqualE(self):
        data = """(5 *= 3) >= 'a' """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Expression", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTExpressionEGreaterEqualE'>")
        self.assertEqual(parsed.GREATEQUAL, '>=')
        self.assertEqual(str(parsed.Expression.__class__), "<class 'AST.ASTExpressionPAREN'>")
        self.assertEqual(str(parsed.Expression2.__class__), "<class 'AST.ASTTerminal'>")

    def test_Expression_EGreaterE(self):
        data = """(5 *= 3) > 'a' """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Expression", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTExpressionEGreaterE'>")
        self.assertEqual(parsed.GREATER, '>')
        self.assertEqual(str(parsed.Expression.__class__), "<class 'AST.ASTExpressionPAREN'>")
        self.assertEqual(str(parsed.Expression2.__class__), "<class 'AST.ASTTerminal'>")

    def test_Expression_EEqualE(self):
        data = """(5 *= 3) = 'a' """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Expression", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTExpressionEEqualE'>")
        self.assertEqual(parsed.EQUAL, '=')
        self.assertEqual(str(parsed.Expression.__class__), "<class 'AST.ASTExpressionPAREN'>")
        self.assertEqual(str(parsed.Expression2.__class__), "<class 'AST.ASTTerminal'>")

    def test_Expression_EDivideEqualE(self):
        data = """(5 *= 3) /= 'a' """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Expression", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTExpressionEDivideEqualE'>")
        self.assertEqual(parsed.DIVIDEEQUAL, '/=')
        self.assertEqual(str(parsed.Expression.__class__), "<class 'AST.ASTExpressionPAREN'>")
        self.assertEqual(str(parsed.Expression2.__class__), "<class 'AST.ASTTerminal'>")

    def test_Expression_EDivideE(self):
        data = """(5 *= 3) / 'a' """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Expression", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTExpressionEDivideE'>")
        self.assertEqual(parsed.DIVIDE, '/')
        self.assertEqual(str(parsed.Expression.__class__), "<class 'AST.ASTExpressionPAREN'>")
        self.assertEqual(str(parsed.Expression2.__class__), "<class 'AST.ASTTerminal'>")

    def test_Expression_ECEqualE(self):
        data = """(5 *= 3) == 'a' """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Expression", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTExpressionECEqualE'>")
        self.assertEqual(parsed.CEQUAL, '==')
        self.assertEqual(str(parsed.Expression.__class__), "<class 'AST.ASTExpressionPAREN'>")
        self.assertEqual(str(parsed.Expression2.__class__), "<class 'AST.ASTTerminal'>")

    def test_Expression_EAANDE(self):
        data = """(5 *= 3) && 'a' """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Expression", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTExpressionEAANDE'>")
        self.assertEqual(parsed.AAND, '&&')
        self.assertEqual(str(parsed.Expression.__class__), "<class 'AST.ASTExpressionPAREN'>")
        self.assertEqual(str(parsed.Expression2.__class__), "<class 'AST.ASTTerminal'>")
        
    def test_Index(self):
        data = """ [ 9 ]"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Index", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTIndex'>")
        self.assertEqual(parsed.LSQUARE, '[')
        self.assertEqual(parsed.RSQUARE, ']')
        self.assertEqual(str(parsed.Expression.__class__), "<class 'AST.ASTTerminal'>")
                
    def test_Index_Invalid(self):
        data = """[ 9 """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Index", data)
        self.assertEqual(parsed, None)
                
    def test_Initializer(self):
        data = """ = (a+b)"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Initializer", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTInitializer'>")
        self.assertEqual(parsed.EQUAL, '=')
        self.assertEqual(str(parsed.Expression.__class__), "<class 'AST.ASTExpressionPAREN'>")
                
    def test_Index_Invalid(self):
        data = """ (null)"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Initializer", data)
        self.assertEqual(parsed, None)

    def test_MaybeArgumentList_Empty(self):
        data = """ """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("MaybeArgumentList", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTMaybeArgumentList'>")
        self.assertEqual(parsed.ArgumentList, None)

    def test_MaybeArgumentList_ArgumentList(self):
        data = """ (a+b) , (x == c) """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("MaybeArgumentList", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTMaybeArgumentList'>")
        self.assertNotEqual(parsed.ArgumentList, None)
        
    def test_MaybeArgumentList_Invalid(self):
        data = """ break ; """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("MaybeArgumentList", data)
        self.assertEqual(parsed.ArgumentList, None)

    def test_MaybeExpression_Empty(self):
        data = """ """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("MaybeExpression", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTMaybeExpression'>")
        self.assertEqual(parsed.Expression, None)

    def test_MaybeExpression_Expression(self):
        data = """ (a+b) """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("MaybeExpression", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTMaybeExpression'>")
        self.assertNotEqual(parsed.Expression, None)
        
    def test_MaybeExpression_Invalid(self):
        data = """ break ; """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("MaybeExpression", data)
        self.assertEqual(parsed.Expression, None)
        
    def test_MaybeInitializer_Empty(self):
        data = """ """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("MaybeInitializer", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTMaybeInitializer'>")
        self.assertEqual(parsed.Initializer, None)

    def test_MaybeInitializer_Initializer(self):
        data = """ = (a+b) """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("MaybeInitializer", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTMaybeInitializer'>")
        self.assertNotEqual(parsed.Initializer, None)
        
    def test_MaybeInitializer_Invalid(self):
        data = """ break ; """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("MaybeInitializer", data)
        self.assertEqual(parsed.Initializer, None)
                
    def test_MaybeParamList_Empty(self):
        data = """ """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("MaybeParamList", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTMaybeParamList'>")
        self.assertEqual(parsed.ParameterList, None)

    def test_MaybeParamList_ParameterList(self):
        data = """ void [] para , string para2 """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("MaybeParamList", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTMaybeParamList'>")
        self.assertNotEqual(parsed.ParameterList, None)
        
    def test_MaybeParamList_Invalid(self):
        data = """ break ; """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("MaybeParamList", data)
        self.assertEqual(parsed.ParameterList, None)

    def test_MethodBody_Empty(self):
        data = """ {} """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("MethodBody", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTMethodBody'>")
        self.assertEqual(parsed.LCURLY, '{')
        self.assertEqual(parsed.RCURLY, '}')
        self.assertEqual(parsed.MultipleStatement.Statement, None)

    def test_MethodBody_Statement(self):
        data = """ { cout << (a+b);} """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("MethodBody", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTMethodBody'>")
        self.assertEqual(parsed.LCURLY, '{')
        self.assertEqual(parsed.RCURLY, '}')
        self.assertNotEqual(parsed.MultipleStatement.Statement, None)
        
    def test_MethodBody_Invalid(self):
        data = """ { cout << (a+b) ; """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("MethodBody", data)
        self.assertEqual(parsed, None)

    def test_MethodDeclaration_Void_LRSquare(self):
        data = """ private void [] test1 (){}"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("MethodDeclaration", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTMethodDeclaration'>")
        self.assertEqual(parsed.Modifier, 'PRIVATE')
        self.assertEqual(parsed.Type, 'void')
        self.assertEqual(parsed.LRSquare, '[]')
        self.assertEqual(str(parsed.MethodSuffix.__class__), "<class 'AST.ASTMethodSuffix'>")

    def test_MethodDeclaration_Void_NoLRSquare(self):
        data = """ public void test1 (){}"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("MethodDeclaration", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTMethodDeclaration'>")
        self.assertEqual(parsed.Modifier, 'PUBLIC')
        self.assertEqual(parsed.Type, 'void')
        self.assertEqual(parsed.LRSquare, None)
        self.assertEqual(str(parsed.MethodSuffix.__class__), "<class 'AST.ASTMethodSuffix'>")
        
    def test_MethodDeclaration_Int_LRSquare(self):
        data = """ private int [] test1 (){}"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("MethodDeclaration", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTMethodDeclaration'>")
        self.assertEqual(parsed.Modifier, 'PRIVATE')
        self.assertEqual(parsed.Type, 'int')
        self.assertEqual(parsed.LRSquare, '[]')
        self.assertEqual(str(parsed.MethodSuffix.__class__), "<class 'AST.ASTMethodSuffix'>")

    def test_MethodDeclaration_int_NoLRSquare(self):
        data = """ public int test1 (){}"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("MethodDeclaration", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTMethodDeclaration'>")
        self.assertEqual(parsed.Modifier, 'PUBLIC')
        self.assertEqual(parsed.Type, 'int')
        self.assertEqual(parsed.LRSquare, None)
        self.assertEqual(str(parsed.MethodSuffix.__class__), "<class 'AST.ASTMethodSuffix'>")
                
    def test_MethodDeclaration_CHAR_LRSquare(self):
        data = """ private char [] test1 (){}"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("MethodDeclaration", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTMethodDeclaration'>")
        self.assertEqual(parsed.Modifier, 'PRIVATE')
        self.assertEqual(parsed.Type, 'char')
        self.assertEqual(parsed.LRSquare, '[]')
        self.assertEqual(str(parsed.MethodSuffix.__class__), "<class 'AST.ASTMethodSuffix'>")

    def test_MethodDeclaration_CHAR_NoLRSquare(self):
        data = """ public char test1 (){}"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("MethodDeclaration", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTMethodDeclaration'>")
        self.assertEqual(parsed.Modifier, 'PUBLIC')
        self.assertEqual(parsed.Type, 'char')
        self.assertEqual(parsed.LRSquare, None)
        self.assertEqual(str(parsed.MethodSuffix.__class__), "<class 'AST.ASTMethodSuffix'>")
                        
    def test_MethodDeclaration_BOOL_LRSquare(self):
        data = """ private bool [] test1 (){}"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("MethodDeclaration", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTMethodDeclaration'>")
        self.assertEqual(parsed.Modifier, 'PRIVATE')
        self.assertEqual(parsed.Type, 'bool')
        self.assertEqual(parsed.LRSquare, '[]')
        self.assertEqual(str(parsed.MethodSuffix.__class__), "<class 'AST.ASTMethodSuffix'>")

    def test_MethodDeclaration_BOOL_NoLRSquare(self):
        data = """ public bool test1 (){}"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("MethodDeclaration", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTMethodDeclaration'>")
        self.assertEqual(parsed.Modifier, 'PUBLIC')
        self.assertEqual(parsed.Type, 'bool')
        self.assertEqual(parsed.LRSquare, None)
        self.assertEqual(str(parsed.MethodSuffix.__class__), "<class 'AST.ASTMethodSuffix'>")

    def test_MethodDeclaration_STRING_LRSquare(self):
        data = """ private string [] test1 (){}"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("MethodDeclaration", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTMethodDeclaration'>")
        self.assertEqual(parsed.Modifier, 'PRIVATE')
        self.assertEqual(parsed.Type, 'string')
        self.assertEqual(parsed.LRSquare, '[]')
        self.assertEqual(str(parsed.MethodSuffix.__class__), "<class 'AST.ASTMethodSuffix'>")

    def test_MethodDeclaration_STRING_NoLRSquare(self):
        data = """ public string test1 (){}"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("MethodDeclaration", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTMethodDeclaration'>")
        self.assertEqual(parsed.Modifier, 'PUBLIC')
        self.assertEqual(parsed.Type, 'string')
        self.assertEqual(parsed.LRSquare, None)
        self.assertEqual(str(parsed.MethodSuffix.__class__), "<class 'AST.ASTMethodSuffix'>")

    def test_MethodDeclaration_ID_LRSquare(self):
        data = """ private test2 [] test1 (){}"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("MethodDeclaration", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTMethodDeclaration'>")
        self.assertEqual(parsed.Modifier, 'PRIVATE')
        self.assertEqual(parsed.Type, 'test2')
        self.assertEqual(parsed.LRSquare, '[]')
        self.assertEqual(str(parsed.MethodSuffix.__class__), "<class 'AST.ASTMethodSuffix'>")

    def test_MethodDeclaration_test2_NoLRSquare(self):
        data = """ public test2 test1 (){}"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("MethodDeclaration", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTMethodDeclaration'>")
        self.assertEqual(parsed.Modifier, 'PUBLIC')
        self.assertEqual(parsed.Type, 'test2')
        self.assertEqual(parsed.LRSquare, None)
        self.assertEqual(str(parsed.MethodSuffix.__class__), "<class 'AST.ASTMethodSuffix'>")
        
    def test_MethodDeclaration_Invalid_LRSquare(self):
        data = """ Public void [0] tests 1 () {}"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("MethodDeclaration", data)
        self.assertEqual(parsed, None)

    def test_MethodDeclaration_Invalid_NoMethod(self):
        data = """ private void [] tests 1 """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("MethodDeclaration", data)
        self.assertEqual(parsed, None)

    def test_MethodDeclaration_Invalid_NoModifier(self):
        data = """ void [] tests 1 () {}"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("MethodDeclaration", data)
        self.assertEqual(parsed, None)

    def test_MethodSuffix_NoParameter(self):
        data = """ () {}"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("MethodSuffix", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTMethodSuffix'>")
        self.assertEqual(parsed.LPAREN, '(')
        self.assertEqual(parsed.RPAREN, ')')
        self.assertEqual(parsed.MaybeParameterList.ParameterList, None)
        self.assertEqual(str(parsed.MethodBody.__class__), "<class 'AST.ASTMethodBody'>")
        
    def test_MethodSuffix_Parameter(self):
        data = """ (void [] test) {}"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("MethodSuffix", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTMethodSuffix'>")
        self.assertEqual(parsed.LPAREN, '(')
        self.assertEqual(parsed.RPAREN, ')')
        self.assertNotEqual(parsed.MaybeParameterList.ParameterList, None)
        self.assertEqual(str(parsed.MethodBody.__class__), "<class 'AST.ASTMethodBody'>")

    def test_MethodSuffix_Invalid(self):
        data = """ ( {}"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("MethodSuffix", data)
        self.assertEqual(parsed, None)
                
    def test_MultipleCase_Single(self):
        data = """case 1 : break;"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("MultipleCase", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTMultipleCase'>")
        self.assertEqual(parsed.Case.CASE, 'case')
        self.assertEqual(parsed.Case.COLON, ':')
        self.assertEqual(str(parsed.Case.MultipleStatement.__class__), "<class 'AST.ASTMultipleStatement'>")
        self.assertEqual(parsed.MultipleCase.Case, None)

    def test_MultipleCase_Multiple(self):
        data = """case 1 : break; case 2 : return;"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("MultipleCase", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTMultipleCase'>")
        self.assertEqual(parsed.Case.CASE, 'case')
        self.assertEqual(parsed.Case.COLON, ':')
        self.assertEqual(str(parsed.Case.MultipleStatement.__class__), "<class 'AST.ASTMultipleStatement'>")
        self.assertEqual(parsed.MultipleCase.Case.CASE, 'case')
        self.assertEqual(parsed.MultipleCase.Case.COLON, ':')
        self.assertEqual(parsed.MultipleCase.MultipleCase.Case, None)

    def test_MultipleCase_Invalid(self):
        data = """ case : break;"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("MultipleCase", data)
        self.assertEqual(parsed.MultipleCase, None)

    def test_MultipleClassDefinition_Single(self):
        data = """ class test {}"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("MultipleClassDefinition", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTMultipleClassDefinition'>")
        self.assertNotEqual(parsed.ClassDefinition.Class, None)
        self.assertEqual(parsed.MultipleClassDefinition.ClassDefinition, None)
        self.assertEqual(parsed.MultipleClassDefinition.MultipleClassDefinition, None)

    def test_MultipleClassDefinition_Multiple(self):
        data = """class test {} class test2{}"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("MultipleClassDefinition", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTMultipleClassDefinition'>")
        self.assertNotEqual(parsed.ClassDefinition.Class, None)
        self.assertNotEqual(parsed.MultipleClassDefinition.ClassDefinition.Class, None)
        self.assertEqual(parsed.MultipleClassDefinition.MultipleClassDefinition.ClassDefinition, None)

    def test_MultipleClassDefinition_Invalid(self):
        data = """ class { """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("MultipleClassDefinition", data)
        self.assertEqual(parsed.MultipleClassDefinition, None)

    def test_MultipleClassMemberDefinition_Single(self):
        data = """ public void [] test () {}"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("MultipleClassMemberDefinition", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTMultipleClassMemberDefinition'>")
        self.assertEqual(str(parsed.ClassMemberDefinition.Method_DataMember_Constructor.__class__), "<class 'AST.ASTMethodDeclaration'>")
        self.assertEqual(parsed.MultipleClassMemberDefinition.ClassMemberDefinition, None)
        self.assertEqual(parsed.MultipleClassMemberDefinition.MultipleClassMemberDefinition, None)

    def test_MultipleClassMemberDefinition_Multiple(self):
        data = """public void [] test () {} private bool test2; constructorTest(){}"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("MultipleClassMemberDefinition", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTMultipleClassMemberDefinition'>")
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTMultipleClassMemberDefinition'>")
        self.assertEqual(str(parsed.ClassMemberDefinition.Method_DataMember_Constructor.__class__), "<class 'AST.ASTMethodDeclaration'>")
        self.assertEqual(str(parsed.MultipleClassMemberDefinition.ClassMemberDefinition.Method_DataMember_Constructor.__class__), "<class 'AST.ASTDataMemberDeclaration'>")
        self.assertEqual(str(parsed.MultipleClassMemberDefinition.MultipleClassMemberDefinition.ClassMemberDefinition.Method_DataMember_Constructor.__class__), "<class 'AST.ASTConstructorDeclaration'>")
        self.assertEqual(parsed.MultipleClassMemberDefinition.MultipleClassMemberDefinition.MultipleClassMemberDefinition.ClassMemberDefinition, None)

    def test_p_MultipleCommaExpression_Single(self):
        data = """, (a+b)  """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("MultipleCommaExpression", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTMultipleCommaExpression'>")
        self.assertNotEqual(parsed.Expression, None)
        self.assertEqual(parsed.MultipleCommaExpression.Expression, None)
        
    def test_p_MultipleCommaExpression_Multiple(self):
        data = """ , this , test.id"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("MultipleCommaExpression", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTMultipleCommaExpression'>")
        self.assertNotEqual(parsed.Expression, None)
        self.assertEqual(str(parsed.MultipleCommaExpression.__class__), "<class 'AST.ASTMultipleCommaExpression'>")
        self.assertNotEqual(parsed.MultipleCommaExpression.Expression, None)
        self.assertEqual(parsed.MultipleCommaExpression.MultipleCommaExpression.Expression, None)

    def test_p_MultipleCommaExpression_Invalid(self):
        data = """ (a+b) """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("MultipleCommaExpression", data)
        self.assertEqual(parsed.MultipleCommaExpression, None)

    def test_p_MultipleCommaParameter_Single(self):
        data = """, char test """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("MultipleCommaParameter", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTMultipleCommaParameter'>")
        self.assertNotEqual(parsed.Parameter, None)
        self.assertEqual(parsed.MultipleCommaParameter.Parameter, None)
        
    def test_p_MultipleCommaParameter_Multiple(self):
        data = """ , string  test , bool [] test2"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("MultipleCommaParameter", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTMultipleCommaParameter'>")
        self.assertNotEqual(parsed.Parameter, None)
        self.assertNotEqual(parsed.MultipleCommaParameter.Parameter, None)
        self.assertEqual(parsed.MultipleCommaParameter.MultipleCommaParameter.Parameter, None)

    def test_p_MultipleCommaParameter_Invalid(self):
        data = """ int test """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("MultipleCommaParameter", data)
        self.assertEqual(parsed.MultipleCommaParameter, None)

    def test_p_MultipleStatement_Single(self):
        data = """ cout << "This is a string" ;"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("MultipleStatement", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTMultipleStatement'>")
        self.assertEqual(parsed.MultipleStatement.Statement, None)
        self.assertNotEqual(parsed.Statement, None)
        
    def test_p_MultipleStatement_Multiple(self):
        data = """ while ( a == b) return ; if (a<b) cout <<  "true"; """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("MultipleStatement", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTMultipleStatement'>")
        self.assertNotEqual(parsed.Statement, None)
        self.assertNotEqual(parsed.MultipleStatement.Statement, None)
        self.assertEqual(parsed.MultipleStatement.MultipleStatement.Statement, None)

    def test_p_MultipleStatement_Invalid(self):
        data = """ return """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("MultipleStatement", data)
        self.assertEqual(parsed, None)

    def test_p_Parameter_Void_NoLRSquare(self):
        data = """void test """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Parameter", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTParameter'>")
        self.assertEqual(parsed.Type, 'void')
        self.assertEqual(parsed.LRSquare, None)
        self.assertEqual(parsed.ID, 'test')

    def test_p_Parameter_Void_LRSquare(self):
        data = """ void [] test"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Parameter", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTParameter'>")
        self.assertEqual(parsed.Type, 'void')
        self.assertEqual(parsed.LRSquare, '[]')
        self.assertEqual(parsed.ID, 'test')

    def test_p_Parameter_Int_NoLRSquare(self):
        data = """int test """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Parameter", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTParameter'>")
        self.assertEqual(parsed.Type, 'int')
        self.assertEqual(parsed.LRSquare, None)
        self.assertEqual(parsed.ID, 'test')

    def test_p_Parameter_Int_LRSquare(self):
        data = """ int [] test"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Parameter", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTParameter'>")
        self.assertEqual(parsed.Type, 'int')
        self.assertEqual(parsed.LRSquare, '[]')
        self.assertEqual(parsed.ID, 'test')

    def test_p_Parameter_Char_NoLRSquare(self):
        data = """char test """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Parameter", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTParameter'>")
        self.assertEqual(parsed.Type, 'char')
        self.assertEqual(parsed.LRSquare, None)
        self.assertEqual(parsed.ID, 'test')

    def test_p_Parameter_Char_LRSquare(self):
        data = """char [] test """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Parameter", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTParameter'>")
        self.assertEqual(parsed.Type, 'char')
        self.assertEqual(parsed.LRSquare, '[]')
        self.assertEqual(parsed.ID, 'test')

    def test_p_Parameter_Bool_NoLRSquare(self):
        data = """bool test """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Parameter", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTParameter'>")
        self.assertEqual(parsed.Type, 'bool')
        self.assertEqual(parsed.LRSquare, None)
        self.assertEqual(parsed.ID, 'test')

    def test_p_Parameter_Bool_LRSquare(self):
        data = """bool [] test """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Parameter", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTParameter'>")
        self.assertEqual(parsed.Type, 'bool')
        self.assertEqual(parsed.LRSquare, '[]')
        self.assertEqual(parsed.ID, 'test')
        
    def test_p_Parameter_String_NoLRSquare(self):
        data = """string test """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Parameter", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTParameter'>")
        self.assertEqual(parsed.Type, 'string')
        self.assertEqual(parsed.LRSquare, None)
        self.assertEqual(parsed.ID, 'test')

    def test_p_Parameter_String_LRSquare(self):
        data = """string [] test """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Parameter", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTParameter'>")
        self.assertEqual(parsed.Type, 'string')
        self.assertEqual(parsed.LRSquare, '[]')
        self.assertEqual(parsed.ID, 'test')

    def test_p_Parameter_Id_NoLRSquare(self):
        data = """ test test1"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Parameter", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTParameter'>")
        self.assertEqual(parsed.Type, 'test')
        self.assertEqual(parsed.LRSquare, None)
        self.assertEqual(parsed.ID, 'test1')

    def test_p_Parameter_Id_LRSquare(self):
        data = """test [] test1 """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Parameter", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTParameter'>")
        self.assertEqual(parsed.Type, 'test')
        self.assertEqual(parsed.LRSquare, '[]')
        self.assertEqual(parsed.ID, 'test1')

    def test_p_Parameter_Invalid(self):
        data = """ [] test """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Parameter", data)
        self.assertEqual(parsed, None)

    def test_p_Parameter_Invalid_NoID(self):
        data = """ test[]  """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Parameter", data)
        self.assertEqual(parsed, None)

    def test_p_ParameterList_Single(self):
        data = """ void list """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("ParameterList", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTParameterList'>")
        self.assertNotEqual(parsed.Parameter, None)
        self.assertEqual(parsed.MultipleCommaParameter.Parameter, None)

    def test_p_ParameterList_Mutliple(self):
        data = """void list, void [] list1 """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("ParameterList", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTParameterList'>")
        self.assertNotEqual(parsed.Parameter, None)
        self.assertNotEqual(parsed.MultipleCommaParameter.Parameter, None)
        self.assertEqual(parsed.MultipleCommaParameter.MultipleCommaParameter.Parameter, None)

    def test_p_ParameterList_Invalid(self):
        data = """ void test , void """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("ParameterList", data)
        self.assertEqual(parsed, None)

    def test_p_StatementToVariableDeclaration(self):
        data = """ bool [] ident ; """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Statement", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTStatementToVariableDeclaration'>")
        self.assertEqual(str(parsed.VariableDeclaration.__class__), "<class 'AST.ASTVariableDeclaration'>")

    def test_p_StatementToVariableDeclaration_Invalid(self):
        data = """ vool [];"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Statement", data)
        self.assertEqual(parsed, None)

    def test_p_Statement_Break(self):
        data = """ break; """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Statement", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTStatementBreak'>")
        self.assertEqual(parsed.BREAK, 'break')
        self.assertEqual(parsed.SEMICOLON, ';')

    def test_p_Statement_Break_Invalid(self):
        data = """ break"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Statement", data)
        self.assertEqual(parsed, None)

    def test_p_Statement_Expression(self):
        data = """ (a_b < c); """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Statement", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTStatementExpression'>")
        self.assertEqual(parsed.SEMICOLON, ';')

    def test_p_Statement_Expression_Invalid(self):
        data = """ (a+b) """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Statement", data)
        self.assertEqual(parsed, None)

    def test_p_Statement_Multiple_None(self):
        data = """ {} """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Statement", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTStatementMultipleStatement'>")
        self.assertEqual(parsed.LCURLY, '{')
        self.assertEqual(parsed.RCURLY, '}')
        self.assertEqual(parsed.MultipleStatement.Statement, None)

    def test_p_Statement_Multiple_Single(self):
        data = """ { cout << "test"; } """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Statement", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTStatementMultipleStatement'>")
        self.assertEqual(parsed.LCURLY, '{')
        self.assertEqual(parsed.RCURLY, '}')
        self.assertNotEqual(parsed.MultipleStatement.Statement, None)
        self.assertEqual(parsed.MultipleStatement.MultipleStatement.Statement, None)

    def test_p_Statement_Multiple_Multiple(self):
        data = """ { cout << "test"; break; } """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Statement", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTStatementMultipleStatement'>")
        self.assertEqual(parsed.LCURLY, '{')
        self.assertEqual(parsed.RCURLY, '}')        
        self.assertNotEqual(parsed.MultipleStatement.Statement, None)
        self.assertNotEqual(parsed.MultipleStatement.MultipleStatement.Statement, None)
        self.assertEqual(parsed.MultipleStatement.MultipleStatement.MultipleStatement.Statement, None)

    def test_p_Statement_Multiple_Invalid(self):
        data = """ { cout << "test"; """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Statement", data)
        self.assertEqual(parsed, None)

    def test_p_Statement_Return_NoExpression(self):
        data = """ return;"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Statement", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTStatementReturn'>")
        self.assertEqual(parsed.RETURN, 'return')
        self.assertEqual(parsed.SEMICOLON, ';')  
        self.assertEqual(parsed.MaybeExpression.Expression, None)

    def test_p_Statement_Return_Expression(self):
        data = """ return (a+b); """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Statement", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTStatementReturn'>")
        self.assertEqual(parsed.RETURN, 'return')
        self.assertEqual(parsed.SEMICOLON, ';')  
        self.assertNotEqual(parsed.MaybeExpression.Expression, None)

    def test_p_Statement_Return_Invalid(self):
        data = """ return """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Statement", data)
        self.assertEqual(parsed, None)

    def test_p_Statement_COUT(self):
        data = """ cout << (A+b.c);"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Statement", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTStatementCOUT'>")
        self.assertEqual(parsed.LEFTSHIFT, '<<')
        self.assertEqual(parsed.COUT, 'cout')
        self.assertEqual(parsed.SEMICOLON, ';')  
        self.assertNotEqual(parsed.Expression, None)

    def test_p_Statement_COUT_InvalidExpression(self):
        data = """ cout << (A+);"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Statement", data)
        self.assertEqual(parsed, None)

    def test_p_Statement_COUT_Invalid(self):
        data = """ cout << (A+b.c)"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Statement", data)
        self.assertEqual(parsed, None)

    def test_p_Statement_CIN(self):
        data = """ cin >> (this);"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Statement", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTStatementCIN'>")
        self.assertEqual(parsed.RIGHTSHIFT, '>>')
        self.assertEqual(parsed.CIN, 'cin')
        self.assertEqual(parsed.SEMICOLON, ';')  
        self.assertNotEqual(parsed.Expression, None)

    def test_p_Statement_CIN_InvalidExpression(self):
        data = """cin >> (a & a);"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Statement", data)
        self.assertEqual(parsed, None)

    def test_p_Statement_CIN_Invalid(self):
        data = """ cin >> (this)"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Statement", data)
        self.assertEqual(parsed, None)

    def test_p_Statement_WHILE(self):
        data = """ while((a==b)) break;"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Statement", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTStatementWhile'>")
        self.assertEqual(parsed.WHILE, 'while')
        self.assertEqual(parsed.RPAREN, ')')
        self.assertEqual(parsed.LPAREN, '(')  
        self.assertNotEqual(parsed.Expression, None)
        self.assertNotEqual(parsed.Statement, None)

    def test_p_Statement_WHILE_Invalid(self):
        data = """while((a==b)) break"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Statement", data)
        self.assertEqual(parsed, None)

    def test_p_Statement_SWITCH(self):
        data = """ switch((true)) {default :}"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Statement", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTStatementSwitch'>")
        self.assertEqual(parsed.SWITCH, 'switch')
        self.assertEqual(parsed.RPAREN, ')')
        self.assertEqual(parsed.LPAREN, '(')  
        self.assertNotEqual(parsed.Expression, None)
        self.assertNotEqual(parsed.CaseBlock, None)

    def test_p_Statement_SWITCH_Invalid(self):
        data = """ switch((true) {default :}"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Statement", data)
        self.assertEqual(parsed, None)
        
    def test_p_Statement_IF(self):
        data = """ if (a == b) cout << true; """
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Statement", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTStatementIF'>")
        self.assertEqual(parsed.IF, 'if')
        self.assertEqual(parsed.RPAREN, ')')
        self.assertEqual(parsed.LPAREN, '(')  
        self.assertNotEqual(parsed.Expression, None)
        self.assertNotEqual(parsed.Statement, None)

    def test_p_Statement_IF_IF(self):
        data = """ {
            if (a + b) break;
            if ((a==b)) cout << false;
        }"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Statement", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTStatementMultipleStatement'>")
        self.assertEqual(str(parsed.MultipleStatement.Statement.__class__), "<class 'AST.ASTStatementIF'>")
        self.assertEqual(str(parsed.MultipleStatement.MultipleStatement.Statement.__class__), "<class 'AST.ASTStatementIF'>")

    def test_p_Statement_IF_ELSE(self):
        data = """ if ((a == b)) cout << true;
                    else cout << false;"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Statement", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTStatementIFELSE'>")
        self.assertEqual(parsed.IF, 'if')
        self.assertEqual(parsed.ELSE, 'else')
        self.assertEqual(parsed.RPAREN, ')')
        self.assertEqual(parsed.LPAREN, '(')  
        self.assertNotEqual(parsed.Expression, None)
        self.assertNotEqual(parsed.Statement, None)
        self.assertNotEqual(parsed.Statement2, None)

    def test_p_Statement_IF_ELSE_Else_Invalid(self):
        data = """ if ((a == b)) cout << true;
                    else cout << false;
                    else true"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Statement", data)
        self.assertEqual(parsed, None)

    def test_p_Statement_IF_IF_ELSE(self):
        data = """ {
            if (a + b) break;
            if ((a==b)) cout << false;
            else false;
        }"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Statement", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTStatementMultipleStatement'>")
        self.assertEqual(str(parsed.MultipleStatement.Statement.__class__), "<class 'AST.ASTStatementIF'>")
        self.assertEqual(str(parsed.MultipleStatement.MultipleStatement.Statement.__class__), "<class 'AST.ASTStatementIFELSE'>")

    def test_p_Statement_IF_Else_Invalid(self):
        data = """ switch((true) {default :}"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("Statement", data)
        self.assertEqual(parsed, None)

    def test_p_VariableDeclaration_Void_NOLR_NOInitial(self):
        data = """ void test;"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("VariableDeclaration", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTVariableDeclaration'>")
        self.assertEqual(parsed.Type, 'void')
        self.assertEqual(parsed.LRSquare, None)
        self.assertEqual(parsed.ID, 'test')
        self.assertEqual(parsed.Initializer.Initializer, None)
        self.assertEqual(parsed.SEMICOLON, ';')
        
    def test_p_VariableDeclaration_Void_NOLR_Initial(self):
        data = """ void test = true;"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("VariableDeclaration", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTVariableDeclaration'>")
        self.assertEqual(parsed.Type, 'void')
        self.assertEqual(parsed.LRSquare, None)
        self.assertEqual(parsed.ID, 'test')
        self.assertNotEqual(parsed.Initializer.Initializer, None)
        self.assertEqual(parsed.SEMICOLON, ';')

    def test_p_VariableDeclaration_Void_LR_NOInitial(self):
        data = """ void[] test ;"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("VariableDeclaration", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTVariableDeclaration'>")
        self.assertEqual(parsed.Type, 'void')
        self.assertNotEqual(parsed.LRSquare, None)
        self.assertEqual(parsed.ID, 'test')
        self.assertEqual(parsed.Initializer.Initializer, None)
        self.assertEqual(parsed.SEMICOLON, ';')

    def test_p_VariableDeclaration_Void_LR_Initial(self):
        data = """ void[] test = false;"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("VariableDeclaration", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTVariableDeclaration'>")
        self.assertEqual(parsed.Type, 'void')
        self.assertNotEqual(parsed.LRSquare, None)
        self.assertEqual(parsed.ID, 'test')
        self.assertNotEqual(parsed.Initializer.Initializer, None)
        self.assertEqual(parsed.SEMICOLON, ';')

    def test_p_VariableDeclaration_int_NOLR_NOInitial(self):
        data = """ int test;"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("VariableDeclaration", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTVariableDeclaration'>")
        self.assertEqual(parsed.Type, 'int')
        self.assertEqual(parsed.LRSquare, None)
        self.assertEqual(parsed.ID, 'test')
        self.assertEqual(parsed.Initializer.Initializer, None)
        self.assertEqual(parsed.SEMICOLON, ';')
        
    def test_p_VariableDeclaration_int_NOLR_Initial(self):
        data = """ int test = true;"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("VariableDeclaration", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTVariableDeclaration'>")
        self.assertEqual(parsed.Type, 'int')
        self.assertEqual(parsed.LRSquare, None)
        self.assertEqual(parsed.ID, 'test')
        self.assertNotEqual(parsed.Initializer.Initializer, None)
        self.assertEqual(parsed.SEMICOLON, ';')

    def test_p_VariableDeclaration_int_LR_NOInitial(self):
        data = """ int[] test ;"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("VariableDeclaration", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTVariableDeclaration'>")
        self.assertEqual(parsed.Type, 'int')
        self.assertNotEqual(parsed.LRSquare, None)
        self.assertEqual(parsed.ID, 'test')
        self.assertEqual(parsed.Initializer.Initializer, None)
        self.assertEqual(parsed.SEMICOLON, ';')

    def test_p_VariableDeclaration_int_LR_Initial(self):
        data = """ int[] test = false;"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("VariableDeclaration", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTVariableDeclaration'>")
        self.assertEqual(parsed.Type, 'int')
        self.assertNotEqual(parsed.LRSquare, None)
        self.assertEqual(parsed.ID, 'test')
        self.assertNotEqual(parsed.Initializer.Initializer, None)
        self.assertEqual(parsed.SEMICOLON, ';')

    def test_p_VariableDeclaration_char_NOLR_NOInitial(self):
        data = """ char test;"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("VariableDeclaration", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTVariableDeclaration'>")
        self.assertEqual(parsed.Type, 'char')
        self.assertEqual(parsed.LRSquare, None)
        self.assertEqual(parsed.ID, 'test')
        self.assertEqual(parsed.Initializer.Initializer, None)
        self.assertEqual(parsed.SEMICOLON, ';')
        
    def test_p_VariableDeclaration_char_NOLR_Initial(self):
        data = """ char test = true;"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("VariableDeclaration", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTVariableDeclaration'>")
        self.assertEqual(parsed.Type, 'char')
        self.assertEqual(parsed.LRSquare, None)
        self.assertEqual(parsed.ID, 'test')
        self.assertNotEqual(parsed.Initializer.Initializer, None)
        self.assertEqual(parsed.SEMICOLON, ';')

    def test_p_VariableDeclaration_char_LR_NOInitial(self):
        data = """ char[] test ;"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("VariableDeclaration", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTVariableDeclaration'>")
        self.assertEqual(parsed.Type, 'char')
        self.assertNotEqual(parsed.LRSquare, None)
        self.assertEqual(parsed.ID, 'test')
        self.assertEqual(parsed.Initializer.Initializer, None)
        self.assertEqual(parsed.SEMICOLON, ';')

    def test_p_VariableDeclaration_char_LR_Initial(self):
        data = """ char[] test = false;"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("VariableDeclaration", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTVariableDeclaration'>")
        self.assertEqual(parsed.Type, 'char')
        self.assertNotEqual(parsed.LRSquare, None)
        self.assertEqual(parsed.ID, 'test')
        self.assertNotEqual(parsed.Initializer.Initializer, None)
        self.assertEqual(parsed.SEMICOLON, ';')

    def test_p_VariableDeclaration_bool_NOLR_NOInitial(self):
        data = """ bool test;"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("VariableDeclaration", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTVariableDeclaration'>")
        self.assertEqual(parsed.Type, 'bool')
        self.assertEqual(parsed.LRSquare, None)
        self.assertEqual(parsed.ID, 'test')
        self.assertEqual(parsed.Initializer.Initializer, None)
        self.assertEqual(parsed.SEMICOLON, ';')
        
    def test_p_VariableDeclaration_bool_NOLR_Initial(self):
        data = """ bool test = true;"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("VariableDeclaration", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTVariableDeclaration'>")
        self.assertEqual(parsed.Type, 'bool')
        self.assertEqual(parsed.LRSquare, None)
        self.assertEqual(parsed.ID, 'test')
        self.assertNotEqual(parsed.Initializer.Initializer, None)
        self.assertEqual(parsed.SEMICOLON, ';')

    def test_p_VariableDeclaration_bool_LR_NOInitial(self):
        data = """ bool[] test ;"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("VariableDeclaration", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTVariableDeclaration'>")
        self.assertEqual(parsed.Type, 'bool')
        self.assertNotEqual(parsed.LRSquare, None)
        self.assertEqual(parsed.ID, 'test')
        self.assertEqual(parsed.Initializer.Initializer, None)
        self.assertEqual(parsed.SEMICOLON, ';')

    def test_p_VariableDeclaration_bool_LR_Initial(self):
        data = """ bool[] test = false;"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("VariableDeclaration", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTVariableDeclaration'>")
        self.assertEqual(parsed.Type, 'bool')
        self.assertNotEqual(parsed.LRSquare, None)
        self.assertEqual(parsed.ID, 'test')
        self.assertNotEqual(parsed.Initializer.Initializer, None)
        self.assertEqual(parsed.SEMICOLON, ';')

    def test_p_VariableDeclaration_string_NOLR_NOInitial(self):
        data = """ string test;"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("VariableDeclaration", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTVariableDeclaration'>")
        self.assertEqual(parsed.Type, 'string')
        self.assertEqual(parsed.LRSquare, None)
        self.assertEqual(parsed.ID, 'test')
        self.assertEqual(parsed.Initializer.Initializer, None)
        self.assertEqual(parsed.SEMICOLON, ';')
        
    def test_p_VariableDeclaration_string_NOLR_Initial(self):
        data = """ string test = true;"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("VariableDeclaration", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTVariableDeclaration'>")
        self.assertEqual(parsed.Type, 'string')
        self.assertEqual(parsed.LRSquare, None)
        self.assertEqual(parsed.ID, 'test')
        self.assertNotEqual(parsed.Initializer.Initializer, None)
        self.assertEqual(parsed.SEMICOLON, ';')

    def test_p_VariableDeclaration_string_LR_NOInitial(self):
        data = """ string[] test ;"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("VariableDeclaration", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTVariableDeclaration'>")
        self.assertEqual(parsed.Type, 'string')
        self.assertNotEqual(parsed.LRSquare, None)
        self.assertEqual(parsed.ID, 'test')
        self.assertEqual(parsed.Initializer.Initializer, None)
        self.assertEqual(parsed.SEMICOLON, ';')

    def test_p_VariableDeclaration_string_LR_Initial(self):
        data = """ string[] test = false;"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("VariableDeclaration", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTVariableDeclaration'>")
        self.assertEqual(parsed.Type, 'string')
        self.assertNotEqual(parsed.LRSquare, None)
        self.assertEqual(parsed.ID, 'test')
        self.assertNotEqual(parsed.Initializer.Initializer, None)
        self.assertEqual(parsed.SEMICOLON, ';')

    def test_p_VariableDeclaration_id_NOLR_NOInitial(self):
        data = """ id test;"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("VariableDeclaration", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTVariableDeclaration'>")
        self.assertEqual(parsed.Type, 'id')
        self.assertEqual(parsed.LRSquare, None)
        self.assertEqual(parsed.ID, 'test')
        self.assertEqual(parsed.Initializer.Initializer, None)
        self.assertEqual(parsed.SEMICOLON, ';')
        
    def test_p_VariableDeclaration_id_NOLR_Initial(self):
        data = """ id test = true;"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("VariableDeclaration", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTVariableDeclaration'>")
        self.assertEqual(parsed.Type, 'id')
        self.assertEqual(parsed.LRSquare, None)
        self.assertEqual(parsed.ID, 'test')
        self.assertNotEqual(parsed.Initializer.Initializer, None)
        self.assertEqual(parsed.SEMICOLON, ';')

    def test_p_VariableDeclaration_id_LR_NOInitial(self):
        data = """ id[] test ;"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("VariableDeclaration", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTVariableDeclaration'>")
        self.assertEqual(parsed.Type, 'id')
        self.assertNotEqual(parsed.LRSquare, None)
        self.assertEqual(parsed.ID, 'test')
        self.assertEqual(parsed.Initializer.Initializer, None)
        self.assertEqual(parsed.SEMICOLON, ';')

    def test_p_VariableDeclaration_id_LR_Initial(self):
        data = """ id[] test = false;"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("VariableDeclaration", data)
        self.assertEqual(str(parsed.__class__), "<class 'AST.ASTVariableDeclaration'>")
        self.assertEqual(parsed.Type, 'id')
        self.assertNotEqual(parsed.LRSquare, None)
        self.assertEqual(parsed.ID, 'test')
        self.assertNotEqual(parsed.Initializer.Initializer, None)
        self.assertEqual(parsed.SEMICOLON, ';')

    def test_p_VariableDeclaration_Invalid(self):
        data = """ int[]  = false;"""
        theLexer.theLexerReturnFucntion(data)
        parsed = theParser.ParseTester("VariableDeclaration", data)
        self.assertEqual(parsed, None)

class Test_SymbolTableVisitor(unittest.TestCase):

    def test_basic(self):
        data = """
        void kxi2023 main (){}
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(symbolTable.has_Error, False)

    def test_duplicate_1(self):
        data = """
        void kxi2023 main (){
            int x = 3;
            int x = 2;
        }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(symbolTable.has_Error, True)
        self.assertEqual(symbolTable.errors[0], "Error: symbol x already defined")

    def test_duplicate_class(self):
        data = """
        class TempClass{}
        class TempClass{}

        void kxi2023 main (){
            int x = 3;
        }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(symbolTable.has_Error, True)
        self.assertEqual(symbolTable.errors[0], "Error: class TempClass is already as a class")

    def test_classMain(self):
        data = """
        class main{}
        class Main{}

        void kxi2023 main (){}
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(symbolTable.has_Error, False)

    def test_classConstructors(self):
        data = """
        class Class{
            Class(){}
        }

        void kxi2023 main (){}
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(symbolTable.has_Error, False)

    def test_classConstructors_multiple(self):
        data = """
        class Class{
            Class(){}
            Class(){}
        }

        void kxi2023 main (){}
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(symbolTable.has_Error, True)
        self.assertEqual(symbolTable.errors[0], "Error: Only one constructor is allowed. Class is duplicated.")

    def test_classConstructors_multiple2(self):
        data = """
        class Test{
            Test(){}
            Test(int x){}
        }

        void kxi2023 main (){}
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(symbolTable.has_Error, True)
        self.assertEqual(symbolTable.errors[0], "Error: Only one constructor is allowed. Test is duplicated.")

    def test_classConstructors_wrongName(self):
        data = """
        class Class{
            Test(){}
        }

        void kxi2023 main (){}
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(symbolTable.has_Error, True)
        self.assertEqual(symbolTable.errors[0], "Error: Constructor Test is being called in a class with a different name. Names must be the same for a constructor.")

    def test_class_duplicate(self):
        data = """
        class Temp{
            Temp(){}
        }
        
        class Temp{
            Temp(){}
        }

        void kxi2023 main (){}
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(symbolTable.has_Error, True)
        self.assertEqual(symbolTable.errors[0], "Error: class Temp is already as a class")
        
    def test_methodDeclaration(self):
        data = """
        class Temp{
            Temp(){}
            public int compute(int x) {
                if (x == 0) {
                    return 0;
                } else if (x == 1) {
                    return 1;
                }
                return compute(1-x) + this.compute(x-2);
            }
        }


        void kxi2023 main (){}
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(symbolTable.has_Error, False)
        
    def test_methodDeclaration_duplicate(self):
        data = """
        class Temp{
            Temp(){}
            public int compute(int x) {
                if (x == 0) {
                    return 0;
                } else if (x == 1) {
                    return 1;
                }
                return compute(1-x) + this.compute(x-2);
            }
            public int compute(int x) {
                if (x == 0) {
                    return 0;
                } else if (x == 1) {
                    return 1;
                }
                return compute(1-x) + this.compute(x-2);
            }
        }


        void kxi2023 main (){}
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(symbolTable.has_Error, True)
        self.assertEqual(symbolTable.errors[0], "Error: symbol compute already defined")
        
    def test_methodDeclaration_duplicate_notSameType(self):
        data = """
        class Temp{
            Temp(){}
            public int compute(int x) {
                if (x == 0) {
                    return 0;
                } else if (x == 1) {
                    return 1;
                }
                return compute(1-x) + this.compute(x-2);
            }
            public char compute(int x) {
                if (x == 0) {
                    return 0;
                } else if (x == 1) {
                    return 1;
                }
                return compute(1-x) + this.compute(x-2);
            }
        }


        void kxi2023 main (){}
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(symbolTable.has_Error, True)
        self.assertEqual(symbolTable.errors[0], "Error: symbol compute already defined")

    def test_methodDeclaration_same_name_as_class(self):
        data = """
        class Temp{
            public int Temp(int x) {
                if (x == 0) {
                    return 0;
                } else if (x == 1) {
                    return 1;
                }
                return compute(1-x) + this.compute(x-2);
            }
            private char test;
            public Fibonacci fib = new Fibonacci();
        }


        void kxi2023 main (){}
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(symbolTable.has_Error, True)
        self.assertEqual(symbolTable.errors[0], "Error: method Temp is defined in class with the same name")
        
    def test_DataMemberDeclaration(self):
        data = """
        class Temp{
            Temp(){}
            public int compute(int x) {
                if (x == 0) {
                    return 0;
                } else if (x == 1) {
                    return 1;
                }
                return compute(1-x) + this.compute(x-2);
            }
            private char test;
            public Fibonacci fib = new Fibonacci();
        }


        void kxi2023 main (){}
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(symbolTable.has_Error, False)

    def test_DataMemberDeclaration_duplicate(self):
        data = """
        class Temp{
            Temp(){}
            private char test;
            public int compute(int x) {
                if (x == 0) {
                    return 0;
                } else if (x == 1) {
                    return 1;
                }
                return compute(1-x) + this.compute(x-2);
            }
            private char test;
            public Fibonacci fib = new Fibonacci();
        }


        void kxi2023 main (){}
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(symbolTable.has_Error, True)
        self.assertEqual(symbolTable.errors[0], "Error: symbol test already defined")

    def test_DataMemberDeclaration_duplicate_notSameType(self):
        data = """
        class Temp{
            Temp(){}
            private string test;
            public int compute(int x) {
                if (x == 0) {
                    return 0;
                } else if (x == 1) {
                    return 1;
                }
                return compute(1-x) + this.compute(x-2);
            }
            private char test;
            public Fibonacci fib = new Fibonacci();
        }


        void kxi2023 main (){}
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(symbolTable.has_Error, True)
        self.assertEqual(symbolTable.errors[0], "Error: symbol test already defined")

    def test_DataMemberDeclaration_same_name_as_class(self):
        data = """
        class Temp{
            private string Temp;
            public int compute(int x) {
                if (x == 0) {
                    return 0;
                } else if (x == 1) {
                    return 1;
                }
                return compute(1-x) + this.compute(x-2);
            }
            private char test;
            public Fibonacci fib = new Fibonacci();
        }


        void kxi2023 main (){}
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(symbolTable.has_Error, True)
        self.assertEqual(symbolTable.errors[0], "Error: dataMember Temp is defined in class with the same name")
        
    def test_DataMemberDeclaration_and_MethodDeclaration(self):
        data = """
        class Temp{
            Temp(){}
            public int compute(int x) {
                if (x == 0) {
                    return 0;
                } else if (x == 1) {
                    return 1;
                }
                return compute(1-x) + this.compute(x-2);
            }
            private char test;
            public Fibonacci fib = new Fibonacci();
        }


        void kxi2023 main (){}
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(symbolTable.has_Error, False)
        
    def test_DataMemberDeclaration_and_MethodDeclaration_sameName(self):
        data = """
        class Temp{
            Temp(){}
            public int compute(int x) {
                if (x == 0) {
                    return 0;
                } else if (x == 1) {
                    return 1;
                }
                return compute(1-x) + this.compute(x-2);
            }
            private char compute;
        }


        void kxi2023 main (){}
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(symbolTable.has_Error, True)
        self.assertEqual(symbolTable.errors[0], "Error: symbol compute already defined as a method")
        
    def test_DataMemberDeclaration_and_MethodDeclaration_sameName2(self):
        data = """
        class Temp{
            Temp(){}
            private char compute;
            public int compute(int x) {
                if (x == 0) {
                    return 0;
                } else if (x == 1) {
                    return 1;
                }
                return compute(1-x) + this.compute(x-2);
            }
        }


        void kxi2023 main (){}
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(symbolTable.has_Error, True)
        self.assertEqual(symbolTable.errors[0], "Error: symbol compute already defined as a dataMember")
        
    def test_Method_with_declarations(self):
        data = """
        class Temp{
            Temp(){}
            private char dataMember;
            public int Method(int x) {
                int dataMember;
                if (x == 0) {
                    return 0;
                } else if (x == 1) {
                    return 1;
                }
                return compute(1-x) + this.compute(x-2);
            }
        }


        void kxi2023 main (){}
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(symbolTable.has_Error, False)
        
    def test_Method_with_declarations_nested(self):
        data = """
        class Temp{
            Temp(){}
            private char dataMember;
            public int Method(int x) {
                int dataMember;
                if (x == 0) {
                    int dataMember = 3;
                    return 0;
                } else if (x == 1) {
                    return 1;
                }
                return compute(1-x) + this.compute(x-2);
            }
        }


        void kxi2023 main (){}
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(symbolTable.has_Error, False)
        
    def test_Method_with_declarations_nested_same_name(self):
        data = """
        class Temp{
            Temp(){}
            private char dataMember;
            public int Method(int x) {
                int dataMember;
                if (x == 0) {
                    int dataMember = 3;
                    char x = 4;
                    string Method = "this is a string";
                    return 0;
                } else if (x == 1) {
                    return 1;
                }
                return compute(1-x) + this.compute(x-2);
            }
        }


        void kxi2023 main (){}
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(symbolTable.has_Error, False)
        
    def test_Method_with_declarations_nested_same_name_else(self):
        data = """
        class Temp{
            Temp(){}
            private char dataMember;
            public int Method(int x) {
                int dataMember;
                if (x == 0) {
                    int dataMember = 3;
                    char x = 4;
                    string Method = "this is a string";
                    return 0;
                } else if (x == 1) {
                    int dataMember = 4;
                    return 1;
                }
                return compute(1-x) + this.compute(x-2);
            }
        }


        void kxi2023 main (){}
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(symbolTable.has_Error, False)
        
    def test_Method_with_declarations_nested_same_name_else_error(self):
        data = """
        class Temp{
            Temp(){}
            private char dataMember;
            public int Method(int x) {
                int dataMember;
                if (x == 0) {
                    int dataMember = 3;
                    char x = 4;
                    string Method = "this is a string";
                    return 0;
                } else if (x == 1) {
                    int dataMember = 4;
                    return 1;
                }
                return compute(1-x) + this.compute(x-2);
                bool dataMember = false;
            }
        }


        void kxi2023 main (){}
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(symbolTable.has_Error, True)
        self.assertEqual(symbolTable.errors[0], "Error: symbol dataMember already defined")
        
    def test_Method_with_declarations_nested_same_name_else_error2(self):
        data = """
        class Temp{
            Temp(){}
            private char dataMember;
            public int Method(int x) {
                int dataMember;
                if (x == 0) {
                    int dataMember = 3;
                    char x = 4;
                    string Method = "this is a string";
                    return 0;
                } else if (x == 1) {
                    int dataMember = 4;
                    return 1;
                }
                return compute(1-x) + this.compute(x-2);
                bool dataMember = false;
            }
        }


        void kxi2023 main (){}
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(symbolTable.has_Error, True)
        self.assertEqual(symbolTable.errors[0], "Error: symbol dataMember already defined")
        
    def test_multiple_Method_with_declarations_nested_same_name(self):
        data = """
        class Temp{
            Temp(){}
            private char dataMember;
            public int Method(int x) {
                int dataMember;
                if (x == 0) {
                    int dataMember = 3;
                    char x = 4;
                    string Method = "this is a string";
                    return 0;
                } else if (x == 1) {
                    int dataMember = 4;
                    return 1;
                }
                return compute(1-x) + this.compute(x-2);
            }
            public int Method2(int x) {
                int dataMember;
                if (x == 0) {
                    int dataMember = 3;
                    char x = 4;
                    string Method = "this is a string";
                    return 0;
                } else if (x == 1) {
                    int dataMember = 4;
                    return 1;
                }
                return compute(1-x) + this.compute(x-2);
            }
        }

        void kxi2023 main (){}
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(symbolTable.has_Error, False)

    def test_MethodBody(self):
        data = """
        class Fibonacci {
            Fibonacci() {}
            public int compute(int x) {
                if (x == 0) {
                    return 0;
                } else if (x == 1) {
                    return 1;
                }
                return compute(1-x) + this.compute(x-2);
            }
        }
        
        void kxi2023 main() {
            int main;
            char t;
            int index;
            int i = 0;
            cin >> t;
            cout << t;
            cin >> t;
            cout << t;
            cin >> index;
            while (i <= index) {
               cout << '\\n';
                cout << i;
                cout << ',';
                cout << ' ';
                i = i + 1;
            }

            int[] arrTest = new int[5];
            cout << test.test(5);
            arrTest[1] = 3;

            int a = 0;

            while (a != 10) {
                cin >> a;
                switch (a) {
                    case 1:
                        cout << '-';
                        break;
                    case 0:
                        cout << '.';
                    case 3:
                        cout << ',';
                        break;
                    default:
                        cout << '+';
                }
            }
        }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(symbolTable.has_Error, False)

    def test_MethodBody_nested(self):
        data = """
        class Fibonacci {
            Fibonacci() {}
            public int compute(int x) {
                if (x == 0) {
                    return 0;
                } else if (x == 1) {
                    return 1;
                }
                return compute(1-x) + this.compute(x-2);
            }
        }
        
        void kxi2023 main() {
            int main;
            char t;
            int index;
            int i = 0;
            cin >> t;
            cout << t;
            cin >> t;
            cout << t;
            cin >> index;
            while (i <= index) {
                bool index = false;
                cout << '\\n';
                cout << i;
                if (index == false){
                    int index = 3;
                }
                cout << ',';
                cout << ' ';
                i = i + 1;
            }

            int[] arrTest = new int[5];
            cout << test.test(5);
            arrTest[1] = 3;

            int a = 0;

            while (a != 10) {
                cin >> a;
                switch (a) {
                    case 1:
                        cout << '-';
                        break;
                        int index = 3;
                    case 0:
                        cout << '.';
                        if (a == 0){
                            bool index = false;
                        }
                    case 3:
                        cout << ',';
                        break;
                    default:
                        cout << '+';
                }
            }
        }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(symbolTable.has_Error, False)

    def test_MethodBody_error(self):
        data = """
        class Fibonacci {
            Fibonacci() {}
            public int compute(int x) {
                if (x == 0) {
                    return 0;
                } else if (x == 1) {
                    return 1;
                }
                return compute(1-x) + this.compute(x-2);
            }
        }
        
        void kxi2023 main() {
            int main;
            char t;
            int index;
            int i = 0;
            cin >> t;
            cout << t;
            cin >> t;
            cout << t;
            cin >> index;
            while (i <= index) {
                bool index = false;
                cout << '\\n';
                cout << i;
                if (index == false){
                    int index = 3;
                }
                cout << ',';
                cout << ' ';
                i = i + 1;
            }

            int[] arrTest = new int[5];
            cout << test.test(5);
            arrTest[1] = 3;

            int a = 0;
            int main = 4;
            while (a != 10) {
                cin >> a;
                switch (a) {
                    case 1:
                        cout << '-';
                        break;
                        int index = 3;
                    case 0:
                        cout << '.';
                        if (a == 0){
                            bool index = false;
                        }
                    case 3:
                        cout << ',';
                        break;
                    default:
                        cout << '+';
                }
            }
        }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(symbolTable.has_Error, True)
        self.assertEqual(symbolTable.errors[0], "Error: symbol main already defined")

    def test_object(self):
        data = """
        class Fibonacci {
            Fibonacci() {}
            public int compute(int x) {
                if (x == 0) {
                    return 0;
                } else if (x == 1) {
                    return 1;
                }
                return compute(1-x) + this.compute(x-2);
            }
        }
        
        void kxi2023 main() {
            Fibonacci fib = new Fibonacci();
        }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(symbolTable.has_Error, False)

    def test_object_duplicate(self):
        data = """
        class Fibonacci {
            Fibonacci() {}
            public int compute(int x) {
                if (x == 0) {
                    return 0;
                } else if (x == 1) {
                    return 1;
                }
                return compute(1-x) + this.compute(x-2);
            }
        }
        
        void kxi2023 main() {
            Fibonacci fib = new Fibonacci();
            Fibonacci fib = new Fibonacci();
        }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(symbolTable.has_Error, True)
        self.assertEqual(symbolTable.errors[0], "Error: symbol fib already defined")

    def test_object_same_name_as_Int(self):
        data = """
        class Fibonacci {
            Fibonacci() {}
            public int compute(int x) {
                if (x == 0) {
                    return 0;
                } else if (x == 1) {
                    return 1;
                }
                return compute(1-x) + this.compute(x-2);
            }
        }
        
        void kxi2023 main() {
            Fibonacci fib = new Fibonacci();
            int fib = 4;
        }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(symbolTable.has_Error, True)
        self.assertEqual(symbolTable.errors[0], "Error: fib is already defined as a variable")

    def test_object_same_name_as_Int_2(self):
        data = """
        class Fibonacci {
            Fibonacci() {}
            public int compute(int x) {
                if (x == 0) {
                    return 0;
                } else if (x == 1) {
                    return 1;
                }
                return compute(1-x) + this.compute(x-2);
            }
        }
        
        void kxi2023 main() {
            int fib = 4;
            Fibonacci fib = new Fibonacci();
        }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(symbolTable.has_Error, True)
        self.assertEqual(symbolTable.errors[0], "Error: fib is already defined as an object")

    def test_object_with_no_class(self):
        data = """
        class Fibonacci {
            Fibonacci() {}
            public int compute(int x) {
                if (x == 0) {
                    return 0;
                } else if (x == 1) {
                    return 1;
                }
                return compute(1-x) + this.compute(x-2);
            }
        }
        
        void kxi2023 main() {
            Fibonacci fib = new Fibonacci();
            Fibonaccis fib = new Fibonacci();
        }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(symbolTable.has_Error, True)
        self.assertEqual(symbolTable.errors[0], "Error: symbol fib tried to create an object of Fibonaccis which doesn't exist")

    def test_object_nested(self):
        data = """
        class Fibonacci {
            Fibonacci() {}
            public int compute(int x) {
                if (x == 0) {
                    return 0;
                } else if (x == 1) {
                    return 1;
                }
                return compute(1-x) + this.compute(x-2);
            }
        }
        
        void kxi2023 main() {
            Fibonacci fib = new Fibonacci();
            int a = 0;

            while (a != 10) {
                cin >> a;
                switch (a) {
                    case 1:
                        Fibonacci fib = new Fibonacci();
                        cout << '-';
                        break;
                    case 0:
                        cout << '.';
                    case 3:
                        cout << ',';
                        break;
                    default:
                        Fibonacci fib = new Fibonacci();
                        int a;
                        cout << '+';
                }
            }
        }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(symbolTable.has_Error, False)

    def test_case_error(self):
        data = """
        class Fibonacci {
            Fibonacci() {}
            public int compute(int x) {
                if (x == 0) {
                    return 0;
                } else if (x == 1) {
                    return 1;
                }
                return compute(1-x) + this.compute(x-2);
            }
        }
        
        void kxi2023 main() {
            Fibonacci fib = new Fibonacci();
            int a = 0;

            while (a != 10) {
                cin >> a;
                switch (a) {
                    case 1:
                        Fibonacci fib = new Fibonacci();
                        cout << '-';
                        break;
                    case 0:
                        cout << '.';
                    case 0:
                        cout << '.';
                    case 3:
                        cout << ',';
                        break;
                    default:
                        Fibonacci fib = new Fibonacci();
                        int a;
                        cout << '+';
                }
            }
        }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(symbolTable.has_Error, True)
        self.assertEqual(symbolTable.errors[0], "Error: symbol 0 already defined")

    def test_big_test_pass(self):
        data = """
        class Fibonacci {
            Fibonacci() {}
            public int compute(int x) {
                if (x == 0) {
                    char x = 'a';
                    return 0;
                } else if (x == 1) {
                    return 1;
                }
                return compute(1-x) + this.compute(x-2);
            }
        }
        
        void kxi2023 main() {
            Fibonacci fib = new Fibonacci();
            int a = 0;

            while (a != 10) {
                cin >> a;
                switch (a) {
                    case 1:
                        Fibonacci fib = new Fibonacci();
                        a = 1;
                        cout << '-';
                        break;
                    case 0:
                        cout << fib;
                        cout << '.';
                    case 3:
                        cout << ',';
                        break;
                    default:
                        Fibonacci fib = new Fibonacci();
                        int a;
                        cout << '+';
                }
            }
        }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(symbolTable.has_Error, False)

class Test_UndeclaredVariables(unittest.TestCase):

    def test_basic(self):
        data = """
        // Tests criteria under the C tier
        // (Everything up to B, sequential code in the main function plus functions including recursion, plus objects and primitive array).
        class Fibonacci {
            Fibonacci() {}
            public int compute(int x) {

                if (x == 0) {
                    return 0;
                } else if (x == 1) {
                    return 1;
                }
                return compute(1-x) + this.compute(x-2);
            }
        }

        class Test {
            Test() {}
            public int test(int x) {
                cout << x;
                char l = '\\n';
                cout << '\\n';
                if (x == 5) {
                    cout << this.test(x + 5);
                    cout << '\\n';
                }
                return x + 5;
            }
        }

        void kxi2023 main() {
            char t;
            int index;
            int i = 0;
            Fibonacci fib = new Fibonacci();
            cin >> t;
            cout << t;
            cin >> t;
            cout << t;
            cin >> index;
            while (i <= index) {
                cout << i;
                cout << ',';
                cout << ' ';
                cout << fib.compute(i);
                cout << '\\n';
                i = i + 1;
            }

            int[] arrTest = new int[5];
            Test test = new Test();
            cout << test.test(5);
            cout << '\\n';
            arrTest[1] = 3;

            int a = 0;

            while (a != 10) {
                cin >> a;
                switch (a) {
                    case 1:
                        cout << '-';
                        break;
                    case 0:
                        cout << '.';
                    case 3:
                        cout << ',';
                        break;
                    default:
                        cout << '+';
                }
            }
        }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(symbolTable.has_Error, False)
        undeclaredVariableVistior = UndeclaredVisitor()
        myAST.accept(undeclaredVariableVistior)
        self.assertEqual(undeclaredVariableVistior.has_Error, False)

    def test_undeclared_class(self):
        data = """
        // Tests criteria under the C tier
        // (Everything up to B, sequential code in the main function plus functions including recursion, plus objects and primitive array).
        class Fibonacci {
            Fibonacci() {}
            public int compute(int x) {
                y = 3;
                if (x == 0) {
                    return 0;
                } else if (x == 1) {
                    return 1;
                }
                return compute(1-x) + this.compute(x-2);
            }
        }

        class Test {
            Test() {}
            public int test(int x) {
                cout << x;
                char l = '\\n';
                cout << '\\n';
                if (x == 5) {
                    cout << this.test(x + 5);
                    cout << '\\n';
                }
                return x + 5;
            }
        }

        void kxi2023 main() {
            char t;
            int index;
            int i = 0;
            Fibonacci fib = new Fibonacci();
            cin >> t;
            cout << t;
            cin >> t;
            cout << t;
            cin >> index;
            while (i <= index) {
                cout << i;
                cout << ',';
                cout << ' ';
                cout << fib.compute(i);
                cout << '\\n';
                i = i + 1;
            }

            int[] arrTest = new int[5];
            Test test = new Test();
            cout << test.test(5);
            cout << '\\n';
            arrTest[1] = 3;

            int a = 0;

            while (a != 10) {
                cin >> a;
                switch (a) {
                    case 1:
                        cout << '-';
                        break;
                    case 0:
                        cout << '.';
                    case 3:
                        cout << ',';
                        break;
                    default:
                        cout << '+';
                }
            }
        }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(symbolTable.has_Error, False)
        undeclaredVariableVistior = UndeclaredVisitor()
        myAST.accept(undeclaredVariableVistior)
        self.assertEqual(undeclaredVariableVistior.has_Error, True)
        self.assertEqual(undeclaredVariableVistior.errors[0], "Error: y is used but never declared or used before it is declared")

    def test_undeclared_object(self):
        data = """
        // Tests criteria under the C tier
        // (Everything up to B, sequential code in the main function plus functions including recursion, plus objects and primitive array).

        class Fibonacci {
            Fibonacci() {}
            public int compute(int x) {
                int y = 3;
                if (x == 0) {
                    y = 3;
                    temp = false;
                    return 0;
                } else if (x == 1) {
                    temp = true;
                    return 1;
                }
                return compute(1-x) + this.compute(x-2);
            }
        }

        class Test {
            Test() {}
            public int test(int x) {
                cout << x;
                l = '\\n';
                char l = '\\n';
                cout << '\\n';
                if (x == 5) {
                    cout << this.test(x + 5);
                    cout << '\\n';
                }
                return x + 5;
            }
        }

        void kxi2023 main() {
            char t;
            index = 3;
            int index;
            int i = 0;
            Fibonacci fib = new Fibonacci();
            cin >> t;
            cout << t;
            cin >> t;
            cout << t;
            cin >> index;
            while (i <= index) {
                cout << i;
                cout << ',';
                cout << ' ';
                cout << fib2.compute(i);
                cout << '\\n';
                i = i + 1;
            }

            int[] arrTest = new int[5];
            Test test = new Test();
            cout << test2.test(5);
            cout << '\\n';
            arrTest[1] = 3;

            int a = 0;

            while (a != 10) {
                cin >> a;
                switch (a) {
                    case 1:
                        cout << '-';
                        break;
                    case 0:
                        myvar = 3;
                        cout << '.';
                    case 3:
                        cout << myvar;
                        break;
                    default:
                        cout << '+';
                }
            }
            
        }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(symbolTable.has_Error, False)
        undeclaredVariableVistior = UndeclaredVisitor()
        myAST.accept(undeclaredVariableVistior)
        self.assertEqual(undeclaredVariableVistior.has_Error, True)
        self.assertEqual(undeclaredVariableVistior.errors[0], "Error: temp is used but never declared or used before it is declared")
        self.assertEqual(undeclaredVariableVistior.errors[1], "Error: temp is used but never declared or used before it is declared")
        self.assertEqual(undeclaredVariableVistior.errors[2], "Error: l is used but never declared or used before it is declared")
        self.assertEqual(undeclaredVariableVistior.errors[3], "Error: index is used but never declared or used before it is declared")
        self.assertEqual(undeclaredVariableVistior.errors[4], "Error: fib2 is used but never declared or used before it is declared")
        self.assertEqual(undeclaredVariableVistior.errors[5], "Error: test2 is used but never declared or used before it is declared")
        self.assertEqual(undeclaredVariableVistior.errors[6], "Error: myvar is used but never declared or used before it is declared")
        self.assertEqual(undeclaredVariableVistior.errors[7], "Error: myvar is used but never declared or used before it is declared")

    def test_undeclared_big(self):
        data = """
        // Tests criteria under the C tier
        // (Everything up to B, sequential code in the main function plus functions including recursion, plus objects and primitive array).
        class Fibonacci {
            Fibonacci() {}
            public int compute(int x) {
                int y = 3;
                if (x == 0) {
                    y = 3;
                    temp = false;
                    return 0;
                } else if (x == 1) {
                    temp = true;
                    return 1;
                }
                return compute(1-x) + this.compute(x-2);
            }
        }

        class Test {
            Test() {}
            public int test(int x) {
                cout << x;
                l = '\\n';
                char l = '\\n';
                cout << '\\n';
                if (x == 5) {
                    cout << this.test(x + 5);
                    cout << '\\n';
                }
                return x + 5;
            }
        }

        void kxi2023 main() {
            char t1;
            int index;
            int i = 0;
            Fibonacci fib = new Fibonacci();
            cin >> t1;
            cout << t1;
            cin >> t1;
            cout << t1;
            cin >> index;
            while (i <= index) {
                cout << i;
                cout << ',';
                cout << ' ';
                cout << fib.compute(i);
                cout << '\\n';
                i = i + 1;
            }

            int[] arrTest = new int[5];
            Test test2 = new Test();
            cout << test2.test2(5);
            cout << '\\n';
            arrTest[1] = 3;

            int a = 0;

            while (a != 10) {
                cin >> a;
                switch (a) {
                    case 1:
                        myVar1 = null;
                        cout << '-';
                        break;
                    case 0:
                        cout << '.';
                    case 3:
                        cout << ',';
                        break;
                    default:
                        cout << '+';
                }
            }
            if (1==1) cout << myVar2;
            if (1==1) cout << "1==1\\n";
            if (-1==-1) cout << "-1==-1\\n";
            if (1==2) cout << "1==2 fail\\n";
            if (2==1) cout << "2==1 fail\\n";


            if (1!=2) cout << "1!=2\\n";
            if (2!=1) cout << "2!=1\\n";
            if (1!=1) cout << "1!=1 fail\\n";


            if (1 < 2) cout << "1<2\\n";
            if (1 < 1) cout << "1<1 fail\\n";
            if (2 < 1) cout << "2<1 fail\\n";


            if (2 > 1) cout << "2>1\\n";
            if (1 > 1) cout << "1>1 fail\\n";
            if (1 > 2) cout << "1>2 fail\\n";

            if (1 <= 2) cout << "1<=2\\n";
            if (1 <= 1) cout << "1<=1\\n";
            if (2 <= 1) cout << "2<=1 fail\\n";

            if (2 >= 1) cout << "2>=1\\n";
            if (1 >= 1) cout << "1>=1\\n";
            if (1 >= 2) cout << "1>=2 fail\\n";

            if (-1 == -(1))
                cout << "-1==-(1)\\n";

            if (1 * 2 / 2 + 4 - 5 * 8 / 8 == 0)
                cout << "good math\\n";

            if (     myVar3 == 'a'
                &&   'b' == 'b'
                && !('c' == 'd')
                &&   'c' != 'd'
                &&   'd' <  'e'
                &&   'a' >  'A' )
                cout << "char comparison is good\\n";

            int un_test = 2;
            un_test = +++++++un_test;
            cout << un_test;
            cout << '\\n';


            int x = 1;
            while (x <= 128) {
                cout << "while: ";
                cout << x;
                cout << '\\n';
                myVar4 = true;
                int i = x;
                int j = 0;
                while(j < 3) {
                    cout << "nested while: ";
                    cout << i * 3;
                    cout << '\\n';
                    i *= 3;
                    myVar5 = 12;
                    j += 1;
                }
                x *= 2;
            }

            //x = j = i;
            //cout << x; cout << '\\n';

            // ASSIGNMENT
            cout << "assneq: ";

            int test = 0-1;
            

            test += 1;
            if (test == 0) {
                cout << '+';
            } else {
                cout << '-';
                cout << test;
            }
            cout << '|';

            test -= 1;
            if (test == -1) {
                cout << '+';
            } else {
                cout << '-';
            }
            cout << '|';

            test *= 2;
            myVar6 *= 4;
            if (test == -2) {
                cout << '+';
            } else {
                cout << '-';
            }
            cout << '|';

            test /= 2;
            bool here;
            if (test == -1) {
                bool after;
                cout << '+';
            } else {
                cout << '-';
            }
            cout << '|';
            cout << '\\n';

            // BOOL EXPRESSIONS
            cout << "bool: ";

            bool t = true;
            bool f = false;
            a = 0;
            int b = 1;
            b = myVar7;

            if (t) {
                cout << '+';
            } else {
                cout << '-';
            }
            cout << '|';
            if (t != f) {
                cout << '+';
            } else {
                cout << '-';
            }
            cout << '|';
            if (a < b) {
                cout << '+';
            } else {
                cout << '-';
            }
            cout << '|';
            if (b > a) {
                cout << '+';
            } else {
                cout << '-';
            }
            cout << '|';
            if (a <= 0) {
                cout << '+';
            } else {
                cout << '-';
            }
            cout << '|';
            if (b >= 1) {
                cout << '+';
            } else {
                cout << '-';
            }
            cout << '|';
            cout << '\\n';
            

            // SWITCH CASE
            cout << "switch: ";

            a = 0;
            switch (a) {
                case 1:
                    cout << '-';
                    +myVar8;
                    break;
                case 0:
                    cout << '.';
                case 3:
                    cout << ',';
                default:
                    cout << '+';
            }
            cout << '|';
            cout << '\\n';

            int v1 = 1;
            int v2 = 2;
            int v3 = 3;

            v1 = v2 = v3;

            if (v1 == 3 && v2 == 3 && v3 == 3) cout << "v1 = v2 = v3 pass\\n";
            else cout << "v1 = v2 = v3 fail\\n";

            v1 += v1 = 2;
            if (v1 == 4) cout << "v1 += v1 = 2 pass\\n";
            else cout << "v1 += v1 = 2 fail\\n";

            v1 = v2 = v3 = 1 + 2 + 3;
            if (v1 == 6 && v2 == 6 && v3 == 6) cout << "v1 = v2 = v3 = 1 + 2 + 3 pass\\n";
            else cout << "v1 = v2 = v3 = 1 + 2 + 3 fail\\n";
            Fibonacci fib2 = new MyVar9();
        }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(symbolTable.has_Error, False)
        undeclaredVariableVistior = UndeclaredVisitor()
        myAST.accept(undeclaredVariableVistior)
        self.assertEqual(undeclaredVariableVistior.has_Error, True)
        self.assertEqual(undeclaredVariableVistior.errors[0], "Error: temp is used but never declared or used before it is declared")
        self.assertEqual(undeclaredVariableVistior.errors[1], "Error: temp is used but never declared or used before it is declared")
        self.assertEqual(undeclaredVariableVistior.errors[2], "Error: l is used but never declared or used before it is declared")
        self.assertEqual(undeclaredVariableVistior.errors[3], "Error: myVar1 is used but never declared or used before it is declared")
        self.assertEqual(undeclaredVariableVistior.errors[4], "Error: myVar2 is used but never declared or used before it is declared")
        self.assertEqual(undeclaredVariableVistior.errors[5], "Error: myVar3 is used but never declared or used before it is declared")
        self.assertEqual(undeclaredVariableVistior.errors[6], "Error: myVar4 is used but never declared or used before it is declared")
        self.assertEqual(undeclaredVariableVistior.errors[7], "Error: myVar5 is used but never declared or used before it is declared")
        self.assertEqual(undeclaredVariableVistior.errors[8], "Error: myVar6 is used but never declared or used before it is declared")
        self.assertEqual(undeclaredVariableVistior.errors[9], "Error: myVar7 is used but never declared or used before it is declared")
        self.assertEqual(undeclaredVariableVistior.errors[10], "Error: myVar8 is used but never declared or used before it is declared")

    def test_undeclared_method(self):
        data = """
        // Tests criteria under the C tier
        // (Everything up to B, sequential code in the main function plus functions including recursion, plus objects and primitive array).
        class Fibonacci {
            Fibonacci() {}
            public int compute(int x) {
                if (x == 0) {
                    return 0;
                } else if (x == 1) {
                    return 1;
                }
                return compute(1-x) + this.compute(x-2);
            }
        }

        class Test {
            Test() {}
            public int test(int x) {
                cout << x;
                char l = '\\n';
                cout << '\\n';
                if (x == 5) {
                    cout << this.test(x + 5);
                    cout << '\\n';
                }
                return x + 5;
            }
        }

        void kxi2023 main() {
            ThisIsATest();
            char t;
            int index;
            int i = 0;
            Fibonacci fib = new Fibonacci();
            cin >> t;
            cout << t;
            cin >> t;
            cout << t;
            cin >> index;
            while (i <= index) {
                cout << i;
                cout << ',';
                cout << ' ';
                cout << fib.compute(i);
                cout << '\\n';
                i = i + 1;
            }

            int[] arrTest = new int[5];
            Test test = new Test();
            cout << test.test(5);
            cout << '\\n';
            arrTest[1] = 3;

            int a = 0;

            while (a != 10) {
                cin >> a;
                switch (a) {
                    case 1:
                        cout << '-';
                        break;
                    case 0:
                        cout << '.';
                    case 3:
                        cout << ',';
                        break;
                    default:
                        cout << '+';
                }
            }
        }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(symbolTable.has_Error, False)
        undeclaredVariableVistior = UndeclaredVisitor()
        myAST.accept(undeclaredVariableVistior)
        self.assertEqual(undeclaredVariableVistior.has_Error, True)
        self.assertEqual(undeclaredVariableVistior.errors[0], "Error: ThisIsATest is used but never declared or used before it is declared")

class Test_ObjectInitializerAndType(unittest.TestCase):

    def test_basic(self):
        data = """
        // Tests criteria under the C tier
        // (Everything up to B, sequential code in the main function plus functions including recursion, plus objects and primitive array).
        class Fibonacci {
            Fibonacci() {}
            public Test myTest;
            public Test myTest2 = new Test();
            public int compute(int x) {

                if (x == 0) {
                    return 0;
                } else if (x == 1) {
                    return 1;
                }
                return compute(1-x) + this.compute(x-2);
            }
        }

        class Test {
            Test() {}
            private Fibonacci fib;
            public Fibonacci fib2 = new Fibonacci();
            private Fibonacci[] fib3 = new Fibonacci[0];
            public int test(int x) {
                cout << x;
                char l = '\\n';
                cout << '\\n';
                if (x == 5) {
                    cout << this.test(x + 5);
                    cout << '\\n';
                }
                return x + 5;
            }
        }

        void kxi2023 main() {
            char t;
            int index;
            int i = 0;
            Fibonacci fib = new Fibonacci();
            Fibonacci[] fibs = new Fibonacci[0];
            cin >> t;
            cout << t;
            cin >> t;
            cout << t;
            cin >> index;
            while (i <= index) {
                cout << i;
                cout << ',';
                cout << ' ';
                cout << fib.compute(i);
                cout << '\\n';
                i = i + 1;
            }

            int[] arrTest = new int[5];
            Test test = new Test();
            cout << test.test(5);
            cout << '\\n';
            arrTest[1] = 3;

            int a = 0;

            while (a != 10) {
                cin >> a;
                switch (a) {
                    case 1:
                        cout << '-';
                        break;
                    case 0:
                        cout << '.';
                    case 3:
                        cout << ',';
                        break;
                    default:
                        cout << '+';
                }
            }
        }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(symbolTable.has_Error, False)
        undeclaredVariableVistior = UndeclaredVisitor()
        myAST.accept(undeclaredVariableVistior)
        self.assertEqual(undeclaredVariableVistior.has_Error, False)
        objectInitializerAndTypeVisitor = ObjectInitializerAndTypeVisitor()
        symbols = symbolTable.symbol_tables
        objectInitializerAndTypeVisitor.symbol_tables = symbols
        myAST.accept(objectInitializerAndTypeVisitor)
        self.assertEqual(objectInitializerAndTypeVisitor.has_Error, False)

    def test_errors_with_Objects_and_Types(self):
            data = """
            // Tests criteria under the C tier
            // (Everything up to B, sequential code in the main function plus functions including recursion, plus objects and primitive array).
            class Fibonacci {
                Fibonacci(notInt X, notTest tesss, int aaa) {}
                public Test myTest = new NotATest();
                public Test myTest2 = new Test[1];
                public int compute(int x) {

                    if (x == 0) {
                        return 0;
                    } else if (x == 1) {
                        return 1;
                    }
                    return compute(1-x) + this.compute(x-2);
                }
            }

            class Test {
                Test() {}
                private Fibonacci fib;
                public Fibonacci[] fib2 = new Fibonacci();
                private Fibonacci[] fib3 = new Fibonacci();
                public void test(int x) {
                    cout << x;
                    char l = '\\n';
                    cout << '\\n';
                    if (x == 5) {
                        cout << this.test(x + 5);
                        cout << '\\n';
                    }
                    return x + 5;
                }
            }

            void kxi2023 main() {
                char t;
                int index;
                int i = 0;
                Fibonacci fib = new Fibonaccisss();
                Fibonacci[] fibs = new Fibonacci[0];
                cin >> t;
                cout << t;
                cin >> t;
                cout << t;
                cin >> index;
                while (i <= index) {
                    cout << i;
                    cout << ',';
                    cout << ' ';
                    cout << fib.compute(i);
                    cout << '\\n';
                    i = i + 1;
                }

                int[] arrTest = new int[5];
                
                int[] arrTest1 = new void[5];
                int[] arrTest2 = new void();
                int arrTest3 = new void[5];
                Test test = new Test();
                cout << test.test(5);
                cout << '\\n';
                arrTest[1] = 3;

                Fibonacci fibfff = new Test();
                int a = 0;

                while (a != 10) {
                    cin >> a;
                    switch (a) {
                        case 1:
                            cout << '-';
                            break;
                        case 0:
                            cout << '.';
                        case 3:
                            cout << ',';
                            break;
                        default:
                            cout << '+';
                    }
                }
            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(symbolTable.has_Error, False)
            undeclaredVariableVistior = UndeclaredVisitor()
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(undeclaredVariableVistior.has_Error, False)
            objectInitializerAndTypeVisitor = ObjectInitializerAndTypeVisitor()
            symbols = symbolTable.symbol_tables
            objectInitializerAndTypeVisitor.symbol_tables = symbols
            myAST.accept(objectInitializerAndTypeVisitor)
            self.assertEqual(objectInitializerAndTypeVisitor.has_Error, True)
            self.assertEqual(objectInitializerAndTypeVisitor.errors[0], "Error: there is no class 'notInt'. Attempting to use a variable of that type is illegal")
            self.assertEqual(objectInitializerAndTypeVisitor.errors[1], "Error: there is no class 'notTest'. Attempting to use a variable of that type is illegal")
            self.assertEqual(objectInitializerAndTypeVisitor.errors[2], 'Error: Attempting to initalize object Test myTest with invalid type of NotATest')
            self.assertEqual(objectInitializerAndTypeVisitor.errors[3], "Error: there is no class 'NotATest'. Attempting to use a variable of that type is illegal")
            self.assertEqual(objectInitializerAndTypeVisitor.errors[4], 'Error: error when attempting to initialize object Test myTest2')
            self.assertEqual(objectInitializerAndTypeVisitor.errors[5], 'Error: error when attempting to initialize object Fibonacci fib2')
            self.assertEqual(objectInitializerAndTypeVisitor.errors[6], 'Error: error when attempting to initialize object Fibonacci fib3')
            self.assertEqual(objectInitializerAndTypeVisitor.errors[7], 'Error: Attempting to initalize object Fibonacci fib with invalid type of Fibonaccisss')
            self.assertEqual(objectInitializerAndTypeVisitor.errors[8], "Error: there is no class 'Fibonaccisss'. Attempting to use a variable of that type is illegal")
            self.assertEqual(objectInitializerAndTypeVisitor.errors[9], 'Error: Attempting to initalize object int arrTest1 with invalid type of void')
            self.assertEqual(objectInitializerAndTypeVisitor.errors[10], 'Error: Attempting to initalize object int arrTest2 with invalid type of void')
            self.assertEqual(objectInitializerAndTypeVisitor.errors[11], "Error : can not use 'NEW' with type void when arrTest2 is an array type")
            self.assertEqual(objectInitializerAndTypeVisitor.errors[12], 'Error: Attempting to initalize object int arrTest3 with invalid type of void')
            self.assertEqual(objectInitializerAndTypeVisitor.errors[13], "Error : can not use 'NEW' with type void without it setting variable arrTest3 to be an array")
            self.assertEqual(objectInitializerAndTypeVisitor.errors[14], "Error: Attempting to initalize object Fibonacci fibfff with invalid type of Test")

#param:
    #test for constructor with the same instance
    #test for contsurctor with other object
    #test for constructo wirh invalid object type

#test New with invalid params