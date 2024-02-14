def get_acronym(phrase):
    return "".join([ n[0].upper() for n in phrase.split() ])
data = 'as soon as possible'
print(get_acronym(data))
