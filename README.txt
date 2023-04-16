This project only entails the lexer as of right now. I am using Python. 

To run the lexer, go to the file directory in a terminal and run 'python3 main.py'
You can pass it a parameter of different files or you can not pass a file and it will run the default data.txt

Things to add:
    finish test cases
Lexer Branch
python3 -m PyInstaller -F ./main.py


symantics needs to handle  invalid assignement. such as 3 = 5 of function f = function g.


Big Questions:
    1) repeat class




Questions for Caiden:



Questions for passoff:
1) unknown token?



can only call constructor with NEW (Syntax)
    1) default initaialize
    2) sytntax initaialize
    3) constructor code



    token for [] [ ] [//comment]
    for [ int/ char/ ]

add testing for LRSquare
do a lot of testing for STRINGS

test chars tokens
    add char testing  to automation (allChar.kxi)
test string tokens

Things for Assembler:
    No overwritting checking
    Lables with invalid signatures?
    Heap Testing
    //when doing sl,sb,etc see if in valid range. then throw an error. 
//make sure heap and sl don't overlap. 



look at offset on symbol tables. 

test DOTprinter with pre/post visit

    def get_from_symbol_table(self, name):
        for symbol_table in reversed(self.symbol_tables):
            if name in symbol_table:
                return symbol_table[name]
        return None
    
    def push_symbol_table(self):
        self.symbol_tables.append({})
    
    def pop_symbol_table(self):
        self.symbol_tables.pop()