bold = "\033[1m"
yellow = "\033[93m"
green = "\033[92m"
red = "\033[91m"
end = "\033[0m"

print(bold+red+"Type 1 if suko na"+end)
print(bold+green+"Type 2 if kaya pa"+end)
print("")


choice=int(input(bold+"Enter your choice:"))
print("")
if choice == 1:
    print(bold+red+"Tangina Surrender ka na boi"+end)
elif choice == 2:
    print(bold+green+"Tibay mo naman gar"+end)
else:
    print("GAGO")
