bold='\033[1m'
end='\033[0m'
red='\033[31m'
green='\033[32m'

print(bold+"JOSE BENEDICT L. BONCAY")
print(bold+"BSCpE 1-2")
print("")
print("")
print(bold+"PROBLEM 1: CHECK IF A NUMBER IS POSITIVE OR NEGATIVE ")
print("")
number=float(input(bold+"ENTER A NUMBER:"+end))
if number >= 0:
      print(bold+"The Number is"+end, bold+green+"POSITIVE."+end)
else:
    print(bold+"The Number is",bold+red+"NEGATIVE."+end)
print("")
number=float(input(bold+"ENTER A NUMBER:"+end))
if number >= 0:
      print(bold+"The Number is"+end, bold+green+"POSITIVE."+end)
else:
    print(bold+"The Number is",bold+red+"NEGATIVE."+end)
print("")
print("")
print(bold+"PROBLEM 2:EVEN OR ODD NUMBER")
print("")
number=int(input(bold+"ENTER A NUMBER:"+end))
if number % 2 == 0:
    print(bold+f"The Number {number} is"+end, bold+green+"EVEN."+end)
else:
    print(bold+f"The Number {number} is",bold+red+"ODD."+end)
print("")
number=int(input(bold+"ENTER A NUMBER:"+end))
if number % 2 == 0:
    print(bold+f"The Number {number} is"+end, bold+green+"EVEN."+end)
else:
    print(bold+f"The Number {number} is",bold+red+"ODD."+end)
print("")
print("")
print(bold+"PROBLEM 3: DETERMINE IF ELIGIBLE TO VOTE")
print("")
age=int(input(bold+"ENTER YOUR AGE:"+end))
if age >= 18:
    print(bold+green+"You are ELIGIBLE to Vote."+end)
else:
    print(bold+red+"You are NOT ELIGIBLE to Vote."+end)
print("")
age=int(input(bold+"ENTER YOUR AGE:"+end))
if age >= 18:
    print(bold+green+"You are ELIGIBLE to Vote."+end)
else:
    print(bold+red+"You are NOT ELIGIBLE to Vote."+end)
print("")
print("")
print(bold+"PROBLEM 4: GRADE CLASSIFICATION")
print("")
grades=float(input(bold+"Enter grade:"))
if grades > 100 or grades <= 50:
    print(bold+red+"INVALID GRADE")
elif grades >= 90:
    print(bold+green+"EXCELLENT"+end)
elif grades >= 80:
    print(bold+green+"VERY GOOD"+end)
elif grades >= 70:
    print(bold+green+"GOOD"+end)
elif grades >=60:
    print(bold_+green+"NEEDS IMPROVEMENT"+end)
elif grades <60:
    print(bold+red+"FAILED"+end)
print("")
print("")
print(bold+"PROBLEM 5: SIMPLE DISCOUNT CALCULATOR")
print("")
amount=float(input(bold+"Enter total amount: "))
if amount >= 1000:
    discount=amount*0.10
    final_price=amount-discount
    print(bold+green+"Discounted amount:"+end,final_price)
else:
    print(bold+red+"No Discount")
print("")
print("")
print(bold+"PROBLEM 6: LARGEST AMONG THREE NUMBERS")
print("")
number1=float(input(bold+"Enter the first number: "))
number2=float(input(bold+"Enter the second number: "))
number3=float(input(bold+"Enter the third number: "))
if number1>number2 and number1>number3:
    largest=number1
elif number2>number3 and number2>number1:
    largest=number2
else:
    largest=number3
print("")
print(green+bold+"The largest number is:"+end, f"{largest}")
print("")
print("")
print(bold+"PROBLEM 7: SALARY BONUS CALCULATOR")
print("")
salary=float(input("Enter salary: "))
years_of_service=int(input("Enter years of service: "))
if years_of_service >= 10:
    bonus=salary*0.10
elif years_of_service >= 5:
    bonus=salary*0.05
else:
   bonus=0
final_salary=salary+bonus
print(f"Final salary with bonus: {final_salary}")
print("")
print("")
print(bold+"PROBLEM 8: SIMPLE ATM MENU")
print("")
print(bold+"ATM Menu")
print(bold+"1.Balance Inquiry")
print(bold+"2.Deposit")
print(bold+"3.Withdraw")
print(bold+"4.Exit")
print("")
choice=int(input("Enter your choice: "+end))
if choice==1:
    print(bold+green+"You chose Balance Inquiry."+end)
    print(bold+"Click enter to continue.")
