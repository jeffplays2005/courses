class Pyramid:
    def __init__(self, base_length=1, base_width=1, height=1):
        self.base_length = base_length
        self.base_width = base_width
        self.height = height
    def get_base_length(self):
        return self.base_length
    def set_base_length(self, new_length):
        if new_length > 0:
            self.base_length = new_length
    def get_base_width(self):
        return self.base_width
    def set_base_width(self, new_width):
        if new_width > 0:
            self.base_width = new_width
    def get_height(self):
        return self.height
    def set_height(self, new_height):
        if new_height > 0:
            self.height = new_height
    def get_base_area(self):
        return self.base_length * self.base_width
    def get_volume(self):
        return self.base_length * self.base_width * self.height / 3
    def __repr__(self):
        return f"Pyramid({self.base_length}, {self.base_width}, {self.height})"
    def __str__(self):
        return f"A pyramid with a base area of {self.base_length*self.base_width} and a volume of {self.base_length * self.base_width * self.height / 3:.2f}."
    def __eq__(self, other):
        if isinstance(other, Pyramid):
            return self.height == other.height and self.base_length == other.base_length and self.base_width == other.base_width
        else:
            return False
    def __lt__(self, other):
        if isinstance(other, Pyramid):
            return self.get_volume() < other.get_volume()
        else: return False
    def __gt__(self, other):
        if isinstance(other, Pyramid):
            return self.get_volume() > other.get_volume()
        else: return False
    def __le__(self, other):
        if isinstance(other, Pyramid):
            return self.get_volume() <= other.get_volume()
        else: return False
    def __ge__(self, other):
        if isinstance(other, Pyramid):
            return self.get_volume() >= other.get_volume()
        else: return False
pyramid1 = Pyramid()
pyramid2 = Pyramid(2, 4, 6)
print(pyramid1)
print(pyramid2)
print(pyramid1 == pyramid2)
print(pyramid1 < pyramid2)
print(pyramid1 <= pyramid2)
print(pyramid1 > pyramid2)
print(pyramid1 >= pyramid2)
# A pyramid with a base area of 1 and a volume of 0.33.
# A pyramid with a base area of 8 and a volume of 16.00.
# False
# True
# True
# False
# False
pyramid1 = Pyramid(3, 5, 10)
print(pyramid1)
pyramid2 = Pyramid(3, 5, 10)
print(pyramid2)
print(pyramid1 == pyramid2)
pyramid3 = Pyramid(1, 1, 5)
print(pyramid1 == pyramid3)
print(pyramid1 == pyramid2)
print(pyramid1 < pyramid2)
print(pyramid1 <= pyramid2)
print(pyramid1 > pyramid2)
print(pyramid1 >= pyramid2)
# A pyramid with a base area of 15 and a volume of 50.00.
# A pyramid with a base area of 15 and a volume of 50.00.
# True
# False
# True
# False
# True
# False
# True