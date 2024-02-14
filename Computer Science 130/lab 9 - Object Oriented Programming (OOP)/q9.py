ParkingSpace = type('ParkingSpace', (object,), { '__init__': lambda self, space_id = 1, available = True : setattr(self, 'space_id', space_id) or setattr(self, 'available', available), 'is_available' : lambda self : self.available, 'mark_as_occupied': lambda self : setattr(self, 'available', False), '__str__': lambda self: f"Parking Space {self.space_id}: {'available' if self.available else 'occupied'}" })

class ParkingSlot:
    def __init__(self, amount = 1):
        self.parking_spaces = [ ParkingSpace(i) for i in range(amount) ]
    def get_available(self):
        return str(a[0]) if len(a:=[ i for i in self.parking_spaces if i.is_available() == True ]) else None
    def check_availability(self):
        return len([ i for i in self.parking_spaces if i.is_available() == True ])
    def mark_as_occupied(self):
        return a[0].mark_as_occupied() if len(a:=[ i for i in self.parking_spaces if i.is_available() == True ]) else (print("Sorry, this parking slot is full"))
# 1 line
ParkingSlot = type('ParkingSlot', (object,), { '__init__': lambda self, amount = 1: setattr(self, 'parking_spaces', [ ParkingSpace(i) for i in range(amount) ]), 'get_available': lambda self : str(a[0]) if len(a:=[ i for i in self.parking_spaces if i.is_available() == True ]) else None, 'check_availability': lambda self : len([ i for i in self.parking_spaces if i.is_available() == True ]), 'mark_as_occupied': lambda self : a[0].mark_as_occupied() if len(a:=[ i for i in self.parking_spaces if i.is_available() == True ]) else (print("Sorry, this parking slot is full")) })
# testing
parking1= ParkingSlot(3)
print(parking1.check_availability())
space1 = parking1.get_available()
print(space1)
parking1.mark_as_occupied()
print(parking1.check_availability())
space2 = parking1.get_available()
print(space2)
# 3
# Parking Space 0: available
# 2
# Parking Space 1: available
parking1 = ParkingSlot(2)
parking1.mark_as_occupied()
print(parking1.check_availability())
parking1.mark_as_occupied()
print(parking1.check_availability())
# 1
# 0