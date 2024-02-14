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

def binary_search(word_scores, search_score):
    left = 0
    right = len(word_scores) - 1
    mid = (left + right) // 2
    found = False
    count = 0 
    while (found == False and (left <= right)) and count <= 5:
        count += 1
        # print(f"    DEBUG: \n       left:{left} right: {right} mid: {mid}")
        if search_score > word_scores[mid].score:
            left = mid + 1
        elif search_score < word_scores[mid].score:
            right = mid - 1
        else:
            found = True
        mid = (left + right) // 2
    if found == True:
        return word_scores[mid].word

a_list = [WordScore('rain'), WordScore('days'), WordScore('trees'), WordScore('everything')]
for element in a_list:
    print(element, end=' ')
print()
print(binary_search(a_list, 62))
print(binary_search(a_list, 28))
# rain(38) days(45) trees(62) everything(123)
# trees
# None

a_list = [WordScore('code'), WordScore('rain'), WordScore('days'), WordScore('object'), WordScore('score'), WordScore('trees'), WordScore('everything')]
for element in a_list:
    print(element, end=' ')
print()
print(binary_search(a_list, 15))
print(binary_search(a_list, 68))
print(binary_search(a_list, 55))
print(binary_search(a_list, 38))
result = binary_search(a_list, 45)
print(result, type(result))
# code(23) rain(38) days(45) object(49) score(55) trees(62) everything(123)
# None
# None
# score
# rain
# days <class 'str'>