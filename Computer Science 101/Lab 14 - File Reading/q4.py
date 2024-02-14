def get_list_of_words_start_with(filename, target_letter):
    input_file = open(filename, "r")
    lines = input_file.read().split()
    input_file.close()
    list_of_found_words = []
    for i in lines:
        i = i.lower()
        if target_letter in i[0] and i not in list_of_found_words:
            list_of_found_words.append(i)
    return list_of_found_words

words_list = get_list_of_words_start_with("sentences.txt", 'a')
print(words_list)
#testing cases
words_list = get_list_of_words_start_with("sentences.txt", 'a')
print(words_list)

words_list = get_list_of_words_start_with("sentences.txt", 's')
print(words_list)

words_list = get_list_of_words_start_with("sentences.txt", 't')
print(words_list)
