bold='\033[1m'
end='\033[0m'

first = int(input(bold+"Enter number 1: "+end))
result = first

for i in range(9):
    num = int(input(bold+"Enter number: "+end))
    result = result - num
print("")
print(bold+"Result="+end, result)