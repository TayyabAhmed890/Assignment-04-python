# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.

import random

NUM_SIDES = 6

def roll_dice():
    die1:int = random.randint(1,NUM_SIDES)
    die2:int = random.randint(1,NUM_SIDES)
    total:int = die1+die2
    print(f"Total of Two dies {total}")


die1:int = 10
print(f"die1 in main() starts as: {str(die1)}")
roll_dice()
roll_dice()
roll_dice()
print(f"die1 in main() is: {str(die1)}")


