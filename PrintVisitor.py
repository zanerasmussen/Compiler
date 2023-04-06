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
        self.graph = None

    def visit_Argument(self, node: ASTArgument):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))
        
        LPARENNodeName = str(node.LPAREN) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(LPARENNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), LPARENNodeName))

        node.MaybeArgumentList.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.MaybeArgumentList)))

        RPARENNodeName = str(node.RPAREN) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(RPARENNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), RPARENNodeName))

    def visit_ArgumentList(self, node: ASTArgumentList):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        node.Expression.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        node.MultipleCommaExpression.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.MultipleCommaExpression)))
    
    def visit_ArgOrIdx(self, node: ASTArgOrIdx):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        node.Arg_Idx.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Arg_Idx)))

    def visit_Case(self, node: ASTCase):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="##7CFC7C"))

        CaseNodeName = str(node.CASE) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(CaseNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), CaseNodeName))

        NumOrCharNodeName = str(node.NumOrChar) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(NumOrCharNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), NumOrCharNodeName))

        ColonNodeName = str(node.COLON) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(ColonNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), ColonNodeName))

        node.MultipleStatement.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.MultipleStatement)))

    def visit_CaseBlock(self, node: ASTCaseBlock):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        LCURLYNodeName = str(node.LCURLY) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(LCURLYNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), LCURLYNodeName))

        node.MultipleCase.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.MultipleCase)))

        DefaultNodeName = str(node.DEFAULT) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(DefaultNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), DefaultNodeName))

        ColonNodeName = str(node.COLON) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(ColonNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), ColonNodeName))

        node.MultipleStatement.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.MultipleStatement)))
        
        RCURLYNodeName = str(node.RCURLY) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(RCURLYNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), RCURLYNodeName))

    def visit_ClassDefinition(self, node: ASTClassDefinition):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        classNodeName = str(node.Class) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(classNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), classNodeName))

        IDNodeName = str(node.ID) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(IDNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), IDNodeName))

        LCURLYNodeName = str(node.LCURLY) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(LCURLYNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), LCURLYNodeName))

        node.MultipleClassMemberDefinition.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.MultipleClassMemberDefinition)))

        RCURLYNodeName = str(node.RCURLY) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(RCURLYNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), RCURLYNodeName))

    def visit_ClassMemberDefinition(self, node: ASTClassMemberDefinition):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        node.Method_DataMember_Constructor.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Method_DataMember_Constructor)))

    def visit_CompilationUnit(self, node: ASTCompilationUnit):

        self.graph = pydot.Dot('my_graph', graph_type='graph')
        start = pydot.Node('Start', shape='diamond', style='filled', fillcolor='cyan')

        self.graph.add_node(start)
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))
        self.graph.add_edge(pydot.Edge('Start', str(node)))

        node.MultipleClassDefinition.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.MultipleClassDefinition)))

        voidNodeName = str(node.void) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(voidNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), voidNodeName))

        kxiNodeName = str(node.kxi2023) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(kxiNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), kxiNodeName))

        mainNodeName = str(node.main) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(mainNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), mainNodeName))

        LPARENNodeName = str(node.LPAREN) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(LPARENNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), LPARENNodeName))
    
        RPARENNodeName = str(node.RPAREN) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(RPARENNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), RPARENNodeName))

        node.MethodBody.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.MethodBody)))

        self.graph.write_png('output.png')

    def visit_ConstructorDeclaration(self, node: ASTConstructorDeclaration):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        IDNodeName = str(node.ID) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(IDNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), IDNodeName))

        node.MethodSuffix.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.MethodSuffix)))

    def visit_DataMemberDeclaration(self, node: ASTDataMemberDeclaration):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        ModifierNodeName = str(node.Modifier) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(ModifierNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), ModifierNodeName))
        
        node.VariableDeclaration.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.VariableDeclaration)))

    def visit_ExpressionArgIdx(self, node: ASTExpressionArgIdx):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        node.Expression.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))
        
        node.ArgOrIdx.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.ArgOrIdx)))

    def visit_ExpressionDotID(self, node: ASTExpressionDotID):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        node.Expression.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        PeriodNodeName = str(node.PERIOD) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(PeriodNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), PeriodNodeName))

        IDNodeName = str(node.ID) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(IDNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), IDNodeName))

    def visit_ExpressionMinus(self, node: ASTExpressionMinus):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        MinusNodeName = str(node.MINUS) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(MinusNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), MinusNodeName))

        node.Expression.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

    def visit_ExpressionNew(self, node: ASTExpressionNew):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        NewNodeName = str(node.NEW) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(NewNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), NewNodeName))

        TypeNodeName = str(node.Type) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(TypeNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), TypeNodeName))

        node.ArgOrIdx.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.ArgOrIdx)))

    def visit_ExpressionNot(self, node: ASTExpressionNot):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        NOTNodeName = str(node.NOT) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(NOTNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), NOTNodeName))

        node.Expression.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

    def visit_ExpressionPlus(self, node: ASTExpressionPlus):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        PLUSNodeName = str(node.PLUS) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(PLUSNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), PLUSNodeName))
        
        node.Expression.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

    def visit_ExpressionPAREN(self, node: ASTExpressionPAREN):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        LPARENNodeName = str(node.LPAREN) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(LPARENNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), LPARENNodeName))
        
        node.Expression.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        RPARENNodeName = str(node.RPAREN) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(RPARENNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), RPARENNodeName))

    def visit_ExpressionEAANDE(self, node: ASTExpressionEAANDE):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        node.Expression.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        AANDNodeName = str(node.AAND) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(AANDNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), AANDNodeName))
        
        node.Expression2.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression2)))

    def visit_ExpresssionECEqualE(self, node: ASTExpressionECEqualE):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        node.Expression.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        CEQUALNodeName = str(node.CEQUAL) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(CEQUALNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), CEQUALNodeName))
        
        node.Expression2.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression2)))

    def visit_ExpressionEDivideE(self, node: ASTExpressionEDivideE):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        node.Expression.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        DIVIDENodeName = str(node.DIVIDE) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(DIVIDENodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), DIVIDENodeName))
        
        node.Expression2.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression2)))

    def visit_ExpressionEDivideEqualE(self, node: ASTExpressionEDivideEqualE):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        node.Expression.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        DivideEqualNodeName = str(node.DIVIDEEQUAL) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(DivideEqualNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), DivideEqualNodeName))
        
        node.Expression2.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression2)))
    
    def visit_ExpressionEEqualE(self, node: ASTExpressionEEqualE):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        node.Expression.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        EqualNodeName = str(node.EQUAL) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(EqualNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), EqualNodeName))
        
        node.Expression2.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression2)))

    def visit_ExpressionEGreaterE(self, node: ASTExpressionEGreaterE):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        node.Expression.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        GREATERNodeName = str(node.GREATER) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(GREATERNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), GREATERNodeName))
        
        node.Expression2.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression2)))

    def visit_ExpressionEGreaterEqualE(self, node: ASTExpressionEGreaterEqualE):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        node.Expression.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        GREATEQUALNodeName = str(node.GREATEQUAL) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(GREATEQUALNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), GREATEQUALNodeName))
        
        node.Expression2.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression2)))

    def visit_ExpressionELessE(self, node: ASTExpressionELessE):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        node.Expression.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        LESSNodeName = str(node.LESS) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(LESSNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), LESSNodeName))
        
        node.Expression2.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression2)))

    def visit_ExpressionELessEqualE(self, node: ASTExpressionELessEqualE):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        node.Expression.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        LESSEQUALNodeName = str(node.LESSEQUAL) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(LESSEQUALNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), LESSEQUALNodeName))
        
        node.Expression2.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression2)))

    def visit_ExpressionEMinusE(self, node: ASTExpressionEMinusE):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        node.Expression.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        MINUSNodeName = str(node.MINUS) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(MINUSNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), MINUSNodeName))
        
        node.Expression2.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression2)))

    def visit_ExpressionEMinusEqualE(self, node: ASTExpressionEMinusEqualE):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        node.Expression.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        MINUSEQUALNodeName = str(node.MINUSEQUAL) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(MINUSEQUALNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), MINUSEQUALNodeName))
        
        node.Expression2.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression2)))

    def visit_ExpressionENotEqualE(self, node: ASTExpressionENotEqualE):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        node.Expression.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        NEQUALNodeName = str(node.NEQUAL) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(NEQUALNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), NEQUALNodeName))
        
        node.Expression2.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression2)))

    def visit_ExpressionEOORE(self, node: ASTExpressionEOORE):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        node.Expression.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        OORNodeName = str(node.OOR) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(OORNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), OORNodeName))
        
        node.Expression2.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression2)))

    def visit_ExpressionEPlusE(self, node: ASTExpressionEPlusE):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        node.Expression.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        PLUSNodeName = str(node.PLUS) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(PLUSNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), PLUSNodeName))
        
        node.Expression2.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression2)))

    def visit_ExpressionEPlusEqualE(self, node: ASTExpressionEPlusEqualE):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        node.Expression.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        PLUSEQUALNodeName = str(node.PLUSEQUAL) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(PLUSEQUALNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), PLUSEQUALNodeName))
        
        node.Expression2.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression2)))

    def visit_ExpressionETimesE(self, node: ASTExpressionETimesE):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        node.Expression.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        TIMESNodeName = str(node.TIMES) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(TIMESNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), TIMESNodeName))
        
        node.Expression2.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression2)))

    def visit_ExpressionETimesEqualE(self, node: ASTExpressionETimesEqualE):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        node.Expression.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        TIMESEQUALNodeName = str(node.TIMESEQUAL) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(TIMESEQUALNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), TIMESEQUALNodeName))
        
        node.Expression2.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression2)))

    def visit_Index(self, node: ASTIndex):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        LSQUARENodeName = str(node.LSQUARE) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(LSQUARENodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), LSQUARENodeName))

        node.Expression.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        RSQUARENodeName = str(node.RSQUARE) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(RSQUARENodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), RSQUARENodeName))
        
    def visit_Initializer(self, node: ASTInitializer):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        EQUALNodeName = str(node.EQUAL) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(EQUALNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), EQUALNodeName))

        node.Expression.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

    def visit_MaybeArgumentList(self, node: ASTMaybeArgumentList):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        if node.ArgumentList is None:
            noneNodeName = "None $" + str(self.UID.getID())
            self.graph.add_node(pydot.Node(noneNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
            self.graph.add_edge(pydot.Edge(str(node), noneNodeName))

        else:
            node.ArgumentList.accept(self)
            self.graph.add_edge(pydot.Edge(str(node), str(node.ArgumentList)))

    def visit_MaybeExpression(self, node: ASTMaybeExpression):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        if node.Expression is None:
            noneNodeName = "None $" + str(self.UID.getID())
            self.graph.add_node(pydot.Node(noneNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
            self.graph.add_edge(pydot.Edge(str(node), noneNodeName))
            
        else:
            node.Expression.accept(self)
            self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

    def visit_MaybeInitializer(self, node: ASTMaybeInitializer):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        if node.Initializer is None:
            noneNodeName = "None $" + str(self.UID.getID())
            self.graph.add_node(pydot.Node(noneNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
            self.graph.add_edge(pydot.Edge(str(node), noneNodeName))
            
        else:
            node.Initializer.accept(self)
            self.graph.add_edge(pydot.Edge(str(node), str(node.Initializer)))

    def visit_MaybeParamList(self, node: ASTMaybeParamList):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        if node.ParameterList is None:
            noneNodeName = "None $" + str(self.UID.getID())
            self.graph.add_node(pydot.Node(noneNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
            self.graph.add_edge(pydot.Edge(str(node), noneNodeName))
            
        else:
            node.ParameterList.accept(self)
            self.graph.add_edge(pydot.Edge(str(node), str(node.ParameterList)))

    def visit_MethodBody(self, node: ASTMethodBody):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        LCURLYNodeName = str(node.LCURLY) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(LCURLYNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), LCURLYNodeName))

        node.MultipleStatement.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.MultipleStatement)))

        RCURLYNodeName = str(node.RCURLY) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(RCURLYNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), RCURLYNodeName))

    def visit_MethodDeclaration(self, node: ASTMethodDeclaration):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        ModifierNodeName = str(node.Modifier) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(ModifierNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), ModifierNodeName))

        TypeNodeName = str(node.Type) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(TypeNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), TypeNodeName))

        LRSquareNodeName = str(node.LRSquare) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(LRSquareNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), LRSquareNodeName))

        IDNodeName = str(node.ID) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(IDNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), IDNodeName))

        node.MethodSuffix.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.MethodSuffix)))

    def visit_MethodSuffix(self, node: ASTMethodSuffix):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        LPARENNodeName = str(node.LPAREN) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(LPARENNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), LPARENNodeName))

        node.MaybeParameterList.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.MaybeParameterList)))

        RPARENNodeName = str(node.RPAREN) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(RPARENNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), RPARENNodeName))

        node.MethodBody.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.MethodBody)))

    def visit_MultipleCase(self, node: ASTMultipleCase):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        if (node.Case == None):
            noneNodeName = "None $" + str(self.UID.getID())
            self.graph.add_node(pydot.Node(noneNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
            self.graph.add_edge(pydot.Edge(str(node), noneNodeName))
            
        else:
            for c in node.Case:
                c.accept(self)
                self.graph.add_edge(pydot.Edge(str(node), str(c)))

    def visit_MultipleClassDefinition(self, node: ASTMultipleClassDefinition):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        if (node.ClassDefinition == None):
            noneNodeName = "None $" + str(self.UID.getID())
            self.graph.add_node(pydot.Node(noneNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
            self.graph.add_edge(pydot.Edge(str(node), noneNodeName))

        else:
            for classDef in node.ClassDefinition:
                classDef.accept(self)
                self.graph.add_edge(pydot.Edge(str(node), str(classDef)))
                
    def visit_MultipleClassMemberDefinition(self, node: ASTMultipleClassMemberDefinition):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        if (node.ClassMemberDefinition == None):
            noneNodeName = "None $" + str(self.UID.getID())
            self.graph.add_node(pydot.Node(noneNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
            self.graph.add_edge(pydot.Edge(str(node), noneNodeName))

        else:
            for classMem in node.ClassMemberDefinition:
                classMem.accept(self)
                self.graph.add_edge(pydot.Edge(str(node), str(classMem)))

    def visit_MultipleCommaExpression(self, node: ASTMultipleCommaExpression):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        CommaNodeName = str(node.COMMA) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(CommaNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), CommaNodeName))

        if node.Expression == None:
            noneNodeName = "None $" + str(self.UID.getID())
            self.graph.add_node(pydot.Node(noneNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
            self.graph.add_edge(pydot.Edge(str(node), noneNodeName))
        else:
            node.Expression.accept(self)
            self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        if node.MultipleCommaExpression == None:
            noneNodeName = "None $" + str(self.UID.getID())
            self.graph.add_node(pydot.Node(noneNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
            self.graph.add_edge(pydot.Edge(str(node), noneNodeName))
        else:
            node.MultipleCommaExpression.accept(self)
            self.graph.add_edge(pydot.Edge(str(node), str(node.MultipleCommaExpression)))

    def visit_MultipleCommaParameter(self, node: ASTMultipleCommaParameter):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        CommaNodeName = str(node.COMMA) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(CommaNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), CommaNodeName))

        if node.Expression == None:
            noneNodeName = "None $" + str(self.UID.getID())
            self.graph.add_node(pydot.Node(noneNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
            self.graph.add_edge(pydot.Edge(str(node), noneNodeName))
        else:
            node.Expression.accept(self)
            self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        if node.MultipleCommaParameter == None:
            noneNodeName = "None $" + str(self.UID.getID())
            self.graph.add_node(pydot.Node(noneNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
            self.graph.add_edge(pydot.Edge(str(node), noneNodeName))
        else:
            node.MultipleCommaParameter.accept(self)
            self.graph.add_edge(pydot.Edge(str(node), str(node.MultipleCommaParameter)))

    def visit_MultipleStatement(self, node: ASTMultipleStatement):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        if (node.Statement == None):
            noneNodeName = "None $" + str(self.UID.getID())
            self.graph.add_node(pydot.Node(noneNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
            self.graph.add_edge(pydot.Edge(str(node), noneNodeName))
            
        else:
            for s in node.Statement:
                s.accept(self)
                self.graph.add_edge(pydot.Edge(str(node), str(s)))

    def visit_Parameter(self, node: ASTParameter):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        TypeNodeName = str(node.Type) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(TypeNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), TypeNodeName))

        LRSquareNodeName = str(node.LRSquare) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(LRSquareNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), LRSquareNodeName))

        IDNodeName = str(node.ID) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(IDNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), IDNodeName))

    def visit_ParameterList(self, node: ASTParameterList):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        node.Parameter.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Parameter)))

        node.MultipleCommaParameter.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.MultipleCommaParameter)))

    def visit_StatementBreak(self, node: ASTStatementBreak):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        BreakNodeName = str(node.BREAK) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(BreakNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), BreakNodeName))

        SEMICOLONNodeName = str(node.SEMICOLON) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(SEMICOLONNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), SEMICOLONNodeName))        

    def visit_StatementCIN(self, node: ASTStatementCIN):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        CINNodeName = str(node.CIN) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(CINNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), CINNodeName))

        RIGHTSHIFTNodeName = str(node.RIGHTSHIFT) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(RIGHTSHIFTNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), RIGHTSHIFTNodeName))

        node.Expression.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        SEMICOLONNodeName = str(node.SEMICOLON) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(SEMICOLONNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), SEMICOLONNodeName))

    def visit_StatementCOUT(self, node: ASTStatementCOUT):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        COUTNodeName = str(node.COUT) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(COUTNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), COUTNodeName))

        LEFTSHIFTNodeName = str(node.LEFTSHIFT) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(LEFTSHIFTNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), LEFTSHIFTNodeName))

        node.Expression.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        SEMICOLONNodeName = str(node.SEMICOLON) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(SEMICOLONNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), SEMICOLONNodeName))

    def visit_StatementExpression(self, node: ASTStatementExpression):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        node.Expression.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        SEMICOLONNodeName = str(node.SEMICOLON) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(SEMICOLONNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), SEMICOLONNodeName))

    def visit_StatementIF(self, node: ASTStatementIF):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        IFNodeName = str(node.IF) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(IFNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), IFNodeName))

        LPARENNodeName = str(node.LPAREN) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(LPARENNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), LPARENNodeName))

        node.Expression.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        RPARENNodeName = str(node.RPAREN) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(RPARENNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), RPARENNodeName))

        node.Statement.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Statement)))

    def visit_StatementIFELSE(self, node: ASTStatementIFELSE):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        IFNodeName = str(node.IF) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(IFNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), IFNodeName))

        LPARENNodeName = str(node.LPAREN) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(LPARENNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), LPARENNodeName))

        node.Expression.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        RPARENNodeName = str(node.RPAREN) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(RPARENNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), RPARENNodeName))

        node.Statement.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Statement)))

        ELSENodeName = str(node.ELSE) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(ELSENodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), ELSENodeName))

        node.Statement2.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Statement2)))

    def visit_StatementMultipleStatement(self, node: ASTStatementMultipleStatement):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        LCURLYNodeName = str(node.LCURLY) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(LCURLYNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), LCURLYNodeName))

        node.MultipleStatement.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.MultipleStatement)))

        RCURLYNodeName = str(node.RCURLY) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(RCURLYNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), RCURLYNodeName))

    def visit_StatementToVariableDeclaration(self, node: ASTStatementToVariableDeclaration):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        node.VariableDeclaration.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.VariableDeclaration)))

    def visit_StatementReturn(self, node: ASTStatementReturn):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        RETURNNodeName = str(node.RETURN) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(RETURNNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), RETURNNodeName))

        node.MaybeExpression.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.MaybeExpression)))

        SEMICOLONNodeName = str(node.SEMICOLON) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(SEMICOLONNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), SEMICOLONNodeName))

    def visit_StatementSwitch(self, node: ASTStatementSwitch):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        SWITCHNodeName = str(node.SWITCH) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(SWITCHNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), SWITCHNodeName))

        LPARENNodeName = str(node.LPAREN) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(LPARENNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), LPARENNodeName))

        node.Expression.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        RPARENNodeName = str(node.RPAREN) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(RPARENNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), RPARENNodeName))

        node.CaseBlock.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.CaseBlock)))

    def visit_StatementWhile(self, node: ASTStatementWhile):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        WHILENodeName = str(node.WHILE) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(WHILENodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), WHILENodeName))

        LPARENNodeName = str(node.LPAREN) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(LPARENNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), LPARENNodeName))

        node.Expression.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Expression)))

        RPARENNodeName = str(node.RPAREN) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(RPARENNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), RPARENNodeName))

        node.Statement.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Statement)))

    def visit_VariableDeclaration(self, node: ASTVariableDeclaration):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        TypeNodeName = str(node.Type) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(TypeNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), TypeNodeName))

        LRSquareNodeName = str(node.LRSquare) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(LRSquareNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), LRSquareNodeName))

        IDNodeName = str(node.ID) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(IDNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), IDNodeName))

        node.Initializer.accept(self)
        self.graph.add_edge(pydot.Edge(str(node), str(node.Initializer)))

        SEMICOLONNodeName = str(node.SEMICOLON) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(SEMICOLONNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), SEMICOLONNodeName))



    def visit_Terminal(self, node: ASTTerminal):
        self.graph.add_node(pydot.Node(str(node), style='filled',  fillcolor="#7CFC7C"))

        TerminalNodeName = str(node.Terminal) + " $" + str(self.UID.getID())
        self.graph.add_node(pydot.Node(TerminalNodeName, shape='octagon', style="filled", fillcolor="#F62020"))
        self.graph.add_edge(pydot.Edge(str(node), TerminalNodeName))