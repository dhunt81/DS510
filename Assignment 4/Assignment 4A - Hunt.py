### Created: June 22, 2025
### DS510 Assignment 4 Part A
### Description: Asks user for size of random list, calculates mean, and displays numbers above that mean
### Inputs: n = size of the list
### Packages: random
### Output: text with the mean and list items above the mean to console
### References: some snippits of code and logic borrowed from code snippets by Loren Rhodes
##################################

''' Assignment text verbatim
Write a Python program which:
(1) prompts the user for a list size N
(2) fills a list of that size with random integers in the range 0 .. N (inclusive of N)
(3) prints these integers
(4) calculates the mean average of the list and prints it out (calculate the mean by summing the values and dividing; don't call a Python function)
(5) prints each element in the list larger than the mean.
'''

import random   #random package library

#create a function to generate a random list of size N, with a range of values from O to N based on a parameterized size
def randList(size):
    rList =  [] # initialize empty list
    #generate list and append random numbers to list
    for i in range(size):
        rList.append(random.randint(0,size)) #generate the random list
        print("i= {0} random int = {1}".format(i,rList[i])) #print each item out
      
    return rList

# create function to calculate the mean of a list
def listMean(inList):
    sum = 0
    for s in inList:
        sum += s
    mean = sum / len(inList)
    return mean

# create function that takes a list and mean and returns elements in the list above the number
def listAboveMean(rList, mean):
    print("Here are the elements larger than the mean:")
    for x in range(len(rList)):
        if rList[x] > mean:
            print("i= {0} random int= {1}".format(x, rList[x]))


if __name__ == "__main__":
    #prompt user for list size
    N = int(input("Enter the size of the list: "))
    # call the function defined above to generate the list
    randList = randList(N)
    # call function to calculate the mean and save to rLMean
    rLMean = listMean(randList)

    #Another printing of the list as a check on logic above
    print("The random list contains {0} numbers.\nThis random list is: {1}".format(len(randList), randList))
    print("The list mean is: {0}".format(rLMean))

    # run the listAboveMean function to print elements above the mean
    listAboveMean(randList, rLMean)

''' Example outputs
>>> %run "c:\\Users\\devin\\OneDrive\\Documents\\positron\\DS510\\Assignment 4\\Assignment 4A - Hunt.py"
Enter the size of the list: 
12
i= 0 random int = 9
i= 1 random int = 8
i= 2 random int = 1
i= 3 random int = 10
i= 4 random int = 5
i= 5 random int = 0
i= 6 random int = 4
i= 7 random int = 5
i= 8 random int = 4
i= 9 random int = 1
i= 10 random int = 12
i= 11 random int = 7
The random list contains 12 numbers.
This random list is: [9, 8, 1, 10, 5, 0, 4, 5, 4, 1, 12, 7]
The list mean is: 5.5
Here are the elements larger than the mean:
i= 0 random int= 9
i= 1 random int= 8
i= 3 random int= 10
i= 10 random int= 12
i= 11 random int= 7


>>> %run "c:\\Users\\devin\\OneDrive\\Documents\\positron\\DS510\\Assignment 4\\Assignment 4A - Hunt.py"
Enter the size of the list: 
25
i= 0 random int = 7
i= 1 random int = 10
i= 2 random int = 11
i= 3 random int = 13
i= 4 random int = 2
i= 5 random int = 21
i= 6 random int = 18
i= 7 random int = 23
i= 8 random int = 22
i= 9 random int = 15
i= 10 random int = 18
i= 11 random int = 16
i= 12 random int = 15
i= 13 random int = 11
i= 14 random int = 12
i= 15 random int = 25
i= 16 random int = 0
i= 17 random int = 0
i= 18 random int = 6
i= 19 random int = 3
i= 20 random int = 25
i= 21 random int = 18
i= 22 random int = 22
i= 23 random int = 25
i= 24 random int = 25
The random list contains 25 numbers.
This random list is: [7, 10, 11, 13, 2, 21, 18, 23, 22, 15, 18, 16, 15, 11, 12, 25, 0, 0, 6, 3, 25, 18, 22, 25, 25]
The list mean is: 14.52
Here are the elements larger than the mean:
i= 5 random int= 21
i= 6 random int= 18
i= 7 random int= 23
i= 8 random int= 22
i= 9 random int= 15
i= 10 random int= 18
i= 11 random int= 16
i= 12 random int= 15
i= 15 random int= 25
i= 20 random int= 25
i= 21 random int= 18
i= 22 random int= 22
i= 23 random int= 25
i= 24 random int= 25


>>> %run "c:\\Users\\devin\\OneDrive\\Documents\\positron\\DS510\\Assignment 4\\Assignment 4A - Hunt.py"
Enter the size of the list: 
3
i= 0 random int = 1
i= 1 random int = 1
i= 2 random int = 2
The random list contains 3 numbers.
This random list is: [1, 1, 2]
The list mean is: 1.3333333333333333
Here are the elements larger than the mean:
i= 2 random int= 2
>>>
'''