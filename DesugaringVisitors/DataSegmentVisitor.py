from AbstractVisitor import ASTVisitor
from SupportFiles.theLexer import theLexerTester
from AST import *

class DataSegmentVisitor(ASTVisitor):
    def __init__(self):
        self.dataSeg = []
        self.TerminalID = []
        self.counter = 0

        #visitor specific
        self.symbolTable = {}
        self.theClass = "main"

    def pre_visit_ClassDefinition(self, node: ASTClassDefinition):
        self.theClass = str(node.ID)
    
    def post_visit_ClassDefinition(self, node: ASTClassDefinition):
        self.theClass = "main"

    def pre_visit_CompilationUnit(self, node: ASTCompilationUnit):
        scope = "main"
        for x in range(len(self.symbolTable)):
            for key, value in self.symbolTable[x].items():
                inClass = False
                if key[1] == 'class':
                    scope = key[0]
                    inClass = True
                if inClass == False:
                    symbol = value['symbol']
                    if key[1] == "variable":
                        if symbol.Type == 'int' or symbol.Type == 'true' or symbol.Type == 'false':
                            param1 = f"&{scope}_{key[0]}"
                            param2 = ".INT" 
                            self.dataSeg.append(f"{param1:<15} {param2:<15}")
                            self.dataSeg.extend([";"])
                            self.TerminalID.append((f"&{scope}_{key[0]}", key[0]))
                            
                        elif symbol.Type == 'char':
                            param1 = f"&{scope}_{key[0]}"
                            param2 = ".BYT" 
                            self.dataSeg.append(f"{param1:<15} {param2:<15}")
                            self.dataSeg.extend([";"])
                            self.TerminalID.append((f"&{scope}_{key[0]}", key[0]))

                        elif symbol.Type == 'bool':
                            param1 = f"&{scope}_{key[0]}"
                            param2 = ".INT" 
                            self.dataSeg.append(f"{param1:<15} {param2:<15}")
                            self.TerminalID.append((f"&{scope}_{key[0]}", key[0]))

                        elif symbol.Type == "string":
                            param1 = f"%{scope}_{key[0]}"
                            param2 = ".INT" 
                            self.dataSeg.append(f"{param1:<15} {param2:<15}")
                            self.dataSeg.extend([";"])
                            self.TerminalID.append((f"%{scope}_{key[0]}", key[0]))
                        else:
                            #could be array or object.
                            pass

    def pre_visit_VariableDeclaration(self, node: ASTVariableDeclaration):
        myVar = f"&{self.theClass}_{node.ID}"
        for x in self.TerminalID:
            if myVar == x[0] and node.ID == x[1]:
                node.ID = myVar
        myVar = f"%{self.theClass}_{node.ID}"
        for x in self.TerminalID:
            if myVar == x[0] and node.ID == x[1]:
                node.ID = myVar

    def post_visit_Terminal(self, node: ASTTerminal):
        tokType = theLexerTester(str(node.Terminal))
        varType = tokType.type
        if varType == "STRING":
            exist = False
            for x in self.TerminalID:
                if x[1] == node.Terminal:
                    exist = True
                    node.Terminal = x[0]
            if exist == False:      
                self.TerminalID.append((f"${self.counter}", node.Terminal)) 
                length = len(node.Terminal)-2
                param1 = f"${self.counter}"
                param2 = ".BYT"
                param3 = f"'{node.Terminal[1]}'"
                self.dataSeg.append(f"{param1:<15} {param2:<15} {param3:<15}")
                for letter in range(2, length+1):
                    param1 = " "
                    param2 = ".BYT"
                    param3 = f"'{node.Terminal[letter]}'" 
                    self.dataSeg.append(f"{param1:<15} {param2:<15} {param3:<15}")
                param1 = " "
                param2 = ".BYT"
                self.dataSeg.append(f"{param1:<15} {param2:<15}")
                self.dataSeg.extend([";"])
                node.Terminal = f"${self.counter}"
                self.counter += 1

        elif varType == "ID":
            myVar = f"&{self.theClass}_{node.Terminal}"
            for x in self.TerminalID:
                if myVar == x[0] and node.Terminal == x[1]:
                    node.Terminal = myVar
            myVar = f"%{self.theClass}_{node.Terminal}"
            for x in self.TerminalID:
                if myVar == x[0] and node.Terminal == x[1]:
                    node.Terminal = myVar

        elif varType == "INT":
            exist = False
            for x in self.TerminalID:
                if x[1] == node.Terminal:
                    exist = True
                    node.Terminal = x[0]
            if exist == False:
                self.TerminalID.append((f"${self.counter}", node.Terminal))
                param1 = f"${self.counter}"
                param2 = ".INT"
                param3 = f"#{node.Terminal}" 
                self.dataSeg.append(f"{param1:<15} {param2:<15} {param3:<15}")
                self.dataSeg.extend([";"])
                node.Terminal = f"${self.counter}"
                self.counter += 1

        elif varType == "TRUE" :
            exist = False
            for x in self.TerminalID:
                if x[1] == node.Terminal:
                    exist = True
                    node.Terminal = x[0]
            if exist == False:
                self.TerminalID.append(("#True", node.Terminal))
                param1 = "#True"
                param2 = ".INT"
                param3 = "#1" 
                self.dataSeg.append(f"{param1:<15} {param2:<15} {param3:<15}")
                self.dataSeg.extend([";"])
                node.Terminal = "#True"
                self.counter += 1

        elif varType == "FALSE":
            exist = False
            for x in self.TerminalID:
                if x[1] == node.Terminal:
                    exist = True
                    node.Terminal = x[0]
            if exist == False:
                self.TerminalID.append(("#False", node.Terminal))
                param1 = "#False"
                param2 = ".INT"
                param3 = "#0" 
                self.dataSeg.append(f"{param1:<15} {param2:<15} {param3:<15}")
                self.dataSeg.extend([";"])
                node.Terminal = "#False"
                self.counter += 1

        elif varType == "CHAR":
            exist = False
            for x in self.TerminalID:
                if x[1] == node.Terminal:
                    exist = True
                    node.Terminal = x[0]
            if exist == False:
                self.TerminalID.append((f"${self.counter}", node.Terminal))
                param1 = f"${self.counter}"
                param2 = ".BYT"
                param3 = f"{node.Terminal}" 
                self.dataSeg.append(f"{param1:<15} {param2:<15} {param3:<15}")
                self.dataSeg.extend([";"])
                node.Terminal = f"${self.counter}"
                self.counter += 1

        
                