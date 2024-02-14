def get_letter_frequency(text):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    list_of_stuff = []
    for char in letters:
        list_of_stuff.append((char, text.lower().count(char)))
    return list_of_stuff
text = "The quick brown fox jumps over the lazy dog"
letter_freq_list = get_letter_frequency(text)
print(f"Letter Frequencies: {letter_freq_list}")