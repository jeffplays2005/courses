# create a new list
list_of_numbers = []
# create a while loop, this continues until a break
while True:
    # ask for a user input, do not use float() or int() because TypeError
    user_input = input("Please enter an integer or end to quit: ");
    # if the user_input is a digit...
    if user_input.isdigit():
        # add the digit to the list_of_numbers list
        list_of_numbers.append(int(user_input))
    # when the user wants to end, break out of the while loop
    elif user_input == "end":
        # break!
        break
# sort the numbers into numerical order and reverse the list
# e.g. [ 100, 20, 60, 40]
# sorted: [ 20, 40, 60, 100 ]
# reversed: [ 100, 60, 40, 20 ]
list_of_numbers.sort(reverse = True)
# print output
print(f"Integers entered: {list_of_numbers}")
