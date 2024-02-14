def word_analysis(text):
    words = text.lower().split(' ')
    object = {}
    for i in words:
        object[i[0]] = 0;
    for i in words:
        object[i[0]] += 1;
    return object
text = "Peter Piper picked a peck of pickled peppers"
word_analysis_dict = word_analysis(text)
for key in sorted(word_analysis_dict):
    print(key, word_analysis_dict[key])