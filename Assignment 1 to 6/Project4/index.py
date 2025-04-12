# Importing the random module to generate a random choice for the computer
import random

# Function to get the user's choice
def get_user_choice():
    # Asking the user to enter their choice
    choice = input("Enter your choice (rock, paper, or scissors): ").lower()

    # Validating the user's input
    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        choice = input("Enter your choice (rock, paper, or scissors): ").lower()

    return choice

# Function to get the computer's choice
def get_computer_choice():
    # Randomly selecting the computer's choice from the list
    return random.choice(["rock", "paper", "scissors"])

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    # Comparing the choices and determining the winner
    if user_choice == computer_choice:
        return "It's a tie!"

    if (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "paper" and computer_choice == "rock") or \
       (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"

    return "You lose!"

# Main function to run the game
def play_game():
    # Display a welcome message
    print("Welcome to Rock, Paper, Scissors Game!")

    # Get the user's choice
    user_choice = get_user_choice()

    # Get the computer's choice
    computer_choice = get_computer_choice()

    # Display the choices made by the user and the computer
    print(f"\nYou chose: {user_choice}")
    print(f"The computer chose: {computer_choice}")

    # Determine and display the winner
    result = determine_winner(user_choice, computer_choice)
    print(result)

# Running the game
if __name__ == "__main__":
    play_game()
