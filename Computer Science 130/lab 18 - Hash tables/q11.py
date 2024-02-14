from unittest.mock import Mock
class SimpleHashTable:
    def __init__(self, size=7):
        self.size = size
        self.slots = [ None for i in range(size) ]
    def __str__(self):
        return f"[{', '.join([str(i) for i in self.slots])}]"
    def get_hash_index(self, key):
        return key % self.size
    def put(self, key):
        thing = key % self.size
        if self.is_full():
            raise IndexError("ERROR: The hash table is full.")
        while self.slots[thing] != None:
            thing += 1
            thing %= self.size
        self.slots[thing] = key
    def is_empty(self):
        return sum([ 1 for i in self.slots if i == None]) == self.size
    def is_full(self):
        return sum([ 1 for i in self.slots if i != None]) == self.size
    def clear(self):
        self.slots = [ None for i in range(self.size) ]
    def __len__(self):
        return sum([ 1 for i in self.slots if i != None ])
# 1 line
SimpleHashTable = type('SimpleHashTable', (object,), { '__init__': lambda self, size=7:(setattr(self, 'size', size) or setattr(self, 'slots', [ None for i in range(size) ])), '__str__': lambda self: (f"[{', '.join([str(i) for i in self.slots])}]"), 'get_hash_index': lambda self, key: (key % self.size), 'put': lambda self, key: (Mock(side_effect=IndexError("ERROR: The hash table is full.")))() if self.is_full() else (self.slots.__setitem__((f:=lambda x, i: self.get_hash_index(i) if self.slots[self.get_hash_index(i)] == None else f(x, i+1)) (key, key), key)), 'is_empty': lambda self: (sum([ 1 for i in self.slots if i == None]) == self.size), 'is_full': lambda self: (sum([ 1 for i in self.slots if i != None]) == self.size), 'clear': lambda self: (setattr(self, 'slots', [ None for i in range(self.size) ])), '__len__': lambda self: (sum([ 1 for i in self.slots if i != None ])) })
# test
try:
    my_hash_table = SimpleHashTable(3)
    my_hash_table.put(13)
    my_hash_table.put(26)
    my_hash_table.put(39)
    my_hash_table.put(52)
except IndexError as e:
    print(e)
print(my_hash_table)
print(my_hash_table.is_empty())
my_hash_table.clear()
print(my_hash_table.is_empty())

# ERROR: The hash table is full.
# [39, 13, 26]
# False
# True
