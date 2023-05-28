This project only entails the lexer as of right now. I am using Python. 

To run the lexer, go to the file directory in a terminal and run 'python3 main.py'
You can pass it a parameter of different files or you can not pass a file and it will run the default data.txt


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
    no index checking for arrays
    




things to check for in semantics:
        calling methods and datamembers inside a classhods)



    2nd class function calls
    check for illegal calls such as f = g
    using DataMembers, constructors, methods, and classes as variabls.


    <= and >= need to compare ints and char (separate)



desguaring
    write all visitor i believe i will need
    go from bottom to top (suggestion) inside to outside, smallest to largest
    fallthourgh for swithc statments (no case found)
    comment on new design submition


calander for peter (20-40 hours) and with a check in points with professor. check in. 


 
Check to make sure 'return' is found in method



 add breaks if error is found between steps. 