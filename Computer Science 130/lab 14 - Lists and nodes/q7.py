class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
        
    def __str__(self):
        return str(self.data)
    
    def get_data(self):
        return self.data
        
    def get_next(self):
        return self.next
        
    def set_data(self, new_data):
        self.data = new_data
        
    def set_next(self, new_next):
        self.next = new_next
    
    def add_after(self, value):
        cache = self.next
        if cache:
            self.next = Node(value)
            self.next.set_next(cache)
        else:
            self.next = Node(value)
    
    def add_list_from_last(self, a_list):
        for pos, i in enumerate(a_list):
                self.add_after(i)
    def get_vowels(self):
        return "".join([ a for a in self.data if a.lower() in "aeiou" ])

node1 = Node('abc')
node2 = Node('def')
node1.set_next(node2)
print(node1.get_vowels())
print(node2.get_vowels())
# a
# e
node1 = Node('life')
node2 = Node('is', node1)
node3 = Node('long', node2)
node4 = Node('journey', node3)
print(node1.get_vowels())
print(node4.get_vowels())
# ie
# oue