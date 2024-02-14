def get_player_guess():
    user_input = input("Please enter your guess: ") # prompt user for input
    # keep looping while the length is not 5 or
    # the input is not alphabetical
    while len(user_input) != 5 or user_input.isalpha() == False:
        user_input = input("Your guess must have 5 letters: ")
    # return the value when the while loop has finished
    return user_input.lower()

# testing cases
print(get_player_guess())