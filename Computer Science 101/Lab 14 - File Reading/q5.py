def process_barchart(filename):
    input_file = open(filename, "r")
    lines = input_file.read().split('\n')
    input_file.close()
    list_of_tuples = []
    for i in lines:
        split = i.split('|')
        a = split[0]
        b = split[1]
        list_of_tuples.append((a, int(len(b.split('#'))) - 1))
    return tuple(list_of_tuples)
    
    
filename = "barchart1.txt"
print(f"Letter frequencies from {filename}: {process_barchart(filename)}")