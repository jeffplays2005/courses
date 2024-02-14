class PolygonalNumber:
    def __init__(self, s=3, terms = 1):
    # def __init__(self, s=3, terms=4):
        self.numbers = [ int(((s-2)*n**2-(s-4)*n)/2) for n in range(1,terms+1) ]
        self.sides = s
        self.terms = terms
        

# test
sequence1 = PolygonalNumber()
print(type(sequence1))
print(sequence1.numbers)
sequence2 = PolygonalNumber()
print(sequence2.numbers)
print(sequence1 == sequence2)
# <class '__main__.PolygonalNumber'>
# [1]
# [1]
# False
sequence2 = PolygonalNumber()
print(sequence2.numbers)
# [1]