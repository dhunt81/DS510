##################################
### Created: July 4, 2025
### Author: Devin Hunt
### DS510 Assignment 6 Part B
### Description: Use a stack class to track high bid history
### Inputs: Node, Stack
### Packages: none 
### Output: console output
### References: 
##################################

from Node import *
from Stack import *

if __name__ == "__main__":
    # initialize instance of stack
    highBids = Stack()

    #response used to keep loop going while equal to Y
    response = "Y"
    while response == "Y":
        #Ask for bid input
        currentBid = int(input("Enter a numeric bid great than 0: "))

        # if empty then place the bid
        if highBids.isEmpty():
            highBids.push(currentBid)
            print("new high bid is: {0}".format(currentBid))
            
        #compare bid to last highest bid
        elif currentBid > highBids.top():
            highBids.push(currentBid)
            print("new high bid is: {0}".format(currentBid))

        #print the stack for testing
        print("High Bid History is: ", highBids)

        #Ask user if they want to continue
        response = input("Do you wish to continue (y/N): ").upper()