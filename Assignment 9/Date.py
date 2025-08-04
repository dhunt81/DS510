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

# Function to convert from day month to text month
def MonthName(mon):
    if mon == 1:
        month = "January"
    elif mon == 2:
        month = "February"
    elif mon == 3:
        month = "March"
    elif mon == 4:
        month = "April"
    elif mon == 5:
        month = "May"
    elif mon == 6:
        month = "June"
    elif mon == 7:
        month = "July"
    elif mon == 8:
        month = "August"
    elif mon == 9:
        month = "September"
    elif mon == 10:
        month = "October"
    elif mon == 11:
        month = "November"
    elif mon == 12:
        month = "December"
    
    return(month)

#create the Date class, with inputs of M, D, Y
class Date:

    #initialize the date class
    def __init__ (self, M, D, Y):
        self.mon = MonthName(M) #Convert M to text month with the function above
        self.M = M
        self.D = D
        self.Y = Y
        
    #default return string of class
    def __str__(self):
        return "{0} {1}, {2}".format(self.mon, str(self.D), str(self.Y))

