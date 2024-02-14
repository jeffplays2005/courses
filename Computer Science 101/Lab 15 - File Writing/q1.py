def read_length_per_line(file_name):
    file = open(file_name)
    lines = file.read().split('\n')
    file.close()
    
    line_list_length = []
    
    for i in lines:
        line_list_length.append(len(i))
    return line_list_length
    
print(read_length_per_line('sentences.txt'))