# Import the random module to generate random numbers
import random

# Welcome the user to the game
print("🎯 Welcome to the 'Guess the Number' Game!")
print("I'm thinking of a number between 1 and 100.")
print("Can you guess what it is?\n")

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Initialize the number of attempts the user will make
attempts = 0

# Start an infinite loop for user guesses
while True:
    # Get the user's guess. input() returns a string, so we need to convert it to an integer.
    guess = input("Enter your guess (1 to 100): ")
    
    # Check if the input is a valid number
    if not guess.isdigit():
        print("❌ Please enter a valid number!")
        continue  # If the input is invalid, prompt the user again.
    
    # Convert the guess into an integer
    guess = int(guess)
    attempts += 1  # Increase the number of attempts after each guess

    # Check if the guess is too low, too high, or correct
    if guess < secret_number:
        print("🔻 Too low! Try a higher number.\n")
    elif guess > secret_number:
        print("🔺 Too high! Try a lower number.\n")
    else:
        # If the guess is correct, congratulate the user and show the number of attempts
        print(f"✅ Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
        break  # Exit the loop when the user guesses correctly
