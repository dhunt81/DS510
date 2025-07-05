##################################
### Created: July 4, 2025
### Author: Devin Hunt
### DS510 Assignment 6 Part C
### Description: Using a stack, calculate a postfix expression value
### Inputs: Node, Stack
### Packages: none 
### Output: console output
### References: 
##################################

from Node import *
from Stack import *

if __name__ == "__main__":

    # define a set of valid operators
    operators = "+-*/"
    
    #Request the post fix expression from user and split it into each character
    postfix = input("Input a postfix expression: ").split()
    
    #create the stack
    postfixExp = Stack()

    #loop through all tokens in the string
    for token in postfix:
        #If token is not an operator then put on the stack
        if token not in operators:
            postfixExp.push(token)
        # if is an operator, build the function and evaluate it
        else:
            #top of stack is second operand
            op2 = postfixExp.top()
            #remove from stack
            postfixExp.pop()
            #next character is first operand
            op1 = postfixExp.top()
            #remove from stack
            postfixExp.pop()
            #create the expression and evaluate it to return
            expression = f"{op1} {token} {op2}"
            result = eval(expression)
            #add result to the top of the stack
            postfixExp.push(result)
            
    print(postfixExp.top())


''' tests
>>> %run "c:\\Users\\devin\\OneDrive\\Documents\\positron\\DS510\\Assignment 6\\Assignment 6C - Hunt.py"
Input a postfix expression: 
4 5 7 2 + - *
-16
>>> %run "c:\\Users\\devin\\OneDrive\\Documents\\positron\\DS510\\Assignment 6\\Assignment 6C - Hunt.py"
Input a postfix expression: 
3 4 + 2 * 7 /
2.0
>>> %run "c:\\Users\\devin\\OneDrive\\Documents\\positron\\DS510\\Assignment 6\\Assignment 6C - Hunt.py"
Input a postfix expression: 
5 7 + 6 2 - *
48
>>> %run "c:\\Users\\devin\\OneDrive\\Documents\\positron\\DS510\\Assignment 6\\Assignment 6C - Hunt.py"
Input a postfix expression: 
4 2 + 3 5 1 - * +
18
>>>
'''