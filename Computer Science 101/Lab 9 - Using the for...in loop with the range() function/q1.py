# user input
input_sentence = input("Please enter some lowercase text: ")
# split the input into individual sentences
# e.g. input_sentence = "hello world. i am new to this world."
# this would then return:
# [ 'hello world', 'i am new to this world.' ]
individual_sentences = input_sentence.split(". ")
# create new list
sentences_with_capital_letter = []
# loop through each sentence
for sentence in individual_sentences:
    # 1. "hello world"
    # 2. "i am new to this world."
    # new list
    capital_sentence = []
    # loop through each character in sentence
    for i, letter in enumerate(sentence):
        # if it is the first character
        if i == 0:
            # add the uppercase char
            capital_sentence.append(letter.upper())
        else: # not the first character
            # add whatever character it was
            capital_sentence.append(letter)
    # add to the sentences with capital letter
    sentences_with_capital_letter.append("".join(capital_sentence))
# output
print(". ".join(sentences_with_capital_letter))
