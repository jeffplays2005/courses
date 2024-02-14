# declare what vowels are
vowels = "aeiou"
# ask for a user input
user_input = input("Enter your text: ")
# create a blank string
output = ""
# loop through each character in user_input
for character in user_input:
    # apparently uppercase characters aren't in the alphabet...lower case!
    # i lost 0.05...0.1...
    lower_character = character.lower()
    # an if statement to check if the character is a vowel
    if lower_character not in vowels:
        # of the character isn't a vowel, add the the blank string
        output += character
# print output
print(output)
