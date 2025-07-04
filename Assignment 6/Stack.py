##################################
### Created: July 4, 2025
### Author: Devin Hunt
### DS510 Assignment 6 Part A
### Description: Creates a stack class with functions to add and remove elements
### Inputs: None
### Packages: collections
### Output: console output
### References: some snippits of code and logic borrowed from code snippets by Loren Rhodes and Gerald Kruse
##################################

from collections import deque

class Stack:
    # initialize with empty deque
    def __init__(self):
        self.stack = deque([])
    
    def push(self, node):
        # append to the "top" of the stack
        self.stack.appendleft(node)
    
    def pop(self):
        # removes the top elements from the stack
        if self.stack:
            self.stack.popleft()
        else:
            print("Stack is empty")

    def top(self):
        # return the top element but don't remove it. Only do if not empty
        if self.stack:
            return self[0]
        else:
            return("Stack is empty")
    
    def isEmpty(self):
        #check if stack is empty
        if self.stack:
            return False
        else:
            return True

    def __repr__(self):
        nodes = []
        for node in self.stack:
            nodes.append(str(node))
        return " -> ".join(nodes)