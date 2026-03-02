bold="\033[1m"
red="\033[31m"
highlight="\033[107m\033[30m"
end="\033[0m"
reset="\033[0m"
print(bold+"Jose Benedict L.Boncay")
print(bold+"BSCpE 1-2")

print((highlight+"BASIC CALCULATOR"+end).center(100))
print(bold+"1-Addition")
print(bold+"2-Subtraction")
print(bold+"3-Multiplication")
print(bold+"4-Division")
print(bold+"5-Modulus")
print(bold+"6-Power")
print(bold+"7-Reciprocal")
print(bold+"8-Root")
print("")
operation= float(input(red+"CHOOSE AN OPERATION:"))

if(operation in [1,2,3,4,5,6,7,8]):
    num1=float(input(reset+bold+"Enter the first number:"))
    num2=float(input(reset+bold+"Enter the second number:"))

    if  (operation==1):
        result=num1+num2
    elif(operation==2):
        result=num1-num2
    elif (operation == 3):
        result=num1*num2
    elif (operation == 4):
        result=num1/num2
    elif (operation == 5):
        result=num1%num2
    elif (operation==6):
        result=num1**num2
    elif (operation == 7):
        if num2 !=0:
            result=1/num2
        else:
            print("Cannot calculate reciprocal of zero")
            result=None
    elif (operation == 8):
        result=num1**(1/num2)

else:
    print("Invalid operation entered")
print("")
print(("TOTAL = {}".format(result)).center(20))
