def read_english_french_info(filename):
    file = open(filename, 'r');
    lines = file.read().split('\n');
    file.close();
    return [ (line.split(':')[0], line.split(':')[1]) for line in lines ];

# testing cases
print(read_english_french_info('english_french1.txt'))
