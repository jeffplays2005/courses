def count_word_occurrences(sentence):
    splitted = sentence.split();
    splitted = sorted(splitted);
    dict = {};
    for i in splitted:
        dict[i] = splitted.count(i);
    return dict;
sentence = 'ann met an ant'
word_counts_dict = count_word_occurrences(sentence)
for key in sorted(word_counts_dict):
    print(key, word_counts_dict[key])
sentence = 'it was the best of times it was the worst of times'
word_counts_dict = count_word_occurrences(sentence)
for key in sorted(word_counts_dict):
    print(key, word_counts_dict[key])