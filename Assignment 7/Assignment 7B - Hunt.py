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
punctuation characters called, string.punctuation.

Next, write a recursive function which returns the string in reversed order.

Then, reverse the order of the characters in the string "un-recursively," by using Python's 
functionality to "slice" and iterate thru strings,  We covered this in the "String Notes," 
but as a reminder, in slicing a string, there are three parameters: [ start : stop : increment ].  
Using a negative increment would start at the end of the string.

Finally, compare these two reversed strings to confirm the recursion is correct.
"""

import string

#Function to take an input string and recursively reverse it
def reverseStr(instr):
    if len(instr) == 1:
        #when the last letter is reached just output the string
        return instr
    else:
        #take the 1 to n values and append the first letter to the end.
        #input the shortened string as the new string and call function again
        return reverseStr(instr[1:]) + instr[0]


# Get input string from user
def getStrToReverse():
    #get string from user
    inputStr = input("Enter a string to reverse: ")
    print ("Original String: {}".format(inputStr))

    rawWords = inputStr.lower()

    # Use default punctions from string.punctuation
    removeChar = string.punctuation
    # Remove punctuation from the words as noted above. This is done by ignoring punctuation using the translate function
    table = str.maketrans('', '', removeChar)
    strippedWords = rawWords.translate(table).replace(' ', '')

    print("Cleaned string: {}".format(strippedWords))

    #call function to reverse string
    recursiveRev = reverseStr(strippedWords)
    # reverse using slices
    funcRev = strippedWords[::-1]
    # reverses match?
    revMatch = recursiveRev == funcRev

    print ("Recursively Reversed: {}".format(recursiveRev))
    print ("Slices Reversed: {}".format(funcRev))
    print ("Reverse Methods Match? {}".format(revMatch))


if __name__ == "__main__":
    getStrToReverse()


""" Testing

Enter a string to reverse: 
Clean this string? and Reverses it!?!
Original String: Clean this string? and Reverses it!?!
Cleaned string: cleanthisstringandreversesit
Recursively Reversed: tisesreverdnagnirtssihtnaelc
Slices Reversed: tisesreverdnagnirtssihtnaelc
Reverse Methods Match? True

Enter a string to reverse: 
Shouldn't this be te#stED? Better?
Original String: Shouldn't this be te#stED? Better?
Cleaned string: shouldntthisbetestedbetter
Recursively Reversed: rettebdetsetebsihttndluohs
Slices Reversed: rettebdetsetebsihttndluohs
Reverse Methods Match? True
>>>

"""