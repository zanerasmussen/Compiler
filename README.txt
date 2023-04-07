This project only entails the lexer as of right now. I am using Python. 

To run the lexer, go to the file directory in a terminal and run 'python3 main.py'
You can pass it a parameter of different files or you can not pass a file and it will run the default data.txt

Things to add:
    finish test cases
Lexer Branch
python3 -m PyInstaller -F ./main.py

Lexer Branch
python3 -m PyInstaller -F ./main.py


Suggestions:
read fron standard in instead of default file
line 74 should faile because of the new line token. unit test for ath. 


symantics needs to handle  invalid assignement. such as 3 = 5 of function f = function g.

add error for each grammar rule

write test case for:
"""
[
    //I mewss with 
    //people
]
"""

Big Questions:

    2)Symbol Table?
    3) shift/reduce errors?
    4) repeat class?


I need to do blocks. Have 


check for \n in tokens python main -l \n


Questions for Caiden:
1) shift/reduce conflicts
    -Key an eye on it. If there are big issues come back to this. Cross my fingers it is done. 
2) help with Assembler Heap
3) sematntics help


Questions for passoff:
1) how does command line accept more than one line?
2) shift reduce errors
3) unknown token?
4) symbol table?? (1st thing built)



can only call constructor with NEW (Syntax)
    1) default initaialize
    2) sytntax initaialize
    3) constructor code




    else in precendece. ply dangling else. do this over that
    token for [] [ ] [//comment]
    for [ int/ char/ ]