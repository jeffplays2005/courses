def get_input(list_of_valid_choices):
    # start off the prompt
    user_input = input("Enter a value: ")
    # if the user input was not inside the valid choices list that was provided, keep while looping
    # also exit if quit is used
    while user_input not in list_of_valid_choices and user_input != "quit":
        # rewrite what user_input is
        user_input = input("Enter a value: ")
    # while loop has finished, return the user_input that was correct
    return user_input