def mad_libs_game():
    print("🎉 Welcome to the Mad Libs Game!")
    print("Fill in the blanks to create a funny story.\n")

    # Ask the user for different types of words
    name = input("Enter a name: ")
    place = input("Enter a place: ")
    adjective1 = input("Enter an adjective: ")
    adjective2 = input("Enter another adjective: ")
    noun1 = input("Enter a noun: ")
    animal = input("Enter an animal: ")
    verb = input("Enter a verb (present tense): ")
    food = input("Enter a type of food: ")

    # Create the story using the inputs
    story = f"""
    One day, {name} went to {place}. It was a {adjective1} day.
    While walking, {name} saw a {adjective2} {noun1} next to a {animal}.
    Suddenly, they decided to {verb} with the {animal}!
    After all the fun, they ate some delicious {food} and went home laughing.

    The end! 😄
    """

    print("\nHere's your Mad Libs story:")
    print(story)

# Run the game
mad_libs_game()
