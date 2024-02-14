class WordScore:
    def __init__(self, word=""): #assume lowercase letters
        valid_letters = 'abcdefghijklmnopqrstuvwxyz'
        score = 0
        for letter in word:
            score += valid_letters.index(letter)
        self.score = score
        self.word = word

    def __str__(self):
        return f"{self.word}({self.score})"
    
    def __eq__(self, comp):
        if isinstance(comp, WordScore) is False:
            return False
        
        return self.word == comp.word
    
    def __lt__(self, comp):
        if isinstance(comp, WordScore) is False:
            return False
        return self.score < comp.score or (self.score == comp.score and self.word < comp.word)

word_score1 = WordScore("zoo")
word_score2 = WordScore("summer")
data = [word_score1, word_score2, WordScore('is'), WordScore('programming')]
data.sort()
for element in data:
    print(element)
print(word_score1 == word_score2)
print(word_score1 < word_score2)
# is(26)
# zoo(53)
# summer(83)
# programming(120)
# False
# True
word_score1 = WordScore("bushes")
word_score2 = WordScore("waits")
word_score3 = WordScore("brown")
word_score4 = WordScore('standand')
print(word_score1 == word_score2)
print(word_score2 == word_score3)
print(word_score2 < word_score3)
print(word_score3 < word_score4)
# False
# False
# False
# True
word_score1 = WordScore("zoo")
word_score2 = WordScore("summer")
data = [word_score1, word_score2, WordScore('is'), WordScore('programming')]
data.sort()
for element in data: 
    print(element)
print(word_score1 == word_score2)
print(word_score1 < word_score2)
# is(26)
# zoo(53)
# summer(83)
# programming(120)
# False
# True
word_score1 = WordScore("bleats")
word_score2 = WordScore("stable")
word_score3 = WordScore("tables")
word_score4 = WordScore("beat")
print(word_score1, word_score2, word_score3, word_score4)
print(word_score1 == word_score2)
print(word_score2 == word_score3)
print(word_score1 == word_score4)
print(word_score1 < word_score2)
print(word_score1 < word_score3)
print(word_score1 < word_score4)
print(word_score2 < word_score3)
print(word_score2 < word_score4)
print(word_score3 < word_score4)
# bleats(53) stable(53) tables(53) beat(24)
# False
# False
# False
# True
# True
# False
# True
# False
# False