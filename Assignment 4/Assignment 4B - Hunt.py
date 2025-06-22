##################################
### Created: June 22, 2025
### Author: Devin Hunt
### DS510 Assignment 4 Part B
### Description: 
### Inputs: 
### Packages: 
### Output: 
### References: 
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
