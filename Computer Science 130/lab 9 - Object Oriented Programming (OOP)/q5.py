Author = type('Author', (object,), { '__init__': lambda self, first, second : setattr(self, 'name', f"{first}, {second[0]}."), '__str__': lambda self:self.name })
class Book:
    def __init__(self, title):
        setattr(self, 'title', title)
        setattr(self, 'authors', [])
    def add_author(self, author):
        self.authors.append(author)
    def __str__(self):
        return f"Title: {self.title} by {', '.join([ str(author) for author in self.authors ])}" if len(self.authors) > 0 else f"Title: {self.title}"

# 1 line
Book = type('Book', (object,), { '__init__': lambda self, title: (setattr(self, 'title', title) or setattr(self, 'authors', [])), 'add_author': lambda self, author : self.authors.append(author), '__str__': lambda self: f"Title: {self.title} by {', '.join([ str(author) for author in self.authors ])}" if len(self.authors) > 0 else f"Title: {self.title}" })

book1 = Book('Mental Fitness')
print(book1)
# Title: Mental Fitness
author2 = Author("Pan", "Peter")
author1 = Author("Wong", "Alan")
book1 = Book('Keepers')
book1.add_author(author1)
book1.add_author(author2)
print(book1)
# Title: Keepers by Wong, A., Pan, P.