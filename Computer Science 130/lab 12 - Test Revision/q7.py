class CommonLetters:
    def __init__(self, first = "first", second = "second"):
        self.first_word = first
        self.second_word = second
        self.common_letters = []
        self.update_common_letters(first, second)
        
    def __str__(self):
        return f"{self.first_word}, {self.second_word} ({''.join(self.common_letters)})"
        
    def set_first_word(self, first_word):
        self.first_word = first_word
        self.update_common_letters(first_word, self.second_word)
        
    def set_second_word(self, second_word):
        self.second_word = second_word
        self.update_common_letters(self.first_word, second_word)
        
    def update_common_letters(self, first_word, second_word):
        self.common_letters = []
        for i in first_word:
            if i in second_word and i not in self.common_letters:
                self.common_letters.append(i)
        self.common_letters.sort()
        
    def get_common_letters(self):
        return "".join(self.common_letters)

class CommonLettersList():
    def __init__(self):
        self.items = []

    def add_item(self, common_letters):
        self.items.append(common_letters)
    
    def __str__(self):
        return "\n".join([ str(i) for i in self.items ])
    
    def get_union(self):
        union = []
        for i in self.items:
            for n in i.common_letters:
                if n not in union:
                    union.append(n)
        union.sort()
        return union
        
object1 = CommonLetters()
object2 = CommonLetters('hello', 'world')
data = CommonLettersList()
data.add_item(object1)
data.add_item(object2)
print(data)
print(data.get_union())
# first, second (s)
# hello, world (lo)
# ['l', 'o', 's']