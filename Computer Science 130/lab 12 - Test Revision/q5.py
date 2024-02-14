class CommonLetters:
    def __init__(self, first = "first", second = "second"):
        self.first_word = first
        self.second_word = second
        self.common_letters = []
        for i in first:
            if i in second and i not in self.common_letters:
                self.common_letters.append(i)
        self.common_letters.sort()
    def __str__(self):
        return f"{self.first_word}, {self.second_word} ({''.join(self.common_letters)})"
        
object1 = CommonLetters()
object2 = CommonLetters('hello', 'world')
print(object1)
print(object2)
print(type(object1.common_letters)) #check the type
object3 = CommonLetters('cat', 'banana')
print(object3)
print(CommonLetters('cat', 'dog'))
# first, second (s)
# hello, world (lo)
# <class 'list'>
# cat, banana (a)
# cat, dog ()