# In this program we show an example of using dictionaries to keep track of information in a phonebook

def phone_number():

    phonebook = {}
    while True:
        usr_name = input("Name: ")
        if usr_name == "":
            break

        usr_number = int(input("Number: "))
        phonebook[usr_name] = usr_number

        return phonebook
    
def print_phonebook(phonebook):
    for i in phonebook:
        print(f"{i} -> {phonebook[i]}")

def lookup_number(phonebook):

    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break
        if name not in phonebook:
            print(name + " is not in the phonebook")
        else:
            print(phonebook[name])


phonebook = phone_number()
print_phonebook(phonebook)
lookup_number(phonebook)
