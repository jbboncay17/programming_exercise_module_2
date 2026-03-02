bold='\033[1m'
end='\033[0m'
red='\033[31m'

# print(bold+"JOSE BENEDICT L. BONCAY"+end)
# print(bold+"BSCpE 1-2"+end)
# print("")
#
# print("")
# print(bold+red+"I. Enter 5 Numbers:"+end)
# print("")


num1 = int(input(bold+"Enter 1st number: "+end))
num2 = int(input(bold+"Enter 2nd number: "+end))
num3 = int(input(bold+"Enter 3rd number: "+end))
num4 = int(input(bold+"Enter 4th number: "+end))
num5 = int(input(bold+"Enter 5th number: "+end))
print("")
list1 = [num1, num2, num3, num4, num5]
list2 = sorted(list1)
print(bold+"Sorted List:"+end, list2)

sum1 = sum(list1)
print(bold+"Sum:"+end, sum1)
print("")

print("")
print(bold+red+"II. Tuple named colors:"+end)
print("")

print(bold+"colors='RED', 'GREEN', 'BLUE', 'YELLOW','ORANGE'"+end)
print("")
colors=('RED', 'GREEN', 'BLUE', 'YELLOW','ORANGE')

print(bold+"The First Color is:"+end, colors[0])
print(bold+"The Last Color is:"+end, colors[4])
print(bold+"The Number of colors:"+end, len(colors))
print("")


print("")
print(bold+red+"III. List of fruits:"+end)
print("")
print(bold+"List of fruits='APPLE','BANANA','MANGO'"+end)
print("")

fruits=['APPLE','BANANA','MANGO']
fruits.append("ORANGE")
fruits.remove("BANANA")
print(bold+"Updated List:"+end, fruits)
print("")


print("")
print(bold+red+"IV. List of Animals to a tuples, and vice versa:"+end)
print("")
list3=['DOG','CAT','BIRD']
print(bold+"List ='DOG','CAT','BIRD'"+end)
print("")
print(bold+"List:"+end, list(list3))
print(bold+"Tuple:"+end, tuple(list3))
print(bold+"Back to List:"+end, list(list3))
print("")


print("")
print(bold+red+"V. Tuple of Student Records:"+end)
print("")
print(bold+"Students-('Anna',85),('Mark',90),('Luke',88)"+end)
students = (('Anna', 85), ('Mark', 90), ('Luke', 88))
print(f"{students[0][0]} - {students[0][1]}")
print(f"{students[1][0]} - {students[1][1]}")
print(f"{students[2][0]} - {students[2][1]}")
top = max(students)
print(bold+'Top Student:'+end, top[0], f"({top[1]})")
