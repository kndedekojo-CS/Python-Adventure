# This function checks if the guess is correct.
def unlock_door(guess):
    if guess == 7:
        print("The door opens!")
    elif guess < 7:
        print("Your guess is too low!")
    else:
        print("Your guess is too high!")


# This asks the player to guess the secret number.
guess = int(input("Guess the secret number: "))

# This calls the function.
unlock_door(guess)