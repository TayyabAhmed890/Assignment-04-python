# Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length

# CODE LOGIC SOLUTION

# CREATE A FUNCTION THAT SHOW LAST ELEM OF LIST

def get_last_elem(lst):
    print(lst[-1])
    # print(lst[len(lst) - 1])

# CREATE ANOTHER FUNCTION FOR CREATE LST VARIABLE TAKE USER INPUT

def get_list():
    lst = []
    user_inp:str = input("Please enter an element of the list or press enter to stop. ")

# USING WHILE LOOP APPEND THE GIVEN VALUES IN LIST

    while user_inp != "":
        lst.append(user_inp)
        user_inp:str = input("Please enter an element of the list or press enter to stop. ")
    return lst

# ALLOVER FUNCTION STORE IN VARIABLE

lst = get_list()

# CALL THE FUNCTIONS WITH PARAMETER

get_last_elem(lst)
