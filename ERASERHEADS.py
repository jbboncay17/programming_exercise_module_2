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
print(bold+"1 peso = 1 minute/s"+end)
print("")
print(bold+"Select Option:"+end)

minutes = 0
rate = 1

while True:
    print(bold+"\n1. Insert Coins"+end)
    print(bold+"2. Check Time/Minutes Remaining"+end)
    print(bold+"3. Exit"+end)
    print("")
    choice=int(input(bold+yellow+"Enter option:"+end))
    if choice==1:
        coin=int(input(bold+"Inserted Coin amount:"+end))
        if coin > 0:
            updated_time=coin * rate
            minutes += updated_time
            print(bold+green+"Your Updated Time is :"+end,updated_time, bold+"minute/s"+end)
        else:
            print(bold+red+"Invalid Amount."+end)

    elif choice == 2:
        if minutes <= 0:
            print(red + "No remaining time. Please insert coins." + end)
            time.sleep(2)
        else:
            while minutes > 0:
                os.system('cls' if os.name == 'nt' else 'clear')

                print(bold+red+"MINUTES REMAINING:…"+end)
                print(bold+f"Remaining Time: {minutes} minute/s"+end)

                time.sleep(5)
                minutes -= 1

            print(red +"\nOoopss. Your time has expired!" + end)
            time.sleep(2)

    elif choice==3:
        print(bold+"===Thank you for Using EraserHeads Piso WiFi. Meow!!!==="+end)
        print("                       🐱🐱🐱🐱")
        break

    else:
        print(bold+red+"INVALID OPTION."+end)
        time.sleep(2)
        break

