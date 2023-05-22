from abc import ABCMeta, abstractmethod
from AbstractVisitor import ASTVisitor
from SupportFiles.theLexer import theLexerTester
from AST import *
    
class BreakVisitor(ASTVisitor):
    def __init__(self):
        self.errors = []
        self.inSwitchOrWhile = False
        self.wasOn = False

    def pre_visit_StatementBreak(self, node: ASTStatementBreak):
        if self.inSwitchOrWhile == False:
            self.errors.append(f"Error: Attempting to break while not in a switch or while loop. Around line {node.lineno}")

    def post_visit_StatementBreak(self, node: ASTStatementBreak):
        pass    

    def pre_visit_StatementSwitch(self, node: ASTStatementSwitch):
        self.inSwitchOrWhile = True

    def post_visit_StatementSwitch(self, node: ASTStatementSwitch):
        self.inSwitchOrWhile = False

    def pre_visit_StatementWhile(self, node: ASTStatementWhile):
        self.inSwitchOrWhile = True

    def post_visit_StatementWhile(self, node: ASTStatementWhile):
        self.inSwitchOrWhile = False

    def pre_visit_StatementExpression(self, node: ASTStatementExpression):
        self.wasOn = self.inSwitchOrWhile
        self.inSwitchOrWhile = False

    def post_visit_StatementExpression(self, node: ASTStatementExpression):
        self.inSwitchOrWhile = self.wasOn
        self.wasOn = False

    def pre_visit_StatementIF(self, node: ASTStatementIF):
        self.wasOn = self.inSwitchOrWhile
        self.inSwitchOrWhile = False

    def post_visit_StatementIF(self, node: ASTStatementIF):
        self.inSwitchOrWhile = self.wasOn
        self.wasOn = False

    def pre_visit_StatementIFELSE(self, node: ASTStatementIFELSE):
        self.wasOn = self.inSwitchOrWhile
        self.inSwitchOrWhile = False

    def post_visit_StatementIFELSE(self, node: ASTStatementIFELSE):
        self.inSwitchOrWhile = self.wasOn
        self.wasOn = False

