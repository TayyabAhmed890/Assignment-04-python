# Ask the user for a number and print its square (the product of the number times itself).

# Here's a sample run of the program (user input is in bold italics):

# Type a number to see its square: 4

# 4.0 squared is 16.0


# LOGIC CODE SOLUTION

# ANSI escape codes for styling

BOLD = "\033[1m"
ITALIC = "\033[3m"
RESET = "\033[0m"

# TAKE INPUT FROM USER

user_inp = float(input("Type a number to see its square: "))

# APPLY FORMULA

square = user_inp ** 2

# PRINT THE VALUE

print(f"{BOLD}{ITALIC}{user_inp}{RESET} squared is {BOLD}{ITALIC}{square}{RESET}")