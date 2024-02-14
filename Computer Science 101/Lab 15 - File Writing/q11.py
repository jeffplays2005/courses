def create_frequency_chart_file(letter_frequencies):
    new_list_of_frequencies = []
    alphabet = ""
    numbers = []
    for i in letter_frequencies:
        if i[1] > 0:
            new_list_of_frequencies.append(i)
            alphabet += i[0]
            numbers.append(i[1])
    maximum = max(numbers)
    
    file = open("upi123.txt", 'w')
    
    for i in range(maximum):
        for pos, number in enumerate(numbers):
            if number >= maximum:
                if pos == (len(numbers) - 1):
                    file.write("#\n")
                else:
                    file.write("#")
            else:
                if pos == (len(numbers) - 1):
                    file.write(" \n")
                else:
                    file.write(" ")
        maximum -= 1
    file.write(alphabet+"\n")
    file.close()

def create_frequency_chart_file(letter_frequencies):
    new_list_of_frequencies = []
    alphabet = ""
    numbers = []
    for i in letter_frequencies:
        if i[1] > 0:
            new_list_of_frequencies.append(i)
            alphabet += i[0]
            numbers.append(i[1])
    maximum = max(numbers)
    
    file = open("upi123.txt", 'w')
    
    for i in range(maximum):
        for pos, number in enumerate(numbers):
            if number >= maximum:
                if pos == (len(numbers) - 1):
                    file.write("#\n")
                else:
                    file.write("#")
            else:
                if pos == (len(numbers) - 1):
                    file.write(" \n")
                else:
                    file.write(" ")
        maximum -= 1
    file.write(alphabet+"\n")
    file.close()

    # print(new_list_of_frequencies)
    # print(alphabet)
# letter_frequencies = [('a', 16), ('b', 1), ('c', 6), ('d', 10), ('e', 18),
                     # ('f', 3), ('g', 8), ('h', 14), ('i', 13), ('j', 0),
                     # ('k', 1), ('l', 4), ('m', 4), ('n', 15), ('o', 12),
                     # ('p', 6), ('q', 0), ('r', 10), ('s', 10), ('t', 8),
                     # ('u', 2), ('v', 2), ('w', 6), ('x', 0), ('y', 5), ('z', 0)]
letter_frequencies = [('a', 5), ('b', 2), ('c', 1), ('d', 2), ('e', 10),
                     ('f', 5), ('g', 5), ('h', 7), ('i', 5), ('j', 0),
                     ('k', 0), ('l', 3), ('m', 5), ('n', 5), ('o', 5),
                     ('p', 0), ('q', 0), ('r', 10), ('s', 3), ('t', 11),
                     ('u', 3), ('v', 0), ('w', 1), ('x', 0), ('y', 6), ('z', 0)];
create_frequency_chart_file(letter_frequencies)
