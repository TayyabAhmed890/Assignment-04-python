# Write a program to solve this age-related riddle!

# Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:

# Anton is 21 years old.

# Beth is 6 years older than Anton.

# Chen is 20 years older than Beth.

# Drew is as old as Chen's age plus Anton's age.

# Ethan is the same age as Chen.

# Your code should store each person's age to a variable and print their names and ages at the end. The autograder is sensitive to capitalization and punctuation, be careful! Your solution should look like this (the below numbers are made up -- your solution should have the correct values!):

# LOGIC CODE SOLUTION

# STORE AGES

Anton:int = 21 

Beth:int = 6 + Anton

Chen:int = 20 + Beth

Drew:int = Chen + Anton

Ethan:int = Chen

# PRINTS THE VALURE USING FSTRING

print(f"Anton: {Anton}\nBeth: {Beth}\nChen: {Chen}\nDrew: {Drew}\nEthan: {Ethan}")
