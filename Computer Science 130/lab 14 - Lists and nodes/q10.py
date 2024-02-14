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

def get_all_vowels(a_node, a_list=None):
    if a_node.get_next() == None:
        a_list = (a_list if isinstance(a_list, list) else []) + ["".join([ i for i in a_node.get_data() if i.lower() in "aeiou"])]
        return a_list
    else:
        a_list = (a_list if isinstance(a_list, list) else []) + ["".join([ i for i in a_node.get_data() if i.lower() in "aeiou"])]
        return get_all_vowels(a_node.get_next(), a_list)

# 1 line
def get_all_vowels(a_node, a_list=None): return a_list if (a_node.get_next() == None and (a_list := (a_list if isinstance(a_list, list) else []) + ["".join([ i for i in a_node.get_data() if i.lower() in "aeiou"])])) else ((a_list := (a_list if isinstance(a_list, list) else []) + ["".join([ i for i in a_node.get_data() if i.lower() in "aeiou"])]) and get_all_vowels(a_node.get_next(), a_list))

node1 = Node('programming')
node2 = Node('to', node1)
node3 = Node('hello', node2)
print_node_chain(node3)
print(get_all_vowels(node3))
# hello to programming
# ['eo', 'o', 'oai']
node1 = Node('great')
node2 = Node('fun', node1)
node3 = Node('happy', node2)
node4 = Node('sad', node3)
print(get_all_vowels(node4))
# ['a', 'a', 'u', 'ea']