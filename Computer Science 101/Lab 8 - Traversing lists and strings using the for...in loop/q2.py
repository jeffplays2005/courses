# create a new list
word_list = []
# ask for a sequence of words
# lowercase the user input
# sorting the words uses the ASCII index, lowercase is not the same as uppercase!
sequence_of_words = input("Please enter a sequence of words: ").lower()
# split the words by " " into an list of strings
# e.g. "Hello my name is Andrew"
# [ "Hello", "my", "name", "is", "Andrew" ]
individual_words = sequence_of_words.split(" ")
# sort the words by alphabetical order
# you can use individual_words.sort()
# e.g. [ "Andrew", "hello", "is", "my", "name" ]
sorted_words = sorted(individual_words)
# loop through each item in the list, i for the index
for i, item in enumerate(sorted_words):
    # print the output
    # we need to .capitalize() because the first letter is lowercase
    # e.g. 2. Is
    print(f"{i}. {item.capitalize()}")
