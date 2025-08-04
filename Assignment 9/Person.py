################################
### Author: Devin Hunt
### Created: June 16, 2025
### DS510 Assignment 3 Part C
### Description: define a person class
### Inputs: name = persons name
###         birthdate = persons birth date as BDate object
###         zipcode = persons zipcode
### Output: string of text with assigned values to person
##################################

""" Assignment text
Define a Person class, in a file Person.py, where:
(1) there is an attribute variable for name.
(2) there is an attribute variable for a birthdate. (Just use your BDate class)
(3) there is an attribute variable for their zipcode.
(4) the __str__ function outputs all attributes of the Person object.  This function can leverage BDate's __str__ function
(5) each attribute has an associated function to update that attribute (setter) as well as a getters.   
    See the test driver below for suggested getter and setter function names. 
    You'll need two getters for the birthday: one for the date and one for the day.
"""

class Person:

    #initialize the date class
    def __init__ (self, name, birthdate, zipcode):
        self.name = name
        self.birthdate = birthdate
        self.zipcode = zipcode

    # series of getters to return object values
    def getName(self):
        return self.name
    
    def getBDay(self):
        return self.birthdate.bday()

    def getZip(self):
        return self.zipcode

    # series of setters to update object values
    def setName(self, newName):
        self.name = newName
    
    def setBDay(self, newBDate):
        self.birthdate = BDate(newBDate)

    def setZip(self, newZip):
        self.zipcode = newZip
        
    def __str__(self):
        return "Name: " + self.name + " BD " + self.birthdate.bday() + " zip: " + str(self.zipcode)