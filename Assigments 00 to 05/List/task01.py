# Write a function that takes a list of numbers and returns the sum of those numbers.

# LOGIC CODE SOLUTION

# CREATE A FUNCTION WHICH TAKE VALUES FROM LIST THEN SUM IT

def sum_of_num(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# CREATING LIST

list_numbers:list[int] = [2,4,5,7,10]

# SEND THE LIST TO FUNCTION AS PARAMETER AND STORE IN VARIABLE

result:int = sum_of_num(list_numbers)

# PRINTS THE VALUE

print(f"Given List: {list_numbers}\nResult: {result}")
