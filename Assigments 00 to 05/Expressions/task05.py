user_inp_1 = int(input("Please enter an integer to be divided: "))
user_inp_2 = int(input("Please enter an integer to divide by: "))

formula = user_inp_1 // user_inp_2
reminder = user_inp_1 % user_inp_2

print(f"The result of this division is {formula} with a remainder of {reminder}")