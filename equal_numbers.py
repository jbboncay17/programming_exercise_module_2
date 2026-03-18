bold="\033[1m"
end="\033[0m"
green="\033[32m"
red="\033[31m"

num1 = float(input(bold+"Enter first number: "))
num2 = float(input(bold+"Enter second number: "))
print("")

if num1 == num2:
    print(bold+green+"The two numbers are Equal"+end)
else:
    print(bold+red+"The two numbers are Not Equal"+end)