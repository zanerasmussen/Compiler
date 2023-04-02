This project only entails the lexer as of right now. I am using Python. 

To run the lexer, go to the file directory in a terminal and run 'python3 main.py'
You can pass it a parameter of different files or you can not pass a file and it will run the default data.txt

Things to add:
    add -l to command line
    finish test cases
Lexer Branch
python3 -m PyInstaller -F ./main.py

Lexer Branch
python3 -m PyInstaller -F ./main.py


Suggestions:
read fron standard in instead of default file
line 74 should faile because of the new line token. unit test for ath. 


Look into MAIN AS A TOKEN!!!
    My solution for this is to, when parsing a CompilationUnit, match an Identifier 
    for the function name, and then if that Identifier is not equivalent to "main" then I throw an error. 

symantics needs to handle  invalid assignement. such as 3 = 5 of function f = function g.

add error for each grammar rule

write test case for:
[
    //I mewss with 
    //people
]
Questions:

 Kenton Renshaw
    I am super confused with how the visitor pattern should be structured. Obviously there are different implementations but I
    think there is a specific implementation we're looking for in this class. A classmate and I compared notes and they differ 
    so I was wondering if someone could clear it up once and for all? For instance, where should node.accept() and visitor.visit() be called?
Jarrett Minton
    node.accept() should be called inside the parent node's accept method. visitor.visit() should be called in the nodes
     own accept method. the parent accept method calls accept on all the children node, then calls visitor.visit on itself 
     (its also possible to call visit before accepts). the accept methods should do all the transversing of the tree. you can do it 
     other ways, but I talked to Dr. Aldous about this and thats how he explained it to me. 

Big Questions:
    1) Am i doing the visitor pattern right?   
        a) what is the visitor pattern?
    2)Symbol Table?
    3) shift/reduce errors?
    4) repeat class?
    5) syntax ideas:
        a) repeat what i am doing but check for 








have subclasses of each type ie : non terminal have nodes

i am doing a linked list. that will be expensive later
I need to do blocks. Have 


shift reduce is most likely caused because of explicit recurssion