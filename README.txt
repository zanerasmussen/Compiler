This project only entails the lexer as of right now. I am using Python. 

To run the lexer, go to the file directory in a terminal and run 'python3 main.py'
You can pass it a parameter of different files or you can not pass a file and it will run the default data.txt




symantics needs to handle invalid assignement. such as 3 = 5 of function f = function g.



Questions for passoff:
1) function calls???
2) .id has to be dataMEmber or mehtod?
3) what is f().a? 
4) how can you have f = g (both functions functions are 2nd class)




can only call constructor with NEW (Syntax)
    1) default initaialize
    2) sytntax initaialize
    3) constructor code


Lexer Testing:
    1) [] [ ] [//comment] LRSquare
    2) [ int/ char/ ]   '['  and ']'
    3) testing for strings
    4) add testing for all possible chars (allChar.kxi)

Things for Assembler:
    No overwritting checking
    Lables with invalid signatures?
    Heap Testing
    //when doing sl,sb,etc see if in valid range. then throw an error. 
    //make sure heap and sl don't overlap. 



look at offset on symbol tables. 



limitations:
    only one constructor. Can be constructor with parameters. No constructor overloading
    removed block level scoping for ease of use
    variables are static. (public int pub can not be accessed in main without an object)
    C++ style of methods/dataMembers. Have to be declared before using them (forward declaring)
    didn't check for array size and if out of bounds
    




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

check when initialized