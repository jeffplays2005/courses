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

def selection_sort(word_scores):  
    for pass_num in range(len(word_scores)-1, 0, -1):
        position_largest = 0
        trimmed_list = word_scores[:pass_num+1]
        # indexes
        cache_index = trimmed_list.index(max(trimmed_list))
        swap_index = pass_num
        # swapping
        maximum_swap = max(trimmed_list)
        to_swap = word_scores[swap_index]
        # print(f"   DEBUG: \n   MAX:{max(trimmed_list)}\n   MAX INDEX:{cache_index}\n   SWAP INDEX: {swap_index}")
        # 
        word_scores[cache_index] = to_swap
        word_scores[swap_index] = maximum_swap
        print(" ".join([str(i) for i in word_scores]))
        # print(" ".join([str(i) for i in trimmed_list]))

a_list = [WordScore('trees'), WordScore('days'), WordScore('everything'), WordScore('rain')]
selection_sort(a_list)
for word_score in a_list:
    print(word_score, end = ' ')
print("DONE")
# trees(62) days(45) rain(38) everything(123)
# rain(38) days(45) trees(62) everything(123)
# rain(38) days(45) trees(62) everything(123)
# rain(38) days(45) trees(62) everything(123) DONE
a_list = [WordScore('trees')]
selection_sort(a_list)
for word_score in a_list:
    print(word_score, end = ' ')
print("DONE")
# trees(62) DONE


a_list = [WordScore('everything'), WordScore('is'), WordScore('fun')]
selection_sort(a_list)
for word_score in a_list:
    print(word_score, end = ' ')
print("DONE")
# fun(38) is(26) everything(123)↩
# is(26) fun(38) everything(123)↩
# is(26) fun(38) everything(123) DONE

	
