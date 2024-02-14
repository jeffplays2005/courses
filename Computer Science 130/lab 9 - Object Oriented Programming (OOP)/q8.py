ParkingSpace = type('ParkingSpace', (object,), { '__init__': lambda self, space_id = 1, available = True : setattr(self, 'space_id', space_id) or setattr(self, 'available', available), 'is_available' : lambda self : self.available, 'mark_as_occupied': lambda self : setattr(self, 'available', False), '__str__': lambda self: f"Parking Space {self.space_id}: {'available' if self.available else 'occupied'}" })

class ParkingSlot:
    def __init__(self, amount = 1):
        self.parking_spaces = [ ParkingSpace(i) for i in range(amount) ]
# 1 line
ParkingSlot = type('ParkingSlot', (object,), { '__init__': lambda self, amount = 1: setattr(self, 'parking_spaces', [ ParkingSpace(i) for i in range(amount) ]) })
# test
slot1 = ParkingSlot()
print(', '.join(str(item) for item in slot1.parking_spaces))
slot2 = ParkingSlot(3)
print(', '.join(str(item) for item in slot2.parking_spaces))
# Parking Space 0: available
# Parking Space 0: available, Parking Space 1: available, Parking Space 2: available