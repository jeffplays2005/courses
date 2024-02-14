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

pyramid1 = Pyramid()
print(pyramid1.get_base_area())
print("{:.2f}".format(pyramid1.get_volume()))
pyramid2 = Pyramid(4, 6, 12)
print(pyramid2.get_base_area())
print("{:.2f}".format(pyramid2.get_volume()))
# 1
# 0.33
# 24
# 96.00