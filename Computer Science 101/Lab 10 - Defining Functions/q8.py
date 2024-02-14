def get_encrypted(word, key):
    template = ""
    for letter in word:
        template += key[ord(letter) - 97]
        
    return template
