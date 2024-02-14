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
# code
def get_reversed(a_node, a_list=None):
    if a_node.get_next() == None:
        a_list = (a_list if isinstance(a_list, list) else []) + [a_node.get_data()]
        return a_list[::-1]
    else:
        a_list = (a_list if isinstance(a_list, list) else []) + [a_node.get_data()]
        return get_reversed(a_node.get_next(), a_list)
# 1 liner
def get_reversed(a_node, a_list=None): return a_list[::-1] if (a_node.get_next() == None and (a_list := (a_list if isinstance(a_list, list) else []) + [a_node.get_data()])) else ((a_list := (a_list if isinstance(a_list, list) else []) + [a_node.get_data()]) and get_reversed(a_node.get_next(), a_list))
# without cheeky
def get_reversed(a_node):
    if a_node.get_next() == None:
        return [a_node.get_data()]
    else:
        return get_reversed(a_node.get_next()) + [a_node.get_data()]
# without cheeky 1 liner
def get_reversed(a_node): return [a_node.get_data()] if a_node.get_next() == None else get_reversed(a_node.get_next()) + [a_node.get_data()]

node1 = Node('hello')
print(get_reversed(node1))
# ['hello']
node1 = Node('hello')
node2 = Node('world')
node3 = Node('goodbye')
node1.set_next(node2)
node2.set_next(node3)
print_node_chain(node1)
a_list = get_reversed(node1)
a_list.append(100)
print_node_chain(node1)
print(a_list)

# hello world goodbye
# hello world goodbye
# ['goodbye', 'world', 'hello', 100]