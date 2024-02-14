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
    
    
object1 = CommonLetters()
object2 = CommonLetters('hello', 'world')
print(object1)
print(object2)
object1.set_first_word('hello')
print(object1)
object2.set_second_word('bubble')
print(object2)
object3 = CommonLetters('cat', 'banana')
print(object3)
print(CommonLetters('cat', 'dog'))
data = object2.get_common_letters()
print(type(data))
print(data)
# first, second (s)
# hello, world (lo)
# hello, second (eo)
# hello, bubble (el)
# cat, banana (a)
# cat, dog ()
# <class 'str'>
# el