import random

while True:
    try:
        i = input("Put s for scissors, r for rock and p for paper: ")

    except:
        break

    l = ["s", "r", 'p']
    r = random.choice(l)
    if r == i:
        print(f"computer got {r} and you chose {i} its a draw")
    if r == "s" and i == "r" or r == "r" and i == "p":
        print(f"computer got {r} and you chose {i} you win")
        break
    if r == "r" and i == "s" or r == "p" and i == "r":
        print(f"computer got {r} and you chose {i} computer wins")
        break
