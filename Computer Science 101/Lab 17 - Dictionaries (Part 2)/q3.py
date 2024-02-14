def create_baby_names_dictionary(filename):
    dict = {}
    file = open(filename)
    lines = file.read().split('\n');
    file.close()
    lines = sorted(lines)
    list_of_names = []
    for i in lines:
        if len(i) > 0:
            possible = i.split()
            for n in possible:
                if len(n) > 0:
                    list_of_names.append(n)
    list_of_names = sorted(list_of_names)
    for i in list_of_names:
        if i[0] in dict.keys():
            dict[i[0]].append(i)
        else:
            dict[i[0]] = [ i ]
    return dict
def print_baby_names(baby_names_dict):
    for i in baby_names_dict.keys():
        print(f"{i}: {' '.join(baby_names_dict[i])}")
        
baby_names_dict = create_baby_names_dictionary('2000TopNames.txt')
print_baby_names(baby_names_dict)