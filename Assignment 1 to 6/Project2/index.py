# Importing the random module to generate random numbers
import random

# Welcoming the user
print("🎯 Welcome to the 'Guess the Number' Game!")
print("I'm thinking of a number between 1 and 100.")
print("Can you guess what it is?\n")

# Randomly generate a number between 1 and 100
secret_number = random.randint(1, 100)

# Variable to keep track of the number of attempts
attempts = 0

# Infinite loop that will keep asking the user until they guess correctly
while True:
    # Ask the user for their guess and convert it to an integer
    guess = input("Enter your guess: ")
    
    # Check if the input is a digit
    if not guess.isdigit():
        print("❌ Please enter a valid number!")
        continue  # Go back to asking for input
    
    # Convert input to integer
    guess = int(guess)
    attempts += 1  # Increase attempt count

    # Check the guess
    if guess < secret_number:
        print("🔻 Too low! Try a higher number.\n")
    elif guess > secret_number:
        print("🔺 Too high! Try a lower number.\n")
    else:
        # Correct guess
        print(f"✅ Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
        break  # Exit the loop
