import random

# Total number of rounds
NUM_ROUNDS = 5

# Player score initialization
score = 0

print("Welcome to the High-Low Game!")
print("--------------------------------")

# Game loop for multiple rounds
for round_num in range(1, NUM_ROUNDS + 1):
    print(f"Round {round_num}")
    
    # Generate random numbers
    player_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)
    
    # Show player number (computer's number is hidden)
    print(f"Your number is {player_number}")
    
    # Get and validate user guess
    guess = input("Do you think your number is higher or lower than the computer's?: ").lower()
    while guess != "higher" and guess != "lower":
        guess = input("Please enter either 'higher' or 'lower': ").lower()
    
    # Game logic
    correct = False
    if guess == "higher" and player_number > computer_number:
        correct = True
    elif guess == "lower" and player_number < computer_number:
        correct = True
    
    # Print result
    if correct:
        print(f"You were right! The computer's number was {computer_number}")
        score += 1
    else:
        print(f"Aww, that's incorrect. The computer's number was {computer_number}")
    
    # Show current score
    print(f"Your score is now {score}\n")

# Final message after all rounds
print("Thanks for playing!")

if score == NUM_ROUNDS:
    print("Wow! You played perfectly!")
elif score >= NUM_ROUNDS // 2:
    print("Good job, you played really well!")
else:
    print("Better luck next time!")
