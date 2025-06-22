# Data types


#Lists
#initialize using a sqaure bracket

zoo = ["Donkey", "Penguin", "Elephant", "Moneky"]
print(zoo)
zoo.append("Giraffe")
zoo.append("Cheeta")
help(zoo)
zoo.pop(2)

# List comprehensions

zoo2 = [ expr for val in zoo if ]


#Tuple
#Like a list but in unmutable
#initialize by using a parenthesis

cars = ("Wranger", "iX M60", "Hummer")
help(cars)


#Dictionaries
#Utilize key pairs
#initialized with curley brackets
#essential a list of tuples
ab = {
    'personal': "devin.hunt@icloud.com",
    'work': "dhunt@iavi.org",
    'ems': "dhunt@pmrems.org",
    'gwg': "dhunt@gwgvfd.org",
    'school': 'djh100@juniata.edu'
}
help(ab)
ab.get('personal')
ab.get('work')

del ab['work']
ab.get('work')
ab['work']='dhunt@iavi.org'

ab.items()


#sequences
# includes lists, typles, strings

shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'work'

#slice a sequence
shoplist[0]
shoplist[0:1]
shoplist[:2]
shoplist[3:]


#Set
#unordered collection of objects
#when existence in set is more important than an order of objects in the set

#can find existance, subsets, intersections, unions, etc.

bri = set(['brazil', 'iran', 'united states', 'india', 'germany'])
bri = {'brazil', 'iran', 'united states', 'india', 'germany'}
help(bri)

'india' in bri
'france' in bri

bric = bri.copy()
bric

bric.add('china')

bric.issuperset(bri)

axis = {'italy', 'denmark', 'germany', 'india', 'pakistan', 'russia', 'mongolia'}

#intersection
axis & bri

#union
axis | bri


# Strings
name = 'Devin Hunt'
name2 = 'Jason Yamamura'

help(str)
