import time
import os


bold="\033[1m"
red="\033[31m"
green="\033[32m"
end="\033[0m"
yellow="\033[33m"

print(bold+green+"             🐱🐱WELCOME TO Ulong Pambura PISO WIFI🐱🐱"+end)
print(bold+red+"Please Connect to EraserHeads WiFi Connection."+end)
print("")
print(bold+"1 peso = 10 minutes"+end)
print("")
print(bold+"Select Option:"+end)
a
minutes = 0
rate = 1

while True:
    print(bold+"\n1. Insert Coins"+end)
    print(bold+"2. Check Remaining Time"+end)
    print(bold+"3. Exit"+end)
    print("")
    choice=int(input(bold+yellow+"Enter option:"+end))
    if choice==1:
        coin=int(input(bold+"Inserted Coin amount:"+end))
        if coin > 0:
            updated_time=coin * rate
            minutes += updated_time
            print(bold+green+"Your Updated Time is :"+end,updated_time, bold+"minutes"+end)
        else:
            print(bold+red+"Invalid Amount."+end)

    elif choice == 2:
        print(bold+"You have", minutes, "minutes left"+end)

    elif choice==3:
        print(bold+"Thank you for Using EraserHeads Piso WiFi. Meow!!!"+end)
        print("🐱🐱🐱🐱")
        break

    else:
        print(bold+red+"INVALID OPTION."+end)
        break

