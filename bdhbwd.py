import time
import os

minutes = 0
rate = 10   # 1 coin = 10 minutes

# (Optional) Color formatting — remove if not needed
bold = "\033[1m"
yellow = "\033[93m"
green = "\033[92m"
red = "\033[91m"
end = "\033[0m"

while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    print(bold+"============================="+end)
    print(bold+"   ERASERHEADS PISO WIFI"+end)
    print(bold+"============================="+end)

    print(bold+"\n1. Insert Coins"+end)
    print(bold+"2. Check Remaining Time"+end)
    print(bold+"3. Start Timer"+end)
    print(bold+"4. Exit"+end)

    choice = int(input(bold+yellow+"\nEnter option: "+end))

    # Insert Coins
    if choice == 1:
        coin = int(input(bold+"Inserted coin amount: "+end))

        if coin > 0:
            added_time = coin * rate
            minutes += added_time
            print(green+f"Added {added_time} minutes."+end)
            time.sleep(2)
        else:
            print(red+"Invalid amount."+end)
            time.sleep(2)

    # Check Remaining Time
    elif choice == 2:
        print(green+f"You have {minutes} minutes remaining."+end)
        input("\nPress Enter to continue...")

    # Start the countdown timer
    elif choice == 3:
        if minutes <= 0:
            print(red+"No remaining time. Please insert coins."+end)
            time.sleep(2)
        else:
            while minutes > 0:
                os.system('cls' if os.name == 'nt' else 'clear')

                print(bold+"TIMER RUNNING…"+end)
                print(f"Remaining Time: {minutes} minutes")

                time.sleep(60)   # 1 minute delay
                minutes -= 1

            print(red+"\nYour time has expired!" + end)
            time.sleep(2)

    # Exit Program
    elif choice == 4:
        print(bold+"Thank you for using EraserHeads Piso WiFi. Meow!!!"+end)
        print("🐱🐱🐱🐱")
        break

    else:
        print(red+"Invalid option."+end)
        time.sleep(2)
