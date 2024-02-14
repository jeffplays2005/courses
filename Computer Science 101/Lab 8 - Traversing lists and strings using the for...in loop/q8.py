user_input = input("Enter your text: ")
to_find = input("Enter the target word: ")
# split words by a space into a list
individual_words = user_input.split(" ")
# declare variables
grammar = "s"
found_times = 0
# loop through each word
for word in individual_words:
    # if the word matches the target, add 1 to the found_times
    if word.lower() == to_find.lower():
        found_times += 1
# match the grammatical requirements of this question
if found_times == 1:
    grammar = ""
# print output
print(f"The word '{to_find}' is found {found_times} time{grammar} in the text.")
