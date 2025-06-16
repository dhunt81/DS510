################################
### Author: Devin Hunt
### Created: June 16, 2025
### DS510 Assignment 3 Part C
### Description: This program calls in the Bdate and Person classes and runs some examples
### Inputs: name = persons name
###         birthdate = BDate object of birthdate input
###         zipcode = zipcode of the person
### Output: string of text for the values of the person object
##################################



from BDate import *
from Person import *

if __name__ == "__main__":
    #Sample person to output
    p1 = Person("Joe",BDate(3,22,2000),16652)
    print("First person is",p1)
    print(p1.getName()+"'s birthday is",p1.getBDay())
    
    #Person 1
    n = input("What is the name?")
    m = int(input("What month is the birthdate (1-12)? "))
    d = int(input("What day is the birthdate (1-31)? "))
    y = int(input("What year is the birthdate? "))
    z = int(input("What is this persons zipcode? "))
    p1 = Person(n,BDate(m,d,y),z)
    print(p1)
    newzip = input("What is the new zip? ")
    p1.setZip(newzip)
    print("Updated:",p1)

    #Person 2
    n = input("What is the name?")
    m = int(input("What month is the birthdate (1-12)? "))
    d = int(input("What day is the birthdate (1-31)? "))
    y = int(input("What year is the birthdate? "))
    z = int(input("What is this persons zipcode? "))
    p2 = Person(n,BDate(m,d,y),z)
    print(p2)
    newzip = input("What is the new zip? ")
    p2.setZip(newzip)
    print("Updated:",p2)


""" Test output

First person is Name: Joe BD March 22nd zip: 16652
Joe's birthday is March 22nd
What is the name?Devin
What month is the birthdate (1-12)? 11
What day is the birthdate (1-31)? 04
What year is the birthdate? 1981
What is this persons zipcode? 20877
Name: Devin BD November 4th zip: 20877
What is the new zip? 18326
Updated: Name: Devin BD November 4th zip: 18326
What is the name?Jason
What month is the birthdate (1-12)? 09
What day is the birthdate (1-31)? 10
What year is the birthdate? 1978
What is this persons zipcode? 18326
Name: Jason BD September 10th zip: 18326
What is the new zip? 20877
Updated: Name: Jason BD September 10th zip: 20877

"""