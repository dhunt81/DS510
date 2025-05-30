"""
DS510 Assignment 1 - Part B
Author: Devin Hunt
Created: May 29, 2025
Description: Prompt user for input string and then change capitalization on it.
"""
""" Assignment Text
Write a Python script which prompts for input (at least three letters) from the user, and then outputs that input as:
(1) all upper case
(2) all lower case
(3) all upper case, except the first and last characters are lower case
Use the available stringn functions and accessing the first character with the 0 index and the last with an appropriate negative index!
"""

#Prompt user for input string
text = input("Enter a string of at least 3 characters: ")

#create variables to upcase, lower case, and uppercase all but first and last letter
textUpper = text.upper()
textLower = text.lower()
textCamel = text[0].lower() + text[1:-1].upper() + text[-1].lower()

#print outputs
print(textUpper)
print(textLower)
print(textCamel)



""" Console Output of Testing
>>> %run "c:\\Users\\devin\\OneDrive\\Documents\\positron\\DS510\\Assignment 1\\Assignment 1B - Hunt.py"
Enter a string of at least 3 characters: 
Test CaseS
TEST CASES
test cases
tEST CASEs
>>> %run "c:\\Users\\devin\\OneDrive\\Documents\\positron\\DS510\\Assignment 1\\Assignment 1B - Hunt.py"
Enter a string of at least 3 characters: 
JuniAta COLLEGe
JUNIATA COLLEGE
juniata college
jUNIATA COLLEGe
>>> %run "c:\\Users\\devin\\OneDrive\\Documents\\positron\\DS510\\Assignment 1\\Assignment 1B - Hunt.py"
Enter a string of at least 3 characters: 
What else can I TYPE?
WHAT ELSE CAN I TYPE?
what else can i type?
wHAT ELSE CAN I TYPE?
>>> %run "c:\\Users\\devin\\OneDrive\\Documents\\positron\\DS510\\Assignment 1\\Assignment 1B - Hunt.py"
Enter a string of at least 3 characters: 
THIS IS GREAT
THIS IS GREAT
this is great
tHIS IS GREAt
"""