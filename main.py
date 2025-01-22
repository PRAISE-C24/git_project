
import random

def make_a_guess():
    """this function generates a random number 0-100 and ask the player to guess the number, if the player's guess is lower or higher than the number the game continues, but if the player's guess is correct the game exits automatically. the player can also enter q to quit the game.
    """
    number = random.randint(0, 100)


    while True:
        guess = input("Guess the Number [q]: ")

        """if guess is equal to q, Quit the Game"""
        if guess.lower() == "q":
            print("Game Over, Try Again Later!")
            break

        """if guess is not an integer start all over"""
        try:
            guess = int(guess)
        except ValueError:
           print(f"{guess} is Not a valid Guess!")
           continue

        """check if guess is either lower or higher the the number, then start over again, but if guess is correct you exit the game 
        """
        if guess > number:
            print(f"{guess} is too High!")
        elif guess < number:
            print(f"{guess} is too Low!")
        else:
            print(f"{guess} is CORRECT!")
            break

# make_a_guess()

"""
 Feature 2.
 this third feature is simple Rock, Paper, Scissors game.
"""

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