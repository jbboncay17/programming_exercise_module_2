bold="\033[1m"
end="\033[0m"

num1=float(input(bold+"Enter the first number:"+end))
num2=float(input(bold+"Enter the second number:"+end))
print("")
if num1 > num2:
    print(bold+"The smaller number is:"+end, num2)
else:
    print(bold+"The smaller number is:"+end, num1)