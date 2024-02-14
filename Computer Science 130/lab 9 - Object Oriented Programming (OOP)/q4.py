Author = type('Author', (object,), { '__init__': lambda self, first, second : setattr(self, 'name', f"{first}, {second[0]}."), '__str__': lambda self:self.name })
class Book:
    def __init__(self, title):
        setattr(self, 'title', title)
        setattr(self, 'authors', [])
    def add_author(self, author):
        self.authors.append(author)

# 1 line
Book = type('Book', (object,), { '__init__': lambda self, title: (setattr(self, 'title', title) or setattr(self, 'authors', [])), 'add_author': lambda self, author : self.authors.append(author) })

book1 = Book('Mental Fitness')
print(book1.title)
print(book1.authors)
print(type(book1))
print(type(book1.title))
print(type(book1.authors))
# Mental Fitness
# []
# <class '__main__.Book'>
# <class 'str'>
# <class 'list'>
author2 = Author("Pan", "Peter")
author1 = Author("Wong", "Alan")
book1 = Book('Keepers')
book1.add_author(author1)
book1.add_author(author2)
print(len(book1.authors))
print(book1.authors[0])
# 2
# Wong, A.
