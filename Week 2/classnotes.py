#Strings in Python

name = "John Doe"
print(name)

#access positions in string
print(name[0])
print(name[1])
print(name[-1])
print(name[0:6])
print(name[2:])

upperName = name.upper()
lowerName = name.lower()
print(name.find("John"))
print(name.find("Doe"))
print(name.find("john"))


name2 = name.replace("John", "Jane")
print(name, name2)
print("John said, \'hi\' !")
print("John said \n\'hi\'!")
print(name+"!")

#casting variables

print(name+3)
#creates an error
print(name+str(3))
