def merge_frequency_dictionaries(letter_freq_dict1, letter_freq_dict2):
    new_dict = {}
    for i in letter_freq_dict1.keys():
        if i in new_dict.keys():
            new_dict[i]+=letter_freq_dict1[i]
        else:
            new_dict[i] = letter_freq_dict1[i]
    for i in letter_freq_dict2.keys():
        if i in new_dict.keys():
            new_dict[i]+=letter_freq_dict2[i]
        else:
            new_dict[i] = letter_freq_dict2[i]
    return new_dict

letter_freq_dict1 = {"a": 1, "b": 2, "c": 3}
letter_freq_dict2 = {"d": 5, "b": 6, "e": 19}
merged_freq_dict = merge_frequency_dictionaries(letter_freq_dict1, letter_freq_dict2)
for key in sorted(merged_freq_dict):
    print(f"{key}: {merged_freq_dict[key]}")
print(type(merged_freq_dict))