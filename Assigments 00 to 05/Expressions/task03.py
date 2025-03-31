# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

INCHES_IN_FOOT:int = 12

user_inp_feet:float = float(input("Enter Number in Feets: "))

calculate_inch = user_inp_feet * INCHES_IN_FOOT

print(f"That is {calculate_inch} inches!")

