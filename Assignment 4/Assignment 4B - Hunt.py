##################################
### Created: June 22, 2025
### Author: Devin Hunt
### DS510 Assignment 4 Part B
### Description: Creates a list of people and determies which two have the closest birthdays
### Inputs: None
### Packages: People.py BDate.py
### Output: console
### References: Code adapted from Dr. Loren Rhodes DS510 course
##################################

''' Assignment Verbatim Text
One of the common tasks in machine learning is to find the near neighbors of data points, or find the pair points that are closest. 
Nearnness is defined by some measure of distance.  Usually we use Euclidean distance (square root of the sum of squares of the differences).  
An alternative is to calculate the distance as the sum of the absolute value between the x's and y's. (Often called the Manhattan distance.)

In this program we are going to use the Person class from the last assignment with names, birthdates and zipcodes.   
Given a list of people, we want to find the two people who have the closest birthdate--our measure of closeness.  
The algorithm to determine how close two birthdates are is to find the number of days between them: 

You have a function from the last assignment that gives you the number of days into the year a date is. 
You subtract these two dates for the difference "D" (you'll need the absolute value). 
If D > 183 (a half year) then you need to calculate 366 - D as the closer smaller difference.
So D = 31 for March 3 and April 3, but for January 1 and December 31 D=1 ( |1-366| = 365 but 366 - |1-366| is 1)
Note no birthdates are more than 183 days apart!
Write a program to do and express the following tasks:

Set N to be the number of people. Let N be at least 5.
Create a list 'people' and append N instances of Person to the list.  
Hand code your Person instances rather than interactively enter the data (too tedious). Be sure there is a nice variation of birthdates.
Print your list of people using a for loop.
Create a function bddiff(p1,p2) that returns the difference between the birthdays of Persons p1 and p2.
Create a matrix diffs (list of list) of the differences between all pairs of birthdates. 
When you print this list of lists, you will have 0's on the diagonal and the matrix will be symmetric (upper and lower triangles are the same).
Search the matrix for the smallest difference and output the two Persons who are closest. 
You must ignore the 0 distance of the same point, the zeros on the diagonal. If zero is off the diagonal then two people have the same birthdate.  
If two or more Persons have the same closest bd difference, just keep track of the first one.
You can do the search as you populate the diffs matrix rather than a completely separate, second nested loop.
 '''

from BDate import *
from Person import *

#create function to calculate the absolute difference between two persons (as parameter)
def bddiff(p1, p2):
    D = abs(p1.birthdate.yrdays() - p2.birthdate.yrdays())
    if D > 183:
        D = 366 - D
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
    #create people null list
    people = []

    #loop through the create Px variables and append into the people list
    for i in range(1, N+1):
        person = eval(f"P{i}")
        people.append(person)

    #print the contents of people
    for z in range(0,len(people)):
        print(people[z])



    #Create square matrix of the people where the contents are the differences in birth days
    mat = []   # a matrix is a list of lists
    for r in range(N):
        row = []  # the row of the matrix is a list
        for c in range(N):
            x = bddiff(people[r], people[c]) #calculate difference between birthdays
            row.append(x)  #add number to the row
                
        mat.append(row)   #add the row to the matrix
            
    # print the matrix in new lines for each row
    for row in mat:
        print(row)

    # Find the smallest value        
    smallest = 366  # start tracking the min by setting the smallest to a larger number
    minr = 366
    minc = 366 

    for r in range(N):
        for c in range(N):
            if r != c and mat[r][c] < smallest:   # exclude diagonal values as this is the same person
                smallest = mat[r][c]
                minr = r
                minc = c
                
    print("The two people with the closest birthdays are:\n {0} \n {1}".format(people[minr], people[minc]))


''' Sample Run
>>> %run "/Users/devinhunt/Documents/Positron Repositories/DS510/Assignment 4/Assignment 4B - Hunt.py"
Name: Devin BD November 4th zip: 18326
Name: Jason BD September 10th zip: 18326
Name: Melanie BD February 19th zip: 96789
Name: Beth BD February 7th zip: 18322
Name: Andrew BD December 31st zip: 18322
Name: Alexa BD March 22nd zip: 18322
Name: Karen BD August 16th zip: 18353
Name: Logan BD January 11st zip: 96789
Name: Chester BD February 28th zip: 18326
[0, 55, 107, 95, 57, 139, 80, 68, 116]
[55, 0, 162, 150, 112, 172, 25, 123, 171]
[107, 162, 0, 12, 50, 32, 179, 39, 9]
[95, 150, 12, 0, 38, 44, 175, 27, 21]
[57, 112, 50, 38, 0, 82, 137, 11, 59]
[139, 172, 32, 44, 82, 0, 147, 71, 23]
[80, 25, 179, 175, 137, 147, 0, 148, 170]
[68, 123, 39, 27, 11, 71, 148, 0, 48]
[116, 171, 9, 21, 59, 23, 170, 48, 0]
The two people with the closest birthdays are:
 Name: Melanie BD February 19th zip: 96789 
 Name: Chester BD February 28th zip: 18326
>>>

'''