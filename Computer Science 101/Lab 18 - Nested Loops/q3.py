def get_sum_vowel_counts(words_list, counter=0):
    for i in "".join(words_list).lower():
        if i in "aeiou":
            counter+= 1
    return counter

	
data = ['this', 'is', 'A', 'very', 'short']
print(get_sum_vowel_counts(data))
