##################################
### Created: July 22, 2025
### Author: Devin Hunt
### DS510 Assignment 7 Part C
### Description: Uses a recurssive function to implement prefix multiplication
### Inputs: User input of a string
### Packages: none
### Output: console output
### References: start code provided by Dr. Kruse and Dr. Rhodes
##################################

if __name__ == "__main__":

    expression = []    # expression is defined as a global variable
    i = 0

    # Get expression from user
    inExp = input("Input a Prefix expression, with all tokens separated by spaces: ")
    #split expression into tokens
    expression = inExp.split()

    def result():
        # get the first/next token from the expression, a string. 
        global i
        token = expression[i]
        i += 1

        # next, check if token is not an operator
        if token not in ('+', '-', '*', '/'):
            return float(token) # not an operator, so it must be a numeric value

        a = result()  # find the first operand
        b = result()  # find the second operand
        if token == '+':
            return a+b
        elif token == '-':
            return a-b
        elif token == '*':
            return a*b
        else:
            return a/b

    prefix = result()
    print (prefix)


""" Testing

>>> %run "/Users/devinhunt/Documents/Positron Repositories/DS510/Assignment 7/Assignment 7C - Hunt.py"
Input a Prefix expression, with all tokens separated by spaces: 
+ 2 3
5.0
>>> %run "/Users/devinhunt/Documents/Positron Repositories/DS510/Assignment 7/Assignment 7C - Hunt.py"
Input a Prefix expression, with all tokens separated by spaces: 
/ + 4 5 * 2 3
1.5
>>> %run "/Users/devinhunt/Documents/Positron Repositories/DS510/Assignment 7/Assignment 7C - Hunt.py"
Input a Prefix expression, with all tokens separated by spaces: 
* + 2 3 - + 7 8 / 6 2
60.0
>>>
 """