

import random

option = ("rock", "paper", "scissors")
play_on = True

while play_on:
    player = ''
    computer = random.choice(option)

    while player not in option:
        player = input("Enter a choice (rock, paper or scissors): ").lower()

    print(f"player:{player}")
    print(f"computer:{computer}")

    if player == computer:
        print("it's a tie!" )
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You Win!")
    else:
        print("You Lose!!")
        if not input("Do you want to play on? (Y/N): ").lower() == "y":
            play_on = False

print("Thanks for playing")
