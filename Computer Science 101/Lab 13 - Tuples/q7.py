def word_analysis(word):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    score = 0
    for i in word:
        score += letters.index(i)
    return word, len(word), score
    
print(word_analysis('at'))