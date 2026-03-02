bold='\033[1m'
end = '\033[0m'
red='\033[31m'

print(bold+"JOSE BENEDICT L. BONCAY"+end)
print(bold+"BSCpE 1-2"+end)
print("")

print(bold+red+"I.NUMBERS"+end)
print("")
print(bold+"Original Set: {1,2,3,4,5}")
numbers={1,2,3,4,5}
numbers.add(6)
print("")
print(bold+"After Adding 6:", numbers)
print("")
print("")

print(bold+red+"II.FRUITS"+end)
print("")
print(bold+"Original Set of Fruits: {'apple','banana','mango','orange'}")
fruits={'apple','banana','mango','orange'}
fruits.remove('banana')

fruits.add('grape')
print("")
print(bold+"Updated Set:", fruits)
print("")

print(bold+red+"III.UNION AND INTERSECTION"+end)
print("")
print(bold+"Set 1= {1,2,3,4}")
print(bold+"Set 2= {3,4,5,6}")
set1={1,2,3,4}
set2={3,4,5,6}
print("")
set3=set2.union(set1)
set4=set2.intersection(set1)
print(bold+"Union:", set3)
print(bold+"Intersection:", set4)
print("")

print(bold+red+"IV.DIFFERENCE AND SYMMETRIC DIFFERENCE"+end)
print("")
print(bold+"A= {'red','green','blue'}")
print(bold+"B= {'yellow','green','orange'}")
A={'red','green','blue'}
B={'yellow','green','orange'}
print("")
C=A.difference(B)
D=B.symmetric_difference(A)
print(bold+"Difference:", C)
print(bold+"Symmetric difference:", D)
print("")

print(bold+red+"V.SET OF ANIMALS"+end)
print("")
print(bold+"animals={'dog','snake','bird','fish','cat','rabbit'}")
animals={'dog','snake','bird','fish','cat','rabbit'}
animal_name=input(bold+"Enter an Animal name (lowercase):"+end)

if animal_name in animals:
    print(f"{animal_name} is in the Set.")
else:
    print(f"{animal_name} is not in the Set.")

print("")
print(bold+"Animals present in the Set:")
for animal_name in animals:
    print(animal_name)

