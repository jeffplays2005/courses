def create_baby_names_dictionary(names_list):
    a_dict = { key[0]:[] for key in names_list }
    for i in names_list:
        a_dict[i[0]].append(i[1])
    a_dict = { key:sorted(value) for (key,value) in a_dict.items() }
    return a_dict
    
data = [('A', 'Anthony'), ('C', 'Connor'), ('A', 'Alex')]
a_dict = create_baby_names_dictionary(data)
for key in sorted(a_dict.keys()):
    print(key, a_dict[key])