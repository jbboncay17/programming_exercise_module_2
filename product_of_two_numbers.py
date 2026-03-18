bold='\033[1m'
end='\033[0m'
green='\033[92m'

num1 = int(input(bold+"Enter first number: "))
num2 = int(input(bold+"Enter second number: "))

product=num1*num2
print(bold+green+"The product of the two numbers is: "+end, product)
