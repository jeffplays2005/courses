def get_acronym_list(phrases_list):
    return [ "".join(n[0] for n in word.split()).upper() for word in phrases_list ]
data = ['as soon as possible', 'laughing out loud', 'graphics interchange format']
print(get_acronym_list(data))
