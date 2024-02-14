def no_consonants(text, set = True):
    [((set := False) or "") for letter in text if letter not in 'aeiouAEIOU']
    return set
print(no_consonants('dry'))
print(no_consonants('show'))
print(no_consonants('order'))
print(no_consonants('adoulie'))
print(no_consonants('oo'))