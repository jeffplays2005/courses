def word_length_analysis(text):
    individual_words = text.split(' ')
    word_length_dict = {}
    for i in individual_words:
        ocurrencies = 0
        for a in individual_words:
            if len(i) == len(a):
                ocurrencies += 1
        word_length_dict[len(i)] = ocurrencies
    return word_length_dict
text = "The quick brown fox jumps over the lazy dog"
word_length_dict = word_length_analysis(text)
for key in sorted(word_length_dict):
    print(f"Word Length: {key}, Number of Words: {word_length_dict[key]}")