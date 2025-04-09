# Fill out the function count_even(lst) which

# first populates a list by prompting the user for integers until they press enter (please use the prompt "Enter an integer or press enter to stop: "),

# and then prints the number of even numbers in the list.

# If you'd prefer to focus on the second task only, scroll down for our implementation of the first task!

def count_even(lst):
    count = 0
    for i in lst:
        if i % 2 == 0:
            count += 1

    print(f"The Even Number in List is {count}")

def get_list():
    lst = []
    usr = input("Enter an integer or press enter to stop: ")
    while usr != "":
        lst.append(int(usr))
        usr = input("Enter an integer or press enter to stop: ")

    return lst


lst = get_list()
count_even(lst)