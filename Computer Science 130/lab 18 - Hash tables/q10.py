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
        while self.slots[thing] != None:
            thing += 1
            thing %= self.size
        self.slots[thing] = key
    # def put(self, key): self.slots[ (f:=lambda x, i: self.get_hash_index(i) if self.slots[self.get_hash_index(i)] == None else f(x, i+1)) (key, key) ] = key
    def put(self, key): self.slots.__setitem__((f:=lambda x, i: self.get_hash_index(i) if self.slots[self.get_hash_index(i)] == None else f(x, i+1)) (key, key), key)
# 1 line
SimpleHashTable = type('SimpleHashTable', (object,), {
    '__init__': lambda self, size=7:(setattr(self, 'size', size) or setattr(self, 'slots', [ None for i in range(size) ])),
    '__str__': lambda self: (f"[{', '.join([str(i) for i in self.slots])}]"),
    'get_hash_index': lambda self, key: (key % self.size),
    'put': lambda self, key: (self.slots.__setitem__((f:=lambda x, i: self.get_hash_index(i) if self.slots[self.get_hash_index(i)] == None else f(x, i+1)) (key, key), key))
})
my_hash_table = SimpleHashTable(13)
my_hash_table.put(13)
my_hash_table.put(26)
my_hash_table.put(14)
my_hash_table.put(15)
my_hash_table.put(16)
my_hash_table.put(17)
print(my_hash_table)
#[13, 26, 14, 15, 16, 17, None, None, None, None, None, None, None]
my_hash_table = SimpleHashTable(13)
my_hash_table.put(13)
my_hash_table.put(26)
my_hash_table.put(39)
my_hash_table.put(52)
print(my_hash_table)
#[13, 26, 39, 52, None, None, None, None, None, None, None, None, None]
