class OddNumber:
    def __init__(self, upper_limit):
        self.upper_limit = upper_limit
    def __iter__(self):
        return OddNumberIterator(self.upper_limit)

class OddNumberIterator:
    def __init__(self, upper_limit):
        self.upper_limit = upper_limit
        self.current_number = 1
    def __next__(self):
        if self.current_number > self.upper_limit:
            raise StopIteration
        else:
            current = self.current_number
            self.current_number += 2
            return current
# 
# class NumbersIterator:
#     def __init__(self, low, high):
#         self.current= low 
#         self.high = high
#     def __next__(self):
#         if self.current > self.high:
#             raise StopIteration
#         else:
#             self.current += 1 
#             return self.current - 1
# 
# for i in Numbers(5,10):
#     print(i)

values = OddNumber(5)
for x in values:
    print(x)
# 1
# 3
# 5
values = OddNumber(3)
for x in values:
    print(x)
# 1
# 3