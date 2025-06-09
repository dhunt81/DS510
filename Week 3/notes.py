"""
Week 3 class demos
"""
import random

"""
number = random.randint(1, 100)

guess = int(input("Enter a number: " ))
if guess == number:
    print("Congratulations!")
elif guess < number:
    print("Higher")
elif guess > number:
    print("Lower")



#set number of runs in a foor loop
for i in range(1, 5):
    print(i)

print('Loop Done')


#conditional loop
notEnd = True
#print(type(notEnd))
while notEnd:
    notEnd = bool(input('Do you wish to continue?') == 'y')
    print(notEnd)

print("Loop Done")
"""


### playing around
number = random.randint(1, 100)

noEnd = True
while noEnd:
    guess = int(input("Enter a number: " ))
    if guess == number:
        print("Congratulations!")
        noEnd = False
    elif guess < number:
        print("Higher")
    elif guess > number:
        print("Lower")
    


### defining functions

def addOne (x):
    return (x+1)

def main():
    a = 5
    print (a)
    b = addOne(a)
    print (b)
    print(addOne(9))

main()
