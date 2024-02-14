class Author:
    def __init__(self, first, second):
        self.name = f"{first}, {second[0]}."
    def __str__(self):
        return self.name

Author = type('Author', (object,), { '__init__': lambda self, first, second : setattr(self, 'name', f"{first}, {second[0]}."), '__str__': lambda self:self.name })

author1 = Author("Hill", "Michael")
print(author1)
print(author1.name)
# Hill, M.
# Hill, M.