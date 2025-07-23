##################################
### Created: July 22, 2025
### Author: Devin Hunt
### DS510 Assignment 7 Part D
### Description: Uses a recurssive function to implement prefix multiplication from Part C, but
###              Part D implements exception handling
### Inputs: User input of a string
### Packages: sys
### Output: console output
### References: start code provided by Dr. Kruse and Dr. Rhodes
##################################
import sys

if __name__ == "__main__":

    expression = []    # expression is defined as a global variable
    i = 0              # counter to parse expression

    # Get expression from user
    inExp = input("Input a Prefix expression, with all tokens separated by spaces: ")
    #split expression into tokens
    expression = inExp.split()

    def result():
        # get the first/next token from the expression, a string. 
        global i, expression
        token = expression[i]
        i += 1

        # check if a valid operator and number. Otherwise raise exceptions
        if token not in ('+', '-', '*', '/'):
            try:
                float(token)
            except ValueError:
                print("{} is not a valid number or operator.".format(token))
                sys.exit()
        
        # next, check if token is not an operator
        if token not in ('+', '-', '*', '/'):
            #check if the numbers/operators are valid, if not throw an exception
            num = float(token)
            return num # not an operator, so it must be a numeric value

        a = result()  # find the first operand
        b = result()  # find the second operand

        if token == '+':
            return a+b
        elif token == '-':
            return a-b
        elif token == '*':
            return a*b
        else:
            try:
                return a/b
            except ZeroDivisionError:
                print("Division by 0 not allowed.")
                sys.exit()

    try:
        prefix = result()
        print (prefix)
    except IndexError:
        print ("Expression is too short. Try Again")
        sys.exit()




""" Testing
>>> %run "/Users/devinhunt/Documents/Positron Repositories/DS510/Assignment 7/Assignment 7D - Hunt.py"
Input a Prefix expression, with all tokens separated by spaces: 
** 2 3
** is not a valid number or operator.
>>> %run "/Users/devinhunt/Documents/Positron Repositories/DS510/Assignment 7/Assignment 7D - Hunt.py"
Input a Prefix expression, with all tokens separated by spaces: 
* 2 3
6.0
>>> %run "/Users/devinhunt/Documents/Positron Repositories/DS510/Assignment 7/Assignment 7D - Hunt.py"
Input a Prefix expression, with all tokens separated by spaces: 
* 2e 4
2e is not a valid number or operator.
>>> %run "/Users/devinhunt/Documents/Positron Repositories/DS510/Assignment 7/Assignment 7D - Hunt.py"
Input a Prefix expression, with all tokens separated by spaces: 
+ + 1 3 
Expression is too short. Try Again
>>> %run "/Users/devinhunt/Documents/Positron Repositories/DS510/Assignment 7/Assignment 7D - Hunt.py"
Input a Prefix expression, with all tokens separated by spaces: 
+ + 1 3 5
9.0
>>> %run "/Users/devinhunt/Documents/Positron Repositories/DS510/Assignment 7/Assignment 7D - Hunt.py"
Input a Prefix expression, with all tokens separated by spaces: 
/ 2 0
Division by 0 not allowed.
>>> %run "/Users/devinhunt/Documents/Positron Repositories/DS510/Assignment 7/Assignment 7D - Hunt.py"
Input a Prefix expression, with all tokens separated by spaces: 
/ 2 1
2.0

 """