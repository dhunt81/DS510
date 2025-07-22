# Exercise 1
a = 1
b = 'France'
c = 36.2

print (a, b, c)

# Exercose 2
ch = "hello"
ch = "how are you"
print (ch)

# Exercise 3
x = 3
y = 8.5

x = str(x)
y = str(y)

type(x)
type(y)

# Exercise 4

weight = input("Enter your weight in kg: ")
print ("you entered weight of {} kgs".format(weight))

# Exercise 5
var = "Hello"

if isinstance(var, str):
    print("String")
elif isinstance(var, int):
    print("Integer")
else:
    print("None Selected")

# Exercise 6
d = 5

if d > 0:
    print("Positive")
elif d < 0:
    print("Negative")
else:
    print("0")

# Exercise 7
age = int(input("Enter your age: "))

if age >= 18:
    print("You are of legal age.")
elif age <18:
    print("You are a minor.")
else:
    print("Error")

# Exercise 8
for i in range(1,21):
    print(i)

i=1
while i < 21:
    print(i)
    i += 1

# Exercise 9
i = 1
for i in range(10,20):
    if i % 2 == 1:
        print(i)
i = 10
while i <= 20:
    if i % 2 == 1:
        print(i)
    i += 1

# Exercise 10
nums = [i for i in range(1,11)]
print(nums)


# ERCISE 11
nums = [i for i in range(2,11,2)]
print(nums)

# Exercise 12
L = [6,8,3,4,1,12,2,9.2]
L.sort()
print(L)

# Exercise 13
L = [3,2,2,1,9,1,2,3,7]
L.count(1)

# Exercise 14
L = []
L.append(10)
L.append(25)
L.append(30)
L.append(45)
L.append(90)
L.append('ab')
L.append('cd')
L.append('ef')
print(L)

# Exercise 15
L = [i for i in range(1,11)]
L1 = L[::3]
print(L)
print(L1)

# Exercise 16
c = "france"
c = "".join(sorted(c))
print(c)

# Exercise 17
L1 = [9,8,7,14,3,2,"a","p","hello","b"]
L2 = ["b",1,9.2,6,3,9,"p"]
L3 = set(L1).intersection(set(L2))
print(L3)

# Exercise 18
# Need to reveiw lambda functions

L = [("Apple", 15), ("Banana", 8), ("Strawberry", 12), ("Kiwi", 9), ("Peach", 2)]
L = 


# Exercise 19
ch = "Hello everyone"
ch_rev = ch[::-1]
print(ch_rev)

# Exercise 20
D = {"Apple":3, "Banana":7, "Kiwi":1}
