# # Fill out the function shorten(lst) which removes elements from the end of lst, which is a list, and prints each item it removes until lst is MAX_LENGTH items long. If lst is already shorter than MAX_LENGTH you should leave it unchanged. We've written a main() function for you which gets a list and passes it into your function once you run the program. For the autograder to pass you will need MAX_LENGTH to be 3, but feel free to change it around to test your program.

# CODE LOGIC SOLUTION

# CREATE A MAX LENGTH VARIABLE WHICH VALIDATE JUST SEE LAST 3 VALUES OF LIST 

MAX_LENGTH = 3

# CREATE A FUNCTION WHICH IMPLEMENT LAST ELEM LOGIC VIA POP METHOD

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        last_elem = lst.pop()
        print(last_elem)

# CREATE ANOTHER FUNCTION WHICH IS DIPLAY OVERALL WORKING

def get_list():
    lst = []
    user_inp:str = input("Please enter an element of the list or press enter to stop. ")

    while user_inp != "":
        lst.append(user_inp)
        user_inp:str = input("Please enter an element of the list or press enter to stop. ")
    return lst
        
# CALL THE FUNCTIONS

lst = get_list()
shorten(lst)
