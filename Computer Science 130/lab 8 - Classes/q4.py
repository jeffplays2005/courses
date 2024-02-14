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

pyramid1 = Pyramid(2, 4, 6)
print(pyramid1)
print(type(pyramid1))
print(repr(pyramid1))
pyramid2 = Pyramid()
print(pyramid2)
print(repr(pyramid2))
# A pyramid with a base area of 8 and a volume of 16.00.
# <class '__main__.Pyramid'>
# Pyramid(2, 4, 6)
# A pyramid with a base area of 1 and a volume of 0.33.
# Pyramid(1, 1, 1)