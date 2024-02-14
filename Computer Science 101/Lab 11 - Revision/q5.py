def upper_vowel(sentence):
    vowels = [ "a", "e", "i", "o", "u" ]
    new_string = ""
    for character in sentence:
        if character in vowels:
            new_string = f"{new_string}{character.upper()}"
        else:
            new_string = f"{new_string}{character.lower()}"
    return new_string
    
# print(upper_vowel("Mohammad"))
print(upper_vowel("World cup 2022"))
