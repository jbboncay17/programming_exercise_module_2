bold='\033[1m'
end='\033[0m'
green='\033[32m'

count=0

for i in range(5):
    odd=int(input(bold+f"Enter number {i+1}: "+end))
    if odd % 2 != 0:
        count += 1
print("")
print(bold+green+"There are"+end,count, bold+green+"odd numbers."+end)
