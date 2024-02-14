def get_words(filename):
    file = open(filename)
    lines = file.read().split('\n')
    file.close()
    filtered_words = []
    for i in lines:
        if len(i) > 0:
            filtered_words.append(i)
    return filtered_words

print(get_words("SampleWords1.txt"))