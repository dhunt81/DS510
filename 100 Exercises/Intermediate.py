# Exercise 34
def f(a,b,x):
    return(a*(x**3)+2*a*(x**2) + b)

f(3,0,1)
f(0,2,2)

# Exercise 35
def CheckPresence(a,L):
    return( a in L)

L=[1,2,3,4,5]
a = 9
CheckPresence(a,L)

# Exercise 36
def numSum():
    in_val = input("Enter a number: ")
    nums = list(int(x) for x in in_val)
    return(sum(nums))

numSum()

# Exercise 37
def calculateSum(L):
    nums = list(x for x in L)
    return(sum(nums))

L=[1,2,3,4,5,6,7,8,9]
calculateSum(L)

# Exercise 38
