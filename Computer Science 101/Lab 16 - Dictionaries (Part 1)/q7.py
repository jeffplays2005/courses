def translate_english_maori(maori_dictionary, word):
    found_word = word in maori_dictionary.keys()
    if found_word:
        print(f"'{word}' is translated into '{maori_dictionary[word]}'.")
    else:
        print("Sorry that word doesn't exist in Maori!")

translate_english_maori({
    'black': 'mangu', 
    'hello': 'kiaora', 
    'house': 'whare', 
    'apple': 'aporo', 
    'tree': 'aroha', 
    'work': 'mana', 
    'red': 'whero'
    }, 
    'gay'
)
    
    