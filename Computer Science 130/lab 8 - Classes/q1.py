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
pyramid1 = Pyramid()
print(pyramid1.get_base_length())
pyramid2 = Pyramid(4, 6, 12)
print(pyramid2.get_base_length())
pyramid1.set_base_length(-1)
print(pyramid1.get_base_length())
pyramid1.set_base_length(12)
print(pyramid1.get_base_length())
pyramid3 = Pyramid(1, 1, 1)
print(pyramid1 == pyramid3)
print(Pyramid(1, 1, 1) == Pyramid(1, 1, 1))
# 1
# 4
# 1
# 12
# False
