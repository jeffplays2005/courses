class PolygonalNumber:
    def __init__(self, s=1, terms=1):
        self.numbers = [ int(((s-2)*n**2-(s-4)*n)/2) for n in range(1,terms+1) ]
        self.sides = s
        self.terms = terms
    def __str__(self):
        return f"The polygon numbers are {self.numbers}."
        

# test
sequence1 = PolygonalNumber()
print(type(sequence1))
print(sequence1.numbers)
sequence2 = PolygonalNumber(3, 4)
print(sequence2.numbers)
print(sequence1 == sequence2)
# <class '__main__.PolygonalNumber'>
# [1]
# [1, 3, 6, 10]
# False
sequence2 = PolygonalNumber(5, 7)
print(sequence2)
# The polygon numbers are [1, 5, 12, 22, 35, 51, 70].

sequence2 = PolygonalNumber(5, 7)
print(sequence2)
# The polygon numbers are [1, 5, 12, 22, 35, 51, 70].
# The polygon numbers are [1, 5, 12, 22, 35, 51, 70]