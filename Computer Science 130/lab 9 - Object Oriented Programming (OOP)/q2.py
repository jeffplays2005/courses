class Circle:
    def __init__(self, radius = 1):
        self.radius = radius
    def __str__(self):
        return f"A circle with a radius of {self.radius:.2f}cm."
    def get_area(self):
        return 3.141592 * self.radius ** 2

class Cone:
    def __init__(self, radius=1, slant_height=1):
        self.radius = radius
        self.slant_height = slant_height
        self.base_circle = Circle(radius)
    def __str__(self):
        return f"A cone with a base circle area of {self.base_circle.get_area():.2f}cm2 and a slant height of {self.slant_height:.2f}cm."
    def get_total_surface_area(self):
        return 3.1415192 * self.radius * self.slant_height + self.base_circle.get_area()
# 1 line
class Cone:
    def __init__(self, radius=1, slant_height=1, Circle = type('Circle', (object,), { '__init__': lambda self, radius=1: (setattr(self, 'radius', radius)), '__str__': lambda self: f"A circle with a radius of {self.radius:.2f}cm.", 'get_area': lambda self: 3.141592 * self.radius ** 2 })):
        ((setattr(self, 'radius', radius) or setattr(self, 'base_circle', Circle(radius)) or setattr(self, 'slant_height', slant_height)))
    def __str__(self):
        return f"A cone with a base circle area of {self.base_circle.get_area():.2f}cm2 and a slant height of {self.slant_height:.2f}cm."
    def get_total_surface_area(self):
        return 3.1415192 * self.radius * self.slant_height + self.base_circle.get_area()
# collated 1 line with 2 classes
Cone = type('Cone', (object,), { '__init__': lambda self, radius=1, slant_height=1, Circle = type('Circle', (object,), { '__init__': lambda self, radius=1: (setattr(self, 'radius', radius)), '__str__': lambda self: f"A circle with a radius of {self.radius:.2f}cm.", 'get_area': lambda self: 3.141592 * self.radius ** 2 }): ((setattr(self, 'radius', radius) or setattr(self, 'base_circle', Circle(radius)) or setattr(self, 'slant_height', slant_height))), '__str__': lambda self: f"A circle with a radius of {self.radius:.2f}cm.", 'get_area': lambda self: 3.141592 * self.radius ** 2, '__str__': lambda self: f"A cone with a base circle area of {self.base_circle.get_area():.2f}cm2 and a slant height of {self.slant_height:.2f}cm.", 'get_total_surface_area': lambda self: 3.1415192 * self.radius * self.slant_height + self.base_circle.get_area() })
# im dumb
Cone = type('Cone', (object,), { '__init__': lambda self, radius=1, slant_height=1: ((setattr(self, 'radius', radius) or setattr(self, 'base_circle', Circle(radius)) or setattr(self, 'slant_height', slant_height))), '__str__': lambda self: f"A circle with a radius of {self.radius:.2f}cm.", 'get_area': lambda self: 3.141592 * self.radius ** 2, '__str__': lambda self: f"A cone with a base circle area of {self.base_circle.get_area():.2f}cm2 and a slant height of {self.slant_height:.2f}cm.", 'get_total_surface_area': lambda self: 3.1415192 * self.radius * self.slant_height + self.base_circle.get_area() })

# ne', (object), { '__init__': lambda self, radius=1, slant_height=1, Circle = type('Circle', (object,), { '__init__': lambda self, radius=1: (setattr(self, 'radius', radius)), '__str__': lambda self: f"A circle with a radius of {self.radius:.2f}cm.", 'get_area': lambda self: 3.141592 * self.radius ** 2 }) : ((setattr(self, 'radius', radius) or setattr(self, 'base_circle', Circle(radius)) or setattr(self, 'slant_height', slant_height))),
# '__str__': lambda self: f"A cone with a base circle area of {self.base_circle.get_area():.2f}cm2 and a slant height of {self.slant_height:.2f}cm.",
# 'get_total_surface_area': lambda self : 3.1415192 * self.radius * self.slant_height + self.base_circle.get_area()
# })
c1 = Cone(2, 4)
print(c1)
print(type(c1))
print(type(c1.base_circle))
print(type(c1.slant_height))
print("{:.2f}".format(c1.get_total_surface_area()))
c2 = Cone()
print(c2)
print("{:.2f}".format(c2.get_total_surface_area()))
# A cone with a base circle area of 12.57cm2 and a slant height of 4.00cm.
# <class '__main__.Cone'>
# <class '__main__.Circle'>
# <class 'int'>
# 37.70
# A cone with a base circle area of 3.14cm2 and a slant height of 1.00cm.
# 6.28
r = Cone(4, 7)
print(r.radius)
print("{:.2f}".format(r.get_total_surface_area()))
print(r)
# 4
# 138.23
# A cone with a base circle area of 50.27cm2 and a slant height of 7.00cm.
