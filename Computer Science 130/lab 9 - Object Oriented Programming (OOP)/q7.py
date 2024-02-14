class ParkingSpace:
    def __init__(self, space_id = 1, available = True):
        self.space_id = space_id
        self.available = available
    def is_available(self):
        return self.available
    def mark_as_occupied(self):
        setattr(self, 'available', False)
    def __str__(self):
        return f"Parking Space {self.space_id}: {'available' if self.available else 'occupied'}"
# 1 line
ParkingSpace = type('ParkingSpace', (object,), { '__init__': lambda self, space_id = 1, available = True : setattr(self, 'space_id', space_id) or setattr(self, 'available', available), 'is_available' : lambda self : self.available, 'mark_as_occupied': lambda self : setattr(self, 'available', False), '__str__': lambda self: f"Parking Space {self.space_id}: {'available' if self.available else 'occupied'}" })

space1 = ParkingSpace()
print(space1)
space2 = ParkingSpace(2)
space2.mark_as_occupied()
print(space2)
# Parking Space 1: available
# Parking Space 2: occupied
space1 = ParkingSpace()
space1.mark_as_occupied()
print(space1)
space2 = ParkingSpace(5)
print(space2)

# Parking Space 1: occupied
# Parking Space 5: available