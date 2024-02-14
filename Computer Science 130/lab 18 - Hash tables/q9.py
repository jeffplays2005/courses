class SimpleHashTable:
    def __init__(self, size=7):
        self.size = size
        self.slots = [ None for i in range(size) ]
    def __str__(self):
        return f"[{', '.join([str(i) for i in self.slots])}]"
    def get_hash_index(self, key):
        return key % self.size
# 1 line
SimpleHashTable = type('SimpleHashTable', (object,), { '__init__': lambda self, size=7:(setattr(self, 'size', size) or setattr(self, 'slots', [ None for i in range(size) ])), '__str__': lambda self: (f"[{', '.join([str(i) for i in self.slots])}]"), 'get_hash_index': lambda self, key: (key % self.size) })

my_hash_table = SimpleHashTable()
print(my_hash_table)
print(type(my_hash_table))
print(my_hash_table.get_hash_index(12))
# [None, None, None, None, None, None, None]
# <class '__main__.SimpleHashTable'>
# 5
my_hash_table=SimpleHashTable(3)
print(my_hash_table)
print(my_hash_table.get_hash_index(14))
# [None, None, None]
# 2
