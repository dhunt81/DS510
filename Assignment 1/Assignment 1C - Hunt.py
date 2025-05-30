"""
DS510 Assignment 1 - Part C
Author: Devin Hunt
Created: May 29, 2025
Description: Prompt user for input string and then adds $ to all characters matching first letter.
"""
""" Assignment Text
Write a Python program which prompts for an input string, and outputs a new string where all occurrences 
of its first char have been replaced by '$', except the first char itself.
"""

#Prompt user for input string
text = input("Enter a string: ")

# join the first character of string and remaining text after replacing that char with $
firstChar = text[0]
remainingString = text[1:].replace(firstChar, "$")
updatedString = firstChar + remainingString

#print the output
print(updatedString)


""" Console Output of Testing
>>> %run "c:\\Users\\devin\\OneDrive\\Documents\\positron\\DS510\\Assignment 1\\Assignment 1C - Hunt.py"
Enter a string: 
This is a tesT
This is a tes$
>>> %run "c:\\Users\\devin\\OneDrive\\Documents\\positron\\DS510\\Assignment 1\\Assignment 1C - Hunt.py"
Enter a string: 
this is a test
this is a $es$
>>> %run "c:\\Users\\devin\\OneDrive\\Documents\\positron\\DS510\\Assignment 1\\Assignment 1C - Hunt.py"
Enter a string: 
infinity times six
inf$n$ty t$mes s$x
>>>
"""