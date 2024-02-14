def count_words_start_with_vowel(list_of_lists):
    total = 0
    for list_i in list_of_lists:
        for item in list_i:
            if item[0] in "aeiou":
                total+=1
    return total