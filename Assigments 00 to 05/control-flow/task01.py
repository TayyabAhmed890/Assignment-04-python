# Guess My Number

# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

# Enter a new number: 25 Your guess is too low

# Enter a new number: 40 Your guess is too low

# Enter a new number: 45 Your guess is too low

# Enter a new number: 48 Congrats! The number was: 48

import random

rand_num = random.randint(0,99)

print("I am thinking of a number between 1 and 99...")

guess = int(input("Enter a guess: "))

while guess != rand_num:
     if guess < rand_num:  # If-statement is True if guess is less than secret number
        print("Your guess is too low")
     else:
        print("Your guess is too high")

     print() # Print an empty line to tidy up the console for new guesses
     guess = int(input("Enter a new guess: "))  # Get a new guess from the user
        
print("Congrats! The number was: " + str(rand_num))