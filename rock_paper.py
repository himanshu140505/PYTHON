from systemcommands import *
import random

def rock_paper_logo():
    print("================================================")
    print("||             ROCK PAPER SCISSORS            ||")
    owner()
    print("================================================")

def rock_paper():
    choices = ["Rock", "Paper", "Scissor"]
    user_choice = 1

    while user_choice != 0:
        clearscreen()

        rock_paper_logo()
        print("================================================")
        print("|| Enter your choice:                         ||")
        print("||   1. Rock                                  ||")
        print("||   2. Paper                                 ||")
        print("||   3. Scissor                               ||")
        print("================================================")

        user_choice = int(input("Enter your choice : "))

        clearscreen()

        if user_choice == 0:
            break

        computer_choice = random.randint(1, 3)

        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        if user_choice == computer_choice:
            print("|                It's a tie babe....            |")
        elif user_choice == 1 and computer_choice == 2:
            print("|                You Won!!!!                    |")
        elif user_choice == 1 and computer_choice == 3:
            print("|                You Won!!!!                    |")
        elif user_choice == 3 and computer_choice == 2:
            print("|                You Won!!!!                    |")
        else:
            print("|                You Lose.....                  |")
        print(f"| Your choice: {choices[user_choice-1]} || Computer choice: {choices[computer_choice-1]} |")
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

        sleepfn(2)


rock_paper()