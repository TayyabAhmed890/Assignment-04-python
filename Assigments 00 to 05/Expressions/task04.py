import math

usr_inp_ab = float(input("Enter the length of AB: "))
usr_inp_ac = float(input("Enter the length of AC: "))

bc:float = math.sqrt(usr_inp_ab ** 2 + usr_inp_ac ** 2)

print(f"The length of BC (the hypotenuse) is: {bc}")

