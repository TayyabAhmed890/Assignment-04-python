# Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element in the list. The list is guaranteed to be non-empty. We've written some code for you which prompts the user to input the list one element at a time.

# CODE LOGIC SOLUTION

# CREATE A FUNCTION WHICH TAKE LIST AS A PARAMETER AND SHOW FIRST INDEX VALUE

def get_first_elem(lst):
    print(lst[0])

# CREATE ANOTHER FUNCTION WHICH IS USER GIVE INPUT

def get_list():
    lst:list[int] = []
    user_inp:str = input("Please enter an element of the list or press enter to stop. ")

# USING WHILE LOOP IN THIS PART AND APPEND THE GIVEN VALUE IN LST VARIABLE

    while user_inp != "":
        lst.append(user_inp)
        user_inp:str = input("Please enter an element of the list or press enter to stop. ")
    return lst

# LST IS EQUAL TO GET LIST FUNCTION ITS TAKE ALL FUNCTIONALLITY IN VARIABLE

lst = get_list()

# NOW WE PASS THE VARIABLE IN FUNCTION AS A ARGUMENT

get_first_elem(lst)

