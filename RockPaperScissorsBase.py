import random
import keyboard
import time


def loader():
    ca = ["\ ", "| ", "/ ", "- "]
    print("Deciding:  ", end=" ")
    for i in range(1, 5):
        for l in range(1, 3):
            time.sleep(0.25)
        print("\b\b" + ca[i - 1], end="")
        # print(".", end="")
        time.sleep(0.25)
        # print('\b\b| ', end="")
        # time.sleep(0.25)
        # print("\b\b/ ", end="")
        # time.sleep(0.25)
        # print("\b\b- ", end="")
    print("\b" * 15, end="")


def start():
    l = ["s", "r", 'p']
    while True:

        try:
            player = input("Put s for scissors, r for rock, p for paper and q for quit: ")
        except:
            break

        loader()

        comp = random.choice(l)

        if comp == player:
            print(f"computer got {comp} and you chose {player} its a draw")
        if comp == "s" and player == "r" or comp == "r" and player == "p" or comp == "p" and player == "s":
            print(f"computer got {comp} and you chose {player} you win")
        if comp == "r" and player == "s" or comp == "p" and player == "r" or comp == "s" and player == "p":
            print(f"computer got {comp} and you chose {player} computer wins")

        if player == "q":
            break


start()
