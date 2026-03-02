bold='\033[1m'
end='\033[0m'
red='\033[31m'
green='\033[32m'

# #NUMBER 2
# for i in range(3):
#     print(i)

# # #NUMBER 3
# i=0
# while i<3:
#     print(i)
#     i+=1

# #NUMBER 6
# for i in range (2,10,3):
#     print(i, end=' ')

# #NUMBER 7
# count=0
# while count<5:
#     print("Hi")
#     count +=2

#NUMBER 8
# for i in range(1,5):
#     print(i)

# #NUMBER 10
# for letter in "PUP":
#     print(letter)

#NUMBER 12
# for i in range (5):
#     pass # empty loop
# print("Empty loop executed")

#NUMBER 13
# for i in range (5):
#     if i==3:
#         break
#     print(i)

#NUMBER 14
# for i in range(3):
#     for j in range(2):
#         print(i,j)

#NUMBER 16
# i=10
# while i<10:
#     print(i)
#     i+=1

#NUMBER 17
# for i in range(1,10,3):
#     print(i,end=' ')

#NUMBER 19
# for num in range(6):
#     if num %2==0:
#         continue
#     print(num)

#NUMBER 20
# x=0
# while x<5:
#     print(x,end=' ')
#     x+=2
# else:
#     print('Done')


####PART 2####

#NUMBER 1
# for i in range(1,11):
#     print(i)

#NUMBER 2
# total=0
# for i in range(1,11):
#     total+=i
# print("Sum=", total)

#NUMBER 3
# num=int(input("Enter a Number:"))
# for i in range(1,11):
#     print(f"{num}x{i}={num*i}")

#NUMBER 4
# i=2
# while i <= 20:
#     print(i)
#     i+=2

#NUMBER 5
# count=10
# while count>0:
#     print(count)
#     count-=1
# print(bold+red+"Meow Meow🐱🐱"+end)

#NUMBER 6
# num=int(input("Enter a number: "))
# factorial=1
#
# for i in range(1,num+1):
#     factorial*=i
#
# print("The Factorial of",num,"is",factorial)

#NUMBER 7
# num=int(input("Enter a number: "))
# sum_digits=0
#
# while num>0:
#     digit=num%10
#     sum_digits+=digit
#     num//=10
# print("Sum of digits=",sum_digits)

#NUMBER 8
# word=input('Enter a word: ')
# reversed_word=""
#
# for ch in word:
#     reversed_word=ch+reversed_word
# print(bold+green+"Reversed word:"+end,reversed_word)

#NUMBER 9
# n=int(input("Enter number of terms:"))
# a,b=0,1
# count=0
#
# while count<n:
#     print(a)
#     a,b=b,a+b
#     count+=1

#NUMBER 10
for num in range(2,51):
    for i in range(2,num):
        if num%i==0:
            break
    else:
        print(num)