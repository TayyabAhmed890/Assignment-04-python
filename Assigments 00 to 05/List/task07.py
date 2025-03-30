# Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.

# Here's a sample run (user input is in blue):

# Enter a value: 1 Enter a value: 2 Enter a value: 3 Enter a value: Here's the list: ['1', '2', '3']

# CODE LOGIC SOLUTION

def lst_work():
# CREATE A LST NAME VARIABLE
    lst = []
# TAKE INPUT FROM USER
    user_inp = input("Enter a value: ") 
# USING WHILE LOOP APPEND THE GIVEN VALUE IN LIST
    while user_inp:
        lst.append(user_inp)
        user_inp = input("Enter a value: ")
    return lst

# PRINT THE VALUE 

print(f"Here is the List: {lst_work()}")

