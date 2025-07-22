##################################
### Created: July 22, 2025
### Author: Devin Hunt
### DS510 Assignment 7 Part B
### Description: Uses a recurssive function to reverse a string and compare using python functions
### Inputs: User input of a string
### Packages: string
### Output: console output
### References: 
##################################

""" Assignment Text
Objective: Implement a simple recursive function.  There is no explicit loop in a recursive solution.

Write a Python program which reverses the characters in a string.

First, you should modify the input string so that ALL punctuation and spaces are removed.  
Remember that we did something similar in Assignment 05 , where  we removed unwanted punctuation. 
Recall that Python's string module (you'll need to import string) has string of all the standard 
punctuation characters called, string.punctuation .

Next, write a recursive function which returns the string in reversed order.

Then, reverse the order of the characters in the string "un-recursively," by using Python's 
functionality to "slice" and iterate thru strings,  We covered this in the "String Notes," 
but as a reminder, in slicing a string, there are three parameters: [ start : stop : increment ].  
Using a negative increment would start at the end of the string.

Finally, compare these two reversed strings to confirm the recursion is correct.
"""

# Get input string from user
inputStr = "This is a test input string.   All punctuation should've been removed!  Ok? Oh, and All White-spaces, too!  "

# Use default punctions from string.punctuation and remove ' and - from the list
removeChar = string.punctuation.replace("'", '').replace("-", "")

