##################################
### Created: June 22, 2025
### Author: Devin Hunt
### DS510 Assignment 4 Part C
### Description: Calculate the checksum of a credit card number
### Inputs: Credit card number from user
### Packages: 
### Output: console
### References: https://en.wikipedia.org/wiki/Luhn_algorithm
##################################


#Ask user to enter a creditcard number

def checkSum(ccnum):
    #save each digit to a list called payload
    for i in range(0,len(ccnum)-1):
        payload.append(int(ccnum[i])) 
    print("Payload (CC without last number) is:", payload)

    #count backwards and double every second number
    for k in range(len(payload)-1,-1,-2):
        payload[k] = payload[k]*2 - 9*((payload[k]*2)>9)
    print("Sum digits ", payload)  
    
    # take sum of the list
    payloadSum = sum(payload)

    #calculate check sum 
    checkSum = (10 - (payloadSum % 10)) % 10

    return checkSum

if __name__ == "__main__":
    #Request CC Number
    cc = input("Enter a credit card number: ")

    payload = []

    csum = checkSum(cc)
    print("our checksum is {0} and your last digit is {1}".format(csum, cc[-1]))


''' Sample testing
Note: It looks like perhaps the example numbers 3 and 5 are incorrect in the provide assignment. 
I got different answers than the provided numbers but manually calculating them matches my responses.


>>> %run "/Users/devinhunt/Documents/Positron Repositories/DS510/Assignment 4/Assignment 4C - Hunt.py"
Enter a credit card number: 
4254082178958925
Payload (CC without last number) is: [4, 2, 5, 4, 0, 8, 2, 1, 7, 8, 9, 5, 8, 9, 2]
Sum digitsL  [8, 2, 1, 4, 0, 8, 4, 1, 5, 8, 9, 5, 7, 9, 4]
our checksum is 5 and your last digit is 5

>>> %run "/Users/devinhunt/Documents/Positron Repositories/DS510/Assignment 4/Assignment 4C - Hunt.py"
Enter a credit card number: 
79927398713
Payload (CC without last number) is: [7, 9, 9, 2, 7, 3, 9, 8, 7, 1]
Sum digitsL  [7, 9, 9, 4, 7, 6, 9, 7, 7, 2]
our checksum is 3 and your last digit is 3

>>> %run "/Users/devinhunt/Documents/Positron Repositories/DS510/Assignment 4/Assignment 4C - Hunt.py"
Enter a credit card number: 
4254082178958836
Payload (CC without last number) is: [4, 2, 5, 4, 0, 8, 2, 1, 7, 8, 9, 5, 8, 8, 3]
Sum digitsL  [8, 2, 1, 4, 0, 8, 4, 1, 5, 8, 9, 5, 7, 8, 6]
our checksum is 4 and your last digit is 6

>>> %run "/Users/devinhunt/Documents/Positron Repositories/DS510/Assignment 4/Assignment 4C - Hunt.py"
Enter a credit card number: 
79927397602
Payload (CC without last number) is: [7, 9, 9, 2, 7, 3, 9, 7, 6, 0]
Sum digitsL  [7, 9, 9, 4, 7, 6, 9, 5, 6, 0]
our checksum is 8 and your last digit is 2

>>> %run "/Users/devinhunt/Documents/Positron Repositories/DS510/Assignment 4/Assignment 4C - Hunt.py"
Enter a credit card number: 
4254082178958834
Payload (CC without last number) is: [4, 2, 5, 4, 0, 8, 2, 1, 7, 8, 9, 5, 8, 8, 3]
Sum digitsL  [8, 2, 1, 4, 0, 8, 4, 1, 5, 8, 9, 5, 7, 8, 6]
our checksum is 4 and your last digit is 4

>>> %run "/Users/devinhunt/Documents/Positron Repositories/DS510/Assignment 4/Assignment 4C - Hunt.py"
Enter a credit card number: 
79927398716
Payload (CC without last number) is: [7, 9, 9, 2, 7, 3, 9, 8, 7, 1]
Sum digitsL  [7, 9, 9, 4, 7, 6, 9, 7, 7, 2]
our checksum is 3 and your last digit is 6
>>>
'''
