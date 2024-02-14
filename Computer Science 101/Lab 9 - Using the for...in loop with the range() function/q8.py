# user input
sequence_of_words = input("Enter a sequence of words: ")
# split into individual words
individual_words = sequence_of_words.split(" ")
# blank strings
first = ""
second = ""

for number in range(0, len(individual_words), 1):
    if((number + 1 )% 2 == 0):
        second += individual_words[number] + " "
    else:
        first += individual_words[number] + " "
        
print("1. "+first)
print("2. "+second)
