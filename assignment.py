bold="\033[1m"
red="\033[31m"
end="\033[0m"
green="\033[32m"

while True:
    p1=input(bold+"Player 1 (rock/paper/scissors or quit):"+end).lower()
    if p1 == "quit":
        break

    p2= input(bold+"Player 2 (rock/paper/scissors or quit):"+end).lower()
    if p1 == "quit":
        break

    if p1==p2:
        print(bold+"It's a Tie"+end)
    elif (p1=="paper" and p2=="rock") or \
         (p1 == "scissors" and p2 == "paper") or \
         (p1 == "rock" and p2 == "scissors"):
        print(bold+green+"You Won!!!!!"+end)
    else:
        print(bold+red+"You Lose!!!!!"+end)
