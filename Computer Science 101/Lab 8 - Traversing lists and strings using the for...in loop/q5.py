# ask for the user to enter something
user_input = input("Enter your text: ")
# create a blank string
output = ""
# loop through each character in user_input
for character in user_input:
    # if the character is an alphabetical character
    if character.isalpha():
        # add the character to the blank string
        output += character
# print output
print(output)
