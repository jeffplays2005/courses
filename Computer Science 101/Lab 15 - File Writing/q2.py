def write_words_start_vowel(filename, names):
    file = open(filename, 'w')
    for i in names:
        if i[0].lower() in 'aeiou':
            file.write(i + '\n')
    file.close()

def print_contents(file_name):
    file = open(file_name)
    print(file.read())
    file.close()
write_words_start_vowel('upi123.txt', ['life', 'is', 'a', 'long', 'journey', 'with', 'problems', 'to', 'solve'])
print_contents('upi123.txt')
