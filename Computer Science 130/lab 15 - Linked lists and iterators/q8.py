"""
The GeometricSequence class provides a list of numbers in a geometric sequence. 
In a geometric sequence, each term is found by multiplying the previous term by a constant. 
In general, we can write a geometric sequence as a, a*r, a*r^2, a*r^3 where a defines the 
first term and r defines the common ratio. Note that r must not be equal to 0. 
For example, the following code fragment:
```
sequence = GeometricSequence(2, 3, 5)
for num in sequence:
    print(num, end = " ")
```
produces:
2 6 18 54 162 (i.e. 2, 2 * 3, 2 * 3 * 3, and so on)
"""

class GeometricSequence:
    def __init__(self, first_term=1, common_ratio=2, n=5):
        self.first_term = first_term
        self.common_ratio = common_ratio
        self.number_of_terms = n        
    def __iter__(self):
        return GeometricIterator(self.first_term, self.common_ratio, self.number_of_terms)

class GeometricIterator:
    def __init__(self, first_term, common_ratio, number_of_terms):
        self.first_term = first_term
        self.common_ratio = common_ratio
        self.number_of_terms = number_of_terms
        self.current_iteration = 1
    def __next__(self):
        if self.current_iteration <= self.number_of_terms:
            self.current_iteration += 1
            current = self.first_term
            self.first_term *= self.common_ratio
            return current
        else:
            raise StopIteration()

values = GeometricSequence(1, 5)
for x in values:
    print(x)
# 1
# 5
# 25
# 125
# 625
values = GeometricSequence(2, 10, 3)
for x in values:
    print(x)
# 2
# 20
# 200