##################################
### Created: July 4, 2025
### Author: Devin Hunt
### DS510 Assignment 6 Part A
### Description: Use the provided test program to test the stack class
### Inputs: Node, Stack
### Packages: none 
### Output: console output
### References: Tester program provided by Loren Rhodes
##################################

from Node import * # Note: since we are saving Node elements on the stack, we use this, but don't need to each time
from Stack import *

if __name__ == "__main__":
    
    stack = Stack()
    nodeA = Node("A")
    stack.push(nodeA)
    print(stack)
    
    nodeB = Node("B")
    stack.push(nodeB)
    print(stack)
    
    nodeC = Node("C")
    stack.push(nodeC)
    print(stack)
    
    stack.pop()

    print(stack)



'''Tester

>>> %run "c:\\Users\\devin\\OneDrive\\Documents\\positron\\DS510\\Assignment 6\\Assignment 6A - Hunt.py"
A
B -> A
C -> B -> A
B -> A
>>>

'''