elif choice==2:
    print(bold+green+"You chose Deposit. "+end)
    print(bold+"Click enter to continue transaction.")
elif choice==3:
    print(bold+green+"You chose Withdraw."+end)
    print(bold+"Click enter to input amount.")
elif choice==4:
    print(bold+green+"You chose Exit."+end)
    print(bold+"Thank you for using!")
print("")
print("")
print(bold+"PROBLEM 9: SELECTING A BEVERAGE"+end)
print("")
print(bold+"Select Beverage")
print(bold+"1.Coke")
print(bold+"2.Sprite")
print(bold+"3.Royal")
print(bold+"4.Water")
print(bold+"5.Coffee")
print("")
choice=int(input(bold+"Select Beverage:"+end))
if (choice==1):
    print(bold+green+"You chose COKE"+end)
elif (choice==2):
    print(bold+green+"You chose SPRITE"+end)
elif (choice==3):
    print(bold+green+"You chose ROYAL"+end)
elif (choice==4):
    print(bold+green+"You chose WATER"+end)
elif (choice==5):
    print(bold+green+"You chose COFFEE"+end)
print("")
print(bold+"Thank you for choosing!"+end)
print("")
print("")
print(bold+"PROBLEM 10:WHAT IS YOUR HOROSCOPE?")
print("")
print(bold+red+"ZODIAC SIGNS"+end)
Aries=print(bold+"Aries")
Taurus=print(bold+"Taurus")
Gemini=print(bold+"Gemini")
Cancer=print(bold+"Cancer")
Leo=print(bold+"Leo")
Virgo=print(bold+"Virgo")
Libra=print(bold+"Libra")
Scorpio=print(bold+"Scorpio")
Sagittarius=print(bold+"Sagittarius")
Capricorn=print(bold+"Capricorn")
Aquarius=print(bold+"Aquarius")
Pisces=print(bold+"Pisces")
print("")
sign=input(bold+"Your Zodiac Sign:")
if sign=="Aries":
    print(bold+green+"YOUR HOROSCOPE:" +end,"A great opportunity is coming. Lucky color is red. Lucky number is 9.")
elif sign=="Taurus":
    print(bold+green+"YOUR HOROSCOPE:" +end,"Focus on patience and stability. Lucky color is green. Lucky number is 6.")
elif sign=="Gemini":
    print(bold+green+"YOUR HOROSCOPE:" +end,"Expect exciting news soon. Lucky color is yellow. Lucky number is 5.")
elif sign=="Cancer":
    print(bold+green+"YOUR HOROSCOPE:" +end,"Trust your intuition. Lucky color is silver. Lucky number is 2.")
elif sign=="Leo":
    print(bold+green+"YOUR HOROSCOPE:" +end,"Confidence will bring success. Lucky color is gold. Lucky number is 1.")
elif sign=="Virgo":
    print(bold+green+"YOUR HOROSCOPE:" +end,"Stay organized and good luck follows. Lucky color is beige. Lucky number is 7.")
elif sign=="Libra":
    print(bold+green+"YOUR HOROSCOPE:"+end, "Harmony and balance guide your day. Lucky color is pink. Lucky number is 8.")
elif sign=="Scorpio":
    print(bold+green+"YOUR HOROSCOPE:"+end," You will have a lucky day. Lucky color is blue. Lucky number is 3.")
elif sign=="Sagittarius":
    print(bold+green+"YOUR HOROSCOPE:"+end,"Adventure awaits you. Lucky color is purple. Lucky number is 4.")
elif sign=="Capricorn":
    print(bold+green+"YOUR HOROSCOPE:"+end,"Hard work will pay off. Lucky color is black. Lucky number is 10.")
elif sign=="Aquarius":
    print(bold+green+"YOUR HOROSCOPE:"+end, "Be creative and think outside the box. Lucky color is turquoise. Lucky number is 11.")
elif sign=="Pisces":
    print(bold+green+"YOUR HOROSCOPE:"+end,"Embrace your emotions today. Lucky color is sea green. Lucky number is 12.")
else:
    print(bold+red+"Invalid Zodiac Sign")

