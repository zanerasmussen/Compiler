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


#Test for Parameter [ ] and Paramter [//comment]
#and test for paramter [
#    //comment
#]



limitations:
    only one constructor. Can be constructor with parameters. No constructor overloading
    removed block level scoping for ease of use
    class can have a DataMember of Another type without being initialized. Error will happen at run time. No way to verify if DataMember is initialized. 

Visitors for Semantics:
    1) SymbolTableVisitor: 
            visits all 'id' and creates a symbol for them. This checks for duplicated/reinitialized variables. 
            This also checks for objects 'id'
            Checks for methods/dataMembers of the same name
            Ensures constructors has the same name of class
            Checks duplicated class Names
            Checks for multiple constructors
            Symbol includes 'isInitialized' to help with future usage of variables. 
    
    2)UndeclaredVarVistitor: 
            Ensures there are no calls to uninitialized variables. 
            

            Makes a new table for parameters and what is needed


    3)ObjectInitializerAndTypeVisitor:
            Anytime VariableDeclaration is called for an object, it checks to make sure object is initiaed properly (excluding parameters)
            Ensures all uses of 'Type' that aren't of default type (int,void, char, etc) are an instance of a class that actually exists. 

    5)DotParamVisitor:
            Checks to make sure all parameters are valid and all calls to that type are passing the correct type of parameters and the correct number. (constructor and methods)
            does index checking
            checks method and datamember calls. checks this statements and also <expression>.<identifier> expressions. 
            checks for private and public calls





Things to think about:
    Are the following cin operations allowed in kxi?
        int arr = new int[1]; 
        cin >> arr[0];
        cin >> arr;
    
    Additionally if we were to instantiate an array with new int[expr], am I correct an assuming we don't need to check if expr is a negative number since that could only be checked during run time?

    