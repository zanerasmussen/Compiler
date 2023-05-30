This project only entails the lexer as of right now. I am using Python. 

To run the lexer, go to the file directory in a terminal and run 'python3 main.py'
You can pass it a parameter of different files or you can not pass a file and it will run the default data.txt


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

limitations:
    only one constructor. Can be constructor with parameters. No constructor overloading
    removed block level scoping for ease of use
    variables are static. (public int pub can not be accessed in main without an object)
    C++ style of methods/dataMembers. Have to be declared before using them (forward declaring)
    didn't check for array size and if out of bounds
    cant do string1 == "test";
    --++-i1;


desguaring
    write all visitor i believe i will need
    go from bottom to top (suggestion) inside to outside, smallest to largest
    fallthourgh for swithc statments (no case found)
    comment on new design submition

    
