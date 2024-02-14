def read_lines(filename):
    input_file = open(filename, "r")
    lines = input_file.read().split('\n')
    input_file.close()
    return lines
print(read_lines('sample_books.txt'))