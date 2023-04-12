from AbstractVisitor import ASTVisitor
from AST import *
import pydot

#singleton Class of Unique so that terminals don't have same name
class Unique:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.id = 0
        return cls._instance

    def getID(self):
        self.id += 1
        return self.id

class PrintDotVisitor(ASTVisitor):
    def __init__(self):
        self.UID = Unique()
        self.graph = pydot.Graph() 
        self.graph = pydot.Dot('my_graph', graph_type='graph')
        start = pydot.Node('Start', shape='diamond', style='filled', fillcolor='cyan')

        self.graph.add_node(start)

    def pre_visit_Argument(self, node: ASTArgument):
        pass

    def post_visit_Argument(self, node: ASTArgument):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))
        
        LPARENNodeName = str(node.LPAREN) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(LPARENNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), LPARENNodeName))
        
        if (node.MaybeArgumentList.ArgumentList!= None):
            self.graph.add_edge(pydot.Edge(str(node), str(node.MaybeArgumentList)))

        RPARENNodeName = str(node.RPAREN) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(RPARENNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), RPARENNodeName))

    def pre_visit_ArgumentList(self, node: ASTArgumentList):
        pass

    def post_visit_ArgumentList(self, node: ASTArgumentList):

        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        self.graph.add_edge(pydot.Edge(str(node), str(node.MultipleCommaExpression)))
    
    def pre_visit_ArgOrIdx(self, node: ASTArgOrIdx):
        pass
    
    def post_visit_ArgOrIdx(self, node: ASTArgOrIdx):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        self.graph.add_edge(pydot.Edge(str(node), str(node.Arg_Idx)))

    def pre_visit_Case(self, node: ASTCase):
        pass

    def post_visit_Case(self, node: ASTCase):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        CaseNodeName = str(node.CASE) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(CaseNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), CaseNodeName))

        NumOrCharNodeName = str(node.NumOrChar) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(NumOrCharNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), NumOrCharNodeName))

        ColonNodeName = str(node.COLON) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(ColonNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), ColonNodeName))

        self.graph.add_edge(pydot.Edge(str(node), str(node.MultipleStatement)))

    def pre_visit_CaseBlock(self, node: ASTCaseBlock):
        pass

    def post_visit_CaseBlock(self, node: ASTCaseBlock):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        LCURLYNodeName = str(node.LCURLY) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(LCURLYNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), LCURLYNodeName))

        self.graph.add_edge(pydot.Edge(str(node), str(node.MultipleCase)))

        DefaultNodeName = str(node.DEFAULT) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(DefaultNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), DefaultNodeName))

        ColonNodeName = str(node.COLON) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(ColonNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), ColonNodeName))

        self.graph.add_edge(pydot.Edge(str(node), str(node.MultipleStatement)))
        
        RCURLYNodeName = str(node.RCURLY) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(RCURLYNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), RCURLYNodeName))

    def pre_visit_ClassDefinition(self, node: ASTClassDefinition):
        pass
    
    def post_visit_ClassDefinition(self, node: ASTClassDefinition):
        #add node for Class Definition
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        #add terminal node for 'Class Node'
        classNodeName = str(node.Class) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(classNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), classNodeName))

        #add terminal node for 'ID Node'
        IDNodeName = str(node.ID) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(IDNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), IDNodeName))

        #add terminal node for '{ Node'
        LCURLYNodeName = str(node.LCURLY) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(LCURLYNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), LCURLYNodeName))

        #check to see if it will be visited. if not don't add edge. 
        if node.MultipleClassMemberDefinition.MultipleClassMemberDefinition != None:
            self.graph.add_edge(pydot.Edge(str(node), str(node.MultipleClassMemberDefinition)))

        #add terminal node for '}Node'
        RCURLYNodeName = str(node.RCURLY) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(RCURLYNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), RCURLYNodeName))

    def pre_visit_ClassMemberDefinition(self, node: ASTClassMemberDefinition):
        pass

    def post_visit_ClassMemberDefinition(self, node: ASTClassMemberDefinition):
        #add node for Class Member Definition
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        #add node for Method/DataMember/Constructor
        self.graph.add_edge(pydot.Edge(str(node), str(node.Method_DataMember_Constructor)))

    def pre_visit_CompilationUnit(self, node: ASTCompilationUnit):
        pass

    def post_visit_CompilationUnit(self, node: ASTCompilationUnit):

        #add Compilation Unit to Start
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))
        self.graph.add_edge(pydot.Edge('Start', str(node)))

        #check to see if this will be visted. If not, don't add edge
        if node.MultipleClassDefinition.ClassDefinition != None and node.MultipleClassDefinition.MultipleClassDefinition != None:
            self.graph.add_edge(pydot.Edge(str(node), str(node.MultipleClassDefinition)))

        #add node for terminal 'void'
        voidNodeName = str(node.void) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(voidNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), voidNodeName))

        #add node for terminal 'KXI2023'
        kxiNodeName = str(node.kxi2023) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(kxiNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), kxiNodeName))

        #add node for terminal 'main'
        mainNodeName = str(node.main) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(mainNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), mainNodeName))


        #add node for terminal '('
        LPARENNodeName = str(node.LPAREN) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(LPARENNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), LPARENNodeName))
    
        #add node for terminal ')'
        RPARENNodeName = str(node.RPAREN) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(RPARENNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), RPARENNodeName))

        #check to see if this will be visted. If not, don't add edge
        if node.MethodBody.MultipleStatement != None:
            self.graph.add_edge(pydot.Edge(str(node), str(node.MethodBody)))

    def pre_visit_ConstructorDeclaration(self, node: ASTConstructorDeclaration):
        pass

    def post_visit_ConstructorDeclaration(self, node: ASTConstructorDeclaration):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        IDNodeName = str(node.ID) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(IDNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), IDNodeName))

        self.graph.add_edge(pydot.Edge(str(node), str(node.MethodSuffix)))

    def pre_visit_DataMemberDeclaration(self, node: ASTDataMemberDeclaration):
        pass

    def post_visit_DataMemberDeclaration(self, node: ASTDataMemberDeclaration):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        ModifierNodeName = str(node.Modifier) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(ModifierNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), ModifierNodeName))
        
        self.graph.add_edge(pydot.Edge(str(node), str(node.VariableDeclaration)))

    def pre_visit_ExpressionArgIdx(self, node: ASTExpressionArgIdx):
        pass

    def post_visit_ExpressionArgIdx(self, node: ASTExpressionArgIdx):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))
        
        self.graph.add_edge(pydot.Edge(str(node), str(node.ArgOrIdx)))

    def pre_visit_ExpressionDotID(self, node: ASTExpressionDotID):
        pass

    def post_visit_ExpressionDotID(self, node: ASTExpressionDotID):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        PeriodNodeName = str(node.PERIOD) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(PeriodNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), PeriodNodeName))

        IDNodeName = str(node.ID) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(IDNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), IDNodeName))

    def pre_visit_ExpressionMinus(self, node: ASTExpressionMinus):
        pass

    def post_visit_ExpressionMinus(self, node: ASTExpressionMinus):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        MinusNodeName = str(node.MINUS) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(MinusNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), MinusNodeName))

        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

    def pre_visit_ExpressionNew(self, node: ASTExpressionNew):
        pass

    def post_visit_ExpressionNew(self, node: ASTExpressionNew):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        NewNodeName = str(node.NEW) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(NewNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), NewNodeName))

        TypeNodeName = str(node.Type) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(TypeNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), TypeNodeName))

        self.graph.add_edge(pydot.Edge(str(node), str(node.ArgOrIdx)))

    def pre_visit_ExpressionNot(self, node: ASTExpressionNot):
        pass

    def post_visit_ExpressionNot(self, node: ASTExpressionNot):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        NOTNodeName = str(node.NOT) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(NOTNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), NOTNodeName))

        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

    def pre_visit_ExpressionPlus(self, node: ASTExpressionPlus):
        pass

    def post_visit_ExpressionPlus(self, node: ASTExpressionPlus):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        PLUSNodeName = str(node.PLUS) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(PLUSNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), PLUSNodeName))
        
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

    def pre_visit_ExpressionPAREN(self, node: ASTExpressionPAREN):
        pass
    
    def post_visit_ExpressionPAREN(self, node: ASTExpressionPAREN):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        LPARENNodeName = str(node.LPAREN) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(LPARENNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), LPARENNodeName))
        
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        RPARENNodeName = str(node.RPAREN) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(RPARENNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), RPARENNodeName))

    def pre_visit_ExpressionEAANDE(self, node: ASTExpressionEAANDE):
        pass

    def post_visit_ExpressionEAANDE(self, node: ASTExpressionEAANDE):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        AANDNodeName = str(node.AAND) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(AANDNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), AANDNodeName))
        
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression2)))

    def pre_visit_ExpresssionECEqualE(self, node: ASTExpressionECEqualE):
        pass

    def post_visit_ExpresssionECEqualE(self, node: ASTExpressionECEqualE):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        CEQUALNodeName = str(node.CEQUAL) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(CEQUALNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), CEQUALNodeName))
        
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression2)))

    def pre_visit_ExpressionEDivideE(self, node: ASTExpressionEDivideE):
        pass

    def post_visit_ExpressionEDivideE(self, node: ASTExpressionEDivideE):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        DIVIDENodeName = str(node.DIVIDE) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(DIVIDENodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), DIVIDENodeName))
        
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression2)))

    def pre_visit_ExpressionEDivideEqualE(self, node: ASTExpressionEDivideEqualE):
        pass

    def post_visit_ExpressionEDivideEqualE(self, node: ASTExpressionEDivideEqualE):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        DivideEqualNodeName = str(node.DIVIDEEQUAL) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(DivideEqualNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), DivideEqualNodeName))
        
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression2)))
    
    def pre_visit_ExpressionEEqualE(self, node: ASTExpressionEEqualE):
        pass

    def post_visit_ExpressionEEqualE(self, node: ASTExpressionEEqualE):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        EqualNodeName = str(node.EQUAL) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(EqualNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), EqualNodeName))
        
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression2)))

    def pre_visit_ExpressionEGreaterE(self, node: ASTExpressionEGreaterE):
        pass

    def post_visit_ExpressionEGreaterE(self, node: ASTExpressionEGreaterE):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        GREATERNodeName = str(node.GREATER) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(GREATERNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), GREATERNodeName))
        
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression2)))

    def pre_visit_ExpressionEGreaterEqualE(self, node: ASTExpressionEGreaterEqualE):
        pass

    def post_visit_ExpressionEGreaterEqualE(self, node: ASTExpressionEGreaterEqualE):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        GREATEQUALNodeName = str(node.GREATEQUAL) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(GREATEQUALNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), GREATEQUALNodeName))
        
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression2)))

    def pre_visit_ExpressionELessE(self, node: ASTExpressionELessE):
        pass

    def post_visit_ExpressionELessE(self, node: ASTExpressionELessE):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        LESSNodeName = str(node.LESS) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(LESSNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), LESSNodeName))
        
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression2)))

    def pre_visit_ExpressionELessEqualE(self, node: ASTExpressionELessEqualE):
        pass

    def post_visit_ExpressionELessEqualE(self, node: ASTExpressionELessEqualE):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        LESSEQUALNodeName = str(node.LESSEQUAL) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(LESSEQUALNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), LESSEQUALNodeName))
        
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression2)))

    def pre_visit_ExpressionEMinusE(self, node: ASTExpressionEMinusE):
        pass

    def post_visit_ExpressionEMinusE(self, node: ASTExpressionEMinusE):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        MINUSNodeName = str(node.MINUS) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(MINUSNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), MINUSNodeName))
        
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression2)))

    def pre_visit_ExpressionEMinusEqualE(self, node: ASTExpressionEMinusEqualE):
        pass

    def post_visit_ExpressionEMinusEqualE(self, node: ASTExpressionEMinusEqualE):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        MINUSEQUALNodeName = str(node.MINUSEQUAL) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(MINUSEQUALNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), MINUSEQUALNodeName))
        
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression2)))

    def pre_visit_ExpressionENotEqualE(self, node: ASTExpressionENotEqualE):
        pass

    def post_visit_ExpressionENotEqualE(self, node: ASTExpressionENotEqualE):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        NEQUALNodeName = str(node.NEQUAL) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(NEQUALNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), NEQUALNodeName))
        
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression2)))

    def pre_visit_ExpressionEOORE(self, node: ASTExpressionEOORE):
        pass

    def post_visit_ExpressionEOORE(self, node: ASTExpressionEOORE):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        OORNodeName = str(node.OOR) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(OORNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), OORNodeName))
        
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression2)))

    def pre_visit_ExpressionEPlusE(self, node: ASTExpressionEPlusE):
        pass
    
    def post_visit_ExpressionEPlusE(self, node: ASTExpressionEPlusE):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        PLUSNodeName = str(node.PLUS) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(PLUSNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), PLUSNodeName))
        
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression2)))

    def pre_visit_ExpressionEPlusEqualE(self, node: ASTExpressionEPlusEqualE):
        pass

    def post_visit_ExpressionEPlusEqualE(self, node: ASTExpressionEPlusEqualE):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        PLUSEQUALNodeName = str(node.PLUSEQUAL) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(PLUSEQUALNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), PLUSEQUALNodeName))
        
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression2)))

    def pre_visit_ExpressionETimesE(self, node: ASTExpressionETimesE):
        pass

    def post_visit_ExpressionETimesE(self, node: ASTExpressionETimesE):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        TIMESNodeName = str(node.TIMES) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(TIMESNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), TIMESNodeName))
        
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression2)))

    def pre_visit_ExpressionETimesEqualE(self, node: ASTExpressionETimesEqualE):
        pass

    def post_visit_ExpressionETimesEqualE(self, node: ASTExpressionETimesEqualE):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        TIMESEQUALNodeName = str(node.TIMESEQUAL) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(TIMESEQUALNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), TIMESEQUALNodeName))
        
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression2)))

    def pre_visit_Index(self, node: ASTIndex):
        pass

    def post_visit_Index(self, node: ASTIndex):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        LSQUARENodeName = str(node.LSQUARE) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(LSQUARENodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), LSQUARENodeName))

        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        RSQUARENodeName = str(node.RSQUARE) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(RSQUARENodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), RSQUARENodeName))
        
    def pre_visit_Initializer(self, node: ASTInitializer):
        pass

    def post_visit_Initializer(self, node: ASTInitializer):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        EQUALNodeName = str(node.EQUAL) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(EQUALNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), EQUALNodeName))

        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

    def pre_visit_MaybeArgumentList(self, node: ASTMaybeArgumentList):
        pass

    def post_visit_MaybeArgumentList(self, node: ASTMaybeArgumentList):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        if node.ArgumentList != None:
            self.graph.add_edge(pydot.Edge(str(node), str(node.ArgumentList)))

    def pre_visit_MaybeExpression(self, node: ASTMaybeExpression):
        pass

    def post_visit_MaybeExpression(self, node: ASTMaybeExpression):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        if node.Expression != None:
            self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

    def pre_visit_MaybeInitializer(self, node: ASTMaybeInitializer):
        pass

    def post_visit_MaybeInitializer(self, node: ASTMaybeInitializer):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        if node.Initializer != None:
            self.graph.add_edge(pydot.Edge(str(node), str(node.Initializer)))

    def pre_visit_MaybeParamList(self, node: ASTMaybeParamList):
        pass

    def post_visit_MaybeParamList(self, node: ASTMaybeParamList):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        if node.ParameterList != None:
            self.graph.add_edge(pydot.Edge(str(node), str(node.ParameterList)))

    def pre_visit_MethodBody(self, node: ASTMethodBody):
        pass

    def post_visit_MethodBody(self, node: ASTMethodBody):
        #add node for MethodBody
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        #add terminal node for '{'
        LCURLYNodeName = str(node.LCURLY) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(LCURLYNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), LCURLYNodeName))

        #check to see if MultipleStatement will be visited. 
        if node.MultipleStatement.MultipleStatement != None and node.MultipleStatement.Statement:
            self.graph.add_edge(pydot.Edge(str(node), str(node.MultipleStatement)))

        #add terminal node for '}'
        RCURLYNodeName = str(node.RCURLY) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(RCURLYNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), RCURLYNodeName))

    def pre_visit_MethodDeclaration(self, node: ASTMethodDeclaration):
        pass

    def post_visit_MethodDeclaration(self, node: ASTMethodDeclaration):
        #add node for MEthodDeclaration
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        #add node for terminal Modifier
        ModifierNodeName = str(node.Modifier) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(ModifierNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), ModifierNodeName))

        #add node for terminal Type

        TypeNodeName = str(node.Type) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(TypeNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), TypeNodeName))

        #add node for terminal []
        if node.LRSquare != None:
            LRSquareNodeName = str(node.LRSquare) + " $" + str(self.UID.getID())
            self.graph.add_node(pydot.Node(LRSquareNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
            self.graph.add_edge(pydot.Edge(str(node), LRSquareNodeName))

        #add node for terminal ID
        IDNodeName = str(node.ID) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(IDNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), IDNodeName))

        #add edge for node.MethodSuffix
        self.graph.add_edge(pydot.Edge(str(node), str(node.MethodSuffix)))

    def pre_visit_MethodSuffix(self, node: ASTMethodSuffix):
        pass

    def post_visit_MethodSuffix(self, node: ASTMethodSuffix):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        LPARENNodeName = str(node.LPAREN) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(LPARENNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), LPARENNodeName))

        if (node.MaybeParameterList.ParameterList!= None):
            self.graph.add_edge(pydot.Edge(str(node), str(node.MaybeParameterList)))

        RPARENNodeName = str(node.RPAREN) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(RPARENNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), RPARENNodeName))

        self.graph.add_edge(pydot.Edge(str(node), str(node.MethodBody)))

    def pre_visit_MultipleCase(self, node: ASTMultipleCase):
        pass

    def post_visit_MultipleCase(self, node: ASTMultipleCase):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        if (node.Case != None):
            self.graph.add_edge(pydot.Edge(str(node), str(node.Case)))

        if (node.MultipleCase.Case != None):
            self.graph.add_edge(pydot.Edge(str(node), str(node.MultipleCase)))

    def pre_visit_MultipleClassDefinition(self, node: ASTMultipleClassDefinition):
        pass

    def post_visit_MultipleClassDefinition(self, node: ASTMultipleClassDefinition):
        #add node for MultipleClass Definition
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        #check to see if this will be visited. If not, don't add edge
        if (node.ClassDefinition != None):
            self.graph.add_edge(pydot.Edge(str(node), str(node.ClassDefinition)))

        #check to see if this will be visited. If not, don't add edge
        if (node.MultipleClassDefinition.ClassDefinition != None):
            self.graph.add_edge(pydot.Edge(str(node), str(node.MultipleClassDefinition)))
                
    def pre_visit_MultipleClassMemberDefinition(self, node: ASTMultipleClassMemberDefinition):
        pass

    def post_visit_MultipleClassMemberDefinition(self, node: ASTMultipleClassMemberDefinition):
        #add node for MultipleClassMemberDefinition
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        #check to see if this will be visited. If not, don't add edge
        if (node.ClassMemberDefinition != None):
            self.graph.add_edge(pydot.Edge(str(node), str(node.ClassMemberDefinition)))
            
        #check to see if this will be visited. If not, don't add edge
        if (node.MultipleClassMemberDefinition.ClassMemberDefinition != None):
            self.graph.add_edge(pydot.Edge(str(node), str(node.MultipleClassMemberDefinition)))

    def pre_visit_MultipleCommaExpression(self, node: ASTMultipleCommaExpression):
        pass

    def post_visit_MultipleCommaExpression(self, node: ASTMultipleCommaExpression):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        CommaNodeName = str(node.COMMA) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(CommaNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), CommaNodeName))

        if node.Expression == None:
            noneNodeName = "None $" + str(self.UID.getID())
            self.graph.add_node(pydot.Node(noneNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
            self.graph.add_edge(pydot.Edge(str(node), noneNodeName))
        else:
            self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        if node.MultipleCommaExpression == None:
            noneNodeName = "None $" + str(self.UID.getID())
            self.graph.add_node(pydot.Node(noneNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
            self.graph.add_edge(pydot.Edge(str(node), noneNodeName))
        else:
            self.graph.add_edge(pydot.Edge(str(node), str(node.MultipleCommaExpression)))

    def pre_visit_MultipleCommaParameter(self, node: ASTMultipleCommaParameter):
        pass

    def post_visit_MultipleCommaParameter(self, node: ASTMultipleCommaParameter):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        CommaNodeName = str(node.COMMA) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(CommaNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), CommaNodeName))

        if node.Parameter == None:
            noneNodeName = "None $" + str(self.UID.getID())
            self.graph.add_node(pydot.Node(noneNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
            self.graph.add_edge(pydot.Edge(str(node), noneNodeName))
        else:
            self.graph.add_edge(pydot.Edge(str(node), str(node.Parameter)))

        if node.MultipleCommaParameter == None:
            noneNodeName = "None $" + str(self.UID.getID())
            self.graph.add_node(pydot.Node(noneNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
            self.graph.add_edge(pydot.Edge(str(node), noneNodeName))
        else:
            self.graph.add_edge(pydot.Edge(str(node), str(node.MultipleCommaParameter)))

    def pre_visit_MultipleStatement(self, node: ASTMultipleStatement):
        pass

    def post_visit_MultipleStatement(self, node: ASTMultipleStatement):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        if (node.Statement != None):
            self.graph.add_edge(pydot.Edge(str(node), str(node.Statement)))
        if (node.MultipleStatement.MultipleStatement != None):
            self.graph.add_edge(pydot.Edge(str(node), str(node.MultipleStatement)))

    def pre_visit_Parameter(self, node: ASTParameter):
        pass

    def post_visit_Parameter(self, node: ASTParameter):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        TypeNodeName = str(node.Type) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(TypeNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), TypeNodeName))

        #add node for terminal []
        if node.LRSquare != None:
            LRSquareNodeName = str(node.LRSquare) + " $" + str(self.UID.getID())
            self.graph.add_node(pydot.Node(LRSquareNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
            self.graph.add_edge(pydot.Edge(str(node), LRSquareNodeName))

        IDNodeName = str(node.ID) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(IDNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), IDNodeName))

    def pre_visit_ParameterList(self, node: ASTParameterList):
        pass

    def post_visit_ParameterList(self, node: ASTParameterList):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        self.graph.add_edge(pydot.Edge(str(node), str(node.Parameter)))

        self.graph.add_edge(pydot.Edge(str(node), str(node.MultipleCommaParameter)))

    def pre_visit_StatementBreak(self, node: ASTStatementBreak):
        pass

    def post_visit_StatementBreak(self, node: ASTStatementBreak):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        BreakNodeName = str(node.BREAK) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(BreakNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), BreakNodeName))

        SEMICOLONNodeName = str(node.SEMICOLON) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(SEMICOLONNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), SEMICOLONNodeName))        

    def pre_visit_StatementCIN(self, node: ASTStatementCIN):
        pass

    def post_visit_StatementCIN(self, node: ASTStatementCIN):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        CINNodeName = str(node.CIN) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(CINNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), CINNodeName))

        RIGHTSHIFTNodeName = str(node.RIGHTSHIFT) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(RIGHTSHIFTNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), RIGHTSHIFTNodeName))

        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        SEMICOLONNodeName = str(node.SEMICOLON) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(SEMICOLONNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), SEMICOLONNodeName))

    def pre_visit_StatementCOUT(self, node: ASTStatementCOUT):
        pass

    def post_visit_StatementCOUT(self, node: ASTStatementCOUT):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        COUTNodeName = str(node.COUT) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(COUTNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), COUTNodeName))

        LEFTSHIFTNodeName = str(node.LEFTSHIFT) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(LEFTSHIFTNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), LEFTSHIFTNodeName))

        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        SEMICOLONNodeName = str(node.SEMICOLON) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(SEMICOLONNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), SEMICOLONNodeName))

    def pre_visit_StatementExpression(self, node: ASTStatementExpression):
        pass

    def post_visit_StatementExpression(self, node: ASTStatementExpression):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        SEMICOLONNodeName = str(node.SEMICOLON) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(SEMICOLONNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), SEMICOLONNodeName))

    def pre_visit_StatementIF(self, node: ASTStatementIF):
        pass

    def post_visit_StatementIF(self, node: ASTStatementIF):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        IFNodeName = str(node.IF) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(IFNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), IFNodeName))

        LPARENNodeName = str(node.LPAREN) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(LPARENNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), LPARENNodeName))

        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        RPARENNodeName = str(node.RPAREN) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(RPARENNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), RPARENNodeName))

        self.graph.add_edge(pydot.Edge(str(node), str(node.Statement)))

    def pre_visit_StatementIFELSE(self, node: ASTStatementIFELSE):
        pass

    def post_visit_StatementIFELSE(self, node: ASTStatementIFELSE):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        IFNodeName = str(node.IF) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(IFNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), IFNodeName))

        LPARENNodeName = str(node.LPAREN) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(LPARENNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), LPARENNodeName))

        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        RPARENNodeName = str(node.RPAREN) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(RPARENNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), RPARENNodeName))

        self.graph.add_edge(pydot.Edge(str(node), str(node.Statement)))

        ELSENodeName = str(node.ELSE) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(ELSENodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), ELSENodeName))

        self.graph.add_edge(pydot.Edge(str(node), str(node.Statement2)))

    def pre_visit_StatementMultipleStatement(self, node: ASTStatementMultipleStatement):
        pass

    def post_visit_StatementMultipleStatement(self, node: ASTStatementMultipleStatement):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        LCURLYNodeName = str(node.LCURLY) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(LCURLYNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), LCURLYNodeName))

        self.graph.add_edge(pydot.Edge(str(node), str(node.MultipleStatement)))

        RCURLYNodeName = str(node.RCURLY) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(RCURLYNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), RCURLYNodeName))

    def pre_visit_StatementToVariableDeclaration(self, node: ASTStatementToVariableDeclaration):
        pass

    def post_visit_StatementToVariableDeclaration(self, node: ASTStatementToVariableDeclaration):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        self.graph.add_edge(pydot.Edge(str(node), str(node.VariableDeclaration)))

    def pre_visit_StatementReturn(self, node: ASTStatementReturn):
        pass

    def post_visit_StatementReturn(self, node: ASTStatementReturn):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        RETURNNodeName = str(node.RETURN) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(RETURNNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), RETURNNodeName))

        if (node.MaybeExpression.Expression != None):
            self.graph.add_edge(pydot.Edge(str(node), str(node.MaybeExpression)))

        SEMICOLONNodeName = str(node.SEMICOLON) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(SEMICOLONNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), SEMICOLONNodeName))

    def pre_visit_StatementSwitch(self, node: ASTStatementSwitch):
        pass

    def post_visit_StatementSwitch(self, node: ASTStatementSwitch):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        SWITCHNodeName = str(node.SWITCH) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(SWITCHNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), SWITCHNodeName))

        LPARENNodeName = str(node.LPAREN) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(LPARENNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), LPARENNodeName))

        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        RPARENNodeName = str(node.RPAREN) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(RPARENNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), RPARENNodeName))

        self.graph.add_edge(pydot.Edge(str(node), str(node.CaseBlock)))

    def pre_visit_StatementWhile(self, node: ASTStatementWhile):
        pass

    def post_visit_StatementWhile(self, node: ASTStatementWhile):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        WHILENodeName = str(node.WHILE) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(WHILENodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), WHILENodeName))

        LPARENNodeName = str(node.LPAREN) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(LPARENNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), LPARENNodeName))

        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        RPARENNodeName = str(node.RPAREN) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(RPARENNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), RPARENNodeName))

        self.graph.add_edge(pydot.Edge(str(node), str(node.Statement)))

    def pre_visit_VariableDeclaration(self, node: ASTVariableDeclaration):
        pass

    def post_visit_VariableDeclaration(self, node: ASTVariableDeclaration):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        TypeNodeName = str(node.Type) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(TypeNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), TypeNodeName))

        #add node for terminal []
        if node.LRSquare != None:
            LRSquareNodeName = str(node.LRSquare) + " $" + str(self.UID.getID())
            self.graph.add_node(pydot.Node(LRSquareNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
            self.graph.add_edge(pydot.Edge(str(node), LRSquareNodeName))

        IDNodeName = str(node.ID) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(IDNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), IDNodeName))

        if (node.Initializer.Initializer != None):
            self.graph.add_edge(pydot.Edge(str(node), str(node.Initializer)))

        SEMICOLONNodeName = str(node.SEMICOLON) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(SEMICOLONNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), SEMICOLONNodeName))

    def pre_visit_Terminal(self, node: ASTTerminal):
        pass

    def post_visit_Terminal(self, node: ASTTerminal):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        TerminalNodeName = str(node.Terminal) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(TerminalNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), TerminalNodeName))