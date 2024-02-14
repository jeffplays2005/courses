# def get_vowels(word):
#     if len(word) == 0:
#         return ""
#     else:
#         if word[0] in "aeiou":
#             return word[0] + get_vowels(word[1:])
#         else:
#             return get_vowels(word[1:])
# 1 line in lambda
get_vowels = (lambda word: "" if len(word) == 0 else (word[0] + get_vowels(word[1:])) if word[0] in "aeiou" else get_vowels(word[1:]))

def get_all_vowels(list):
    if len(list) == 0:
        return []
    else:
        if (get_vowels := (lambda word: "" if len(word) == 0 else (word[0] + get_vowels(word[1:])) if word[0] in "aeiou" else get_vowels(word[1:])))(list[0]):
            return [get_vowels(list[0])] + get_all_vowels(list[1:])
        else:
            return get_all_vowels(list[1:])

# 1 line
def get_all_vowels(list): return [] if len(list) == 0 else [get_vowels(list[0])] + get_all_vowels(list[1:]) if (get_vowels := (lambda word: "" if len(word) == 0 else (word[0] + get_vowels(word[1:])) if word[0] in "aeiou" else get_vowels(word[1:])))(list[0]) else get_all_vowels(list[1:])

print(get_all_vowels(['hello', 'world']))
# ['eo', 'o']