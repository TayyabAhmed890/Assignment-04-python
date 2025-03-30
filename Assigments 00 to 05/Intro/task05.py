# Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).

# Here's a sample run of the program (user input is in bold italics):

# What is the length of side 1? 3

# What is the length of side 2? 4

# What is the length of side 3? 5.5

# The perimeter of the triangle is 12.5

# LOGIC CODE SOLUTION

# ANSI escape codes for styling

BOLD = "\033[1m"
ITALIC = "\033[3m"
RESET = "\033[0m"

# TAKE USER INPUTS

user_inp_side1 = float(input("What is the length of side 1? "))
user_inp_side2 = float(input("What is the length of side 2? "))
user_inp_side3 = float(input("What is the length of side 3? "))

# APPLY FORMULA

perimeter_value_triangle = user_inp_side1 + user_inp_side2 + user_inp_side3

# PRINTS THE VALUE

print(f"The perimeter of the triangle is: {BOLD}{ITALIC}{perimeter_value_triangle}{RESET}")