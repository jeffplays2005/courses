def get_words(filename):
    input_file = open(filename, "r")
    lines = input_file.read().split('\n')
    input_file.close()
    letter = lines.pop(0)
    length = int(lines.pop(0))
    
    new_list = []
    for i in lines:
        if i.startswith(letter):
            if int(len(i)) == length:
                new_list.append(i)
    
    return (letter, length, new_list)
    
filename = "many_words1.txt"
data_tuple = get_words(filename)
print(data_tuple[1]," letter words beginning with ",data_tuple[0],": ",data_tuple[2],sep="")