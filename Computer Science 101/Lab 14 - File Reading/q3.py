def read_numbers(filename):
    input_file = open(filename, "r")
    lines = input_file.read().split('\n')
    input_file.close()
    total = 0
    a_list = []
    for line in lines:
        splitted = line.split()
        for i in splitted:
            total += int(i)
            a_list.append(i)
    return (total, round(total / len(a_list), 1))

def read_numbers(filename):
    input_file = open(filename, "r")
    lines = input_file.read().split()
    input_file.close()
    print(lines)
    


filename = "Lab14Q03_1.txt"
print(read_numbers(filename))