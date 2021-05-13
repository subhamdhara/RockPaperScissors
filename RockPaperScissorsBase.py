import random

while True:
    try:
        i = input("Put s for scissors, r for rock, p for paper and q for quit: ")

    except:
        break

    l = ["s", "r", 'p']
    r = random.choice(l)
    if r == i:
        print(f"computer got {r} and you chose {i} its a draw")
    if r == "s" and i == "r" or r == "r" and i == "p" or r == "p" and i == "s":
        print(f"computer got {r} and you chose {i} you win")
    if r == "r" and i == "s" or r == "p" and i == "r" or r == "s" and i == "p":
        print(f"computer got {r} and you chose {i} computer wins")
    if i == "q":
        break
