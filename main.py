
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

        """check if guess is either lower or higher the the number, then start over again, but if guess is correct you exit the game """
        if guess > number:
            print(f"{guess} is too High!")
        elif guess < number:
            print(f"{guess} is too Low!")
        else:
            print(f"{guess} is CORRECT!")
            break

make_a_guess()