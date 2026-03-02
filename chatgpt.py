print("BASIC CALCULATOR")
print("1-Add")
print("2-Subtract")
print("3-Multiply")
print("4-Divide")
print("5-Modulus")
print("6-Power")
print("7-Reciprocal")
print("8-Root")
operation= int(input("Choose an operation:"))

if(operation in [1,2,3,4,5,6,7,8]):
    num1=int(input("Enter the first number:"))
    num2=int(input("Enter the second number:"))

if operation == 1:
    result = num1 + num2
elif operation == 2:
    result = num1 - num2
elif operation == 3:
    result = num1 * num2
elif operation == 4:
    result = num1 / num2
elif operation == 5:
    result = num1 % num2
elif operation == 6:
    result = num1 ** num2
elif operation == 7:  # Reciprocal
    if num2 != 0:
        result = 1 / num2  # or num1 depending on your design
    else:
        print("Cannot calculate reciprocal of zero")
        result = None
elif operation == 8:  # Root
    result = num1 ** (1 / num2)
else:
    print("Invalid choice")
    result = None

if result is not None:
    print("TOTAL = {}".format(result))
