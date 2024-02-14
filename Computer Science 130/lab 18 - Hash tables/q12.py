class QuadraticHashTable:
    def __init__(self, size=7):
        self.size = size
        self.slots = [ None for i in range(size) ]
    def __str__(self):
        return f"[{', '.join([str(i) for i in self.slots])}]"
    def get_hash_index(self, key):
        return key % self.size
    def is_empty(self):
        return sum([ 1 for i in self.slots if i == None]) == self.size
    def is_full(self):
        return sum([ 1 for i in self.slots if i != None]) == self.size
    def clear(self):
        self.slots = [ None for i in range(self.size) ]
    def __len__(self):
        return sum([ 1 for i in self.slots if i != None ])
    # changed
    def put(self, key, fail = 1):
        thing = key % self.size
        cache = thing
        if self.is_full():
            raise IndexError("ERROR: The hash table is full.")
        while self.slots[cache] != None:
            cache = (thing + fail ** 2) % self.size
            fail += 1
        self.slots[cache] = key

my_hash_table=QuadraticHashTable()
my_hash_table.put(1)
print(my_hash_table)
my_hash_table.put(8)
print(my_hash_table)
my_hash_table.put(15)
print(my_hash_table)
my_hash_table.put(22)
print(my_hash_table)
# [None, 1, None, None, None, None, None]
# [None, 1, 8, None, None, None, None]
# [None, 1, 8, None, None, 15, None]
# [None, 1, 8, 22, None, 15, None]
