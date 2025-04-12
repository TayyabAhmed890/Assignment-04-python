# Guess My Number

# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

# Enter a new number: 25 Your guess is too low

# Enter a new number: 40 Your guess is too low

# Enter a new number: 45 Your guess is too low

# Enter a new number: 48 Congrats! The number was: 48

import random

# Randomly choose a number between 0 and 99
secret_number = random.randint(0, 99)

# Ask the user for their first guess
guess = int(input("I am thinking of a number between 0 and 99... Enter a guess: "))

# Keep asking until the guess is correct
while guess != secret_number:
    if guess > secret_number:
        print("Your guess is too high")
    else:
        print("Your guess is too low")
    
    # Ask for a new guess
    guess = int(input("Enter a new number: "))

# User guessed correctly
print(f"Congrats! The number was: {secret_number}")
