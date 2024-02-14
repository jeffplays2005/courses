def convert_2d_lists(sentences):
    result = []
    for line in sentences:
        two_d_list = []
        splitted = line.split()
        for i in splitted:
            two_d_list.append(i)
        result.append(two_d_list)
    return result

def convert_2d_lists(sentences): return [ i for i in (line.split() for line in sentences) ]

data = ['life is a long     journey', 'problems\nto\nsolve', 'lessons\tto\tlearn']
result = convert_2d_lists(data)
print(result)