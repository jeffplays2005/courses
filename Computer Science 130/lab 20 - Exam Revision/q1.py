def get_rainfall_data(filename):
    try:
        file = open(filename)
        lines = file.read().strip().split('\n')
        compiled = []
        for i in lines:
            splitted = i.split(',')
            if len(splitted) == 3:
                compiled.append((splitted[1], float(splitted[2])))
        file.close()
        return compiled
    except:
        print(f"ERROR: \"{filename}\" does not exist.")
        return []
    
data = get_rainfall_data('auckland_test.txt')
print(data)
print(type(data))
print(type(data[0]))
# [('January', 228.8), ('February', 194.9), ('March', 189.2), ('April', 157.3)]
# <class 'list'>
# <class 'tuple'>
data = get_rainfall_data('input_error.txt')
print(data)
# ERROR: "input_error.txt" does not exist.
# []
data = get_rainfall_data('auckland_error.txt')
print(data)
# [('January', 228.8), ('March', 189.2)]
