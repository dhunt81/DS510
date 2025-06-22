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
