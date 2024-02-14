# given by question
lowercase_alpha = "abcdefghijklmnopqrstuvwxyz"
uppercase_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# user input...
user_input = input("Please enter your text: ")
# blank str
new_text = ""
# loop through user_input
for char in user_input:
    # if the char is lowercase
    if char in lowercase_alpha:
        # add to the new_text string
        new_text += char.upper()
    # if the char is uppercase
    elif char in uppercase_alpha:
        # add to the new_text string
        new_text += char.lower()
    # isn't an alphabetical character, don't lower/upper, just add to the string
    else:
        # add to the new_text string
        new_text += char
# output
print(f"New text: {new_text}")
