class Hashtable:
    def __init__(self, size = 7, table = []):
        self.size = size
        self.table = []
        for i in range(size):
            self.table.append([])

    def hash_function(self, key):
        position = key % self.size
        return position

    def put(self, key):
        position = self.hash_function(key)
        self.table[position].append(key)

    def contains(self, key):
        for value in self.table:
            for keys in value:
                if keys == key:
                    return True
        return False

    def remove(self, key):
        for value in self.table:
            for keys in value:
                if keys == key:
                    value.remove(keys)

    def __str__(self):
        new_string = ""
        for i in range(self.size):
            new_string += "[{}:] {}".format(i, self.table[i])
            new_string += "\n"
        return new_string.strip()
