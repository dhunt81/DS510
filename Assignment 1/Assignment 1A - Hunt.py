"""
DS510 Assignment 1 - Part A
Author: Devin Hunt
Created: May 29, 2025
Description: Prompt user for temperature in F and prints conversion to C
"""

"""
Assignment text:
Program A
Write a Python program which prompts for an input temperature, in degrees Fahrenheit, 
and outputs the temperature in degrees Celsius. Be sure your prompt doesn't presume
the user knows what to input, and your output is to two decimals, clearly explained 
and formatted. Reminder the formula is C = 5/9(F-32).  
Do not hard code the input into your program.  Use the input() function.
"""



# Prompt user to enter temperature in F, 
### Assume proper input that can be converted to float
tempF = input("Enter a temperature in degrees Fahrenheit: ")

#Convert to C and round to two decimals
tempC = 5/9*(float(tempF)-32)
outputText = "Your temperature of {0} Fahrenheit equals {1} Celsius.".format(tempF, "{0:.2f}".format(tempC))

#print out converted degrees
print(outputText)





""" Console output testing
>>> %run "c:\\Users\\devin\\OneDrive\\Documents\\positron\\DS510\\Assignment 1\\Assignment 1 - Hunt.py"
Enter a temperature in degrees Fahrenheit: 
32.0
Your temperature of 32.0 Fahrenheit equals 0.00 Celsius.
>>> %run "c:\\Users\\devin\\OneDrive\\Documents\\positron\\DS510\\Assignment 1\\Assignment 1 - Hunt.py"
Enter a temperature in degrees Fahrenheit: 
32
Your temperature of 32 Fahrenheit equals 0.00 Celsius.
>>> %run "c:\\Users\\devin\\OneDrive\\Documents\\positron\\DS510\\Assignment 1\\Assignment 1 - Hunt.py"
Enter a temperature in degrees Fahrenheit: 
-40
Your temperature of -40 Fahrenheit equals -40.00 Celsius.
>>> %run "c:\\Users\\devin\\OneDrive\\Documents\\positron\\DS510\\Assignment 1\\Assignment 1 - Hunt.py"
Enter a temperature in degrees Fahrenheit: 
212
Your temperature of 212 Fahrenheit equals 100.00 Celsius.
>>> %run "c:\\Users\\devin\\OneDrive\\Documents\\positron\\DS510\\Assignment 1\\Assignment 1 - Hunt.py"
Enter a temperature in degrees Fahrenheit: 
52.66
Your temperature of 52.66 Fahrenheit equals 11.48 Celsius.
>>>
"""