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

        #compare bid to last highest bid
        if highBids.isEmpty():
            highBids.push(currentBid)
            print("new high bid is: {0}".format(currentBid))

        elif currentBid > highBids.top():
            highBids.push(currentBid)
            print("new high bid is: {0}".format(currentBid))

        response = input("Do you wish to continue (y/N): ").upper()

''' Testing

PS C:\Users\devin\OneDrive\Documents\positron\DS510> & C:/Users/devin/AppData/Local/Programs/Python/Python313/python.exe "c:/Users/devin/OneDrive/Documents/positron/DS510/Assignment 6/Assignment 6B - Hunt.py"
Enter a numeric bid great than 0: 2
new high bid is: 2
Do you wish to continue (y/N): y
Enter a numeric bid great than 0: 6
new high bid is: 6
Do you wish to continue (y/N): y
Enter a numeric bid great than 0: 5
Do you wish to continue (y/N): y
Enter a numeric bid great than 0: 16
new high bid is: 16
Do you wish to continue (y/N): y
Enter a numeric bid great than 0: 10
Do you wish to continue (y/N): y
Enter a numeric bid great than 0: 16
Do you wish to continue (y/N): y
Enter a numeric bid great than 0: 19
new high bid is: 19
Do you wish to continue (y/N): n
PS C:\Users\devin\OneDrive\Documents\positron\DS510> 

'''