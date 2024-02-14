class Circle:
    def __init__(self, radius = 1):
        self.radius = radius
    def __str__(self):
        return f"A circle with a radius of {self.radius:.2f}cm."
    def get_area(self):
        return 3.141592 * self.radius ** 2
# 1 liner
Circle = type('Circle', (object,), { '__init__': lambda self, radius=1: (setattr(self, 'radius', radius)), '__str__': lambda self: f"A circle with a radius of {self.radius:.2f}cm.", 'get_area': lambda self: 3.141592 * self.radius ** 2 })

r = Circle(2.5)
print(r)
print(type(r))
print("{:.2f}".format(r.get_area()))
r2 = Circle()
print(r2)
print("{:.2f}".format(r2.get_area()))
# A circle with a radius of 2.50cm.
# <class '__main__.Circle'>
# 19.63
# A circle with a radius of 1.00cm.
# 3.14
r = Circle()
print(r.radius)
print("{:.2f}".format(r.get_area()))
print(r)
# 1
# 3.14
# A circle with a radius of 1.00cm.