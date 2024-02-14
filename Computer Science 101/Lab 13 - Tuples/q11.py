def get_letter_frequency(text):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    list_of_stuff = []
    for char in letters:
        list_of_stuff.append((char, text.lower().count(char)))
    return list_of_stuff
    
def draw_letter_frequency_chart(letter_freq_list):
    for i in letter_freq_list:
        if i[1] > 0:
            freq = "#" * i[1]
            print(f"{i[0]}|{freq}{i[1]}")
        
text = "A journey of a 1000 miles begins with a single step."
letter_freq_list = get_letter_frequency(text)
print("Letter Frequencies:")
draw_letter_frequency_chart(letter_freq_list)