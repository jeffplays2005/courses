def create_last_letter_dictionary(words_list):
    words_list = sorted(words_list)
    letter_dict = {}
    for i in words_list:
        if i[-1] in letter_dict.keys():
            letter_dict[i[-1]].append(i)
        else:
            letter_dict[i[-1]] = [ i ]
            
    return letter_dict


words = ['reset', 'punch', 'dragon', 'heat', 'cart', 'judge', 'peace', 'piece', 
         'python', 'java', 'guava', 'germ', 'today', 'hooray']
words_dict = create_last_letter_dictionary(words)
for key in sorted(words_dict) :
    print(f"{key}: {', '.join(words_dict[key])}")
