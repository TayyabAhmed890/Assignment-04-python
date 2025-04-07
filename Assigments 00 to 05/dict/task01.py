# This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

# An example run of the program looks like this (user input is in blue):

# Enter a number: 3 Enter a number: 4 Enter a number: 3 Enter a number: 6 Enter a number: 4 Enter a number: 3 Enter a number: 12 Enter a number: 3 appears 3 times. 4 appears 2 times. 6 appears 1 times. 12 appears 1 times.

def get_list():

    user_numbers = []

    while True:
        usr_inp = input("Enter a Number: ")

        if usr_inp == "":
            break

        num = int(usr_inp)
        user_numbers.append(num)

    return user_numbers

def count_nums(number):

    num_dict = {}
    for num in number:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1

    return num_dict

def print_counts(num_dict):

    for i in num_dict:
        print(f"{i} appears {num_dict[i]} times.")

            

user_numbers = get_list()
num_dict = count_nums(user_numbers)
print_counts(num_dict)