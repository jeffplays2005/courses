def get_vowels(word):
    if len(word) == 0:
        return ""
    else:
        if word[0] in "aeiou":
            return word[0] + get_vowels(word[1:])
        else:
            return get_vowels(word[1:])

# 1 line
def get_vowels(word): return "" if len(word) == 0 else (word[0] + get_vowels(word[1:])) if word[0] in "aeiou" else get_vowels(word[1:])


s = 'hello'
print(get_vowels(s))
# eo
s = 'yellow colour'
print(get_vowels(s))
# eooou