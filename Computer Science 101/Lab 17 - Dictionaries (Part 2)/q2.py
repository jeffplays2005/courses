def display_translation(word, radio_telephone_dictionary):
    list_of_words = []
    for i in word:
        list_of_words.append(radio_telephone_dictionary[i.upper()]);
    print(" ".join(list_of_words))
radio_telephone_dict = {'B': 'Bravo', 'U': 'Uniform', 'M': 'Mike', 'S': 'Sierra', 'G': 'Golf', 'E': 'Echo', 'N': 'November', 'L': 'Lima', 'X': 'X-ray', 'D': 'Delta', 'W': 'Whiskey', 'V': 'Victor', 'Z': 'Zulu', 'F': 'Foxtrot', 'K': 'Kilo', 'O': 'Oscar', 'R': 'Romeo', 'A': 'Alpha', 'Q': 'Quebec', 'Y': 'Yankee', 'H': 'Hotel', 'J': 'Juliett', 'T': 'Tango', 'P': 'Papa', 'I': 'India', 'C': 'Charlie'}
display_translation('aeroplane', radio_telephone_dict)