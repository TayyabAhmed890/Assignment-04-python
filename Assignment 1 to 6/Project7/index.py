import random
import string

def generate_password(length=12):
    # Define the characters that the password can consist of
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly select characters to form the password
    password = ''.join(random.choice(all_characters) for i in range(length))
    
    return password

def main():
    print("Welcome to the Password Generator!")
    
    # Get password length from the user
    try:
        length = int(input("Enter the length of the password (e.g., 12): "))
        
        # Ensure the length is valid (positive number)
        if length < 8:
            print("Password should be at least 8 characters long for security reasons.")
        else:
            # Generate and display the password
            generated_password = generate_password(length)
            print(f"Your generated password is: {generated_password}")
    
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
