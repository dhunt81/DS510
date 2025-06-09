################################
### Author: Devin Hunt
### Created: June 8, 2025
### DS510 Assignment 2 Part B
### Description: This program takes date parts from user and outputs a word version of the date.
### Inputs: day = numeric day from 1 to 31
###         month = numeric month from 1 to 12
###         year = numeric year
### Output: date formatted in Month Day, Year format
##################################

### Ask user for inputs as noted above

# create function that takes in an int between 1 and 12 and outputs the month in text
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

# main function
def main():
    # initialize variable to continue while loop
    noEnd = True

    #while loop so long as noEnd is True
    while noEnd:
        #prompt user for inputs
        mon = int(input("Enter a Month, numeric, 1-12: "))
        day = int(input("Enter a Day, numeric, 1-31: "))
        year = int(input("Enter a year, numeric, 1583 or after: "))

        # call function and store output 
        month = MonthName(mon)
        
        # create formatted date 
        dateFmt = "{0} {1}, {2}".format(month, day, year)

        # output date entered and formatted date
        print("You entered: {0}/{1}/{2}".format(mon, day, year))
        print("Which is: {0}".format(dateFmt))

        # ask user if they want to continue
        cont = input("Would you like to enter another date? (y/N): ")

        # check is lowercase y is entered. if so continue, if anything else then stop
        noEnd = cont.lower() == "y"

#run main function
main()  

""" Test runs

>>> %run "c:\\Users\\devin\\OneDrive\\Documents\\positron\\DS510\\Assignment 2\\Assignment 2B - Hunt.py"
Enter a Month, numeric, 1-12: 11
Enter a Day, numeric, 1-31: 04
Enter a year, numeric, 1583 or after: 1981
You entered: 11/4/1981
Which is: November 4, 1981
Would you like to enter another date? (y/N): y
Enter a Month, numeric, 1-12: 09
Enter a Day, numeric, 1-31: 10
Enter a year, numeric, 1583 or after: 1978
You entered: 9/10/1978
Which is: September 10, 1978
Would you like to enter another date? (y/N): n
>>>

"""