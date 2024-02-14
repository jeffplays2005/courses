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

def print_node_chain(a_node):
    if a_node.get_next() == None:
        print(a_node.get_data())
    else:
        print(a_node.get_data(), end=" ")
        return print_node_chain(a_node.get_next())
# 1 liner
def print_node_chain(a_node): return print(a_node.get_data()) if a_node.get_next() == None else (print(a_node.get_data(), end=" ") or print_node_chain(a_node.get_next()))

node1 = Node('hello')
node2 = Node('world')
node3 = Node('goodbye')
node1.set_next(node2)
node2.set_next(node3)
print_node_chain(node1)
print("END")
# hello world goodbye
# END