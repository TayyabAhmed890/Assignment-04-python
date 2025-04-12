import random

# List of words to choose from
word_list = ['python', 'java', 'javascript', 'hangman', 'computer', 'programming', 'developer']

# Function to choose a random word from the list
def get_random_word():
    return random.choice(word_list)

# Function to display the current status of the word with guessed letters and underscores for unguessed letters
def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display.strip()

# Function to play the hangman game
def play_game():
    print("Welcome to Hangman Game!")
    
    # Choose a random word from the word list
    word = get_random_word()
    guessed_letters = []  # List to store guessed letters
    incorrect_guesses = 0  # Counter for incorrect guesses
    max_incorrect_guesses = 6  # Max incorrect guesses allowed
    
    # Game loop
    while incorrect_guesses < max_incorrect_guesses:
        print("\nWord to guess: " + display_word(word, guessed_letters))
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        
        # Ask the user for a letter guess
        guess = input("Guess a letter: ").lower()
        
        # Validate the guess input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
        
        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
        
        # Add the guess to the list of guessed letters
        guessed_letters.append(guess)
        
        # Check if the guessed letter is in the word
        if guess in word:
            print(f"Good guess! The letter '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Oops! The letter '{guess}' is not in the word.")
        
        # Check if the user has guessed all letters in the word
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You've guessed the word: " + word)
            break
        
    # If the player has used up all incorrect guesses, they lose
    if incorrect_guesses == max_incorrect_guesses:
        print(f"\nGame Over! The word was: {word}")

# Running the game
if __name__ == "__main__":
    play_game()
