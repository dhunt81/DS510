################################
### Author: Devin Hunt
### Created: June 15, 2025
### DS510 Assignment 3 Part B
### Description: This program creates a subclass BDate of Date class
### Inputs: M = month as a number
###         D = day as a number
###         Y = year as a number
### Output: text with the converted date and next holiday
##################################

""" Assignment text
(1) utilize the super in the function __init__
(2) utilize the super in the function __str__ so it still outputs the date in the form Month Day (numeric), 
    Year (numeric) as the default string output.
(3) define a new instance string variable birthday that holds just the Month day string without the year, 
    but add the string "st" or "nd" or "rd" or "th" if the day ends in 1, 2, 3 or otherwise. 
(4) define a funtion bday() that returns the birthday string (this type of function is sometimes called a 'getter') 
    So  b=BDate(3,22,2024) followed by a print(b.bday()) would output "March 22nd"
(5) define a second function yrdays() that returns the numeric day of the year for the birthday. So  print(yrdays(b)) 
    would output 82 (Janurary has 31 days, Februrary has 29 days  and add 22 for March = 82).  
    Leap year just won't figure in since it depends on the current year, not the year of birth.
"""

from Date import *

class BDate(Date):

    def __init__ (self, M, D, Y):
        super().__init__(M, D, Y)

        # else if statement to add ordinal suffix to day value
        # get the last digit of int and check what it is
        if D % 10 == 1:
            dayord = str(D) + "st"
        elif D % 10 == 2:
            dayord = str(D) + "nd"
        elif D % 10 == 3:
            dayord = str(D) + "rd"
        else:
            dayord = str(D) + "th"

        self.birthday = str(self.mon + " " + dayord )
        

    def bday(self):
        return self.birthday

    def yrdays(self):
        #define array with maximum number of days in each month
        maxDayMonth = [31,29,31,30,31,30,31,31,30,31,30,31]
        #define variable that sums prior month day and adds in current month day count
        self.dayOfYearSum = sum(maxDayMonth[:self.M-1]) + self.D

        return self.dayOfYearSum

    def __str__(self):
        return super().__str__()