bold='\033[1m'
end='\033[0m'

count=0

for i in range(10):
    num=int(input(bold+"Enter a number:"+end))
    if num % 2 == 0:
        count=count+1
print("")
print(bold+"Even Numbers Counter="+end, count)