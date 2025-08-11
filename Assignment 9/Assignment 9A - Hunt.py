##################################
### Created: August 3, 2025
### Author: Devin Hunt
### DS510 Assignment 9 Part A
### Description: Uses prior assignment 4 work to find closest birthdays, and uses NumPy instead of base python code
### Inputs: User input of a string
### Packages: string
### Output: console output
### References: 
##################################

import numpy as np
from BDate import *
from Person import *

#create function to calculate the absolute difference between two persons (as parameter)
def bddiff(p1, p2):
    D = abs(p1 - p2)
    #where np.where function to apply conditional logic to each value in matrix
    D = np.where(D > 183, 366 - D, D)
    return D

if __name__ == "__main__":

    #hardcode a set of people objects
    P1 = Person("Devin", BDate(11,4,1981),18326)
    P2 = Person('Jason', BDate(9,10,1978), 18326)
    P3 = Person('Melanie', BDate(2,19,1976), 96789)
    P4 = Person('Beth', BDate(2,7,1984), 18322)
    P5 = Person('Andrew', BDate(12,31,2012), 18322)
    P6 = Person('Alexa', BDate(3,22,2018), 18322)
    P7 = Person('Karen', BDate(8,16,1956), 18353)
    P8 = Person('Logan', BDate(1,11,2011), 96789)
    P9 = Person('Chester', BDate(2,28,2022), 18326)


    N = 9
    
    # Use NumPy to create birthday arrays
    person = list([P1, P2, P3, P4, P5, P6, P7, P8, P9])
    names = np.array([[p.name for p in person]])
    bdays = np.array([[p.birthdate.yrdays() for p in person]])
    bdt = np.array([[p.getBDay() for p in person]])

    #Create a matrix subtracting each bday from all others. Diagonal is self substraction (0)
    diff = bddiff(bdays.T, bdays)

    #fill diagonal with high values
    np.fill_diagonal(diff, 200)
    
    # use argmin to select coordinates of smalled values
    row,col = np.unravel_index(np.argmin(diff), np.shape(diff))

    # Get names and birthdays from arrays based on index values
    name1 = names[0,row]
    name2 = names[0,col]
    bdt1 = bdt[0,row]
    bdt2 = bdt[0,col]

    print("The two people with the closest birthdays are:\n {0} {1}\n {2} {3}".format(name1, bdt1, name2, bdt2))

""" Testing
>>> %run "c:\\Users\\devin\\OneDrive\\Documents\\positron\\DS510\\Assignment 9\\Assignment 9A - Hunt.py"
The two people with the closest birthdays are:
 Melanie February 19th
 Chester February 28th
>>>


"""