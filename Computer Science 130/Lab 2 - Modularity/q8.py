def print_dictionary(a_dict):
    width = get_longest_string_length(a_dict)
    for i in a_dict.items():
        print("{:<{}} {:.2f}".format(i[0], width, (i[1])))
    
def get_longest_string_length(dictionary): 
    return max([ len(str(i)) for i in dictionary.keys() ])
    
# 1 line
def print_dictionary(a_dict): print("\n".join([ "{:<{}} {:.2f}".format(i[0], max([ len(str(i)) for i in a_dict.keys() ]), (i[1])) for i in a_dict.items() ]))
    

data = {'Auckland': 1212.5, 'Tauranga': 1180.8999999999999, 'Hamilton': 1108.3, 'Rotorua': 1341.5, 'Taupo': 960.5}
print_dictionary(data)
