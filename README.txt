This project only entails the lexer as of right now. I am using Python. 

To run the lexer, go to the file directory in a terminal and run 'python3 main.py'
You can pass it a parameter of different files or you can not pass a file and it will run the default data.txt

Things to add:
    finish test cases
Lexer Branch
python3 -m PyInstaller -F ./main.py


symantics needs to handle  invalid assignement. such as 3 = 5 of function f = function g.



Questions for passoff:
1) function calls???
2) .id has to be dataMEmber or mehtod?
3) what is f().a? 
4) how can you have f = g (both functions functions are 2nd class)




3) summer? options?



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
    variables are static. (public int pub can not be accessed in main without an object)
    C++ style of methods/dataMembers. Have to be declared before using them (forward declaring)

Visitors for Semantics:
    1) SymbolTableVisitor: 
            visits all 'id' and creates a symbol for them. This checks for duplicated/reinitialized variables. 
            This also checks for objects 'id'
            Checks for methods/dataMembers of the same name
            Ensures constructors has the same name of class
            Checks duplicated class Names
            Checks for multiple constructors
            Symbol includes 'isInitialized' to help with future usage of variables. 
            create 'paramlist' for eash use for methods and constructors
    
    2)UndeclaredVarVistitor: 
            Ensures there are no calls to uninitialized variables. 
            This can not be used in function of main
            Ensures '.'ID is a method or dataMember
            checks to see if method/datamember that is private is trying to be accessed outside of class
            ensures any object is initialized before calling
            

    3)ObjectInitializerAndTypeVisitor:
            Anytime VariableDeclaration is called for an object, it checks to make sure object is initiaed properly (excluding parameters)
            Ensures all uses of 'Type' that aren't of default type (int,void, char, etc) are an instance of a class that actually exists. 

    


added case can only be int/char in symbol table
added checking for void
int[] a;
cout << a[2]; //error thrown for not initialized
int[] b = new int[5];
cout << b[8] //passes but failed at runtime.


Things to think about:
    Are the following cin operations allowed in kxi?
        int arr = new int[1]; 
        cin >> arr[0];
        cin >> arr;
    
    Additionally if we were to instantiate an array with new int[expr], am I correct an assuming we don't need to check if expr is a negative number since that could only be checked during run time?


things to check for in semantics:
    calling declared but not intialized variables
    number of and types of parameters passed when calling functions
        creating objects inside of a class
        calling methods and datamembers inside a class
    Checks to make sure all parameters are valid and all calls to that type are passing the correct type of parameters and the correct number. (constructor and methods)
    does index checking
    checks method and datamember calls. checks this statements and also <expression>.<identifier> expressions. j
    if method is of type void. 
        no return expression can be found


    2nd class function calls
    check for illegal calls such as f = g
    using DataMembers, constructors, methods, and classes as variabls.


    <= and >= need to compare ints and char (separate)