#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 10:58:01 2021

@author: rhodes
"""

# Part A
"""
Building a list of random numbers is the crux of this part.
As a pattern, this will collect a roll of 5 dice, like in Yahtzee and
determine if the roll has at least a 3 of a kind.
We will use a couple of functions to break down the steps in this solution.
"""
import random   #we need  this library of methods

"""
Returns a sorted list of 5 numbers representing dice thrown
"""
def Roll5():
    dice =  []
    for d in range(5):
        dice.append(random.randint(1,6))
        
    dice.sort() #put the dice  in number order to easily spot a 3 of a kind
    return dice
"""
Assumes a sorted list and prints whether there's a three of a kind and its value
"""
def ThreeOfAKind(dice):
    if dice[0]==dice[1] and dice[0]==dice[2]:
        print("Three of a kind as {}'s".format(dice[0]))
    elif dice[1]==dice[2] and dice[1]==dice[3]:
        print("Three of a kind as {}'s".format(dice[1]))
    elif dice[2]==dice[3] and dice[2]==dice[4]:
        print("Three of a kind as {}'s".format(dice[2]))
    else:
        print("There is not a 3 of a kind.")
        
if __name__ == "__main__":
    dice = Roll5()
    print("The dice thrown are ")
    #for d in dice: #in a list, the loop control variable can be the item
    #    print(d,end=' ')
    for i in range(5): #this is an alternative way to print the list
        print(dice[i],end=' ')
    print()# output to next line
    ThreeOfAKind(dice)
    
    
    
# Part B
"""
Created on Thu Jun  8 10:35:30 2023
Assignment 03 Part B matrix patterns
@author: rhodes
Building and populating a 2 dimension list, with rows and columns 
is the objective of this problem.
Think of matrices as lists of lists.  A row is a list and the matrix has a 
list of rows.

"""


"""
populating a matrix with random numbers
"""
import random

if __name__ == "__main__":
    mat = []   # a matrix is a list of lists
    
    n = int(input("Enter size of square matrix: "))
    
    for r in range(n):
        row = []  # the row of the matrix is a list
        for c in range(n):
            x = random.randint(0, 100)
            row.append(x)  #add number to the row
            
        mat.append(row)   #add the row to the matrix
        
        
    print(mat) #check it out as a list of lists
    
     
    
    """
    let's find the largest value and where it's located
    """
    
    largest = 0  # gotta start tracking the largest so far
    maxr = 0
    maxc = 0     # where is this largest ?
    
    for r in range(n):
        for c in range(n):
            if mat[r][c] > largest:   # use >= if want last position of duplicate max
                largest = mat[r][c]
                maxr = r
                maxc = c
    print("Max=",largest)
    print("and is found in row",maxr,"and in column",maxc)
            

"""
More matrix examples
Further  down, there's code for random selection from a list.
"""
import random
if __name__ == "__main__":
    # brute force creation of a fixed sized array
    # A 5 x 10 matrix of 1's
    ones =  [1]*10  # * is repetition of an element
    rowsOfOnes = [ones]*5
    print(rowsOfOnes) #not output in a very organized way, have to look for [ ]
    
    # a bit more interactive and different contents
    rows = int(input("How many rows? "))
    cols = int(input("How many columns? "))
    
    matx = [['x']*cols for i in range(rows)]
    #now let's nicely print the table without [ ]
    for r in range(rows): # lcv are an index
        for c in range(cols):
            print (matx[r][c], end=' ') #explicitly access the element with indexes
            
        print()#end of line
    #other Python ways to print the matrix
    for row in matx: # each row is an element
        for elem in row: # each element of the row is the matrix element
            print (elem,end=' ')
        print() # note this print pattern is very common
    
    #let's make a list of the alphabet.
    alpha = [chr(letter+65)  for letter in range(26)]
    print(alpha)
    
    #assuming you didn't create a matrix with more than 26 elements
    # 5x5 is good 3x8 is good, 2 x 13 is good, 8x 4 is not
    #randomly populate the matrix with a unique letter
    
    for r in range(rows):
        for c in range(cols):
            #get a random letter
            next = alpha[random.randint(0,len(alpha)-1)] #alpha's length changes
            matx[r][c] = next #put in the selected letter
            alpha.remove(next) # remove as a future candidate letter
            
      #display the random letters in the matrix      
    for row in matx: # each row is an element
        for elem in row: # each element of the row is the matrix element
            print (elem,end=' ')
        print() #       
    
    



# Part C
"""
Objectives here are considering the elements of a string (of digits), converting
the character digits to integers and then manipulating the list of integers.
Using some interesting mathematical operations (modulus)
"""
import random
if __name__ == "__main__":
    ccnumber = input("Enter a long number like a credit card number: ")
    digits = []
    for char in ccnumber:
            #skip - and spaces and  other bad input
        if char in('0','1','2','3','4','5','6','7','8','9'): 
            digits.append(int(char))
    # let's look  at  the list
    print(digits)
    
    #create a simple check sum digit by adding up the whole list
    sum = 0
    for d in digits:
        sum += d
    print("Checksum={}".format(sum % 10))