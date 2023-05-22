import unittest
import SupportFiles.theLexer as theLexer
import SupportFiles.theParser as theParser
from SemanticsVisitors.CreateSymbolTableVisitor import SymbolTableVisitor
from SemanticsVisitors.UndeclaredVisitor import UndeclaredVisitor
from SemanticsVisitors.TypeChecking import TypeChecking
from SemanticsVisitors.AssignmentVisitor import AssignmentVisitor
from SemanticsVisitors.BreakVisitor import BreakVisitor

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
        data = """
        ()
        """
        temp = theLexer.theLexerReturnFucntion(data)
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
        self.assertEqual(len(symbolTable.errors), 0)

    def test_main_duplicate(self):
        data = """
            void kxi2023 main(){
                int x = 3;
                int x = 2;
            }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertNotEqual(len(symbolTable.errors), 0)
        self.assertEqual(symbolTable.errors[0], "Error: symbol x already defined. Around line 4")

    def test_main_duplicate_nested(self):
        data = """
            void kxi2023 main(){
                int x = 3;
                if (2 ==2){
                    int x = 2;
                }
            }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertNotEqual(len(symbolTable.errors), 0)
        self.assertEqual(symbolTable.errors[0], "Error: symbol x already defined. Around line 5")

    def test_main_duplicate_in_class(self):
        data = """
            class TempClass{
                private int x;
            }
            void kxi2023 main(){
                int x = 3;
                if (2 ==2){
                    x = 2;
                }
            }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(len(symbolTable.errors), 0)

    def test_main_duplicate_in_separate_class(self):
        data = """
            class TempClass{
                private int x;
            }
            class OtherClass{
                private int x;
            }
            void kxi2023 main(){
                int x = 3;
                if (2 ==2){
                    x = 2;
                }
            }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(len(symbolTable.errors), 0)

    def test_duplicate_class(self):
        data = """
            class TempClass{
                private int x;
            }
            class TempClass{
                private bool s;
            }
            void kxi2023 main(){
                int x = 3;
                if (2 ==2){
                    x = 2;
                }
            }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertNotEqual(len(symbolTable.errors), 0)
        self.assertEqual(symbolTable.errors[0], "Error: class TempClass is already as a class. Around line 5")

    def test_same_variable_different_type(self):
        data = """
            class TempClass{
                private int x;
            }
            void kxi2023 main(){
                int[] x = new int[5];
                if (2 ==2){
                    bool x = false;
                }
            }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertNotEqual(len(symbolTable.errors), 0)
        self.assertEqual(symbolTable.errors[0], "Error: symbol x already defined. Around line 8")
        
    def test_duplicate_dataMembers(self):
        data = """
            class TempClass{
                private int x;
                private int x;
            }
            void kxi2023 main(){
                int x = 3;
                if (2 ==2){
                    x = 2;
                }
            }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertNotEqual(len(symbolTable.errors), 0)
        self.assertEqual(symbolTable.errors[0], "Error: symbol x already defined. Around line 4")
        
    def test_duplicate_dataMembers_differnet_types(self):
        data = """
            class TempClass{
                private int x;
                public bool x;
            }
            void kxi2023 main(){
                int x = 3;
                if (2 ==2){
                    x = 2;
                }
            }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertNotEqual(len(symbolTable.errors), 0)
        self.assertEqual(symbolTable.errors[0], "Error: symbol x already defined. Around line 4")
        
    def test_duplicate_dataMembers_differnet_types_array(self):
        data = """
            class TempClass{
                private int[] x;
                private int x;
            }
            void kxi2023 main(){
                int x = 3;
                if (2 ==2){
                    x = 2;
                }
            }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertNotEqual(len(symbolTable.errors), 0)
        self.assertEqual(symbolTable.errors[0], "Error: symbol x already defined. Around line 4")
        
    def test_duplicate_methods(self):
        data = """
            class TempClass{
                private string x (){}
                public string x (){}
                
            }
            void kxi2023 main(){
                int x = 3;
                if (2 ==2){
                    x = 2;
                }
            }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertNotEqual(len(symbolTable.errors), 0)
        self.assertEqual(symbolTable.errors[0], "Error: symbol x already defined. Around line 4")
        
    def test_duplicate_methods_array(self):
        data = """
            class TempClass{
                private string x (){}
                public string[] x (){}
                
            }
            void kxi2023 main(){
                int x = 3;
                if (2 ==2){
                    x = 2;
                }
            }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertNotEqual(len(symbolTable.errors), 0)
        self.assertEqual(symbolTable.errors[0], "Error: symbol x already defined. Around line 4")
        
    def test_methods_duplicate_nested(self):
        data = """
            class TempClass{
                private string x (){
                    int y;
                }
                public string[] z (){
                    int y;
                }
                
            }
            void kxi2023 main(){
                int x = 3;
                if (2 ==2){
                    x = 2;
                }
            }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(len(symbolTable.errors), 0)
        
    def test_methods_duplicate_nested_dataMember(self):
        data = """
            class TempClass{
                private bool y;
                private string x (){
                    int y;
                }
                public string[] z (){
                    int y;
                }
                
            }
            void kxi2023 main(){
                int y = 3;
                if (2 ==2){
                    y = 2;
                }
            }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(len(symbolTable.errors), 0)
        
    def test_case(self):
        data = """
            class TempClass{
                private bool y;
                private string x (){
                    int y;
                }
                public string[] z (){
                    int y;
                }
                
            }
            void kxi2023 main(){
                int y = 3;
                if (2 ==2){
                    y = 2;
                }
                int a = 0;
                    a = 0;
                switch (a) {
                    case 1:
                        cout << '-';
                        break;
                    case 0:
                        cout << '.';
                    case 3:
                        cout << ',';
                    default:
                        cout << '+';
                }
            }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(len(symbolTable.errors), 0)
        
    def test_case_duplicate(self):
        data = """
            class TempClass{
                private bool y;
                private string x (){
                    int y;
                }
                public string[] z (){
                    int y;
                }
                
            }
            void kxi2023 main(){
                int y = 3;
                if (2 ==2){
                    y = 2;
                }
                int a = 0;
                    a = 0;
                switch (a) {
                    case 1:
                        cout << '-';
                        break;
                    case 1:
                        cout << '-';
                        break;
                    case 0:
                        cout << '.';
                    case 3:
                        cout << ',';
                    default:
                        cout << '+';
                }
            }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(len(symbolTable.errors), 0)
        
    def test_case_duplicate_block(self):
        data = """
            class TempClass{
                private bool y;
                private string x (){
                    int y;
                }
                public string[] z (){
                    int y;
                }
                
            }
            void kxi2023 main(){
                int y = 3;
                if (2 ==2){
                    y = 2;
                }
                int a = 0;
                    a = 0;
                switch (a) {
                    case 1:
                        cout << '-';
                        break;
                    case 1:
                        cout << '-';
                        break;
                    case 0:
                        cout << '.';
                    case 3:
                        cout << ',';
                    default:
                        cout << '+';
                }
                switch (a) {
                    case 1:
                        cout << '-';
                        break;
                    case 1:
                        cout << '-';
                        break;
                    case 0:
                        cout << '.';
                    case 3:
                        cout << ',';
                    default:
                        cout << '+';
                }
            }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(len(symbolTable.errors), 0)
        
    def test_case_nested(self):
        data = """
            class TempClass{
                private bool y;
                private string x (){
                    int y;
                }
                public string[] z (){
                    int y;
                }
                
            }
            void kxi2023 main(){
                int y = 3;
                if (2 ==2){
                    y = 2;
                }
                int a = 0;
                    a = 0;
                switch (a) {
                    case 1:
                        cout << '-';
                        int a;
                        break;
                    case 0:
                        cout << '.';
                    case 3:
                        cout << ',';
                    default:
                        cout << '+';
                }
            }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertNotEqual(len(symbolTable.errors), 0)
        self.assertEqual(symbolTable.errors[0], "Error: symbol a already defined. Around line 22")

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
        self.assertEqual(len(symbolTable.errors), 0)

    def test_constructor_Class(self):
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
        self.assertEqual(len(symbolTable.errors), 0)

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
        self.assertNotEqual(len(symbolTable.errors), 0)
        self.assertEqual(symbolTable.errors[0], "Error: Only one constructor is allowed. Class is duplicated. Around line 4")

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
        self.assertNotEqual(len(symbolTable.errors), 0)
        self.assertEqual(symbolTable.errors[0], "Error: Only one constructor is allowed. Test is duplicated. Around line 4")

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
        self.assertNotEqual(len(symbolTable.errors), 0)
        self.assertEqual(symbolTable.errors[0], "Error: Constructor Test is being called in a class with a different name. Names must be the same for a constructor. Around line 3")

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
        self.assertNotEqual(len(symbolTable.errors), 0)
        self.assertEqual(symbolTable.errors[0], "Error: class Temp is already as a class. Around line 6")
        
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
        self.assertEqual(len(symbolTable.errors), 0)

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
        self.assertNotEqual(len(symbolTable.errors), 0)
        self.assertEqual(symbolTable.errors[0], "Error: symbol compute already defined. Around line 12")
        
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
        self.assertNotEqual(len(symbolTable.errors), 0)
        self.assertEqual(symbolTable.errors[0], "Error: symbol compute already defined. Around line 12")

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
        self.assertNotEqual(len(symbolTable.errors), 0)
        self.assertEqual(symbolTable.errors[0], "Error: method Temp is defined in class with the same name. Around line 3")

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
        }


        void kxi2023 main (){}
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(len(symbolTable.errors), 0)

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
        self.assertNotEqual(len(symbolTable.errors), 0)
        self.assertEqual(symbolTable.errors[0], "Error: symbol test already defined. Around line 13")

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
        self.assertNotEqual(len(symbolTable.errors), 0)
        self.assertEqual(symbolTable.errors[0], "Error: symbol test already defined. Around line 13")

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
        self.assertNotEqual(len(symbolTable.errors), 0)
        self.assertEqual(symbolTable.errors[0], "Error: dataMember Temp is defined in class with the same name. Around line 3")
        
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
        }


        void kxi2023 main (){}
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(len(symbolTable.errors), 0)
        
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
        self.assertNotEqual(len(symbolTable.errors), 0)
        self.assertEqual(symbolTable.errors[0], "Error: symbol compute already defined as a method. Around line 12")
        
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
        self.assertNotEqual(len(symbolTable.errors), 0)
        self.assertEqual(symbolTable.errors[0], "Error: symbol compute already defined as a dataMember. Around line 5")
        
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
        self.assertEqual(len(symbolTable.errors), 0)
        
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
        self.assertNotEqual(len(symbolTable.errors), 0)
        self.assertEqual(symbolTable.errors[0], "Error: symbol dataMember already defined. Around line 8")
        
    def test_Method_with_declarations_nested_same_name(self):
        data = """
        class Temp{
            Temp(){}
            private char dataMember;
            public int Method(int x) {
                int dataMember;
                if (x == 0) {
                    char y = 4;
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
        self.assertEqual(len(symbolTable.errors), 0)
        
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
        self.assertNotEqual(len(symbolTable.errors), 0)
        self.assertEqual(symbolTable.errors[0], "Error: symbol dataMember already defined. Around line 8")
        self.assertEqual(symbolTable.errors[1], "Error: symbol x already defined. Around line 9")
        self.assertEqual(symbolTable.errors[2], "Error: symbol dataMember already defined. Around line 13")
        
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
        self.assertNotEqual(len(symbolTable.errors), 0)
        self.assertEqual(symbolTable.errors[0], "Error: symbol dataMember already defined. Around line 8")
        self.assertEqual(symbolTable.errors[1], "Error: symbol x already defined. Around line 9")
        self.assertEqual(symbolTable.errors[2], "Error: symbol dataMember already defined. Around line 13")
        
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
        self.assertNotEqual(len(symbolTable.errors), 0)
        self.assertEqual(symbolTable.errors[0], "Error: symbol dataMember already defined. Around line 8")
        self.assertEqual(symbolTable.errors[1], "Error: symbol x already defined. Around line 9")
        self.assertEqual(symbolTable.errors[2], "Error: symbol dataMember already defined. Around line 13")
        self.assertEqual(symbolTable.errors[3], "Error: symbol dataMember already defined. Around line 17")
        
    def test_multiple_Method_with_declarations_nested_same_name(self):
        data = """
        class Temp{
            Temp(){}
            private char dataMember;
            public int Method(int x) {
                int dataMember;
                if (x == 0) {
                    dataMember = 3;
                    x = 4;
                    string Method = "this is a string";
                    return 0;
                } else if (x == 1) {
                    dataMember = 4;
                    return 1;
                }
                return compute(1-x) + this.compute(x-2);
            }
            public int Method2(int x) {
                int dataMember;
                if (x == 0) {
                    dataMember = 3;
                    x = 4;
                    string Method = "this is a string";
                    return 0;
                } else if (x == 1) {
                    dataMember = 4;
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
        self.assertEqual(len(symbolTable.errors), 0)
        
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
        self.assertEqual(len(symbolTable.errors), 0)
        
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
        self.assertEqual(len(symbolTable.errors), 4)
        self.assertEqual(symbolTable.errors[0], "Error: symbol index already defined. Around line 25")
        self.assertEqual(symbolTable.errors[1], "Error: symbol index already defined. Around line 29")
        self.assertEqual(symbolTable.errors[2], "Error: symbol index already defined. Around line 48")
        self.assertEqual(symbolTable.errors[3], "Error: symbol index already defined. Around line 52")

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
        self.assertEqual(len(symbolTable.errors), 5)
        self.assertEqual(symbolTable.errors[0], "Error: symbol index already defined. Around line 25")
        self.assertEqual(symbolTable.errors[1], "Error: symbol index already defined. Around line 29")
        self.assertEqual(symbolTable.errors[2], "Error: symbol main already defined. Around line 41")
        self.assertEqual(symbolTable.errors[3], "Error: symbol index already defined. Around line 48")
        self.assertEqual(symbolTable.errors[4], "Error: symbol index already defined. Around line 52")

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
        self.assertEqual(len(symbolTable.errors), 0)

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
        self.assertEqual(len(symbolTable.errors), 1)
        self.assertEqual(symbolTable.errors[0], "Error: symbol fib already defined. Around line 16")

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
        self.assertEqual(len(symbolTable.errors), 1)
        self.assertEqual(symbolTable.errors[0], "Error: fib is already defined as a variable. Around line 16")

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
        self.assertEqual(len(symbolTable.errors), 1)
        self.assertEqual(symbolTable.errors[0], "Error: fib is already defined as an object. Around line 16")

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
        self.assertEqual(len(symbolTable.errors), 2)
        self.assertEqual(symbolTable.errors[0], "Error: symbol fib already defined. Around line 16")
        self.assertEqual(symbolTable.errors[1], "Error: Fibonaccis is not a valid class or type for KXI. Symbol checking")

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
        self.assertEqual(len(symbolTable.errors), 0)

    def test_big_test_pass(self):
        data = """
        class Fibonacci {
            Fibonacci() {}
            public int compute(int x) {
                if (x == 0) {
                    char y = 'a';
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
                        Fibonacci fib1 = new Fibonacci();
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
                        Fibonacci fib2 = new Fibonacci();
                        int b;
                        cout << '+';
                }
            }
        }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(len(symbolTable.errors), 0)

    def test_symbolTable(self):
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

        class Test {
            Test() {}
            private bool[] asdfasdf;
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
            Test[] tttest = new Test[5];
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
        }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(len(symbolTable.errors), 0)
        self.assertEqual(len(symbolTable.symbol_tables[0]), 9)
        self.assertEqual(len(symbolTable.symbol_tables[1]), 3)
        self.assertEqual(len(symbolTable.symbol_tables[2]), 1)
        self.assertEqual(len(symbolTable.symbol_tables[3]), 4)
        self.assertEqual(len(symbolTable.symbol_tables[4]), 2)

    def test_parameters(self):
        data = """
        class Fibonacci {
            Fibonacci(Test test, int[] array,  bool[] boolArray, Test[] testArray) {}
            public int compute(int x, string[] strings) {
                if (x == 0) {
                    return 0;
                } else if (x == 1) {
                    return 1;
                }
                return compute(1-x, strings) + this.compute(x-2, strings);
            }
        }  

        class Test {
            Test(Fibonacci obj, int[] arr, bool[] boolArray, Fibonacci[] fibArray) {}
            private bool[] asdfasdf;
            public int test(int x, Fibonacci obj, int intValue, char charValue, bool boolValue, string stringValue, Fibonacci fib) {
                cout << x;
                char l = '\\n';
                cout << '\\n';
                if (x == 5) {
                    cout << this.test(x + 5, obj, voidArray, intValue, charValue, boolValue, stringValue, fib);
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
            Test[] tttest = new Test[5];
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
        }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(len(symbolTable.errors), 0)
        self.assertEqual(len(symbolTable.paramList[0]['paramTypes']), 5)
        self.assertEqual(symbolTable.paramList[0]['paramTypes'][1], "Test")
        self.assertEqual(symbolTable.paramList[0]['paramTypes'][2], "int[]")
        self.assertEqual(symbolTable.paramList[0]['paramTypes'][3], "bool[]")
        self.assertEqual(symbolTable.paramList[0]['paramTypes'][4], "Test[]")
        self.assertEqual(len(symbolTable.paramList[1]['paramTypes']), 3)
        self.assertEqual(symbolTable.paramList[1]['paramTypes'][1], "int")
        self.assertEqual(symbolTable.paramList[1]['paramTypes'][2], "string[]")
        self.assertEqual(len(symbolTable.paramList[2]['paramTypes']), 5)
        self.assertEqual(symbolTable.paramList[2]['paramTypes'][1], "Fibonacci")
        self.assertEqual(symbolTable.paramList[2]['paramTypes'][2], "int[]")
        self.assertEqual(symbolTable.paramList[2]['paramTypes'][3], "bool[]")
        self.assertEqual(symbolTable.paramList[2]['paramTypes'][4], "Fibonacci[]")
        self.assertEqual(len(symbolTable.paramList[3]['paramTypes']), 8)
        self.assertEqual(symbolTable.paramList[3]['paramTypes'][1], "int")
        self.assertEqual(symbolTable.paramList[3]['paramTypes'][2], "Fibonacci")
        self.assertEqual(symbolTable.paramList[3]['paramTypes'][3], "int")
        self.assertEqual(symbolTable.paramList[3]['paramTypes'][4], "char")
        self.assertEqual(symbolTable.paramList[3]['paramTypes'][5], "bool")
        self.assertEqual(symbolTable.paramList[3]['paramTypes'][6], "string")
        self.assertEqual(symbolTable.paramList[3]['paramTypes'][7], "Fibonacci")

    def test_parameter_void(self):
        data = """
        class Class{
            Class(void a){}
            private bool[] b (void c){}
        }

        void kxi2023 main (){}
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(len(symbolTable.errors), 2)
        self.assertEqual(symbolTable.errors[0], "Error: Parameter a can not be of type void. Around line 3")
        self.assertEqual(symbolTable.errors[1], "Error: Parameter c can not be of type void. Around line 4")

    def test_parameter_NonExisitent_Object(self):
        data = """
        class Class{
            Class(int a){}
            private bool[] b (Fibonacci c){}
        }

        void kxi2023 main (){}
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(len(symbolTable.errors), 2)
        self.assertEqual(symbolTable.errors[0], "Error: Fibonacci is not a valid class or type for KXI. Param checking")
        self.assertEqual(symbolTable.errors[1], "Error: Fibonacci is not a valid class or type for KXI. Symbol checking")

    def test_parameter_in_constructor_same_type(self):
        data = """
        class Class{
            Class(Class a){}
            private bool[] b (Class c){}
        }

        void kxi2023 main (){}
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(len(symbolTable.errors), 1)
        self.assertEqual(symbolTable.errors[0], "Error: Since only one constructor is allowed, it is illegal to have a parameter Class a be of the same type as the class Class. Around line 3")

    def test_parameter_in_constructor_same_type_array(self):
        data = """
        class Class{
            Class(Class[] a){}
            private bool[] b (Class c){}
        }

        void kxi2023 main (){}
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(len(symbolTable.errors), 1)
        self.assertEqual(symbolTable.errors[0], "Error: Since only one constructor is allowed, it is illegal to have a parameter Class a be of the same type as the class Class. Around line 3")

    def test_void_array(self):
        data = """
            class TempClass{
                private int x;
            }
            void kxi2023 main(){
                int x = 3;
                if (2 ==2){
                    x = 2;
                }
            }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(len(symbolTable.errors), 0)

    def test_object_array(self):
        data = """
            class TempClass{
                private int x;
            }
            void kxi2023 main(){
                TempClass[] tt = new TempClass[3];
                int x = 3;
                if (2 ==2){
                    x = 2;
                }
            }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(len(symbolTable.errors), 0)

    def test_array_dataMember(self):
        data = """
            class Fib{}

            class TempClass{
                public Fib[] t;
                private int x;
            }
            void kxi2023 main(){
                TempClass[] tt = new TempClass[3];
                int x = 3;
                if (2 ==2){
                    x = 2;
                }
            }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(len(symbolTable.errors), 0)

    def test_array_methods(self):
        data = """
            class Fib{}

            class TempClass{
                public Fib[] t;
                private int x;
                public Fib[] f(){}
            }
            void kxi2023 main(){
                TempClass[] tt = new TempClass[3];
                int x = 3;
                if (2 ==2){
                    x = 2;
                }
            }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(len(symbolTable.errors), 0)

    def test_array_variables(self):
        data = """
            class Fib{}

            class TempClass{
                public Fib[] t;
                private int x;
                public Fib[] f(){}
            }
            void kxi2023 main(){
                TempClass[] tt = new TempClass[3];
                int[]ab = new int[5];
                char[]ac = new char[4];
                bool[] ad = new bool[4];
                string[] ae = new string[4];
                Wront[] af = new Wront[4];
                int x = 3;
                if (2 ==2){
                    x = 2;
                }
            }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(len(symbolTable.errors), 1)
        self.assertEqual(symbolTable.errors[0], "Error: Wront[] is not a valid class or type for KXI. Symbol checking")

    def test_array_dataMember_same_name_as_method(self):
        data = """
            class Fib{}

            class TempClass{
                public Fib[] t;
                private int x;
                public int[] x(){}
                public Fib[] t(){}
            }
            void kxi2023 main(){
                TempClass[] tt = new TempClass[3];
                int[]ab = new int[5];

                int x = 3;
                if (2 ==2){
                    x = 2;
                }
            }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(len(symbolTable.errors), 2)
        self.assertEqual(symbolTable.errors[0], "Error: symbol x already defined as a dataMember. Around line 7")
        self.assertEqual(symbolTable.errors[1], "Error: symbol t already defined as a dataMember. Around line 8")

    def test_array_method_same_name_as_dataMember(self):
        data = """
            class Fib{}

            class TempClass{
                public int[] x(){}
                public Fib[] t(){}
                public Fib[] t;
                private int x;
            }
            void kxi2023 main(){
                TempClass[] tt = new TempClass[3];
                int[]ab = new int[5];

                int x = 3;
                if (2 ==2){
                    x = 2;
                }
            }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(len(symbolTable.errors), 2)
        self.assertEqual(symbolTable.errors[0], "Error: symbol t already defined as a method. Around line 7")
        self.assertEqual(symbolTable.errors[1], "Error: symbol x already defined as a method. Around line 8")

    def test_method_parameter_array(self):
        pass

    def test_constructor_array(self):
        data = """
            class Fib{}

            class TempClass{
                TempClass(Fib[] f){}
                public int[] x(){}
                private int a;
            }
            void kxi2023 main(){
                TempClass[] tt = new TempClass[3];
                int[]ab = new int[5];

                int x = 3;
                if (2 ==2){
                    x = 2;
                }
            }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(len(symbolTable.errors), 0)

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
        self.assertEqual(len(symbolTable.errors), 0)
        undeclaredVariableVistior = UndeclaredVisitor()
        undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
        myAST.accept(undeclaredVariableVistior)
        self.assertEqual(len(undeclaredVariableVistior.errors), 0)

    def test_undeclared_in_method(self):
        data = """
        // Tests criteria under the C tier
        // (Everything up to B, sequential code in the main function plus functions including recursion, plus objects and primitive array).
        class Fibonacci {
            Fibonacci() {}
            public int compute(int x) {
                y = 3;
                int y = 3;
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
        self.assertEqual(len(symbolTable.errors), 0)
        undeclaredVariableVistior = UndeclaredVisitor()
        undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
        myAST.accept(undeclaredVariableVistior)
        self.assertEqual(len(undeclaredVariableVistior.errors), 1)
        self.assertEqual(undeclaredVariableVistior.errors[0], "Error: y is used but never declared or used before it is declared. Around line 7")

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
        self.assertEqual(len(symbolTable.errors), 0)
        undeclaredVariableVistior = UndeclaredVisitor()
        undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
        myAST.accept(undeclaredVariableVistior)
        self.assertEqual(len(undeclaredVariableVistior.errors), 8)
        self.assertEqual(undeclaredVariableVistior.errors[0], "Error: temp is used but never declared or used before it is declared. Around line 11")
        self.assertEqual(undeclaredVariableVistior.errors[1], "Error: temp is used but never declared or used before it is declared. Around line 14")
        self.assertEqual(undeclaredVariableVistior.errors[2], "Error: l is used but never declared or used before it is declared. Around line 25")
        self.assertEqual(undeclaredVariableVistior.errors[3], "Error: index is used but never declared or used before it is declared. Around line 38")
        self.assertEqual(undeclaredVariableVistior.errors[4], "Error: fib2 is used but never declared or used before it is declared. Around line 51")
        self.assertEqual(undeclaredVariableVistior.errors[5], "Error: test2 is used but never declared or used before it is declared. Around line 58")
        self.assertEqual(undeclaredVariableVistior.errors[6], "Error: myvar is used but never declared or used before it is declared. Around line 71")
        self.assertEqual(undeclaredVariableVistior.errors[7], "Error: myvar is used but never declared or used before it is declared. Around line 74")

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
        self.assertEqual(len(symbolTable.errors), 0)
        undeclaredVariableVistior = UndeclaredVisitor()
        undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
        myAST.accept(undeclaredVariableVistior)
        self.assertEqual(len(undeclaredVariableVistior.errors), 13)
        self.assertEqual(undeclaredVariableVistior.errors[0], "Error: temp is used but never declared or used before it is declared. Around line 10")
        self.assertEqual(undeclaredVariableVistior.errors[1], "Error: temp is used but never declared or used before it is declared. Around line 13")
        self.assertEqual(undeclaredVariableVistior.errors[2], "Error: l is used but never declared or used before it is declared. Around line 24")
        self.assertEqual(undeclaredVariableVistior.errors[3], "Error: Attempting to use '.'test2. Must be a dataMember or a method. Around line 56")
        self.assertEqual(undeclaredVariableVistior.errors[4], "Error: myVar1 is used but never declared or used before it is declared. Around line 66")
        self.assertEqual(undeclaredVariableVistior.errors[5], "Error: myVar2 is used but never declared or used before it is declared. Around line 78")
        self.assertEqual(undeclaredVariableVistior.errors[6], "Error: myVar3 is used but never declared or used before it is declared. Around line 113")
        self.assertEqual(undeclaredVariableVistior.errors[7], "Error: myVar4 is used but never declared or used before it is declared. Around line 132")
        self.assertEqual(undeclaredVariableVistior.errors[8], "Error: myVar5 is used but never declared or used before it is declared. Around line 139")
        self.assertEqual(undeclaredVariableVistior.errors[9], "Error: myVar6 is used but never declared or used before it is declared. Around line 172")
        self.assertEqual(undeclaredVariableVistior.errors[10], "Error: myVar7 is used but never declared or used before it is declared. Around line 198")
        self.assertEqual(undeclaredVariableVistior.errors[11], "Error: myVar8 is used but never declared or used before it is declared. Around line 246")
        self.assertEqual(undeclaredVariableVistior.errors[12], "Error: Attempting to initialize an object of type MyVar9 and no such class exists. Around line 274")

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
            char t;
            int index;
            int i = 0;
            Fibonacci fib = new Fibonacci();
            fib.ThisIsATest();
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
        self.assertEqual(len(symbolTable.errors), 0)
        undeclaredVariableVistior = UndeclaredVisitor()
        undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
        myAST.accept(undeclaredVariableVistior)
        self.assertEqual(len(undeclaredVariableVistior.errors), 1)
        self.assertEqual(undeclaredVariableVistior.errors[0], "Error: Attempting to use '.'ThisIsATest. Must be a dataMember or a method. Around line 35")

    def test_new_declared_undeclared(self):
        data = """
        class MyClass {
            public int a;
            public bool b = true;

            public int c(){}
            private char d(){
                MyClass test = new NotClass();
                OtherClass test2 = new NotClass2();
            }

            MyClass(){
                MyClass test = new NotClass();
                OtherClass test2 = new NotClass2();
            }
        }

        class OtherClass{
            OtherClass(){
                MyClass test = new NotClass();
                OtherClass test2 = new NotClass2();
            }
            private string[] otherString;
        }

        void kxi2023 main (){
            MyClass test = new NotClass();
            OtherClass test2 = new NotClass2();
        }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(len(symbolTable.errors), 0)
        undeclaredVariableVistior = UndeclaredVisitor()
        undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
        myAST.accept(undeclaredVariableVistior)
        self.assertEqual(len(undeclaredVariableVistior.errors), 8)
        self.assertEqual(undeclaredVariableVistior.errors[0],'Error: Attempting to initialize an object of type NotClass and no such class exists. Around line 8')
        self.assertEqual(undeclaredVariableVistior.errors[1],'Error: Attempting to initialize an object of type NotClass2 and no such class exists. Around line 9')
        self.assertEqual(undeclaredVariableVistior.errors[2],'Error: Attempting to initialize an object of type NotClass and no such class exists. Around line 13')
        self.assertEqual(undeclaredVariableVistior.errors[3],'Error: Attempting to initialize an object of type NotClass2 and no such class exists. Around line 14')
        self.assertEqual(undeclaredVariableVistior.errors[4],'Error: Attempting to initialize an object of type NotClass and no such class exists. Around line 20')
        self.assertEqual(undeclaredVariableVistior.errors[5],'Error: Attempting to initialize an object of type NotClass2 and no such class exists. Around line 21')
        self.assertEqual(undeclaredVariableVistior.errors[6],'Error: Attempting to initialize an object of type NotClass and no such class exists. Around line 27')
        self.assertEqual(undeclaredVariableVistior.errors[7],'Error: Attempting to initialize an object of type NotClass2 and no such class exists. Around line 28')

    def test_new_undeclared_declared(self):
        data = """
        class MyClass {
            public int a;
            public bool b = true;

            public int c(){}
            private char d(){
                NotClass test = new MyClass();
                NotClass2 test2 = new OtherClass();
            }

            MyClass(){
                NotClass test = new MyClass();
                NotClass2 test2 = new OtherClass();
            }
        }

        class OtherClass{
            OtherClass(){
                NotClass test = new MyClass();
                NotClass2 test2 = new OtherClass();
            }
            private string[] otherString;
        }

        void kxi2023 main (){
            NotClass test = new MyClass();
            NotClass2 test2 = new OtherClass();
        }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(len(symbolTable.errors), 8)
        self.assertEqual(symbolTable.errors[0],'Error: NotClass is not a valid class or type for KXI. Symbol checking')
        self.assertEqual(symbolTable.errors[1],'Error: NotClass2 is not a valid class or type for KXI. Symbol checking')
        self.assertEqual(symbolTable.errors[2],'Error: NotClass is not a valid class or type for KXI. Symbol checking')
        self.assertEqual(symbolTable.errors[3],'Error: NotClass2 is not a valid class or type for KXI. Symbol checking')
        self.assertEqual(symbolTable.errors[4],'Error: NotClass is not a valid class or type for KXI. Symbol checking')
        self.assertEqual(symbolTable.errors[5],'Error: NotClass2 is not a valid class or type for KXI. Symbol checking')
        self.assertEqual(symbolTable.errors[6],'Error: NotClass is not a valid class or type for KXI. Symbol checking')
        self.assertEqual(symbolTable.errors[7],'Error: NotClass2 is not a valid class or type for KXI. Symbol checking')
        # Undeclared u = new Declared()
        #in main, in classes, in separate classes, in methods, in constructors

    def test_new_undeclared_undeclared(self):
        data = """
        class MyClass {
            public int a;
            public bool b = true;

            public int c(){}
            private char d(){
                NotClass test = new NotClass();
                NotClass2 test2 = new NotClass2();
            }

            MyClass(){
                NotClass test = new NotClass();
                NotClass2 test2 = new NotClass2();
            }
        }

        class OtherClass{
            OtherClass(){
                NotClass test = new NotClass();
                NotClass2 test2 = new NotClass2();
            }
            private string[] otherString;
        }

        void kxi2023 main (){
            NotClass test = new NotClass();
            NotClass2 test2 = new NotClass2();
        }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(len(symbolTable.errors), 8)

    def test_new_declared_declared(self):
        data = """
        class MyClass {
            public int a;
            public bool b = true;

            public int c(){}
            private char d(){
                MyClass test = new MyClass();
                OtherClass test2 = new OtherClass();
            }

            MyClass(){
                MyClass test = new MyClass();
                OtherClass test2 = new OtherClass();
            }
        }

        class OtherClass{
            OtherClass(){
                MyClass test = new MyClass();
                OtherClass test2 = new OtherClass();
            }
            private string[] otherString;
        }

        void kxi2023 main (){
            MyClass test = new MyClass();
            OtherClass test2 = new OtherClass();
        }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(len(symbolTable.errors), 0)
        undeclaredVariableVistior = UndeclaredVisitor()
        undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
        myAST.accept(undeclaredVariableVistior)
        self.assertEqual(len(undeclaredVariableVistior.errors), 0)

    def test_this_in_main_and_methods(self):
        data = """
        class MyClass {
            public int a;
            public bool b = true;

            public int c(){}
            private char d(){
                MyClass test = new MyClass();
                bool c = this.b;
                OtherClass test2 = new OtherClass();
            }

            MyClass(){
                int c = 3;
                MyClass test = new MyClass();
                this.a = c;
                OtherClass test2 = new OtherClass();
            }
        }

        class OtherClass{
            OtherClass(){
                MyClass test = new MyClass();
                this.c;
                OtherClass test2 = new OtherClass();
            }
            private string[] otherString;
        }

        void kxi2023 main (){
            MyClass test = new MyClass();
            OtherClass test2 = new OtherClass();
            this.c;
        }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(len(symbolTable.errors), 0)
        undeclaredVariableVistior = UndeclaredVisitor()
        undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
        myAST.accept(undeclaredVariableVistior)
        self.assertEqual(len(undeclaredVariableVistior.errors), 1)
        self.assertEqual(undeclaredVariableVistior.errors[0],"Error: 'this' is used and 'this' can not be used outside of a class. Around line 33")

    def test_undeclared_vars_then_declareThem(self):
        data = """
        class MyClass {
            public int a;
            public bool b = true;

            public int c(){}
            private char d(){
                MyClass test = new MyClass();
                OtherClass test2 = new OtherClass();
                jj = 1;
                kk[3] = 3;
                ll = 'a';
                mm[1] = 'a';
                nn = true;
                oo[3] = false;
                pp = "string string";
                qq[2] = "other string";
            
                int jj;
                int[] kk;
                char ll;
                char[] mm;
                bool nn;
                bool[] oo;
                string pp;
                string[] qq;
            }

            MyClass(){
                int c = 3;
                MyClass test = new MyClass();
                this.a = c;
                OtherClass test2 = new OtherClass();
                aaa = 1;
                bbb[3] = 3;
                ccc = 'a';
                ddd[1] = 'a';
                eee = true;
                fff[3] = false;
                ggg = "string string";
                hhh[2] = "other string";
            
                int aaa;
                int[] bbb;
                char ccc;
                char[] ddd;
                bool eee;
                bool[] fff;
                string ggg;
                string[] hhh;
            }
        }

        class OtherClass{
            OtherClass(){
                MyClass test = new MyClass();
                OtherClass test2 = new OtherClass();
            }
            private string[] otherString;
        }

        void kxi2023 main (){
            MyClass test = new MyClass();
            OtherClass test2 = new OtherClass();
            aa = 1;
            bb[3] = 3;
            cc = 'a';
            dd[1] = 'a';
            ee = true;
            ff[3] = false;
            gg = "string string";
            hh[2] = "other string";
        
            int aa;
            int[] bb;
            char cc;
            char[] dd;
            bool ee;
            bool[] ff;
            string gg;
            string[] hh;
        }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(len(symbolTable.errors), 0)
        undeclaredVariableVistior = UndeclaredVisitor()
        undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
        myAST.accept(undeclaredVariableVistior)
        self.assertEqual(len(undeclaredVariableVistior.errors), 24)
        self.assertEqual(undeclaredVariableVistior.errors[0], 'Error: jj is used but never declared or used before it is declared. Around line 10')
        self.assertEqual(undeclaredVariableVistior.errors[1], 'Error: kk is used but never declared or used before it is declared. Around line 11')
        self.assertEqual(undeclaredVariableVistior.errors[2], 'Error: ll is used but never declared or used before it is declared. Around line 12')
        self.assertEqual(undeclaredVariableVistior.errors[3], 'Error: mm is used but never declared or used before it is declared. Around line 13')
        self.assertEqual(undeclaredVariableVistior.errors[4], 'Error: nn is used but never declared or used before it is declared. Around line 14')
        self.assertEqual(undeclaredVariableVistior.errors[5], 'Error: oo is used but never declared or used before it is declared. Around line 15')
        self.assertEqual(undeclaredVariableVistior.errors[6], 'Error: pp is used but never declared or used before it is declared. Around line 16')
        self.assertEqual(undeclaredVariableVistior.errors[7], 'Error: qq is used but never declared or used before it is declared. Around line 17')
        self.assertEqual(undeclaredVariableVistior.errors[8], 'Error: aaa is used but never declared or used before it is declared. Around line 34')
        self.assertEqual(undeclaredVariableVistior.errors[9], 'Error: bbb is used but never declared or used before it is declared. Around line 35')
        self.assertEqual(undeclaredVariableVistior.errors[10],  'Error: ccc is used but never declared or used before it is declared. Around line 36')
        self.assertEqual(undeclaredVariableVistior.errors[11], 'Error: ddd is used but never declared or used before it is declared. Around line 37')
        self.assertEqual(undeclaredVariableVistior.errors[12], 'Error: eee is used but never declared or used before it is declared. Around line 38')
        self.assertEqual(undeclaredVariableVistior.errors[13], 'Error: fff is used but never declared or used before it is declared. Around line 39')
        self.assertEqual(undeclaredVariableVistior.errors[14], 'Error: ggg is used but never declared or used before it is declared. Around line 40')
        self.assertEqual(undeclaredVariableVistior.errors[15], 'Error: hhh is used but never declared or used before it is declared. Around line 41')
        self.assertEqual(undeclaredVariableVistior.errors[16], 'Error: aa is used but never declared or used before it is declared. Around line 65')
        self.assertEqual(undeclaredVariableVistior.errors[17], 'Error: bb is used but never declared or used before it is declared. Around line 66')
        self.assertEqual(undeclaredVariableVistior.errors[18], 'Error: cc is used but never declared or used before it is declared. Around line 67')
        self.assertEqual(undeclaredVariableVistior.errors[19], 'Error: dd is used but never declared or used before it is declared. Around line 68')
        self.assertEqual(undeclaredVariableVistior.errors[20], 'Error: ee is used but never declared or used before it is declared. Around line 69')
        self.assertEqual(undeclaredVariableVistior.errors[21], 'Error: ff is used but never declared or used before it is declared. Around line 70')
        self.assertEqual(undeclaredVariableVistior.errors[22], 'Error: gg is used but never declared or used before it is declared. Around line 71')
        self.assertEqual(undeclaredVariableVistior.errors[23], 'Error: hh is used but never declared or used before it is declared. Around line 72')

    def test_declaring_all_types(self):
        data = """
        class MyClass {
            public int a = 1;
            public bool b = true;
            public char c = 'a';
            public string d = "string";
            private int[] e = new int[4];
            private bool[] f = new bool[2];
            private char[] g = new char[6];
            private string[]h = new string[3];

            private char asdfasd(){
                MyClass test = new MyClass();
                OtherClass test2 = new OtherClass();
            
                int jj = 3;
                int[] kk = new int[3];
                char ll;
                char[] mm = new char[3];
                bool nn;
                bool[] oo = new bool[3];
                string pp;
                string[] qq = new string[6];

                jj = 1;
                kk[3] = 3;
                ll = 'a';
                mm[1] = 'a';
                nn = true;
                oo[3] = false;
                pp = "string string";
                qq[2] = "other string";
            }

            MyClass(){
                int c = 3;
                MyClass test = new MyClass();
                OtherClass test2 = new OtherClass();
            
                int aaa;
                int[] bbb;
                char ccc;
                char[] ddd;
                bool eee;
                bool[] fff;
                string ggg;
                string[] hhh;

                aaa = 1;
                bbb[3] = 3;
                ccc = 'a';
                ddd[1] = 'a';
                eee = true;
                fff[3] = false;
                ggg = "string string";
                hhh[2] = "other string";
            }
        }

        class OtherClass{
            OtherClass(){
                MyClass test = new MyClass();
                OtherClass test2 = new OtherClass();
            }
            private string[] otherString;
        }

        void kxi2023 main (){
            MyClass test = new MyClass();
            OtherClass test2 = new OtherClass();
            int aa;
            int[] bb;
            char cc;
            char[] dd;
            bool ee;
            bool[] ff;
            string gg;
            string[] hh;

            aa = 1;
            bb[3] = 3;
            cc = 'a';
            dd[1] = 'a';
            ee = true;
            ff[3] = false;
            gg = "string string";
            hh[2] = "other string";
        

        }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(len(symbolTable.errors), 0)
        undeclaredVariableVistior = UndeclaredVisitor()
        undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
        myAST.accept(undeclaredVariableVistior)
        self.assertEqual(len(undeclaredVariableVistior.errors), 0)

    def test_index_array_undeclared(self):
        data = """
        void kxi2023 main (){
            bb[3] = 3;
        
            int[] bb;
        }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(len(symbolTable.errors), 0)
        undeclaredVariableVistior = UndeclaredVisitor()
        undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
        myAST.accept(undeclaredVariableVistior)
        self.assertEqual(len(undeclaredVariableVistior.errors), 1)
        self.assertEqual(undeclaredVariableVistior.errors[0], 'Error: bb is used but never declared or used before it is declared. Around line 3')

    def test_declared_period_declared_DataMem_private(self):
        data = """
        class MyClass {
            public int a;
            private bool b = true;

            public int c(){}
            private char d(){
                MyClass test = new MyClass();
                OtherClass test2 = new OtherClass();
                test.b = false; //fail
                test2.priv = "new string"; //fail
                this.b = false; //pass
                b = false; //pass
                
            }

            MyClass(){
                MyClass test3 = new MyClass();
                OtherClass test4 = new OtherClass();
                test3.b = false; //fail
                test4.priv = "new string"; //fail
            }
        }

        class OtherClass{
            public char pub = 'a';
            private string priv = "string";

            OtherClass(){
                MyClass test5 = new MyClass();
                OtherClass test6 = new OtherClass();
                test5.b = false; //fail
                test6.priv = "new string"; //fail
            }
        }

        void kxi2023 main (){
            MyClass test7 = new MyClass();
            OtherClass test8 = new OtherClass();
            test7.b = false; //fail
            test8.priv = "new string"; //fail
        }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(len(symbolTable.errors), 0)
        undeclaredVariableVistior = UndeclaredVisitor()
        undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
        myAST.accept(undeclaredVariableVistior)
        self.assertEqual(len(undeclaredVariableVistior.errors), 8)
        self.assertEqual(undeclaredVariableVistior.errors[0], "Error: Attempting to use '.'b. This is a private method/datamember and can only be access in the class. Around line 10")
        self.assertEqual(undeclaredVariableVistior.errors[1], "Error: Attempting to use '.'priv. This is a private method/datamember and can only be access in the class. Around line 11")
        self.assertEqual(undeclaredVariableVistior.errors[2], "Error: Attempting to use '.'b. This is a private method/datamember and can only be access in the class. Around line 20")
        self.assertEqual(undeclaredVariableVistior.errors[3], "Error: Attempting to use '.'priv. This is a private method/datamember and can only be access in the class. Around line 21")
        self.assertEqual(undeclaredVariableVistior.errors[4], "Error: Attempting to use '.'b. This is a private method/datamember and can only be access in the class. Around line 32")
        self.assertEqual(undeclaredVariableVistior.errors[5], "Error: Attempting to use '.'priv. This is a private method/datamember and can only be access in the class. Around line 33")
        self.assertEqual(undeclaredVariableVistior.errors[6], "Error: Attempting to use '.'b. This is a private method/datamember and can only be access in the class. Around line 40")
        self.assertEqual(undeclaredVariableVistior.errors[7], "Error: Attempting to use '.'priv. This is a private method/datamember and can only be access in the class. Around line 41")
        #declared.declaredMethod.private
        #in main, in classes, in separate classes, in methods, in constructors

    def test_declared_period_declared_DataMem_public(self):
        data = """
        class MyClass {
            public int a;
            private bool b = true;

            public int c(){}
            private char d(){
                MyClass test = new MyClass();
                OtherClass test2 = new OtherClass();
                test.a = 1;
                test2.pub = 'b';
                a = 2;
                this.a = 3;
            }

            MyClass(){
                MyClass test3 = new MyClass();
                OtherClass test4 = new OtherClass();
                test3.a = 4;
                test4.pub = 'c';
                a = 5;
                this.a = 6;
                pub = 'd';
            }
        }

        class OtherClass{
            public char pub = 'a';
            private string priv = "string";

            OtherClass(){
                MyClass test5 = new MyClass();
                OtherClass test6 = new OtherClass();
                test5.a = 7;
                test6.pub = 'e';
                pub = 'f';
                this.pub = 'g';
            }
        }

        void kxi2023 main (){
            MyClass test7 = new MyClass();
            OtherClass test8 = new OtherClass();
            test7.a = 8;
            a = 9;
            test8.pub = 'h';
            pub = 'i';
        }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(len(symbolTable.errors), 0)
        undeclaredVariableVistior = UndeclaredVisitor()
        undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
        myAST.accept(undeclaredVariableVistior)
        self.assertEqual(len(undeclaredVariableVistior.errors), 3)
        self.assertEqual(undeclaredVariableVistior.errors[0], 'Error: pub is used but never declared or used before it is declared. Around line 23')
        self.assertEqual(undeclaredVariableVistior.errors[1], 'Error: a is used but never declared or used before it is declared. Around line 45')
        self.assertEqual(undeclaredVariableVistior.errors[2], 'Error: pub is used but never declared or used before it is declared. Around line 47')
        
        #declared.declaredMethod.public
        #in main, in classes, in separate classes, in methods, in constructors

    def test_decalred_period_undeclared_DataMem(self):
        data = """
        class MyClass {
            public int a;
            private bool b = true;

            public int c(){}
            private char d(){
                MyClass test = new MyClass();
                OtherClass test2 = new OtherClass();
                test.cee = 1;
                test2.puba = 'b';
                this.asdf = 1;
            }

            MyClass(){
                MyClass test3 = new MyClass();
                OtherClass test4 = new OtherClass();
                test3.abb = 4;
                test4.pubs = 'c';
                this.aasdf = 6;
            }
        }

        class OtherClass{
            public char pub = 'a';
            private string priv = "string";

            OtherClass(){
                MyClass test5 = new MyClass();
                OtherClass test6 = new OtherClass();
                test5.abbb = 7;
                test6.pube = 'e';
                this.pubff = 'g';
            }
        }

        void kxi2023 main (){
            MyClass test7 = new MyClass();
            OtherClass test8 = new OtherClass();
            test7.ayy = 8;
            test8.pubu = 'h';
        }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(len(symbolTable.errors), 0)
        undeclaredVariableVistior = UndeclaredVisitor()
        undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
        myAST.accept(undeclaredVariableVistior)
        self.assertEqual(len(undeclaredVariableVistior.errors), 11)
        self.assertEqual(undeclaredVariableVistior.errors[0], "Error: Attempting to use '.'cee. Must be a dataMember or a method. Around line 10")
        self.assertEqual(undeclaredVariableVistior.errors[1], "Error: Attempting to use '.'puba. Must be a dataMember or a method. Around line 11")
        self.assertEqual(undeclaredVariableVistior.errors[2], "Error: Attempting to use '.'asdf. Must be a dataMember or a method. Around line 12")
        self.assertEqual(undeclaredVariableVistior.errors[3], "Error: Attempting to use '.'abb. Must be a dataMember or a method. Around line 18")
        self.assertEqual(undeclaredVariableVistior.errors[4], "Error: Attempting to use '.'pubs. Must be a dataMember or a method. Around line 19")
        self.assertEqual(undeclaredVariableVistior.errors[5], "Error: Attempting to use '.'aasdf. Must be a dataMember or a method. Around line 20")
        self.assertEqual(undeclaredVariableVistior.errors[6], "Error: Attempting to use '.'abbb. Must be a dataMember or a method. Around line 31")
        self.assertEqual(undeclaredVariableVistior.errors[7], "Error: Attempting to use '.'pube. Must be a dataMember or a method. Around line 32")
        self.assertEqual(undeclaredVariableVistior.errors[8], "Error: Attempting to use '.'pubff. Must be a dataMember or a method. Around line 33")
        self.assertEqual(undeclaredVariableVistior.errors[9], "Error: Attempting to use '.'ayy. Must be a dataMember or a method. Around line 40")
        self.assertEqual(undeclaredVariableVistior.errors[10], "Error: Attempting to use '.'pubu. Must be a dataMember or a method. Around line 41")

    def test_undeclared_period_declared_DataMem_public(self):
        data = """
        class MyClass {
            public int a;
            private bool b = true;

            public int c(){}
            private char d(){
                test.a = 1;
                test2.pub = 'b';
                a = 2;
                this.a = 3;
            }

            MyClass(){
                test3.a = 4;
                test4.pub = 'c';
                a = 5;
                this.a = 6;
                pub = 'd';
            }
        }

        class OtherClass{
            public char pub = 'a';
            private string priv = "string";

            OtherClass(){
                test5.a = 7;
                test6.pub = 'e';
                pub = 'f';
                this.pub = 'g';
            }
        }

        void kxi2023 main (){
            test7.a = 8;
            a = 9;
            test8.pub = 'h';
            pub = 'i';
        }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(len(symbolTable.errors), 0)
        undeclaredVariableVistior = UndeclaredVisitor()
        undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
        myAST.accept(undeclaredVariableVistior)
        self.assertEqual(len(undeclaredVariableVistior.errors), 11)
        self.assertEqual(undeclaredVariableVistior.errors[0], 'Error: test is used but never declared or used before it is declared. Around line 8')
        self.assertEqual(undeclaredVariableVistior.errors[1], 'Error: test2 is used but never declared or used before it is declared. Around line 9')
        self.assertEqual(undeclaredVariableVistior.errors[2], 'Error: test3 is used but never declared or used before it is declared. Around line 15')
        self.assertEqual(undeclaredVariableVistior.errors[3], 'Error: test4 is used but never declared or used before it is declared. Around line 16')
        self.assertEqual(undeclaredVariableVistior.errors[4], 'Error: pub is used but never declared or used before it is declared. Around line 19')
        self.assertEqual(undeclaredVariableVistior.errors[5], 'Error: test5 is used but never declared or used before it is declared. Around line 28')
        self.assertEqual(undeclaredVariableVistior.errors[6], 'Error: test6 is used but never declared or used before it is declared. Around line 29')
        self.assertEqual(undeclaredVariableVistior.errors[7], 'Error: test7 is used but never declared or used before it is declared. Around line 36')
        self.assertEqual(undeclaredVariableVistior.errors[8], 'Error: a is used but never declared or used before it is declared. Around line 37')
        self.assertEqual(undeclaredVariableVistior.errors[9], 'Error: test8 is used but never declared or used before it is declared. Around line 38')
        self.assertEqual(undeclaredVariableVistior.errors[10], 'Error: pub is used but never declared or used before it is declared. Around line 39')

    def test_undecalred_period_undeclared_DataMem(self):
        data = """
        class MyClass {
            public int a;
            private bool b = true;

            public int c(){}
            private char d(){
                test.ab = 1;
                test2.puba = 'b';
                ac = 2;
                this.ad = 3;
            }

            MyClass(){
                test3.ae = 4;
                test4.pubb = 'c';
                af = 5;
                this.ag = 6;
                pubc = 'd';
            }
        }

        class OtherClass{
            public char pub = 'a';
            private string priv = "string";

            OtherClass(){
                test5.ah = 7;
                test6.pubd = 'e';
                pube = 'f';
                this.pubf = 'g';
            }
        }

        void kxi2023 main (){
            test7.ai = 8;
            aj = 9;
            test8.pubg = 'h';
            pubh = 'i';
        }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(len(symbolTable.errors), 0)
        undeclaredVariableVistior = UndeclaredVisitor()
        undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
        myAST.accept(undeclaredVariableVistior)
        self.assertEqual(len(undeclaredVariableVistior.errors), 25)

    def test_declared_period_declared_method_private(self):
        data = """
        class ClassOne{

            public int dataMem1 = 1;
            private int dataMem2 = 2;

            public void pubMeth1(){

            }
            private void privMeth1(){
                
            }
            public void pubMeth2(){
                ClassOne c1 = new ClassOne();
                OtherClass c2 = new OtherClass();
                c1.privMeth1();
                this.privMeth1();
                privMeth1();
                c2.privMeth3();
            }
            private void privMeth2(){
                privMeth1();
            }
            ClassOne(){
                ClassOne c8 = new ClassOne();
                OtherClass c9 = new OtherClass();
                c8.privMeth1();
                c9.privMeth4();
            }
        }

        class OtherClass{
            public int dataMem3 = 3;
            private int dataMem4 = 4;

            public void pubMeth3(){

            }
            private void privMeth3(){
            
            }
            public void pubMeth4(){
                ClassOne c3 = new ClassOne();
                OtherClass c4 = new OtherClass();
                c3.privMeth1();
                c4.privMeth4();
                privMeth3();
                this.privMeth3();
            }
            private void privMeth4(){
            
            }
        }

        void kxi2023 main(){
            ClassOne c5 = new ClassOne();
            OtherClass c6 = new OtherClass();
            c5.privMeth3();
            c6.privMeth4();
        }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(len(symbolTable.errors), 0)
        undeclaredVariableVistior = UndeclaredVisitor()
        undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
        myAST.accept(undeclaredVariableVistior)
        self.assertEqual(len(undeclaredVariableVistior.errors), 8)
        self.assertEqual(undeclaredVariableVistior.errors[0], "Error: Attempting to use '.'privMeth1. This is a private method/datamember and can only be access in the class. Around line 16")
        self.assertEqual(undeclaredVariableVistior.errors[1], "Error: Attempting to use '.'privMeth3. This is a private method/datamember and can only be access in the class. Around line 19")
        self.assertEqual(undeclaredVariableVistior.errors[2], "Error: Attempting to use '.'privMeth1. This is a private method/datamember and can only be access in the class. Around line 27")
        self.assertEqual(undeclaredVariableVistior.errors[3], "Error: Attempting to use '.'privMeth4. This is a private method/datamember and can only be access in the class. Around line 28")
        self.assertEqual(undeclaredVariableVistior.errors[4], "Error: Attempting to use '.'privMeth1. This is a private method/datamember and can only be access in the class. Around line 45")
        self.assertEqual(undeclaredVariableVistior.errors[5], "Error: Attempting to use '.'privMeth4. This is a private method/datamember and can only be access in the class. Around line 46")
        self.assertEqual(undeclaredVariableVistior.errors[6], "Error: Attempting to use '.'privMeth3. This is a private method/datamember and can only be access in the class. Around line 58")
        self.assertEqual(undeclaredVariableVistior.errors[7], "Error: Attempting to use '.'privMeth4. This is a private method/datamember and can only be access in the class. Around line 59")

    def test_declared_period_declared_method_public(self):
        data = """
        class ClassOne{

            public int dataMem1 = 1;
            private int dataMem2 = 2;

            public void pubMeth1(){

            }
            private void privMeth1(){
                
            }
            public void pubMeth2(){
                ClassOne c1 = new ClassOne();
                OtherClass c2 = new OtherClass();
                c1.pubMeth1();
                this.pubMeth1();
                pubMeth1();
                c2.pubMeth3();
            }
            private void privMeth2(){
                pubMeth2();
            }
            ClassOne(){
                ClassOne c8 = new ClassOne();
                OtherClass c9 = new OtherClass();
                c8.pubMeth2();
                c9.pubMeth4();
            }
        }

        class OtherClass{
            public int dataMem3 = 3;
            private int dataMem4 = 4;

            public void pubMeth3(){

            }
            private void privMeth3(){
            
            }
            public void pubMeth4(){
                ClassOne c3 = new ClassOne();
                OtherClass c4 = new OtherClass();
                c3.pubMeth1();
                c4.pubMeth3();
                pubMeth3();
                this.pubMeth3();
            }
            private void privMeth4(){
            
            }
        }

        void kxi2023 main(){
            ClassOne c5 = new ClassOne();
            OtherClass c6 = new OtherClass();
            c5.pubMeth2();
            c6.pubMeth3();
        }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(len(symbolTable.errors), 0)
        undeclaredVariableVistior = UndeclaredVisitor()
        undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
        myAST.accept(undeclaredVariableVistior)
        self.assertEqual(len(undeclaredVariableVistior.errors), 0)

    def test_decalred_period_undeclared_method(self):
        data = """
        class ClassOne{

            public int dataMem1 = 1;
            private int dataMem2 = 2;

            public void pubMeth1(){

            }
            private void privMeth1(){
                
            }
            public void pubMeth2(){
                ClassOne c1 = new ClassOne();
                OtherClass c2 = new OtherClass();
                c1.aa();
                this.bb();
                cc();
                c2.dd();
            }
            private void privMeth2(){
                ee();
            }
            ClassOne(){
                ClassOne c8 = new ClassOne();
                OtherClass c9 = new OtherClass();
                c8.ff();
                c9.gg();
            }
        }

        class OtherClass{
            public int dataMem3 = 3;
            private int dataMem4 = 4;

            public void pubMeth3(){

            }
            private void privMeth3(){
            
            }
            public void pubMeth4(){
                ClassOne c3 = new ClassOne();
                OtherClass c4 = new OtherClass();
                c3.hh();
                c4.ii();
                jj();
                this.kk();
            }
            private void privMeth4(){
            
            }
        }

        void kxi2023 main(){
            ClassOne c5 = new ClassOne();
            OtherClass c6 = new OtherClass();
            c5.ll();
            c6.mm();
        }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(len(symbolTable.errors), 0)
        undeclaredVariableVistior = UndeclaredVisitor()
        undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
        myAST.accept(undeclaredVariableVistior)
        self.assertEqual(len(undeclaredVariableVistior.errors), 13)

    def test_undeclared_period_declared_method_public(self):
        data = """
        class ClassOne{

            public int dataMem1 = 1;
            private int dataMem2 = 2;

            public void pubMeth1(){

            }
            private void privMeth1(){
                
            }
            public void pubMeth2(){
                c1.pubMeth1();
                this.pubMeth1();
                pubMeth1();
                c2.pubMeth3();
            }
            private void privMeth2(){
                pubMeth2();
            }
            ClassOne(){
                c8.pubMeth2();
                c9.pubMeth4();
            }
        }

        class OtherClass{
            public int dataMem3 = 3;
            private int dataMem4 = 4;

            public void pubMeth3(){

            }
            private void privMeth3(){
            
            }
            public void pubMeth4(){
                c3.pubMeth1();
                c4.pubMeth3();
                pubMeth3();
                this.pubMeth3();
            }
            private void privMeth4(){
            
            }
        }

        void kxi2023 main(){
            c5.pubMeth2();
            c6.pubMeth3();
        }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(len(symbolTable.errors), 0)
        undeclaredVariableVistior = UndeclaredVisitor()
        undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
        myAST.accept(undeclaredVariableVistior)
        self.assertEqual(len(undeclaredVariableVistior.errors), 8)

    def test_undecalred_period_undeclared_method(self):
        data = """
        class ClassOne{

            public int dataMem1 = 1;
            private int dataMem2 = 2;

            public void pubMeth1(){

            }
            private void privMeth1(){
                
            }
            public void pubMeth2(){
                c1.aa();
                this.bb();
                dd();
                c2.dd();
            }
            private void privMeth2(){
                ee();
            }
            ClassOne(){
                c8.ff();
                c9.gg();
            }
        }

        class OtherClass{
            public int dataMem3 = 3;
            private int dataMem4 = 4;

            public void pubMeth3(){

            }
            private void privMeth3(){
            
            }
            public void pubMeth4(){
                c3.hh();
                c4.ii();
                jj();
                this.kk();
            }
            private void privMeth4(){
            
            }
        }

        void kxi2023 main(){
            c5.ll();
            c6.mm();
        }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(len(symbolTable.errors), 0)
        undeclaredVariableVistior = UndeclaredVisitor()
        undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
        myAST.accept(undeclaredVariableVistior)
        self.assertEqual(len(undeclaredVariableVistior.errors), 21)








    # def test_index_array_uninitialized(self):
    #     data = """
    #     void kxi2023 main (){
    #         int[] bb;
    #         bb[3] = 3;
    #     }
    #     """
    #     theLexer.theLexerReturnFucntion(data)
    #     myAST = theParser.Parse(data)
    #     symbolTable = SymbolTableVisitor()
    #     myAST.accept(symbolTable)
    #     self.assertEqual(len(symbolTable.errors), 0)
    #     undeclaredVariableVistior = UndeclaredVisitor()
    #     undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
    #     myAST.accept(undeclaredVariableVistior)
    #     self.assertEqual(len(undeclaredVariableVistior.errors), 1)
    #     self.assertEqual(undeclaredVariableVistior.errors[0], 'Error: bb is used but never declared or used before it is declared. Around line 3')

class Test_TypeChecking(unittest.TestCase):

    def test_big(self):
        data = """
    void kxi2023 main() {
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

    if (     'a' == 'a'
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

        int i = x;
        int j = 0;
        while(j < 3) {
            cout << "nested while: ";
            cout << i * 3;
            cout << '\\n';
            i *= 3;
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
    if (test == -2) {
        cout << '+';
    } else {
        cout << '-';
    }
    cout << '|';

    test /= 2;
    if (test == -1) {
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
    int a = 0;
    int b = 1;

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
}
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(len(symbolTable.errors), 0)
        undeclaredVariableVistior = UndeclaredVisitor()
        undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
        myAST.accept(undeclaredVariableVistior)
        self.assertEqual(len(undeclaredVariableVistior.errors), 0)
        typeCheck = TypeChecking()
        typeCheck.paramList = symbolTable.paramList
        typeCheck.symbol_tables = symbolTable.symbol_tables
        myAST.accept(typeCheck)
        self.assertEqual(len(typeCheck.errors), 0)

    def test_big1(self):
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
                    //return compute(1-x) + this.compute(x-2);
                    return this.compute(1-x) + compute(x-2);
                }
            }

            class Test {
                Test() {}
                private bool[] asdfasdf;
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
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 0)

    def test_big2(self):
            data = """
            class AnotherTest
            {
            private char memeberVarThree;

                public void FuncThree(char j)
            {
                    int k;
                }
            }

            class AnotherTest2
            {
                private char memeberVar4;

                public void Func4(char B)
                {
                    int T;
                }
            }


            void kxi2023 main()
            {
                cout << "Hello World!";
            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 0)

    def test_big3(self):
            data = """
            class MyClass {
                public char [] id1 = new char[3];
            }

            class OtherClass{
                private int id2;
                private bool id4;
                public string id5;
            }

            class TempClass{

            }

            void kxi2023 main (){}
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 0)

    def test_big4(self):
            data = """
            class MyClass {}

            void kxi2023 main (){}
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 0)

    def test_big5(self):
            data = """
            class MyClass {
                public int a;
                public bool b = true;

                public int c(){
                    return 1;
                }
                private char d(){
                    return 'a';
                }

                MyClass(){}
            }

            void kxi2023 main (){}
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 0)

    def test_big6(self):
            data = """
            class MyClass {
            public int a;
            public bool b = true;

            public int c(){
                if (b == false) true; else false;
                if (true == false) true; else false;
                return 1;
            }
            private char d(){
                a = a + 1;
                return 'a';
            }

            MyClass(int g){
                a = g;
            }
        }

        void kxi2023 main (){}
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 0)

    def test_big7(self):
            data = """
            void kxi2023 main (){
                bool b;
                int a = 1 + 2;
                char char1 = 'c';

                string beef = "beef";
                string beef_more = "no more \\n beef";
            
            int[] array = new int[2];
            while (array[0] != 10){
                array[0] += 1;
                array[1] -= 2;
            }

            cout << beef;

            cout << beef_more;

            array[0];
            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 0)

    def test_int_variableDeclaration_Main(self):
        data = """
        class IntClass{
            IntClass(){}
            public int a = 1;
            private int b;
            public int[] c;
            private int d(){
                int a = 1;
                return a;
            }
            public int[] e(){
                int[] f = new int[4];
                return f;
            }
        }

        class Other{
            public int otherInt;
            public int myMethod(int x){
                x += 3;
                return x;
            }
            Other(){}
        }

        void kxi2023 main (){
            //do some initializing 
            int a = new int[1];                 //error 0
            int c;
            int[] d = new int[1];
            int[] e;
            int f;
            IntClass iii = new IntClass();
            Other ooo = new Other();

            //create variables of all types
            char char1;
            char[] char2;
            bool boo = false;
            bool[] boo2;
            string str;
            string[] str2;

            
            //assign to ints
            c = iii.a;
            c = iii.e();                           //error 1 line 47
            e = iii.a;                             //error 2
            e = iii.e();
            c  = ooo.otherInt;
            c = ooo.myMethod(f);
            d[1] = 3;
            f = -123;

            //wrong type 
            c = iii.otherInt;                   //error line 56
            c = iii.myMethod(f);
            int x = new Other();
            int y;
            int[] z;
            y = char1;
            y = char2;
            y = boo;
            y = boo2;
            y = str;
            y = str2;
            y = iii;
            z = char1;
            z = char2;
            z = boo;
            z = boo2;
            z = str;
            z = str2;
            z = iii;
        }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(len(symbolTable.errors), 0)
        undeclaredVariableVistior = UndeclaredVisitor()
        undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
        myAST.accept(undeclaredVariableVistior)
        self.assertEqual(len(undeclaredVariableVistior.errors), 0)
        typeCheck = TypeChecking()
        typeCheck.paramList = symbolTable.paramList
        typeCheck.symbol_tables = symbolTable.symbol_tables
        myAST.accept(typeCheck)
        self.assertEqual(len(typeCheck.errors), 23)

    def test_char_variableDeclaration_Main(self):
        data = """
        class CharClass{
            CharClass(){}
            public char a = 'a';
            private char b;
            public char[] c;
            private char d(){
                char a = 'n';
                return a;
            }
            public char[] e(){
                char[] f = new char[4];
                return f;
            }
        }

        class Other{
            public char otherChar;
            public char myMethod(char x){
                x = 'b';
                return x;
            }
            Other(){}
        }

        void kxi2023 main (){
            //do some initializing 
            char a = new char[1];                 //error 0
            char c;
            char[] d = new char[1];
            char[] e;
            char f;
            CharClass iii = new CharClass();
            Other ooo = new Other();

            //create variables of all types
            int int1;
            int[] int2;
            char char1;
            char[] char2;
            bool boo = false;
            bool[] boo2;
            string str;
            string[] str2;

            
            //assign to ints
            c = iii.a;
            c = iii.e();                           //error 1 line 49
            e = iii.a;                             //error 2
            e = iii.e();
            c  = ooo.otherChar;
            c = ooo.myMethod(f);
            c = ooo.myMethod('a');
            d[1] = 'a';
            d = 'b';
            f = 'a';

            //wrong type 
            c = iii.otherChar;                   //error line 56
            c = ooo.myMethod(3);
            char x = new Other();
            char y;
            char[] z;
            y = char1;
            y = char2;
            y = boo;
            y = boo2;
            y = str;
            y = str2;
            y = iii;
            y= int1;
            y = int2;
            z = char1;
            z = char2;
            z = boo;
            z = boo2;
            z = str;
            z = str2;
            z = iii;
            z = int1;
            z = int2;
        }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(len(symbolTable.errors), 0)
        undeclaredVariableVistior = UndeclaredVisitor()
        undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
        myAST.accept(undeclaredVariableVistior)
        self.assertEqual(len(undeclaredVariableVistior.errors), 0)
        typeCheck = TypeChecking()
        typeCheck.paramList = symbolTable.paramList
        typeCheck.symbol_tables = symbolTable.symbol_tables
        myAST.accept(typeCheck)
        self.assertEqual(len(typeCheck.errors), 24)

    def test_bool_variableDeclaration_Main(self):
        data = """
        class BoolClass{
            BoolClass(){}
            public bool a = true;
            private bool b;
            public bool[] c;
            private bool d(){
                bool a = true;
                return a;
            }
            public bool[] e(){
                bool[] f = new bool[4];
                return f;
            }
        }

        class Other{
            public bool otherBool;
            public bool myMethod(bool x){
                x = false;
                return x;
            }
            Other(){}
        }

        void kxi2023 main (){
            //do some initializing 
            bool a = new bool[1];                 //error 0
            bool c;
            bool[] d = new bool[1];
            bool[] e;
            bool f;
            BoolClass iii = new BoolClass();
            Other ooo = new Other();

            //create variables of all types
            int int1;
            int[] int2;
            char char1;
            char[] char2;
            bool boo = false;
            bool[] boo2;
            string str;
            string[] str2;

            
            //assign to ints
            c = iii.a;
            c = iii.e();                           //error 1 line 49
            e = iii.a;                             //error 2
            e = iii.e();
            c  = ooo.otherBool;
            c = ooo.myMethod(f);
            c = ooo.myMethod(true);
            d[1] = true;
            d = false;
            f = true;

            //wrong type 
            c = iii.otherBool;                   //error line 60
            c = ooo.myMethod(3);
            bool x = new Other();
            bool y;
            bool[] z;
            y = char1;
            y = char2;
            y = boo;
            y = boo2;
            y = str;
            y = str2;
            y = iii;
            y= int1;
            y = int2;
            z = char1;
            z = char2;
            z = boo;
            z = boo2;
            z = str;
            z = str2;
            z = iii;
            z = int1;
            z = int2;
        }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(len(symbolTable.errors), 0)
        undeclaredVariableVistior = UndeclaredVisitor()
        undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
        myAST.accept(undeclaredVariableVistior)
        self.assertEqual(len(undeclaredVariableVistior.errors), 0)
        typeCheck = TypeChecking()
        typeCheck.paramList = symbolTable.paramList
        typeCheck.symbol_tables = symbolTable.symbol_tables
        myAST.accept(typeCheck)
        self.assertEqual(len(typeCheck.errors), 24)

    def test_string_variableDeclaration_Main(self):
        data = """
        class StringClass{
            StringClass(){}
            public string a = "true";
            private string b;
            public string[] c;
            private string d(){
                string a = "new string";
                return a;
            }
            public string[] e(){
                string[] f = new string[4];
                return f;
            }
        }

        class Other{
            public string otherString;
            public string myMethod(string x){
                x = "other string";
                return x;
            }
            Other(){}
        }

        void kxi2023 main (){
            //do some initializing 
            string a = new string[1];                 //error 0
            string c;
            string[] d = new string[1];
            string[] e;
            string f;
            StringClass iii = new StringClass();
            Other ooo = new Other();

            //create variables of all types
            int int1;
            int[] int2;
            char char1;
            char[] char2;
            bool boo = false;
            bool[] boo2;
            string str;
            string[] str2;

            
            //assign to ints
            c = iii.a;
            c = iii.e();                           //error 1 line 49
            e = iii.a;                             //error 2
            e = iii.e();
            c  = ooo.otherString;
            c = ooo.myMethod(f);
            c = ooo.myMethod("true");
            d[1] = "asdfasdf";
            d = "fffffff";
            f = "aaaaaaaaaaa";

            //wrong type 
            c = iii.otherString;                   //error line 60
            c = ooo.myMethod(3);
            string x = new Other();
            string y;
            string[] z;
            y = char1;
            y = char2;
            y = boo;
            y = boo2;
            y = str;
            y = str2;
            y = iii;
            y= int1;
            y = int2;
            z = char1;
            z = char2;
            z = boo;
            z = boo2;
            z = str;
            z = str2;
            z = iii;
            z = int1;
            z = int2;
        }
        """
        theLexer.theLexerReturnFucntion(data)
        myAST = theParser.Parse(data)
        symbolTable = SymbolTableVisitor()
        myAST.accept(symbolTable)
        self.assertEqual(len(symbolTable.errors), 0)
        undeclaredVariableVistior = UndeclaredVisitor()
        undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
        myAST.accept(undeclaredVariableVistior)
        self.assertEqual(len(undeclaredVariableVistior.errors), 0)
        typeCheck = TypeChecking()
        typeCheck.paramList = symbolTable.paramList
        typeCheck.symbol_tables = symbolTable.symbol_tables
        myAST.accept(typeCheck)
        self.assertEqual(len(typeCheck.errors), 24)

    def test_null(self):
            data = """
            class MyClass {
                MyClass(){}
                public int pubInt1 = 1;
                public int[] pubInt2;
                public char pubChar1;
                public char[] pubChar2;
                public bool pubBool1;
                public bool[] pubBool2;
                public string pubStr1;
                public string[] pubStr2;
                public OtherClass other1;
            }

            class OtherClass{
                OtherClass(){}
                public string[]otherSt1(){
                    string[] ssss = new string[2];
                    return ssss;
                }
                public OtherClass otherother(){
                    OtherClass ccc = new OtherClass();
                    return ccc;
                }
            }


            void kxi2023 main (){
                int int1 = null;
                int[] int2 = null;
                char char1 = null;
                char[] char2 = null;
                bool bool1 = null;
                bool[] bool2 = null;
                string str1 = null;
                string[] str2 = null;

                int int3 = 1;
                int[] int4 = new int[3];
                char char3 = 'a';
                char[] char4 = new char[5];
                bool bool3 = false;
                bool[] bool4 = new bool[7];
                string str3 = "test 1";
                string[] str4 = new string[2];  

                int3 = null;
                int4 = null;
                char3 = null;
                char4 = null;
                bool3 = null;
                bool4 = null;
                str3 = null;
                str4 = null;     

                MyClass myclass = new MyClass();
                OtherClass otherclass = new OtherClass();

                myclass.pubInt1 = null;
                myclass.pubInt2 = null;   
                myclass.pubChar1 = null;
                myclass.pubChar2 = null;
                myclass.pubBool1 = null; 
                myclass.pubBool2 = null;
                myclass.pubStr1 = null; 
                myclass.pubStr2 = null; 

                myclass = null;
                otherclass = null;

                MyClass[] myclass2 = new MyClass[2];
                OtherClass[] otherclass2 = new OtherClass[1];

                otherclass.otherother = null;
                otherclass.otherSt1 = null;
                otherclass2[2].otherother = null;
                otherclass2[2].otherSt1 = null;

                myclass2 = null;
                otherclass2 = null;
                myclass2[1] = null;
                otherclass2[3] = null;

                MyClass[] myclass3 = null;
                OtherClass[] otherclass3 = null;
                MyClass myclass4 = null;
                OtherClass otherclass4 = null;
            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 24)

    def test_parameters(self):
            data = """
            class MyClass {
                MyClass(){}
                public void myMethod(int int1, char[] charArray, bool b){}
                public bool[] myBool;
  
            }

            class OtherClass{
                OtherClass(MyClass mycl, int ii, bool[] b_array, string str, char cc){}
                public string sss = "this is a string";
            }


            void kxi2023 main (){
                int x;
                OtherClass other = new OtherClass(x, x, x, x, x);
                OtherClass other1 = new OtherClass(); //5 errors

                MyClass mine = new MyClass();
                bool[] b;
                string s = "this is a string";
                char c = 'c';
                OtherClass good = new OtherClass(mine, x, b, s, c);
                OtherClass good1 = new OtherClass(mine, x, mine.myBool, good.sss, c);
                OtherClass bad = new OtherClass(mine, x, b, s, s); // 6 errors

            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 6)

    def test_if_statements(self):
            data = """
            class MyClass {
                MyClass(){}
                public bool[] myBool;
                public bool boolMethod(int ii){
                    if (ii == 2) return true;
                }
                public MyClass returnMyClass(){
                    MyClass nnn = new MyClass();
                }

                public bool bb;
  
            }

            class OtherClass{
                OtherClass(MyClass mycl, int ii, bool[] b_array, string str, char cc, bool b){
                    if (b) true;
                    if (b_array) cout << str; //error 1
                }
            }


            void kxi2023 main (){
                int x;
                MyClass mine = new MyClass();
                if (mine.myBool) false; //error 2
                if (mine.boolMethod(x)) false;
                if (mine.boolMethod()) false; //error 3
                if (mine.bb) true;
                if (mine.returnMyClass().bb) true;
                if (mine.returnMyClass().myBool) true; //error 4
                if ('a') true; //error 5
                if (3 +3) cout << "done"; //error 6
                if (true) true;
                if (false) false;
            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 6)

    def test_while_statements(self):
            data = """
            class MyClass {
                MyClass(){}
                public bool[] myBool;
                public bool boolMethod(int ii){
                    if (ii == 2) return true;
                }
                public MyClass returnMyClass(){
                    MyClass nnn = new MyClass();
                    return nnn;
                }

                public bool bb;
  
            }

            class OtherClass{
                OtherClass(MyClass mycl, int ii, bool[] b_array, string str, char cc, bool b){
                    if (b) true;
                }
            }


            void kxi2023 main (){
                int x = 3;
                MyClass mine = new MyClass();

                while (true) cout << "test";
                while (false) cout << "test";
                while (x == 1) cout << "test1";
                while (x == 'a') cout << "test2";       //error 1 and 2
                while (x != 3) cout << "test3";      
                while (x < 'a') cout << "test4";      //error3 
                while (x < 1) cout << "test5";
                while (x <= 1) cout << "test6";
                while (x > 1) cout << "test7";
                while (x >= 1) cout << "test8";
                while (x >= 'a') cout << "test9";       //error 4
                while( x && true) cout << "test10";     //error 5 and 6
                while(x || false) cout << "test 11";    //error 7
                while(mine.myBool || false) cout << "test 12";  //error 8
                while(mine.boolMethod(x) || false) cout << "test 13";  
                while(mine.bb || false) cout << "test 14";  
                while(mine.returnMyClass().bb || false) cout << "test 15";  
                while(mine.returnMyClass() || false) cout << "test 16";  //error 9
            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 12)

    def test_bool_comparisons(self):
            data = """
            class MyClass {
                MyClass(){}
                public bool[] myBool;
                public bool boolMethod(int ii){
                    if (ii == 2) return true;
                }
                public MyClass returnMyClass(){
                    MyClass nnn = new MyClass();
                }

                public bool bb;
  
            }

            class OtherClass{
                OtherClass(MyClass mycl, int ii, bool[] b_array, string str, char cc, bool b){
                    if (b) true;
                }
            }


            void kxi2023 main (){
                true == true;
                true == false;
                false == false;
                false == true;
                
                true != true;
                true != false;
                false != false;
                false != true;
                
                true && true;
                true && false;
                false && false;
                false && true;
                
                true && true;
                true && false;
                false && false;
                false && true;
                
            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 0)

    def test_return_type(self):
            data = """
            class MyClass {
                MyClass(){}
                public bool boolMethod(int ii){
                    if (ii == 2) return true;
                }

                public MyClass returnMyClass(){
                    MyClass nnn = new MyClass();
                    return nnn;
                    return 1;           //error 1
                    return 'a';         //errror 2
                    return true;        //error 3
                    return "string";    //error 4

                    int int1;
                    int[] int2 = new int[3];
                    char char1;
                    char[] char2 = new char[3];
                    bool bool1;
                    bool[] bool2 = new bool[3];
                    string str1;
                    string[] str2 = new string[3];

                    return int1;        //error 5
                    return int2;         //error 6   
                    return char1;       //error 7
                    return char2;       //error 8
                    return bool1;       //error 9
                    return bool2;       //error 10
                    return str1;        //error 11
                    return str2;           //error 12 

                }
  
            }

            class OtherClass{
                OtherClass(MyClass mycl, int ii, bool[] b_array, string str, char cc, bool b){
                    if (b) true;
                }
                public void Voooid(){           //error 13- 27
                    MyClass nnn = new MyClass();
                    return nnn;         //error
                    return 1;           //error 1
                    return 'a';         //errror 2
                    return true;        //error 3
                    return false;        //error 
                    return "string";    //error 4

                    int int1;
                    int[] int2 = new int[3];
                    char char1;
                    char[] char2 = new char[3];
                    bool bool1;
                    bool[] bool2 = new bool[3];
                    string str1;
                    string[] str2 = new string[3];

                    return int1;        //error 5
                    return int2;         //error 6   
                    return char1;       //error 7
                    return char2;       //error 8
                    return bool1;       //error 9
                    return bool2;       //error 10
                    return str1;        //error 11
                    return str2;           //error 12 
                }
            }

            class Working{
                Working(){}

                private int i3;
                private int[] i5;
                private char c3;
                private char[] c5;
                private bool b3;
                private bool[] b5;
                private string s3;
                private string[] s5;
                private MyClass m3;
                private MyClass[] m5;

                public void Vooid(){
                    return;
                }
                public void Vooid2(){
                    int x = 1;
                }
                public int I1(){
                    return 1;
                }
                public int I2(){
                    int iii = 1;
                    return iii;
                }
                public int I3(){
                    return i3;
                }
                private int[] I444(){
                    int[] iii = new int[4];
                    return iii;
                }
                public int[] I5(){
                    return i5;
                }

                
                public char C1(){
                    return 'a';
                }
                public char C2(){
                    char ccc = 'a';
                    return ccc;
                }
                public char C3(){
                    return c3;
                }
                private char[] C444(){
                    char[] ccc = new char[4];
                    return ccc;
                }
                public char[] C5(){
                    return c5;
                }
                

                public bool B1(){
                    return true;
                }
                public bool B11(){
                    return false;
                }
                public bool B2(){
                    bool bbb = true;
                    return bbb;
                }
                public bool B3(){
                    return b3;
                }
                private bool[] B444(){
                    bool[] bbb = new bool[4];
                    return bbb;
                }
                public bool[] B5(){
                    return b5;
                }

                
                public string S1(){
                    return "a";
                }
                public string S2(){
                    string sss = "aaaa";
                    return sss;
                }
                public string S3(){
                    return s3;
                }
                private string[] s444(){
                    string[] sss = new string[4];
                    return sss;
                }
                public string[] S5(){
                    return s5;
                }
                

                public MyClass M2(){
                    MyClass mmm = new MyClass();
                    return mmm;
                }
                public MyClass M3(){
                    return m3;
                }
                private MyClass[] M444(){
                    MyClass[] mmm = new MyClass[4];
                    return mmm;
                }
                public MyClass[] M5(){
                    return m5;
                }
                
            }


            void kxi2023 main (){
                
            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 26)

    def test_cout_statement(self):
            data = """
            class MyClass {
                MyClass(){}
                public bool boolMethod(int ii){
                    if (ii == 2) return true;
                }

                public MyClass returnMyClass(){
                    MyClass nnn = new MyClass();
                    cout << nnn;                    //error 1
                    return nnn;
                }
            }

            class OtherClass{
                OtherClass(MyClass mycl, int ii, bool[] b_array, string str, char cc, bool b){
                    if (b) true;
                }
                public void Voooid(){          
                    cout << 1;
                    cout << (1+2);
                    int a;
                    int b;
                    cout << (a+b);
                    return;
                }
            }

            void kxi2023 main (){
                cout << true;       //error 2
                cout << false;      //error 3

                bool b;
                cout << b;          //error 4

                cout << 'a';
                char cc;
                cout << cc;

                char[] carray = new char[3];
                cout << carray;    //error 5
                cout << carray[4];
                
                int[] iarray = new int[5];
                cout << iarray;     //error 6
                cout << iarray[3];

                cout << "this is string";
                string ss = "sssss";
                cout << ss;

                string[] sarray = new string[4];
                cout << sarray;            //error 7
            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 7)

    def test_cin_statement(self):
            data = """
            class MyClass {
                MyClass(){}
                private int iii;
                public bool boolMethod(int ii){
                    if (ii == 2) return true;
                }

                public MyClass returnMyClass(){
                    MyClass nnn = new MyClass();
                    cin >> nnn;                    //error 1
                    cin >> iii;
                    return nnn;
                }
            }

            class OtherClass{
                OtherClass(MyClass mycl, int ii, bool[] b_array, string str, char cc, bool b){
                    if (b) true;
                }
                public void Voooid(){          
                    cin >> 1;       
                    cin >> (1+2);   
                    int a;
                    int b;
                    cin >> (a+b);   
                    cin >> a;
                    cin >> b;
                    return;
                }
            }

            void kxi2023 main (){
                cin >> 'a';
                char cc;
                cin >> cc;

                char[] carray = new char[3];
                cin >> carray;
                cin >> carray[4];   //error 2

                int[] iarray = new int[5];
                cin >> iarray;      //error 3
                cin >> iarray[3];

                cin >> "this is string";        //error 4
                string ss = "sssss";
                cin >> ss;     //error 5

                string[] sarray = new string[4];
                cin >> sarray;      //error 6
                cin >> sarray[2];       //error 7

            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 7)

    def test_switch(self):
            data = """
            class MyClass {
                MyClass(){}
                public int iii;
                public bool boolMethod(int ii){
                    if (ii == 2) return true;
                }

                public MyClass returnMyClass(){
                    MyClass nnn = new MyClass();
                    return nnn;
                }
            }

            class OtherClass{
                OtherClass(MyClass mycl, int ii, bool[] b_array, string str, char cc, bool b){
                    if (b) true;
                }
                public void Voooid(){          
                    return;
                }
            }

            void kxi2023 main (){ 
                int a;
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
                int[] b;
                switch (b) {        //error 1
                    case 1:
                        cout << '-';
                        break;
                    case 'a':
                        cout << '.';
                    case 3:
                        cout << ',';
                        break;
                    default:
                        cout << '+';
                }
                switch (b[1]) {        
                    case 1:
                        cout << '-';
                        break;
                    case 'a':
                        cout << '.';
                    case 3:
                        cout << ',';
                        break;
                    default:
                        cout << '+';
                }
                char c;
                switch (c) {        
                    case 1:
                        cout << '-';
                        break;
                    case 'a':
                        cout << '.';
                    case 3:
                        cout << ',';
                        break;
                    default:
                        cout << '+';
                }
                char[] cc;
                switch (cc) {        //error 2
                    case 1:
                        cout << '-';
                        break;
                    case 'a':
                        cout << '.';
                    case 3:
                        cout << ',';
                        break;
                    default:
                        cout << '+';
                }
                switch (cc[1]) {        
                    case 1:
                        cout << '-';
                        break;
                    case 'a':
                        cout << '.';
                    case 3:
                        cout << ',';
                        break;
                    default:
                        cout << '+';
                }
                bool bb;
                switch (bb) {        //error 3
                    case 1:
                        cout << '-';
                        break;
                    case 'a':
                        cout << '.';
                    case 3:
                        cout << ',';
                        break;
                    default:
                        cout << '+';
                }
                bool[] bbb;
                switch (bbb) {        //error 4
                    case 1:
                        cout << '-';
                        break;
                    case 'a':
                        cout << '.';
                    case 3:
                        cout << ',';
                        break;
                    default:
                        cout << '+';
                }
                switch (true) {        //error 5
                    case 1:
                        cout << '-';
                        break;
                    case 'a':
                        cout << '.';
                    case 3:
                        cout << ',';
                        break;
                    default:
                        cout << '+';
                }
                switch (false) {        //error 6
                    case 1:
                        cout << '-';
                        break;
                    case 'a':
                        cout << '.';
                    case 3:
                        cout << ',';
                        break;
                    default:
                        cout << '+';
                }
                switch (null) {        //error 7
                    case 1:
                        cout << '-';
                        break;
                    case 'a':
                        cout << '.';
                    case 3:
                        cout << ',';
                        break;
                    default:
                        cout << '+';
                }
                string sss;
                switch (sss) {        //error 8
                    case 1:
                        cout << '-';
                        break;
                    case 'a':
                        cout << '.';
                    case 3:
                        cout << ',';
                        break;
                    default:
                        cout << '+';
                }
                string[] ssss;
                switch (ssss) {        //error 9
                    case 1:
                        cout << '-';
                        break;
                    case 'a':
                        cout << '.';
                    case 3:
                        cout << ',';
                        break;
                    default:
                        cout << '+';
                }
                switch (ssss[1]) {        //error 10
                    case 1:
                        cout << '-';
                        break;
                    case 'a':
                        cout << '.';
                    case 3:
                        cout << ',';
                        break;
                    default:
                        cout << '+';
                }
                switch ('a') {        
                    case 1:
                        cout << '-';
                        break;
                    case 'a':
                        cout << '.';
                    case 3:
                        cout << ',';
                        break;
                    default:
                        cout << '+';
                }
                switch (1) {        
                    case 1:
                        cout << '-';
                        break;
                    case 'a':
                        cout << '.';
                    case 3:
                        cout << ',';
                        break;
                    default:
                        cout << '+';
                }
                MyClass mm = new MyClass();
                switch (mm.iii) {        
                    case 1:
                        cout << '-';
                        break;
                    case 'a':
                        cout << '.';
                    case 3:
                        cout << ',';
                        break;
                    default:
                        cout << '+';
                }
                switch (mm.returnMyClass().iii) {        
                    case 1:
                        cout << '-';
                        break;
                    case 'a':
                        cout << '.';
                    case 3:
                        cout << ',';
                        break;
                    default:
                        cout << '+';
                }
            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 10)

    def test_ExEqualEx2(self):
            data = """
            class MyClass {
                MyClass(){}
                public int iii;

                public bool boolMethod(int ii){
                    if (ii == 2) return true;
                }

                public MyClass returnMyClass(){
                    MyClass nnn = new MyClass();
                    return nnn;
                }
            }

            class OtherClass{
                OtherClass(MyClass mycl, int ii, bool[] b_array, string str, char cc, bool b){
                    if (b) true;
                }
                public void Voooid(){         
                    return;
                }
            }

            void kxi2023 main (){
                MyClass m = null;
                int[] iarray = null;
                char[] carray = null;
                bool[] barray = null;
                string[] sarray = null;

                null = m;       //error 1
                m.returnMyClass() = null;
                m.returnMyClass().iii = null;       //error 2 ,3
                1 = 3;
                int i1;
                int i2;
                i1 = 1;
                1 = i1;
                i1 = i2;

                iarray = i1;        //error 4
                iarray[2] = i2;
                i2 = iarray[3];     
                iarray[3] = m.returnMyClass().iii;
                i1 = 'a';           //error 5
                i1 = true;          //error 6
                i1 = false;         //error 7
                bool boo;
                i1 = boo;           //error 8
                i1 = "string";      //error 9
                string str;     
                char cc;
                i1 = str;           //error 10
                i1 = cc;            //error 11

                'a' = 'b';
                cc = 'a';
                'a' = cc;
                carray = cc;       //error 12
                cc = carray;        //error 13
                cc = carray[1];
                carray[2] = cc;
                cc = null;      //error 14 15
                cc = 1;         //15
                cc = i1;        //16
                cc = iarray;        //17
                cc = true;  //18    
                cc = false; //19
                cc = boo;   //20
                cc = "string";  //21
                cc = str;       //22
                cc = m;     //23
                i1 = m;     //25

                "string" = "string";
                "string" = str;
                str = "string";
                str = sarray;   //26
                sarray = str;   //27
                sarray[1] = str;
                str = sarray[3];
                str = null;     //28 29
                str = 1;    //30
                str = i1;   //31
                str = iarray;   //32
                str = 'a';      //33
                str = cc;       //34
                str = true;     //35
                str = false;        //36
                str = boo;      //37
                str = m;        //38

                true = false;   //39
                false = false;  //40
                true = true;    //41
                false = false;  //42
                true = boo;     //43
                boo = true;
                false = boo;    //44
                boo = false;
                boo = barray;       //39
                barray = boo;       //40
                barray[1] = boo;
                boo = barray[1];
                true = barray[1];   //45
                barray[1] = true;
                false = barray[1];  //46
                barray[1] = false;
                barray = false;     //41
                false = barray;        //42
                barray = true;      //43
                true = barray;      //44


            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 52)

    def test_ExPlusEqualEx2(self):
            data = """
            class MyClass {
                MyClass(){}
                public int iii;
                public char ccc;
                public int[] iarray;

                public MyClass returnMyClass(){
                    MyClass nnn = new MyClass();
                    return nnn;
                }
            }

            void kxi2023 main (){
                MyClass m = null;
                int i1;
                int[] iarray;
                char c1;
                bool b1;
                string s1;
                bool[] barray;

                i1 += null; //1
                i1 += 1;
                1 += i1;
                i1 += i1;
                i1 += m.returnMyClass().iii;
                i1 += m.iii;
                m.returnMyClass().iii += i1;
                m.iii += m.returnMyClass().iii;

                i1 += iarray;   //2
                iarray += i1;   //3
                i1 += iarray[1];
                iarray[1] += i1;
                i1 += 'c';  //4
                i1 += c1;   //5
                'c' += i1;  //6
                c1 += i1;   //7
                true += i1; //8
                i1 += true; //9
                false += i1;    //10
                i1 += false;    //11
                i1 += b1;       //12
                b1 += i1;       //13
                i1 += s1;       //14
                s1 += i1;       //15
                m += i1;        //16
                i1 += m;        //17

                null += null;       //18
                iarray += iarray;       //19
                null += i1;         //20
                iarray[1] += iarray[45];
                'c' += 'c';     //21
                c1 += c1;       //22
                'c' += c1;      //23
                c1 += 'c';      //24

                true += true;   //25
                false += false; //26
                true += false;  //27
                false += false; //28
                b1 += b1;       //29
                b1 += true;     //30
                b1 += false;       // 31
                true += b1;     //32
                false += b1;        //33
                b1 += barray;       //34
                b1 += barray[1];      //35
                barray[1] += b1;        //36
                s1 += s1;       //37
                "string" += s1;     //38
                s1 += "sss";        //39
                m += m;     //40
            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 40)
    
    def test_ExMinusEqualEx2(self):
            data = """
            class MyClass {
                MyClass(){}
                public int iii;
                public char ccc;
                public int[] iarray;

                public MyClass returnMyClass(){
                    MyClass nnn = new MyClass();
                    return nnn;
                }
            }

            void kxi2023 main (){
                MyClass m = null;
                int i1;
                int[] iarray;
                char c1;
                bool b1;
                string s1;
                bool[] barray;

                i1 -= null; //1
                i1 -= 1;
                1 -= i1;
                i1 -= i1;
                i1 -= m.returnMyClass().iii;
                i1 -= m.iii;
                m.returnMyClass().iii -= i1;
                m.iii -= m.returnMyClass().iii;

                i1 -= iarray;   //2
                iarray -= i1;   //3
                i1 -= iarray[1];
                iarray[1] -= i1;
                i1 -= 'c';  //4
                i1 -= c1;   //5
                'c' -= i1;  //6
                c1 -= i1;   //7
                true -= i1; //8
                i1 -= true; //9
                false -= i1;    //10
                i1 -= false;    //11
                i1 -= b1;       //12
                b1 -= i1;       //13
                i1 -= s1;       //14
                s1 -= i1;       //15
                m -= i1;        //16
                i1 -= m;        //17

                null -= null;       //18
                iarray -= iarray;       //19
                null -= i1;         //20
                iarray[1] -= iarray[45];
                'c' -= 'c';     //21
                c1 -=c1;       //22
                'c'-= c1;      //23
                c1 -= 'c';      //24

                true -= true;   //25
                false -= false; //26
                true -= false;  //27
                false -= false; //28
                b1 -= b1;       //29
                b1 -= true;     //30
                b1 -= false;       // 31
                true -= b1;     //32
                false -= b1;        //33
                b1 -= barray;       //34
                b1 -= barray[1];      //35
                barray[1] -= b1;        //36
                s1 -= s1;       //37
                "string" -= s1;     //38
                s1 -= "sss";        //39
                m -= m;     //40
            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 40)

    def test_ExDivideEqualEx2(self):
            data = """
            class MyClass {
                MyClass(){}
                public int iii;
                public char ccc;
                public int[] iarray;

                public MyClass returnMyClass(){
                    MyClass nnn = new MyClass();
                    return nnn;
                }
            }

            void kxi2023 main (){
                MyClass m = null;
                int i1;
                int[] iarray;
                char c1;
                bool b1;
                string s1;
                bool[] barray;

                i1 /= null; //1
                i1 /= 1;
                1 /= i1;
                i1 /= i1;
                i1 /= m.returnMyClass().iii;
                i1 /= m.iii;
                m.returnMyClass().iii /= i1;
                m.iii /= m.returnMyClass().iii;

                i1 /= iarray;   //2
                iarray /= i1;   //3
                i1 /= iarray[1];
                iarray[1] /= i1;
                i1 /= 'c';  //4
                i1 /= c1;   //5
                'c' /= i1;  //6
                c1 /= i1;   //7
                true /= i1; //8
                i1 /= true; //9
                false /= i1;    //10
                i1 /= false;    //11
                i1 /= b1;       //12
                b1 /= i1;       //13
                i1 /= s1;       //14
                s1 /= i1;       //15
                m /= i1;        //16
                i1 /= m;        //17

                null /= null;       //18
                iarray /= iarray;       //19
                null /= i1;         //20
                iarray[1] /= iarray[45];
                'c' /= 'c';     //21
                c1 /=c1;       //22
                'c' /= c1;      //23
                c1 /= 'c';      //24

                true /= true;   //25
                false /= false; //26
                true /= false;  //27
                false /= false; //28
                b1 /= b1;       //29
                b1 /= true;     //30
                b1 /= false;       // 31
                true /= b1;     //32
                false /= b1;        //33
                b1 /= barray;       //34
                b1 /= barray[1];      //35
                barray[1] /= b1;        //36
                s1 /= s1;       //37
                "string" /= s1;     //38
                s1 /= "sss";        //39
                m /= m;     //40
            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 40)

    def test_ExMultiplyEqualEx2(self):
            data = """
            class MyClass {
                MyClass(){}
                public int iii;
                public char ccc;
                public int[] iarray;

                public MyClass returnMyClass(){
                    MyClass nnn = new MyClass();
                    return nnn;
                }
            }

            void kxi2023 main (){
                MyClass m = null;
                int i1;
                int[] iarray;
                char c1;
                bool b1;
                string s1;
                bool[] barray;

                i1 *= null; //1
                i1 *= 1;
                1 *= i1;
                i1 *= i1;
                i1 *= m.returnMyClass().iii;
                i1 *= m.iii;
                m.returnMyClass().iii *= i1;
                m.iii *= m.returnMyClass().iii;

                i1 *= iarray;   //2
                iarray *= i1;   //3
                i1 *= iarray[1];
                iarray[1] *= i1;
                i1 *= 'c';  //4
                i1 *= c1;   //5
                'c' *= i1;  //6
                c1 *= i1;   //7
                true *=i1; //8
                i1 *= true; //9
                false *= i1;    //10
                i1 *= false;    //11
                i1 *= b1;       //12
                b1 *= i1;       //13
                i1 *= s1;       //14
                s1 *= i1;       //15
                m *= i1;        //16
                i1 *= m;        //17

                null *= null;       //18
                iarray *= iarray;       //19
                null *= i1;         //20
                iarray[1] *= iarray[45];
                'c' *= 'c';     //21
                c1 *=c1;       //22
                'c' *= c1;      //23
                c1 *= 'c';      //24

                true *= true;   //25
                false *= false; //26
                true *= false;  //27
                false *= false; //28
                b1 *= b1;       //29
                b1 *= true;     //30
                b1 *= false;       // 31
                true *= b1;     //32
                false *= b1;        //33
                b1 *= barray;       //34
                b1 *= barray[1];      //35
                barray[1] *= b1;        //36
                s1 *= s1;       //37
                "string" *= s1;     //38
                s1 *= "sss";        //39
                m *= m;     //40
            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 40)

    def test_ExPlusEx2(self):
            data = """
            class MyClass {
                MyClass(){}
                public int iii;
                public char ccc;
                public int[] iarray;

                public MyClass returnMyClass(){
                    MyClass nnn = new MyClass();
                    return nnn;
                }
            }

            void kxi2023 main (){
                MyClass m = null;
                int i1;
                int[] iarray;
                char c1;
                bool b1;
                string s1;
                bool[] barray;

                i1 + null; //1
                i1 + 1;
                1 + i1;
                i1 + i1;
                i1 + m.returnMyClass().iii;
                i1 + m.iii;
                m.returnMyClass().iii + i1;
                m.iii + m.returnMyClass().iii;

                i1 + iarray;   //2
                iarray + i1;   //3
                i1 + iarray[1];
                iarray[1] + i1;
                i1 + 'c';  //4
                i1 + c1;   //5
                'c' + i1;  //6
                c1 + i1;   //7
                true +i1; //8
                i1 + true; //9
                false + i1;    //10
                i1 + false;    //11
                i1 + b1;       //12
                b1 + i1;       //13
                i1 + s1;       //14
                s1 + i1;       //15
                m + i1;        //16
                i1 + m;        //17

                null + null;       //18
                iarray + iarray;       //19
                null + i1;         //20
                iarray[1] + iarray[45];
                'c' + 'c';     //21
                c1 +c1;       //22
                'c' + c1;      //23
                c1 + 'c';      //24

                true + true;   //25
                false + false; //26
                true + false;  //27
                false + false; //28
                b1 + b1;       //29
                b1 + true;     //30
                b1 + false;       // 31
                true + b1;     //32
                false + b1;        //33
                b1 + barray;       //34
                b1 + barray[1];      //35
                barray[1] + b1;        //36
                s1 + s1;       //37
                "string" +s1;     //38
                s1 + "sss";        //39
                m + m;     //40
            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 40)

    def test_ExMinusEx2(self):
            data = """
            class MyClass {
                MyClass(){}
                public int iii;
                public char ccc;
                public int[] iarray;

                public MyClass returnMyClass(){
                    MyClass nnn = new MyClass();
                    return nnn;
                }
            }

            void kxi2023 main (){
                MyClass m = null;
                int i1;
                int[] iarray;
                char c1;
                bool b1;
                string s1;
                bool[] barray;

                i1 - null; //1
                i1 - 1;
                1 - i1;
                i1 - i1;
                i1 - m.returnMyClass().iii;
                i1 - m.iii;
                m.returnMyClass().iii - i1;
                m.iii - m.returnMyClass().iii;

                i1 - iarray;   //2
                iarray - i1;   //3
                i1 - iarray[1];
                iarray[1] - i1;
                i1 - 'c';  //4
                i1 - c1;   //5
                'c' - i1;  //6
                c1 - i1;   //7
                true -i1; //8
                i1 - true; //9
                false - i1;    //10
                i1 - false;    //11
                i1 - b1;       //12
                b1 - i1;       //13
                i1 - s1;       //14
                s1- i1;       //15
                m - i1;        //16
                i1 - m;        //17

                null - null;       //18
                iarray - iarray;       //19
                null - i1;         //20
                iarray[1] - iarray[45];
                'c' - 'c';     //21
                c1 -c1;       //22
                'c' - c1;      //23
                c1 - 'c';      //24

                true - true;   //25
                false - false; //26
                true -false;  //27
                false - false; //28
                b1 - b1;       //29
                b1 - true;     //30
                b1 - false;       // 31
                true - b1;     //32
                false - b1;        //33
                b1 - barray;       //34
                b1 - barray[1];      //35
                barray[1] - b1;        //36
                s1 - s1;       //37
                "string" - s1;     //38
                s1 - "sss";        //39
                m - m;     //40
            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 40)

    def test_ExMultiplyEx2(self):
            data = """
            class MyClass {
                MyClass(){}
                public int iii;
                public char ccc;
                public int[] iarray;

                public MyClass returnMyClass(){
                    MyClass nnn = new MyClass();
                    return nnn;
                }
            }

            void kxi2023 main (){
                MyClass m = null;
                int i1;
                int[] iarray;
                char c1;
                bool b1;
                string s1;
                bool[] barray;

                i1 * null; //1
                i1 * 1;
                1 * i1;
                i1 * i1;
                i1 * m.returnMyClass().iii;
                i1 * m.iii;
                m.returnMyClass().iii * i1;
                m.iii * m.returnMyClass().iii;

                i1 * iarray;   //2
                iarray * i1;   //3
                i1 * iarray[1];
                iarray[1] * i1;
                i1 * 'c';  //4
                i1 * c1;   //5
                'c' * i1;  //6
                c1 * i1;   //7
                true *i1; //8
                i1 * true; //9
                false * i1;    //10
                i1 * false;    //11
                i1 * b1;       //12
                b1 * i1;       //13
                i1 * s1;       //14
                s1 * i1;       //15
                m * i1;        //16
                i1 * m;        //17

                null * null;       //18
                iarray * iarray;       //19
                null * i1;         //20
                iarray[1] * iarray[45];
                'c' * 'c';     //21
                c1 *c1;       //22
                'c' * c1;      //23
                c1 * 'c';      //24

                true * true;   //25
                false * false; //26
                true * false;  //27
                false * false; //28
                b1 * b1;       //29
                b1 * true;     //30
                b1 * false;       // 31
                true * b1;     //32
                false * b1;        //33
                b1 * barray;       //34
                b1 * barray[1];      //35
                barray[1] * b1;        //36
                s1 * s1;       //37
                "string" * s1;     //38
                s1 * "sss";        //39
                m * m;     //40
            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 40)

    def test_ExDivideEx2(self):
            data = """
            class MyClass {
                MyClass(){}
                public int iii;
                public char ccc;
                public int[] iarray;

                public MyClass returnMyClass(){
                    MyClass nnn = new MyClass();
                    return nnn;
                }
            }

            void kxi2023 main (){
                MyClass m = null;
                int i1;
                int[] iarray;
                char c1;
                bool b1;
                string s1;
                bool[] barray;

                i1 / null; //1
                i1 / 1;
                1 / i1;
                i1 / i1;
                i1 / m.returnMyClass().iii;
                i1 / m.iii;
                m.returnMyClass().iii / i1;
                m.iii / m.returnMyClass().iii;

                i1 / iarray;   //2
                iarray / i1;   //3
                i1 / iarray[1];
                iarray[1] / i1;
                i1 / 'c';  //4
                i1 / c1;   //5
                'c' / i1;  //6
                c1 / i1;   //7
                true /i1; //8
                i1 / true; //9
                false / i1;    //10
                i1 / false;    //11
                i1 / b1;       //12
                b1 / i1;       //13
                i1 / s1;       //14
                s1 / i1;       //15
                m / i1;        //16
                i1 / m;        //17

                null / null;       //18
                iarray / iarray;       //19
                null / i1;         //20
                iarray[1] / iarray[45];
                'c' / 'c';     //21
                c1/c1;       //22
                'c' / c1;      //23
                c1 / 'c';      //24

                true / true;   //25
                false / false; //26
                true / false;  //27
                false / false; //28
                b1 / b1;       //29
                b1 / true;     //30
                b1 / false;       // 31
                true / b1;     //32
                false / b1;        //33
                b1 / barray;       //34
                b1 / barray[1];      //35
                barray[1] / b1;        //36
                s1 / s1;       //37
                "string" / s1;     //38
                s1 / "sss";        //39
                m / m;     //40
            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 40)

    def test_ExCEqualEx2(self):
            data = """
            class MyClass {
                MyClass(){}
                public int iii;

                public bool boolMethod(int ii){
                    if (ii == 2) return true;
                }

                public MyClass returnMyClass(){
                    MyClass nnn = new MyClass();
                    return nnn;
                }
            }

            class OtherClass{
                OtherClass(MyClass mycl, int ii, bool[] b_array, string str, char cc, bool b){
                    if (b) true;
                }
                public void Voooid(){         
                    return;
                }
            }

            void kxi2023 main (){
                MyClass m = null;
                OtherClass oc;
                int[] iarray = null;
                char[] carray = null;
                bool[] barray = null;
                string[] sarray = null;
                char c1;
                string s1;
                bool b1;

                null == m;       
                m.returnMyClass() == null; 
                m.returnMyClass().iii == null;       //3
                1 == 3;
                int i1;
                int i2;
                i1 == 1;
                1 == i1;
                i1 == i2;
                m.returnMyClass().iii == i1;
                m.returnMyClass().iii == 1;
                m.returnMyClass().iii == 'a';   //4
                1 == m.returnMyClass().iii;
                iarray == 1;    //5
                1 == iarray;    //6
                i1 == iarray;   //7
                iarray == i1;   //8
                iarray[1] == 1;
                1 == iarray[3];
                i1 == iarray[2];
                iarray[2] == i1;
                i1 == c1;   //7
                i1 == null; //8
                null == 10;     //9
                null == i1;
                null == 'c';
                null == c1;
                null == true;
                null == false;  
                null == b1; 
                null == s1; //16
                null == m;  
                i1 == b1;   //17
                i1 == s1;
                i1 == m;    //19

                c1 == c1;
                c1 == carray;
                carray == c1;   //21
                c1 == 'a';
                'a' == c1;
                carray[1] == c1;
                carray[1] == 'a';
                c1 == b1;
                c1 == s1;
                c1 == m;    //24

                b1 == b1;
                b1 == true;
                b1 == false;
                true == true;
                false == false;
                false == b1;
                true == b1;
                b1 == barray;
                barray == b1; //28
                barray[1] == true;
                b1 == barray[2];
                b1 == s1;
                b1 == m;    //30

                s1 == s1;
                "string" == "string";
                s1 == "string";
                "string" == s1;
                s1 == sarray[1];
                sarray[1] == "a";
                sarray == "hello";
                "hh" == sarray; //32
                s1 == m;

                m == s1;
                m == b1;
                m == c1;
                m == i1;        //35

                m == null;
                iarray == null;
                barray == null;
                sarray == null;
                carray == null;

                null == m;
                null == iarray;
                null == barray;
                null == sarray;
                null == carray;
            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 35)

    def test_ExNotEqualEx2(self):
            data = """
            class MyClass {
                MyClass(){}
                public int iii;

                public bool boolMethod(int ii){
                    if (ii == 2) return true;
                }

                public MyClass returnMyClass(){
                    MyClass nnn = new MyClass();
                    return nnn;
                }
            }

            class OtherClass{
                OtherClass(MyClass mycl, int ii, bool[] b_array, string str, char cc, bool b){
                    if (b) true;
                }
                public void Voooid(){         
                    return;
                }
            }

            void kxi2023 main (){
                MyClass m = null;
                OtherClass oc;
                int[] iarray = null;
                char[] carray = null;
                bool[] barray = null;
                string[] sarray = null;
                char c1;
                string s1;
                bool b1;

                null != m;       
                m.returnMyClass() != null; 
                m.returnMyClass().iii != null;       //3
                1 != 3;
                int i1;
                int i2;
                i1 != 1;
                1 != i1;
                i1 != i2;
                m.returnMyClass().iii != i1;
                m.returnMyClass().iii != 1;
                m.returnMyClass().iii != 'a';   //4
                1 != m.returnMyClass().iii;
                iarray != 1;    //5
                1 != iarray;    //6
                i1 != iarray;   //7
                iarray != i1;   //8
                iarray[1] != 1;
                1 != iarray[3];
                i1 != iarray[2];
                iarray[2] != i1;
                i1 != c1;   //7
                i1 != null; //8
                null != 10;     //9
                null != i1;
                null != 'c';
                null != c1;
                null != true;
                null != false;  
                null != b1; 
                null != s1; //16
                null != m;  
                i1 != b1;   //17
                i1 != s1;
                i1 != m;    //19

                c1 != c1;
                c1 != carray;
                carray != c1;   //21
                c1 != 'a';
                'a' != c1;
                carray[1] != c1;
                carray[1] != 'a';
                c1 != b1;
                c1 != s1;
                c1 != m;    //24

                b1 != b1;
                b1 != true;
                b1 != false;
                true != true;
                false != false;
                false != b1;
                true != b1;
                b1 != barray;
                barray != b1; //28
                barray[1] != true;
                b1 != barray[2];
                b1 != s1;
                b1 != m;    //30

                s1 != s1;
                "string" != "string";
                s1 != "string";
                "string" != s1;
                s1 != sarray[1];
                sarray[1] != "a";
                sarray != "hello";
                "hh" != sarray; //32
                s1 != m;

                m != s1;
                m!= b1;
                m != c1;
                m != i1;        //35

                m != null;
                iarray != null;
                barray != null;
                sarray != null;
                carray != null;

                null != m;
                null != iarray;
                null != barray;
                null != sarray;
                null != carray;
            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 35)

    def test_ExGreaterEx2(self):
            data = """
            class MyClass {
                MyClass(){}
                public int iii;

                public bool boolMethod(int ii){
                    if (ii == 2) return true;
                }

                public MyClass returnMyClass(){
                    MyClass nnn = new MyClass();
                    return nnn;
                }
            }

            class OtherClass{
                OtherClass(MyClass mycl, int ii, bool[] b_array, string str, char cc, bool b){
                    if (b) true;
                }
                public void Voooid(){         
                    return;
                }
            }

            void kxi2023 main (){
                MyClass m = null;
                OtherClass oc;
                int[] iarray = null;
                char[] carray = null;
                bool[] barray = null;
                string[] sarray = null;
                MyClass[] marray = new MyClass[3];
                char c1;
                int i1;
                string s1;
                bool b1;

                null > i1;
                null > 1;
                i1 > null;
                null > 1;

                null > c1;
                null > 'c';
                c1 > null;
                'c' > null;

                true > null;
                null > true;
                false > null;
                null > false;
                b1 > null;
                null > b1;

                s1 > null;
                null > s1;
                "string" > null;
                null > "string";

                m > null;
                null > m;

                iarray > null;
                null > iarray;
                carray > null;
                null > carray;
                barray > null;
                null > barray;
                sarray > null;
                null > sarray;
                marray > null;
                null > marray; //30

                i1 > 1;
                1 > i1;
                i1 > i1;
                1 > 2;
                i1 > iarray[1];
                iarray[1] > i1;
                i1 > m.iii;
                m.iii > i1;

                i1 > iarray;
                iarray > i1;
                i1 > c1;
                c1 > i1;
                i1 > carray;
                carray > i1;
                i1 > true;
                true > i1;
                i1 > false;
                false > i1;
                i1 > b1;
                b1 > i1;
                barray > i1;
                i1 > barray;
                i1 > "test";
                "test" > i1;
                i1 > s1;
                s1 > i1;
                sarray > i1;
                i1 > sarray;
                i1 > m;
                m > i1; //52

                'c' > 'c';
                c1 > 'c';
                'c' > c1;
                carray[1] > c1;
                c1 > carray[1];
                carray[1] > 'b';
                'b' > carray[1];

                c1 > 1;
                1 > c1;
                c1 > i1;
                i1 > c1;
                c1 > iarray;
                iarray > c1;
                c1 > carray;
                carray > c1;        //60
                true > c1;
                c1 > true;
                false > c1;
                c1 > false;
                b1 > c1;
                c1 > b1;
                barray > c1;
                c1 > barray;
                "tt" > c1;
                c1 > "cd";
                c1 > s1;
                s1 > c1;
                sarray > c1;
                c1 > sarray;
                m > c1;
                c1 > m;         //76

                b1 > true;
                false > b1;
                true > b1;
                b1 > b1;        //80
                b1 > false;
                barray[1] > b1;
                b1 > barray[1];
                b1 > "tt";
                "ttt" > b1;
                b1 > s1;
                s1 > b1;
                m > b1;
                b1 > m;

                "string" > "string";
                "ss" > s1;
                s1 > "sg";
                s1 > s1;
                s1 > sarray;
                sarray > s1;
                m > s1;
                s1 > m;
                
                m > m;
                m > m.returnMyClass();
            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 99)

    def test_ExGreaterEqualEx2(self):
            data = """
            class MyClass {
                MyClass(){}
                public int iii;

                public bool boolMethod(int ii){
                    if (ii == 2) return true;
                }

                public MyClass returnMyClass(){
                    MyClass nnn = new MyClass();
                    return nnn;
                }
            }

            class OtherClass{
                OtherClass(MyClass mycl, int ii, bool[] b_array, string str, char cc, bool b){
                    if (b) true;
                }
                public void Voooid(){         
                    return;
                }
            }

            void kxi2023 main (){
                MyClass m = null;
                OtherClass oc;
                int[] iarray = null;
                char[] carray = null;
                bool[] barray = null;
                string[] sarray = null;
                MyClass[] marray = new MyClass[3];
                char c1;
                int i1;
                string s1;
                bool b1;

                null >= i1;
                null >= 1;
                i1 >= null;
                null >= 1;

                null >= c1;
                null >= 'c';
                c1 >= null;
                'c' >= null;

                true >= null;
                null >=true;
                false >= null;
                null >= false;
                b1 >= null;
                null >= b1;

                s1 >= null;
                null >= s1;
                "string" >= null;
                null >= "string";

                m >= null;
                null >= m;

                iarray >= null;
                null >= iarray;
                carray >= null;
                null >= carray;
                barray >= null;
                null >= barray;
                sarray >= null;
                null >= sarray;
                marray >= null;
                null >= marray; //30

                i1 >= 1;
                1 >= i1;
                i1 >= i1;
                1 >= 2;
                i1 >= iarray[1];
                iarray[1] >= i1;
                i1 >= m.iii;
                m.iii >= i1;

                i1 >= iarray;
                iarray >= i1;
                i1 >= c1;
                c1 >= i1;
                i1 >= carray;
                carray >= i1;
                i1 >= true;
                true >= i1;
                i1 >= false;
                false >= i1;
                i1 >= b1;
                b1 >= i1;
                barray >= i1;
                i1 >= barray;
                i1 >= "test";
                "test" >= i1;
                i1 >= s1;
                s1 >= i1;
                sarray >= i1;
                i1 >= sarray;
                i1 >= m;
                m >= i1; //52

                'c' >= 'c';
                c1 >= 'c';
                'c' >= c1;
                carray[1] >= c1;
                c1 >= carray[1];
                carray[1] >= 'b';
                'b' >= carray[1];

                c1 >= 1;
                1 >= c1;
                c1 >= i1;
                i1 >= c1;
                c1 >= iarray;
                iarray >= c1;
                c1 >= carray;
                carray >= c1;        //60
                true >= c1;
                c1 >= true;
                false >= c1;
                c1 >= false;
                b1 >= c1;
                c1 >= b1;
                barray >= c1;
                c1 >= barray;
                "tt" >= c1;
                c1 >= "cd";
                c1 >= s1;
                s1 >= c1;
                sarray >= c1;
                c1 >= sarray;
                m >= c1;
                c1 >= m;         //76

                b1 >= true;
                false >= b1;
                true >= b1;
                b1 >= b1;        //80
                b1 >= false;
                barray[1] >= b1;
                b1 >= barray[1];
                b1 >= "tt";
                "ttt" >= b1;
                b1 >= s1;
                s1 >= b1;
                m >= b1;
                b1 >= m;

                "string" >= "string";
                "ss" >= s1;
                s1 >= "sg";
                s1 >= s1;
                s1 >= sarray;
                sarray >= s1;
                m >= s1;
                s1 >= m;
                
                m >= m;
                m >= m.returnMyClass();
            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 99)

    def test_ExLessEx2(self):
            data = """
            class MyClass {
                MyClass(){}
                public int iii;

                public bool boolMethod(int ii){
                    if (ii == 2) return true;
                }

                public MyClass returnMyClass(){
                    MyClass nnn = new MyClass();
                    return nnn;
                }
            }

            class OtherClass{
                OtherClass(MyClass mycl, int ii, bool[] b_array, string str, char cc, bool b){
                    if (b) true;
                }
                public void Voooid(){         
                    return;
                }
            }

            void kxi2023 main (){
                MyClass m = null;
                OtherClass oc;
                int[] iarray = null;
                char[] carray = null;
                bool[] barray = null;
                string[] sarray = null;
                MyClass[] marray = new MyClass[3];
                char c1;
                int i1;
                string s1;
                bool b1;

                null < i1;
                null < 1;
                i1 < null;
                null < 1;

                null < c1;
                null < 'c';
                c1 < null;
                'c' < null;

                true < null;
                null <true;
                false < null;
                null < false;
                b1 < null;
                null < b1;

                s1 < null;
                null < s1;
                "string" < null;
                null < "string";

                m < null;
                null < m;

                iarray < null;
                null < iarray;
                carray < null;
                null < carray;
                barray < null;
                null < barray;
                sarray < null;
                null < sarray;
                marray < null;
                null < marray; //30

                i1 < 1;
                1 < i1;
                i1 < i1;
                1 < 2;
                i1 < iarray[1];
                iarray[1] < i1;
                i1 < m.iii;
                m.iii < i1;

                i1 < iarray;
                iarray < i1;
                i1 < c1;
                c1 < i1;
                i1 < carray;
                carray < i1;
                i1 < true;
                true < i1;
                i1 < false;
                false < i1;
                i1 < b1;
                b1 < i1;
                barray < i1;
                i1 < barray;
                i1 < "test";
                "test" < i1;
                i1 < s1;
                s1 < i1;
                sarray < i1;
                i1 < sarray;
                i1 < m;
                m < i1; //52

                'c' < 'c';
                c1 < 'c';
                'c' < c1;
                carray[1] < c1;
                c1 < carray[1];
                carray[1] < 'b';
                'b' < carray[1];

                c1 < 1;
                1 < c1;
                c1 < i1;
                i1 < c1;
                c1 < iarray;
                iarray < c1;
                c1 < carray;
                carray < c1;        //60
                true < c1;
                c1 < true;
                false < c1;
                c1 < false;
                b1 < c1;
                c1 < b1;
                barray < c1;
                c1 < barray;
                "tt" < c1;
                c1 < "cd";
                c1 < s1;
                s1 < c1;
                sarray < c1;
                c1 < sarray;
                m < c1;
                c1 < m;         //76

                b1 < true;
                false < b1;
                true < b1;
                b1 < b1;        //80
                b1 < false;
                barray[1] < b1;
                b1 < barray[1];
                b1 < "tt";
                "ttt" < b1;
                b1 < s1;
                s1 < b1;
                m < b1;
                b1 < m;

                "string" < "string";
                "ss" < s1;
                s1 < "sg";
                s1 < s1;
                s1 < sarray;
                sarray < s1;
                m < s1;
                s1 < m;
                
                m < m;
                m < m.returnMyClass();
            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 99)

    def test_ExOOREx2(self):
            data = """
            class MyClass {
                MyClass(){}
                public int iii;

                public bool boolMethod(int ii){
                    if (ii == 2) return true;
                }

                public MyClass returnMyClass(){
                    MyClass nnn = new MyClass();
                    return nnn;
                }
            }

            class OtherClass{
                OtherClass(MyClass mycl, int ii, bool[] b_array, string str, char cc, bool b){
                    if (b) true;
                }
                public void Voooid(){         
                    return;
                }
            }

            void kxi2023 main (){
                MyClass m = null;
                OtherClass oc;
                int[] iarray = null;
                char[] carray = null;
                bool[] barray = null;
                string[] sarray = null;
                MyClass[] marray = new MyClass[3];
                char c1;
                int i1;
                string s1;
                bool b1;

                true || false;
                true || true;
                false || false;
                false || true;
                b1 || true;
                true || b1;
                b1 || false;
                false || b1;
                b1 || b1;
                b1 || (1 < 3);
                (1 < 3) || b1;
                (i1 == i1) || ('c' <= 'c');

                i1 || b1;
                b1 || i1;
                c1 || b1;
                b1 || c1;
                i1 || c1;
                s1 || b1;
                b1 || s1;
            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 7)

    def test_ExAANDEx2(self):
            data = """
            class MyClass {
                MyClass(){}
                public int iii;

                public bool boolMethod(int ii){
                    if (ii == 2) return true;
                }

                public MyClass returnMyClass(){
                    MyClass nnn = new MyClass();
                    return nnn;
                }
            }

            class OtherClass{
                OtherClass(MyClass mycl, int ii, bool[] b_array, string str, char cc, bool b){
                    if (b) true;
                }
                public void Voooid(){         
                    return;
                }
            }

            void kxi2023 main (){
                MyClass m = null;
                OtherClass oc;
                int[] iarray = null;
                char[] carray = null;
                bool[] barray = null;
                string[] sarray = null;
                MyClass[] marray = new MyClass[3];
                char c1;
                int i1;
                string s1;
                bool b1;

                true && false;
                true && true;
                false && false;
                false && true;
                b1 && true;
                true && b1;
                b1 && false;
                false && b1;
                b1 && b1;
                b1 && (1 < 3);
                (1 < 3) && b1;
                (i1 == i1) && ('c' <= 'c');

                i1 && b1;
                b1 && i1;
                c1 && b1;
                b1 && c1;
                i1 && c1;
                s1 && b1;
                b1 && s1;
            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 7)

    def test_plus_minus__not_Expression(self):
            data = """
            class MyClass {
                MyClass(){}
                public int iii;

                public bool boolMethod(int ii){
                    if (ii == 2) return true;
                }

                public MyClass returnMyClass(){
                    MyClass nnn = new MyClass();
                    return nnn;
                }
            }

            class OtherClass{
                OtherClass(MyClass mycl, int ii, bool[] b_array, string str, char cc, bool b){
                    if (b) true;
                }
                public void Voooid(){         
                    return;
                }
            }

            void kxi2023 main (){
                MyClass m = null;
                OtherClass oc;
                int[] iarray = null;
                char[] carray = null;
                bool[] barray = null;
                string[] sarray = null;
                MyClass[] marray = new MyClass[3];
                char c1;
                int i1;
                string s1;
                bool b1;

                +i1;
                -i1;
                !i1;
                +1;
                -1;
                !1; //2
                -m.returnMyClass().iii;
                +m.returnMyClass().iii;
                !m.returnMyClass().iii;     //3

                +iarray;
                -iarray;
                !iarray;        //6

                +true;
                -true;      //8
                !true;
                +false;
                -false;     //10
                !false;

                +b1;
                -b1;            //12
                !b1;

                +barray;
                -barray;
                !barray;

                +'c';
                -'c';
                !'c';
                +c1;
                -c1;
                !c1;
                
                +"string";
                -"string";
                !"string";
                +s1;
                -s1;
                !s1;

                +m;
                -m;
                !m;
            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 30)

    def test_new_expression(self):
            data = """
            class MyClass {
                MyClass(){}
                public int iii;

                public bool boolMethod(int ii){
                    if (ii == 2) return true;
                }

                public MyClass returnMyClass(){
                    MyClass nnn = new MyClass();
                    return nnn;
                }
            }

            class OtherClass{
                OtherClass(MyClass mycl, int ii, bool[] b_array, string str, char cc, bool b){
                    if (b) true;
                }
                public void Voooid(){         
                    return;
                }
            }

            void kxi2023 main (){
                MyClass m = null;
                OtherClass oc;
                int[] iarray = new int[1];
                char[] carray = new char[3];
                bool[] barray = new bool[3];
                string[] sarray = new string[2];
                MyClass[] marray = new MyClass[3];
                char c1;
                int i1;
                string s1;
                bool b1;

                new int[1];
                new char[1];
                new bool[1];
                new string[1];
                new OtherClass[1];
                new MyClass();

                OtherClass xxx = new OtherClass[4];
                MyClass mm = new MyClass();

                int i2 = new int[1];
                char c2 = new char[1];
                string s2 = new string[3];
                bool b2 = new bool[3];
                MyClass mmm = new OtherClass[3];
                OtherClass occc = new MyClass();


            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 7)

    def test_index(self):
            data = """
            class MyClass {
                MyClass(){}
                public int iii;

                public bool boolMethod(int ii){
                    if (ii == 2) return true;
                }

                public MyClass returnMyClass(){
                    MyClass nnn = new MyClass();
                    return nnn;
                }
            }

            class OtherClass{
                OtherClass(MyClass mycl, int ii, bool[] b_array, string str, char cc, bool b){
                    if (b) true;
                }
                public void Voooid(){         
                    return;
                }
            }

            void kxi2023 main (){
                MyClass m = null;
                OtherClass oc;
                int[] iarray = new int[1];
                char[] carray = new char[3];
                bool[] barray = new bool[3];
                string[] sarray = new string[2];
                MyClass[] marray = new MyClass[3];
                int i1;
                bool b1;
                int[] iarray1 = new int[1+2];
                char[] carray1 = new char[m.returnMyClass.iii];
                bool[] barray1 = new bool[i1];

                string[] sarray1 = new string['a'];
                MyClass[] marray1 = new MyClass[true];
                MyClass[] marray2 = new MyClass[b1];
                MyClass[] marray3 = new MyClass["string"];


            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 4)

    def test_GradeB(self):
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
                    return this.compute(1-x) + compute(x-2);
                }
            }

            class Test {
                Test() {}
                private bool[] asdfasdf;
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
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 0)

class Test_Assignments(unittest.TestCase):

    def test_basic(self):
            data = """
            void kxi2023 main() {
                int a;
                cout << a;
                a = 1;
                cout << a;
            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 0)
            assignmentCheck = AssignmentVisitor()
            assignmentCheck.paramList = symbolTable.paramList
            assignmentCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(assignmentCheck)
            self.assertEqual(len(assignmentCheck.errors), 1)

    def test_if(self):
            data = """
            void kxi2023 main() {
                bool b1;
                if (b1) cout << "done";
                if (true) cout << "done";
                if (false) cout << "done";
                b1 = true;
                if (b1) cout << "done";

                bool b2;
                if (b2) cout << "done"; else cout << "not done";
                if (true) cout << "done"; else cout << "not done";
                if (false) cout << "done"; else cout << "not done";
                b2 = false;
                if (b2) cout << "done"; else cout << "not done";
            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 0)
            assignmentCheck = AssignmentVisitor()
            assignmentCheck.paramList = symbolTable.paramList
            assignmentCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(assignmentCheck)
            self.assertEqual(len(assignmentCheck.errors), 2)

    def test_while(self):
            data = """
            void kxi2023 main() {
                bool b1;
                while (b1) cout << "test";
                while (true) cout << "test";
                while (false) cout << "test";
                b1 = true;
                while (b1) cout << "test";
            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 0)
            assignmentCheck = AssignmentVisitor()
            assignmentCheck.paramList = symbolTable.paramList
            assignmentCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(assignmentCheck)
            self.assertEqual(len(assignmentCheck.errors), 1)

    def test_return(self):
            data = """
            class MyClass{
                MyClass(){}
                public bool m (){
                    return true;
                    return false;
                    bool b1;
                    return b1;
                    b1 = true;
                    return b1;
                }
                public int i (){
                    return 1;
                    int i1;
                    return i1;
                    i1 = 3;
                    return i1;
                }
                public int[] iii (){
                    int[] iarray;
                    return iarray;
                    iarray = new int[3];
                    return iarray;
                }
                public bool[] bbb (){
                    bool[] barray;
                    return barray;
                    barray = new bool[3];
                    return barray;
                }
                public char[] ccc (){
                    char[] carray;
                    return carray;
                    carray = new char[3];
                    return carray;
                }
                public string[] sss (){
                    string[] sarray;
                    return sarray;
                    sarray = new string[3];
                    return sarray;
                }
                public OtherClass[] oc (){
                    OtherClass[] otherarray;
                    return otherarray;
                    otherarray = new OtherClass[3];
                    return otherarray;
                }
                public char cc (){
                    return 'a';
                    char c1;
                    return c1;
                    c1 = 'a';
                    return c1;
                }
                public string ss (){
                    return "string";
                    string s1;
                    return s1;
                    s1 = "test";
                    return s1;
                }

            }

            class OtherClass{
                OtherClass(){}
            }
            void kxi2023 main() {
            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 0)
            assignmentCheck = AssignmentVisitor()
            assignmentCheck.paramList = symbolTable.paramList
            assignmentCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(assignmentCheck)
            self.assertEqual(len(assignmentCheck.errors), 9)

    def test_cout(self):
            data = """
            class MyClass{
                MyClass(){}
                public int iii;
                public MyClass returnMyClass () {
                    MyClass mmm = new MyClass();
                    return mmm;
                }
                public bool m (){
                    bool b1;
                    b1 = true;
                    return b1;
                }
            }

            class OtherClass{
                OtherClass(){}
            }

            void kxi2023 main() {
                MyClass ass;
                cout << ass.iii;    //error
                ass = new MyClass();
                cout << ass.iii;
                string s1;
                string[] sarray;
                string[] sarray2 = new string[3];

                cout << s1;
                cout << sarray[1];  //error 3

                s1 = "test";
                sarray = sarray2;

                cout << s1;
                cout << sarray[2];
                cout << sarray2[4];
                cout << "Test";

                int i1;
                int i2;
                int[] iarray;
                int[] iarray2 = new int[3];

                cout << i1;
                cout << i2;
                cout << iarray[3];

                i1 = 123;
                i2 = i1;
                iarray = new int[3];

                cout << i1;
                cout << i2;
                cout << iarray[3];
                cout << 123;

                char c1;
                char c2;
                char[] carray;
                char[] carray2;

                cout << c1;
                cout << c2;
                cout << carray[3];

                c1 = 'a';
                c2 = '&';
                carray = new char[4];

                cout << c1;
                cout << c2;
                cout << carray[2];

                int[] testMe;
                cout << testMe[4];

                int[] testMe2 = new int[4];
                cout << testMe2[6];
            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 0)
            assignmentCheck = AssignmentVisitor()
            assignmentCheck.paramList = symbolTable.paramList
            assignmentCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(assignmentCheck)
            self.assertEqual(len(assignmentCheck.errors), 14)

    def test_cin(self):
            data = """
            class MyClass{
                MyClass(){}
                public int iii;
                public MyClass returnMyClass(){
                    MyClass mm = new MyClass();
                    return mm;
                }
                public bool m (){
                    bool b1;
                    b1 = true;
                    return b1;
                }
            }

            class OtherClass{
                OtherClass(){}
            }

            void kxi2023 main() {
                int i1;
                char c1;
                MyClass mc = new MyClass();
                MyClass notInit;

                cin >> notInit.iii; //1
                cout << notInit.iii;    //2
                cin >> mc.iii;
                cout << mc.iii;
                cin >> 1;   //3
                cout << i1;  //4
                cin >> i1;
                cout << i1;

                cin >> 'a';  //5
                cout << 'a';
                cout << c1; //6
                cin >> c1;
                cout << c1;

            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 0)
            assignmentCheck = AssignmentVisitor()
            assignmentCheck.paramList = symbolTable.paramList
            assignmentCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(assignmentCheck)
            self.assertEqual(len(assignmentCheck.errors), 6)

    def test_switch(self):
            data = """
            class MyClass {
                MyClass(){}
                public int iii;
                public bool boolMethod(int ii){
                    if (ii == 2) return true;
                }

                public MyClass returnMyClass(){
                    MyClass nnn = new MyClass();
                    return nnn;
                }
            }

            class OtherClass{
                OtherClass(MyClass mycl, int ii, bool[] b_array, string str, char cc, bool b){
                    if (b) true;
                }
                public void Voooid(){          
                    return;
                }
            }

            void kxi2023 main (){ 
                int a;
                switch (a) { // 1
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
                a = 3;
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

                int[] b;
                switch (b[1]) {        // 2 and 3
                    case 1:
                        cout << '-';
                        break;
                    case 'a':
                        cout << '.';
                    case 3:
                        cout << ',';
                        break;
                    default:
                        cout << '+';
                }
                b = new int[3];
                switch (b[1]) {        
                    case 1:
                        cout << '-';
                        break;
                    case 'a':
                        cout << '.';
                    case 3:
                        cout << ',';
                        break;
                    default:
                        cout << '+';
                }
                char c;
                switch (c) {        //4
                    case 1:
                        cout << '-';
                        break;
                    case 'a':
                        cout << '.';
                    case 3:
                        cout << ',';
                        break;
                    default:
                        cout << '+';
                }
                c = 'a';
                switch (c) {        
                    case 1:
                        cout << '-';
                        break;
                    case 'a':
                        cout << '.';
                    case 3:
                        cout << ',';
                        break;
                    default:
                        cout << '+';
                }
                char[] cc;
                switch (cc[1]) {        //5 and 6
                    case 1:
                        cout << '-';
                        break;
                    case 'a':
                        cout << '.';
                    case 3:
                        cout << ',';
                        break;
                    default:
                        cout << '+';
                }
                cc = new char[3];
                switch (cc[1]) {        
                    case 1:
                        cout << '-';
                        break;
                    case 'a':
                        cout << '.';
                    case 3:
                        cout << ',';
                        break;
                    default:
                        cout << '+';
                }
                switch ('a') {        
                    case 1:
                        cout << '-';
                        break;
                    case 'a':
                        cout << '.';
                    case 3:
                        cout << ',';
                        break;
                    default:
                        cout << '+';
                }
                switch (1) {        
                    case 1:
                        cout << '-';
                        break;
                    case 'a':
                        cout << '.';
                    case 3:
                        cout << ',';
                        break;
                    default:
                        cout << '+';
                }
                MyClass mm = new MyClass();
                switch (mm.iii) {        
                    case 1:
                        cout << '-';
                        break;
                    case 'a':
                        cout << '.';
                    case 3:
                        cout << ',';
                        break;
                    default:
                        cout << '+';
                }
                switch (mm.returnMyClass().iii) {        
                    case 1:
                        cout << '-';
                        break;
                    case 'a':
                        cout << '.';
                    case 3:
                        cout << ',';
                        break;
                    default:
                        cout << '+';
                }
            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 0)
            assignmentCheck = AssignmentVisitor()
            assignmentCheck.paramList = symbolTable.paramList
            assignmentCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(assignmentCheck)
            self.assertEqual(len(assignmentCheck.errors), 6)

    def test_ExEqualEx2(self):
            data = """
            class MyClass {
                MyClass(){}
                public int iii;

                public bool boolMethod(int ii){
                    if (ii == 2) return true;
                }

                public MyClass returnMyClass(){
                    MyClass nnn = new MyClass();
                    return nnn;
                }
            }

            class OtherClass{
                OtherClass(MyClass mycl, int ii, bool[] b_array, string str, char cc, bool b){
                    if (b) true;
                }
                public void Voooid(){         
                    return;
                }
            }

            void kxi2023 main (){
                MyClass m = null;
                int[] iarray = null;
                char[] carray = null;
                bool[] barray = null;
                string[] sarray = null;

                m.returnMyClass() = null;       //1 line 32

                1 = 3; //2
                int i1;
                int i2;
                i1 = 1;
                1 = i1; //3
                i1 = i2; //4 line 39

                iarray[2] = i2; //5 and 6
                iarray = new int[3];
                i2 = iarray[3];     
                iarray[3] = m.returnMyClass().iii; //7

                m = new MyClass();
                iarray[3] = m.returnMyClass().iii;

                bool boo;
                string str;     
                char cc;

                'a' = 'b'; //8 line 53
                cc = 'a';
                'a' = cc; //9
                cc = carray[1]; //10 and 11
                carray[2] = cc;  //12  line 57

                "string" = "string";    //13
                "string" = str; //14
                str = "string";
                sarray[1] = str;    //15 
                str = sarray[3];    //16 and 17 line 63
                boo = true;
                boo = false;

                barray[1] = boo;    //18
                boo = barray[1];    //19 and 20

                barray[1] = true;   //21
                barray[1] = false;  //22

                barray = new bool[3];

                barray[1] = boo;    
                boo = barray[1];    

                barray[1] = true;   
                barray[1] = false;  

                new MyClass() = m; //23 line 81

                m = m.returnMyClass(); //24
                i1 = m.returnMyClass().iii;
                boo = m.boolMethod(1); //25
            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 0)
            assignmentCheck = AssignmentVisitor()
            assignmentCheck.paramList = symbolTable.paramList
            assignmentCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(assignmentCheck)
            self.assertEqual(len(assignmentCheck.errors), 25)

    def test_ExPlusEqualEx2(self):
            data = """
            class MyClass {
                MyClass(){}
                public int iii;
                public char ccc;
                public int[] iarray;

                public MyClass returnMyClass(){
                    MyClass nnn = new MyClass();
                    return nnn;
                }
            }

            void kxi2023 main (){
                MyClass m = null;
                m = new MyClass();
                int i1;
                int[] iarray;


                i1 += 1;
                1 += i1; //1 line 25
                i1 += i1;
                i1 += m.returnMyClass().iii;
                i1 += m.iii;
                m.returnMyClass().iii += i1;
                m.iii += m.returnMyClass().iii;
                
                int i2;
                i2 += i2; //2
                i2 += 1;
                i2 += iarray[4]; //3 and 4
                iarray[3] += i2; //5

                iarray = new int[3];
                i2 += iarray[4]; 
                iarray[3] += i2;

            }
            """
          
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 0)
            assignmentCheck = AssignmentVisitor()
            assignmentCheck.paramList = symbolTable.paramList
            assignmentCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(assignmentCheck)
            self.assertEqual(len(assignmentCheck.errors), 5)

    def test_ExMinusEqualEx2(self):
            data = """
            class MyClass {
                MyClass(){}
                public int iii;
                public char ccc;
                public int[] iarray;

                public MyClass returnMyClass(){
                    MyClass nnn = new MyClass();
                    return nnn;
                }
            }

            void kxi2023 main (){
                MyClass m = null;
                m = new MyClass();
                int i1;
                int[] iarray;


                i1 -= 1;
                1 -= i1; //1 line 25
                i1 -= i1;
                i1 -= m.returnMyClass().iii;
                i1 -= m.iii;
                m.returnMyClass().iii -= i1;
                m.iii -= m.returnMyClass().iii;
                
                int i2;
                i2 -= i2; //2
                i2 -= 1;
                i2 -= iarray[4]; //3 and 4
                iarray[3] -= i2; //5

                iarray = new int[3];
                i2 -= iarray[4]; 
                iarray[3] -= i2;

            }
            """
          
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 0)
            assignmentCheck = AssignmentVisitor()
            assignmentCheck.paramList = symbolTable.paramList
            assignmentCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(assignmentCheck)
            self.assertEqual(len(assignmentCheck.errors), 5)

    def test_ExTimesEqualEx2(self):
            data = """
            class MyClass {
                MyClass(){}
                public int iii;
                public char ccc;
                public int[] iarray;

                public MyClass returnMyClass(){
                    MyClass nnn = new MyClass();
                    return nnn;
                }
            }

            void kxi2023 main (){
                MyClass m = null;
                m = new MyClass();
                int i1;
                int[] iarray;


                i1 *= 1;
                1 *= i1; //1 line 25
                i1 *= i1;
                i1 *= m.returnMyClass().iii;
                i1 *= m.iii;
                m.returnMyClass().iii *= i1;
                m.iii *= m.returnMyClass().iii;
                
                int i2;
                i2 *= i2; //2
                i2 *= 1;
                i2 *= iarray[4]; //3 and 4
                iarray[3] *= i2; //5

                iarray = new int[3];
                i2 *= iarray[4]; 
                iarray[3] *= i2;

            }
            """
          
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 0)
            assignmentCheck = AssignmentVisitor()
            assignmentCheck.paramList = symbolTable.paramList
            assignmentCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(assignmentCheck)
            self.assertEqual(len(assignmentCheck.errors), 5)

    def test_ExDivideEqualEx2(self):
            data = """
            class MyClass {
                MyClass(){}
                public int iii;
                public char ccc;
                public int[] iarray;

                public MyClass returnMyClass(){
                    MyClass nnn = new MyClass();
                    return nnn;
                }
            }

            void kxi2023 main (){
                MyClass m = null;
                m = new MyClass();
                int i1;
                int[] iarray;


                i1 /= 1;
                1 /= i1; //1 line 25
                i1 /= i1;
                i1 /= m.returnMyClass().iii;
                i1 /= m.iii;
                m.returnMyClass().iii /= i1;
                m.iii /= m.returnMyClass().iii;
                
                int i2;
                i2 /= i2; //2
                i2 /= 1;
                i2 /= iarray[4]; //3 and 4
                iarray[3] /= i2; //5

                iarray = new int[3];
                i2 /= iarray[4]; 
                iarray[3] /= i2;

            }
            """
          
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 0)
            assignmentCheck = AssignmentVisitor()
            assignmentCheck.paramList = symbolTable.paramList
            assignmentCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(assignmentCheck)
            self.assertEqual(len(assignmentCheck.errors), 5)

    def test_ExPlusEx2(self):
            data = """
            class MyClass {
                MyClass(){}
                public int iii;
                public char ccc;
                public int[] iarray;

                public MyClass returnMyClass(){
                    MyClass nnn = new MyClass();
                    return nnn;
                }
            }

            void kxi2023 main (){
                MyClass m = null;
                m = new MyClass();
                int i1;
                int[] iarray;
                char c1;
                bool b1;
                string s1;
                bool[] barray;

                i1 + 1; //1
                1 + i1; //2
                i1 + i1; //3
                i1 + m.returnMyClass().iii; //4
                i1 + m.iii; //5
                m.returnMyClass().iii + i1; //6
                m.iii + m.returnMyClass().iii;

                i1 = 3;
                i1 + 1; 
                1 + i1; 
                i1 + i1; 
                i1 + m.returnMyClass().iii; 
                i1 + m.iii; 
                m.returnMyClass().iii + i1; 
                m.iii + m.returnMyClass().iii;

            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 0)
            assignmentCheck = AssignmentVisitor()
            assignmentCheck.paramList = symbolTable.paramList
            assignmentCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(assignmentCheck)
            self.assertEqual(len(assignmentCheck.errors), 6)

    def test_ExMinusEx2(self):
            data = """
            class MyClass {
                MyClass(){}
                public int iii;
                public char ccc;
                public int[] iarray;

                public MyClass returnMyClass(){
                    MyClass nnn = new MyClass();
                    return nnn;
                }
            }

            void kxi2023 main (){
                MyClass m = null;
                m = new MyClass();
                int i1;
                int[] iarray;
                char c1;
                bool b1;
                string s1;
                bool[] barray;

                i1 - 1; //1
                1 - i1; //2
                i1 - i1; //3
                i1 - m.returnMyClass().iii; //4
                i1 - m.iii; //5
                m.returnMyClass().iii - i1; //6
                m.iii - m.returnMyClass().iii;

                i1 = 3;
                i1 - 1; 
                1 - i1; 
                i1 - i1; 
                i1 - m.returnMyClass().iii; 
                i1 - m.iii; 
                m.returnMyClass().iii - i1; 
                m.iii - m.returnMyClass().iii;
            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 0)
            assignmentCheck = AssignmentVisitor()
            assignmentCheck.paramList = symbolTable.paramList
            assignmentCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(assignmentCheck)
            self.assertEqual(len(assignmentCheck.errors), 6)

    def test_ExTimesEx2(self):
            data = """
            class MyClass {
                MyClass(){}
                public int iii;
                public char ccc;
                public int[] iarray;

                public MyClass returnMyClass(){
                    MyClass nnn = new MyClass();
                    return nnn;
                }
            }

            void kxi2023 main (){
                MyClass m = null;
                m = new MyClass();
                int i1;
                int[] iarray;
                char c1;
                bool b1;
                string s1;
                bool[] barray;

                i1 * 1; //1
                1 * i1; //2
                i1 * i1; //3
                i1 * m.returnMyClass().iii; //4
                i1 * m.iii; //5
                m.returnMyClass().iii* i1; //6
                m.iii * m.returnMyClass().iii;

                i1 = 3;
                i1 * 1; 
                1 *i1; 
                i1 * i1; 
                i1 * m.returnMyClass().iii; 
                i1 * m.iii; 
                m.returnMyClass().iii * i1; 
                m.iii * m.returnMyClass().iii;

            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 0)
            assignmentCheck = AssignmentVisitor()
            assignmentCheck.paramList = symbolTable.paramList
            assignmentCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(assignmentCheck)
            self.assertEqual(len(assignmentCheck.errors), 6)

    def test_ExDivideEx2(self):
            data = """
            class MyClass {
                MyClass(){}
                public int iii;
                public char ccc;
                public int[] iarray;

                public MyClass returnMyClass(){
                    MyClass nnn = new MyClass();
                    return nnn;
                }
            }

            void kxi2023 main (){
                MyClass m = null;
                m = new MyClass();
                int i1;
                int[] iarray;
                char c1;
                bool b1;
                string s1;
                bool[] barray;

                i1 / 1; //1
                1 / i1; //2
                i1 / i1; //3
                i1 / m.returnMyClass().iii; //4
                i1 / m.iii; //5
                m.returnMyClass().iii / i1; //6
                m.iii / m.returnMyClass().iii;

                i1 = 3;
                i1 / 1; 
                1 / i1; 
                i1 / i1; 
                i1 / m.returnMyClass().iii; 
                i1 / m.iii; 
                m.returnMyClass().iii / i1; 
                m.iii / m.returnMyClass().iii;

            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 0)
            assignmentCheck = AssignmentVisitor()
            assignmentCheck.paramList = symbolTable.paramList
            assignmentCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(assignmentCheck)
            self.assertEqual(len(assignmentCheck.errors), 6)

    def test_ExCEqualEx2(self):
            data = """
            class MyClass {
                MyClass(){}
                public int iii;

                public bool boolMethod(int ii){
                    if (ii == 2) return true;
                }

                public MyClass returnMyClass(){
                    MyClass nnn = new MyClass();
                    return nnn;
                }
            }

            class OtherClass{
                OtherClass(MyClass mycl, int ii, bool[] b_array, string str, char cc, bool b){
                    if (b) true;
                }
                public void Voooid(){         
                    return;
                }
            }

            void kxi2023 main (){
                MyClass m = null;
                OtherClass oc;
                int[] iarray = null;
                char[] carray = null;
                bool[] barray = null;
                string[] sarray = null;
                char c1;
                string s1;
                bool b1;

                null == m;
                m = new MyClass();
                m.returnMyClass() == null;
                1 == 3;
                int i1;
                int i2;
                i1 == 1; //1 line 42
                1 == i1; //2
                i1 == i2; //3
                m.returnMyClass().iii == i1; //4
                m.returnMyClass().iii == 1;
                1 == m.returnMyClass().iii;
                iarray[1] == 1; //5 6 line 48
                1 == iarray[3]; //7 8
                i1 == iarray[2]; //9 10
                iarray[2] == i1; // 11 12
                null == m;  //line 52

                i1 = 1;
                i2 = 4;
                iarray = new int[4];
                i1 == 1; 
                1 == i1; 
                i1 == i2; 
                m.returnMyClass().iii == i1; 
                m.returnMyClass().iii == 1;
                1 == m.returnMyClass().iii;
                iarray[1] == 1; 
                1 == iarray[3]; 
                i1 == iarray[2]; 
                iarray[2] == i1; 
                null == m;  

                c1 == c1; //line 69 13
                c1 == 'a';//14
                'a' == c1;  //15
                carray[1] == c1; //16 17
                carray[1] == 'a'; //18 19

                carray = new char[4];
                c1 = 'f';
                c1 == c1; 
                c1 == 'a';
                'a' == c1;  
                carray[1] == c1; 
                carray[1] == 'a'; 

                b1 == b1; // line 83 20
                b1 == true; //21
                b1 == false; //22
                true == true; 
                false == false;
                false == b1; //23
                true == b1; //24
                barray[1] == true; //25 26
                b1 == barray[2]; //27 28 line 91

                b1 = true;
                barray = new bool[3];
                b1 == b1; 
                b1 == true; 
                b1 == false; 
                true == true; 
                false == false;
                false == b1; 
                true == b1; 
                barray[1] == true; 
                b1 == barray[2]; 

                s1 == s1; // 29 line 105
                "string" == "string";
                s1 == "string";  // 30
                "string" == s1;  //31
                s1 == sarray[1];  //32 33
                sarray[1] == "a";  //34 35

                s1 = ";";
                sarray = new string[3];
                s1 == s1; 
                "string" == "string";
                s1 == "string";  
                "string" == s1;  
                s1 == sarray[1];  
                sarray[1] == "a"; 

                m == null;
                iarray == null;
                barray == null;
                sarray == null;
                carray == null;

                null == m;
                null == iarray;
                null == barray;
                null == sarray;
                null == carray;
            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 0)
            assignmentCheck = AssignmentVisitor()
            assignmentCheck.paramList = symbolTable.paramList
            assignmentCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(assignmentCheck)
            self.assertEqual(len(assignmentCheck.errors), 35)

    def test_ExNotEqualEx2(self):
            data = """
            class MyClass {
                MyClass(){}
                public int iii;

                public bool boolMethod(int ii){
                    if (ii == 2) return true;
                }

                public MyClass returnMyClass(){
                    MyClass nnn = new MyClass();
                    return nnn;
                }
            }

            class OtherClass{
                OtherClass(MyClass mycl, int ii, bool[] b_array, string str, char cc, bool b){
                    if (b) true;
                }
                public void Voooid(){         
                    return;
                }
            }

            void kxi2023 main (){
                MyClass m = null;
                OtherClass oc;
                int[] iarray = null;
                char[] carray = null;
                bool[] barray = null;
                string[] sarray = null;
                char c1;
                string s1;
                bool b1;

                null != m;
                m = new MyClass();
                m.returnMyClass() != null;
                1 != 3;
                int i1;
                int i2;
                i1 != 1; //1 line 42
                1 != i1; //2
                i1 != i2; //3
                m.returnMyClass().iii != i1; //4
                m.returnMyClass().iii != 1;
                1 != m.returnMyClass().iii;
                iarray[1] != 1; //5 6 line 48
                1 != iarray[3]; //7 8
                i1 != iarray[2]; //9 10
                iarray[2] != i1; // 11 12
                null != m;  //line 52

                i1 = 1;
                i2 = 4;
                iarray = new int[4];
                i1 != 1; 
                1 != i1; 
                i1 != i2; 
                m.returnMyClass().iii != i1; 
                m.returnMyClass().iii != 1;
                1 != m.returnMyClass().iii;
                iarray[1] != 1; 
                1 != iarray[3]; 
                i1 != iarray[2]; 
                iarray[2] != i1; 
                null != m;  

                c1 != c1; //line 69 13
                c1 != 'a';//14
                'a' != c1;  //15
                carray[1] != c1; //16 17
                carray[1] != 'a'; //18 19

                carray = new char[4];
                c1 = 'f';
                c1 != c1; 
                c1 != 'a';
                'a' != c1;  
                carray[1] != c1; 
                carray[1] != 'a'; 

                b1 != b1; // line 83 20
                b1 != true; //21
                b1 != false; //22
                true != true; 
                false != false;
                false != b1; //23
                true != b1; //24
                barray[1] != true; //25 26
                b1 != barray[2]; //27 28 line 91

                b1 = true;
                barray = new bool[3];
                b1!= b1; 
                b1 != true; 
                b1 != false; 
                true != true; 
                false != false;
                false != b1; 
                true != b1; 
                barray[1] != true; 
                b1 != barray[2]; 

                s1 != s1; // 29 line 105
                "string" != "string";
                s1 != "string";  // 30
                "string" != s1;  //31
                s1 != sarray[1];  //32 33
                sarray[1] != "a";  //34 35

                s1 = ";";
                sarray = new string[3];
                s1 != s1; 
                "string" != "string";
                s1 != "string";  
                "string" != s1;  
                s1 != sarray[1];  
                sarray[1] != "a"; 

                m != null;
                iarray != null;
                barray != null;
                sarray != null;
                carray != null;

                null != m;
                null != iarray;
                null != barray;
                null != sarray;
                null != carray;
            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 0)
            assignmentCheck = AssignmentVisitor()
            assignmentCheck.paramList = symbolTable.paramList
            assignmentCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(assignmentCheck)
            self.assertEqual(len(assignmentCheck.errors), 35)

    def test_ExGreaterEx2(self):
            data = """
            class MyClass {
                MyClass(){}
                public int iii;

                public bool boolMethod(int ii){
                    if (ii == 2) return true;
                }

                public MyClass returnMyClass(){
                    MyClass nnn = new MyClass();
                    return nnn;
                }
            }

            class OtherClass{
                OtherClass(MyClass mycl, int ii, bool[] b_array, string str, char cc, bool b){
                    if (b) true;
                }
                public void Voooid(){         
                    return;
                }
            }

            void kxi2023 main (){
                MyClass m = new MyClass();
                
                OtherClass oc;
                int[] iarray = null;
                char[] carray = null;
                bool[] barray = null;
                string[] sarray = null;
                MyClass[] marray = new MyClass[3];
                char c1;
                int i1;

                i1 > 1; // error 1 
                1 > i1; //2
                i1 > i1;    //3
                1 > 2;
                i1 > iarray[1]; //4 5
                iarray[1] > i1; //6 7
                i1 > m.iii; //8
                m.iii > i1; //9
                
                i1 = 3;
                iarray = new int[3];
                i1 > 1; 
                1 > i1;
                i1 > i1;    
                1 > 2;
                i1 > iarray[1]; 
                iarray[1] > i1; 
                i1 > m.iii; 
                m.iii > i1; 

                'c' > 'c';
                c1 > 'c';   //10
                'c' > c1;   //11
                carray[1] > c1;     //12 13
                c1 > carray[1]; //14 15
                carray[1] > 'b';    //16 17
                'b' > carray[1];    //18 19

                c1 = 'l';
                carray = new char[4];
                'c' > 'c';
                c1 > 'c';
                'c' > c1;
                carray[1] > c1;
                c1 > carray[1];
                carray[1] > 'b';
                'b' > carray[1];
            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 0)
            assignmentCheck = AssignmentVisitor()
            assignmentCheck.paramList = symbolTable.paramList
            assignmentCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(assignmentCheck)
            self.assertEqual(len(assignmentCheck.errors), 19)

    def test_ExGreaterEqualEx2(self):
            data = """
            class MyClass {
                MyClass(){}
                public int iii;

                public bool boolMethod(int ii){
                    if (ii == 2) return true;
                }

                public MyClass returnMyClass(){
                    MyClass nnn = new MyClass();
                    return nnn;
                }
            }

            class OtherClass{
                OtherClass(MyClass mycl, int ii, bool[] b_array, string str, char cc, bool b){
                    if (b) true;
                }
                public void Voooid(){         
                    return;
                }
            }

            void kxi2023 main (){
                MyClass m = new MyClass();
                
                OtherClass oc;
                int[] iarray = null;
                char[] carray = null;
                bool[] barray = null;
                string[] sarray = null;
                MyClass[] marray = new MyClass[3];
                char c1;
                int i1;

                i1 >= 1; // error 1 
                1 >= i1; //2
                i1 >= i1;    //3
                1 >= 2;
                i1 >= iarray[1]; //4 5
                iarray[1] >= i1; //6 7
                i1 >= m.iii; //8
                m.iii >= i1; //9
                
                i1 = 3;
                iarray = new int[3];
                i1 >= 1; 
                1 >= i1;
                i1 >= i1;    
                1 >= 2;
                i1 >= iarray[1]; 
                iarray[1] >= i1; 
                i1 >= m.iii; 
                m.iii >= i1; 

                'c' >= 'c';
                c1 >= 'c';   //10
                'c' >= c1;   //11
                carray[1] >= c1;     //12 13
                c1 >= carray[1]; //14 15
                carray[1] >= 'b';    //16 17
                'b' >= carray[1];    //18 19

                c1 = 'l';
                carray = new char[4];
                'c' >= 'c';
                c1 >= 'c';
                'c' >= c1;
                carray[1] >= c1;
                c1 >= carray[1];
                carray[1] >= 'b';
                'b' >= carray[1];
            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 0)
            assignmentCheck = AssignmentVisitor()
            assignmentCheck.paramList = symbolTable.paramList
            assignmentCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(assignmentCheck)
            self.assertEqual(len(assignmentCheck.errors), 19)

    def test_ExLessEx2(self):
            data = """
            class MyClass {
                MyClass(){}
                public int iii;

                public bool boolMethod(int ii){
                    if (ii == 2) return true;
                }

                public MyClass returnMyClass(){
                    MyClass nnn = new MyClass();
                    return nnn;
                }
            }

            class OtherClass{
                OtherClass(MyClass mycl, int ii, bool[] b_array, string str, char cc, bool b){
                    if (b) true;
                }
                public void Voooid(){         
                    return;
                }
            }

            void kxi2023 main (){
                MyClass m = new MyClass();
                
                OtherClass oc;
                int[] iarray = null;
                char[] carray = null;
                bool[] barray = null;
                string[] sarray = null;
                MyClass[] marray = new MyClass[3];
                char c1;
                int i1;

                i1 < 1; // error 1 
                1 < i1; //2
                i1 < i1;    //3
                1 < 2;
                i1 < iarray[1]; //4 5
                iarray[1] < i1; //6 7
                i1 < m.iii; //8
                m.iii < i1; //9
                
                i1 = 3;
                iarray = new int[3];
                i1 < 1; 
                1 < i1;
                i1 < i1;    
                1 < 2;
                i1 < iarray[1]; 
                iarray[1] < i1; 
                i1 < m.iii; 
                m.iii < i1; 

                'c' < 'c';
                c1 < 'c';   //10
                'c' < c1;   //11
                carray[1] < c1;     //12 13
                c1 < carray[1]; //14 15
                carray[1] < 'b';    //16 17
                'b' < carray[1];    //18 19

                c1 = 'l';
                carray = new char[4];
                'c' < 'c';
                c1 < 'c';
                'c' < c1;
                carray[1] < c1;
                c1 < carray[1];
                carray[1] < 'b';
                'b' < carray[1];
            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 0)
            assignmentCheck = AssignmentVisitor()
            assignmentCheck.paramList = symbolTable.paramList
            assignmentCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(assignmentCheck)
            self.assertEqual(len(assignmentCheck.errors), 19)

    def test_ExLessEqualEx2(self):
            data = """
            class MyClass {
                MyClass(){}
                public int iii;

                public bool boolMethod(int ii){
                    if (ii == 2) return true;
                }

                public MyClass returnMyClass(){
                    MyClass nnn = new MyClass();
                    return nnn;
                }
            }

            class OtherClass{
                OtherClass(MyClass mycl, int ii, bool[] b_array, string str, char cc, bool b){
                    if (b) true;
                }
                public void Voooid(){         
                    return;
                }
            }

            void kxi2023 main (){
                MyClass m = new MyClass();
                
                OtherClass oc;
                int[] iarray = null;
                char[] carray = null;
                bool[] barray = null;
                string[] sarray = null;
                MyClass[] marray = new MyClass[3];
                char c1;
                int i1;

                i1 <= 1; // error 1 
                1 <= i1; //2
                i1 <= i1;    //3
                1 <= 2;
                i1 <= iarray[1]; //4 5
                iarray[1] <= i1; //6 7
                i1 <= m.iii; //8
                m.iii <= i1; //9
                
                i1 = 3;
                iarray = new int[3];
                i1 <= 1; 
                1 <= i1;
                i1 <= i1;    
                1 <= 2;
                i1 <= iarray[1]; 
                iarray[1] <= i1; 
                i1 <= m.iii; 
                m.iii <= i1; 

                'c' <= 'c';
                c1 <= 'c';   //10
                'c' <= c1;   //11
                carray[1] <= c1;     //12 13
                c1 <= carray[1]; //14 15
                carray[1] <= 'b';    //16 17
                'b' <= carray[1];    //18 19

                c1 = 'l';
                carray = new char[4];
                'c' <= 'c';
                c1 <= 'c';
                'c' <= c1;
                carray[1] <= c1;
                c1 <= carray[1];
                carray[1] <= 'b';
                'b' <= carray[1];
            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 0)
            assignmentCheck = AssignmentVisitor()
            assignmentCheck.paramList = symbolTable.paramList
            assignmentCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(assignmentCheck)
            self.assertEqual(len(assignmentCheck.errors), 19)

    def test_ExOOREx2(self):
            data = """
            class MyClass {
                MyClass(){}
                public int iii;

                public bool boolMethod(int ii){
                    if (ii == 2) return true;
                }

                public MyClass returnMyClass(){
                    MyClass nnn = new MyClass();
                    return nnn;
                }
            }

            class OtherClass{
                OtherClass(MyClass mycl, int ii, bool[] b_array, string str, char cc, bool b){
                    if (b) true;
                }
                public void Voooid(){         
                    return;
                }
            }

            void kxi2023 main (){
                MyClass m = null;
                OtherClass oc;
                int[] iarray = null;
                char[] carray = null;
                bool[] barray = null;
                string[] sarray = null;
                MyClass[] marray = new MyClass[3];
                char c1;
                int i1;
                string s1;
                bool b1;

                true || false;
                true || true;
                false || false;
                false || true;
                b1 || true; //1 line 42
                true || b1; //2
                b1 || false; //3
                false || b1; //4
                b1 || b1; //5
                b1 || (1 < 3); //6
                (1 < 3) || b1; //7
                (i1 == i1) || ('c' <= 'c'); //8 13
                barray[3] || b1; //9 10
                b1 || barray[3]; // 11 12

                true || false;
                true || true;
                false || false;
                false || true;
                b1 = true;
                b1 || true;
                i1 = 2;
                true || b1;
                b1 || false;
                false || b1;
                b1 || b1;
                b1 || (1 < 3);
                (1 < 3) || b1;
                (i1 == i1) || ('c' <= 'c');

            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 0)
            assignmentCheck = AssignmentVisitor()
            assignmentCheck.paramList = symbolTable.paramList
            assignmentCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(assignmentCheck)
            self.assertEqual(len(assignmentCheck.errors), 13)

    def test_ExAANDEx2(self):
            data = """
            class MyClass {
                MyClass(){}
                public int iii;

                public bool boolMethod(int ii){
                    if (ii == 2) return true;
                }

                public MyClass returnMyClass(){
                    MyClass nnn = new MyClass();
                    return nnn;
                }
            }

            class OtherClass{
                OtherClass(MyClass mycl, int ii, bool[] b_array, string str, char cc, bool b){
                    if (b) true;
                }
                public void Voooid(){         
                    return;
                }
            }

            void kxi2023 main (){
                MyClass m = null;
                OtherClass oc;
                int[] iarray = null;
                char[] carray = null;
                bool[] barray = null;
                string[] sarray = null;
                MyClass[] marray = new MyClass[3];
                char c1;
                int i1;
                string s1;
                bool b1;

                true && false;
                true && true;
                false && false;
                false && true;
                b1 && true; //1 line 42
                true && b1; //2
                b1 && false; //3
                false && b1; //4
                b1 && b1; //5
                b1 && (1 < 3); //6
                (1 < 3) && b1; //7
                (i1 == i1) && ('c' <= 'c'); //8 13
                barray[3] && b1; //9 10
                b1 && barray[3]; // 11 12

                true && false;
                true && true;
                false && false;
                false && true;
                b1 = true;
                b1 && true;
                i1 = 2;
                true && b1;
                b1 && false;
                false && b1;
                b1 && b1;
                b1 && (1 < 3);
                (1 < 3) && b1;
                (i1 == i1) && ('c' <= 'c');

            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 0)
            assignmentCheck = AssignmentVisitor()
            assignmentCheck.paramList = symbolTable.paramList
            assignmentCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(assignmentCheck)
            self.assertEqual(len(assignmentCheck.errors), 13)
            
    def test_plus_minus__not_Expression(self):
            data = """
            class MyClass {
                MyClass(){}
                public int iii;

                public bool boolMethod(int ii){
                    if (ii == 2) return true;
                }

                public MyClass returnMyClass(){
                    MyClass nnn = new MyClass();
                    return nnn;
                }
            }

            class OtherClass{
                OtherClass(MyClass mycl, int ii, bool[] b_array, string str, char cc, bool b){
                    if (b) true;
                }
                public void Voooid(){         
                    return;
                }
            }

            void kxi2023 main (){
                MyClass m = new MyClass();
                OtherClass oc;
                int[] iarray = null;
                char[] carray = null;
                bool[] barray = null;
                string[] sarray = null;
                MyClass[] marray = new MyClass[3];
                char c1;
                int i1;
                string s1;
                bool b1;

                +i1; //1 line 38
                -i1;
                +1;
                -1;
                -m.returnMyClass().iii;
                +m.returnMyClass().iii;


                !true;
                !false;

                !b1;

                i1 = 3;
                b1 = false;
                +i1;
                -i1;
                +1;
                -1;
                -m.returnMyClass().iii;
                +m.returnMyClass().iii;


                !true;
                !false;

                !b1;
            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 0)
            assignmentCheck = AssignmentVisitor()
            assignmentCheck.paramList = symbolTable.paramList
            assignmentCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(assignmentCheck)
            self.assertEqual(len(assignmentCheck.errors), 3)

    def test_GradeB(self):
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
                    return this.compute(1-x) + compute(x-2);
                }
            }

            class Test {
                Test() {}
                private bool[] asdfasdf;
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
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 0)
            assignmentCheck = AssignmentVisitor()
            assignmentCheck.paramList = symbolTable.paramList
            assignmentCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(assignmentCheck)
            self.assertEqual(len(assignmentCheck.errors), 0)
            
class Test_Break(unittest.TestCase):

    def test_basic(self):
            data = """
            void kxi2023 main() {
            while (1 >2)
                break;
            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 0)
            assignmentCheck = AssignmentVisitor()
            assignmentCheck.paramList = symbolTable.paramList
            assignmentCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(assignmentCheck)
            self.assertEqual(len(assignmentCheck.errors), 0)    
            breakReturn = BreakVisitor()
            myAST.accept(breakReturn)
            self.assertEqual(len(breakReturn.errors), 0)    

    def test_break(self):
            data = """
            void kxi2023 main() {
                break;
            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 0)
            assignmentCheck = AssignmentVisitor()
            assignmentCheck.paramList = symbolTable.paramList
            assignmentCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(assignmentCheck)
            self.assertEqual(len(assignmentCheck.errors), 0)    
            breakReturn = BreakVisitor()
            myAST.accept(breakReturn)
            self.assertEqual(len(breakReturn.errors), 1)    

    def test_if_else(self):
            data = """
            void kxi2023 main() {
                if (true) break; else break;
                if (true) break;
            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 0)
            assignmentCheck = AssignmentVisitor()
            assignmentCheck.paramList = symbolTable.paramList
            assignmentCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(assignmentCheck)
            self.assertEqual(len(assignmentCheck.errors), 0)    
            breakReturn = BreakVisitor()
            myAST.accept(breakReturn)
            self.assertEqual(len(breakReturn.errors), 3)    

    def test_while(self):
            data = """
            void kxi2023 main() {
                while (true){
                    break;
                }
            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 0)
            assignmentCheck = AssignmentVisitor()
            assignmentCheck.paramList = symbolTable.paramList
            assignmentCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(assignmentCheck)
            self.assertEqual(len(assignmentCheck.errors), 0)    
            breakReturn = BreakVisitor()
            myAST.accept(breakReturn)
            self.assertEqual(len(breakReturn.errors), 0)    

    def test_if_else_nested(self):
            data = """
            void kxi2023 main() {
                if (true) {
                    if(false) break;    //1
                    while (true){
                        int i1 = 3;
                        cout << i1;
                        break;
                    }
                }
                else{
                    cin >> i1;
                    break;      //2
                }
                if (true) {
                    cout << 1;
                }
            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 0)
            assignmentCheck = AssignmentVisitor()
            assignmentCheck.paramList = symbolTable.paramList
            assignmentCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(assignmentCheck)
            self.assertEqual(len(assignmentCheck.errors), 0)    
            breakReturn = BreakVisitor()
            myAST.accept(breakReturn)
            self.assertEqual(len(breakReturn.errors), 2)    

    def test_switch(self):
            data = """
            void kxi2023 main() {
                int a = 1;
                switch (a) { // 1
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
                a = 3;
            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 0)
            assignmentCheck = AssignmentVisitor()
            assignmentCheck.paramList = symbolTable.paramList
            assignmentCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(assignmentCheck)
            self.assertEqual(len(assignmentCheck.errors), 0)    
            breakReturn = BreakVisitor()
            myAST.accept(breakReturn)
            self.assertEqual(len(breakReturn.errors), 0)    

    def test_switch_if(self):
            data = """
            void kxi2023 main() {
                int a = 1;
                switch (a) { // 1
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
                        if (false) break;
                }
                a = 3;
            }
            """
            theLexer.theLexerReturnFucntion(data)
            myAST = theParser.Parse(data)
            symbolTable = SymbolTableVisitor()
            myAST.accept(symbolTable)
            self.assertEqual(len(symbolTable.errors), 0)
            undeclaredVariableVistior = UndeclaredVisitor()
            undeclaredVariableVistior.oldSymbols = symbolTable.symbol_tables
            myAST.accept(undeclaredVariableVistior)
            self.assertEqual(len(undeclaredVariableVistior.errors), 0)
            typeCheck = TypeChecking()
            typeCheck.paramList = symbolTable.paramList
            typeCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(typeCheck)
            self.assertEqual(len(typeCheck.errors), 0)
            assignmentCheck = AssignmentVisitor()
            assignmentCheck.paramList = symbolTable.paramList
            assignmentCheck.symbol_tables = symbolTable.symbol_tables
            myAST.accept(assignmentCheck)
            self.assertEqual(len(assignmentCheck.errors), 0)    
            breakReturn = BreakVisitor()
            myAST.accept(breakReturn)
            self.assertEqual(len(breakReturn.errors), 1)    



# class Test_Z_All_Semantics(unittest.TestCase):

#     def test_Test1(self):
#         pass
    
