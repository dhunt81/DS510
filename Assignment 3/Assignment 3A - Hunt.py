################################
### Author: Devin Hunt
### Created: June 15, 2025
### DS510 Assignment 3 Part A
### Description: This program creates the Date class
### Inputs: M = month as a number
###         D = day as a number
###         Y = year as a number
### Output: text with the converted date and next holiday
##################################

#Import date class definition
from Date import *

#create main function with test outputs
if __name__ == "__main__":
     today = Date(6,7,2025)
     print("Today is ",today)
     jfourth = Date(7,4,2025)
     print("The next holiday is ",jfourth)
     memorialday = Date(5,26, 2025)
     print("We just celebrated memorial day on ", memorialday)



""" Sample test output as requested

Today is  June 7, 2025
The next holiday is  July 4, 2025
We just celebrated memorial day on  May 26, 2025

"""