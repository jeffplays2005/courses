class ParkingSpace:
    def __init__(self, space_id = 1, available = True):
        self.space_id = space_id
        self.available = available
    def is_available(self):
        return self.available
# 1 line
ParkingSpace = type('ParkingSpace', (object,), { '__init__': lambda self, space_id = 1, available = True : setattr(self, 'space_id', space_id) or setattr(self, 'available', available), 'is_available' : lambda self : self.available })
# testing
space1 = ParkingSpace()
print(type(space1))
print(space1.available)
space2 = ParkingSpace(2)
print(type(space2))
print(space2.available)
print(space1.is_available())
# <class '__main__.ParkingSpace'>
# True
# <class '__main__.ParkingSpace'>
# True
# True
space1 = ParkingSpace()
print(type(space1))
print(space1.available)
space2 = ParkingSpace(5)
print(type(space2))
print(space2.available)
print(space1.is_available())
# <class '__main__.ParkingSpace'>
# True
# <class '__main__.ParkingSpace'>
# True
# True
