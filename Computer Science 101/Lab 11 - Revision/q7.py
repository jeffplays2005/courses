def main():
   sentence = get_sentence()
   vowels = get_number_of_vowels(sentence)
   spaces = get_number_of_spaces(sentence)
   percentage = calculate_percentage(vowels, spaces, len(sentence))
   display_feedback(percentage)

def get_sentence():
    return input("Enter a sentence: ")

def get_number_of_vowels(sentence):
    sentence = sentence.lower()
    vowels = 'aeiou'
    count = 0
    for letter in sentence:
        if letter in vowels:
            count += 1
    return count

def get_number_of_spaces(sentence):
    count = 0
    for letter in sentence:
        if letter == ' ':
            count += 1
    return count

def calculate_percentage(num_vowels, num_spaces, sentence_length):
    value = sentence_length - num_spaces
    percentage = num_vowels * 100 / value
    return percentage
    
def display_feedback(percentage):
    print(round(percentage), "% are vowels.", sep="")
