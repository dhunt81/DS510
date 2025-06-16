################################
### Author: Devin Hunt
### Created: June 15, 2025
### DS510 Assignment 3 Part B
### Description: This program runs examples of the Bdate class, building off Date class
### Inputs: day = numeric day from 1 to 31
###         month = numeric month from 1 to 12
###         year = numeric year
### Output: displays the birthday month and year with ordinal text
### Referenced forum page: https://stackoverflow.com/questions/24914412/python-how-to-get-first-5-or-last-5-from-list-of-10
##################################

from BDate import *

if __name__ == "__main__":
    today = Date(6,25,2020)
    print("Today is ",today)
    bd = BDate(3,22,2000)
    print("Date of birth is",bd)
    print("Birthday is",bd.bday())
    print("It is",bd.yrdays(),"days into the year")
    nye = BDate(12,31,2023)
    print("Someone born on New Year's eve:",nye) 
    print(nye.bday())
    print("It is",nye.yrdays(),"days into the year")
    JasonBday = BDate(9,10,1978)
    print("Jason\'s date of birth is", JasonBday)
    print("Jason\'s birthday is", JasonBday.bday())
    print("It is", JasonBday.yrdays(), "days into the year")





""" Output terminal
Today is  June 25, 2020
Date of birth is March 22, 2000
Birthday is March 22nd
It is 82 days into the year
Someone born on New Year's eve: December 31, 2023
December 31st
It is 366 days into the year
Jason's date of birth is September 10, 1978
Jason's birthday is September 10th
It is 254 days into the year

"""