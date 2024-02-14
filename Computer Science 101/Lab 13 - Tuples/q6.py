def get_string_length_tuples(words_list):
    new_list = []
    for i in words_list:
        new_list.append((i, len(i)))
    return new_list

word_list = ['fish', 'barrel', 'like', 'noon', 'sand', 'bank']
result = get_string_length_tuples(word_list)
print(result)
print(type(result))