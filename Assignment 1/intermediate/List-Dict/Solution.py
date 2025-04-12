# -------------------------------
# Problem #1: List Practice
# -------------------------------

def list_practice():
    # Create a list called `fruit_list`
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    
    # Print the length of the list
    print("Length of fruit list:", len(fruit_list))
    
    # Add 'mango' at the end of the list
    fruit_list.append('mango')
    
    # Print the updated list
    print("Updated fruit list:", fruit_list)


# -------------------------------
# Problem #2: Index Game
# -------------------------------

# Function to access element by index
def access_element(my_list, index):
    if 0 <= index < len(my_list):
        return f"Element at index {index}: {my_list[index]}"
    else:
        return "Index out of range."

# Function to modify element at index
def modify_element(my_list, index, new_value):
    if 0 <= index < len(my_list):
        old_value = my_list[index]
        my_list[index] = new_value
        return f"Replaced '{old_value}' with '{new_value}'.", my_list
    else:
        return "Index out of range.", my_list

# Function to slice the list
def slice_list(my_list, start, end):
    if 0 <= start <= len(my_list) and 0 <= end <= len(my_list) and start < end:
        return my_list[start:end]
    else:
        return "Invalid slice range."

# Game interaction function
def index_game():
    my_list = ['apple', 'banana', 'cherry', 'date', 'fig']

    while True:
        print("\n--- Index Game ---")
        print("Current List:", my_list)
        print("Choose an operation:")
        print("1. Access element")
        print("2. Modify element")
        print("3. Slice list")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            idx = int(input("Enter index to access: "))
            print(access_element(my_list, idx))

        elif choice == "2":
            idx = int(input("Enter index to modify: "))
            val = input("Enter new value: ")
            msg, my_list = modify_element(my_list, idx, val)
            print(msg)

        elif choice == "3":
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print("Sliced list:", slice_list(my_list, start, end))

        elif choice == "4":
            print("Exiting the game. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


# -------------------------------
# Main Function
# -------------------------------

def main():
    print("=== Problem #1 ===")
    list_practice()
    
    print("\n=== Problem #2 ===")
    index_game()

# Run the program
main()
