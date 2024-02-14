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
    # 
    # def add_after(self, value):
    #     cache = self.next
    #     if cache:
    #         self.next = Node(value)
    #         self.next.set_next(cache)
    #     else:
    #         self.next = Node(value)
    # # 
    # def add_list_from_last(self, a_list):
    #     for pos, i in enumerate(a_list):
    #             self.add_after(i)

    def get_vowels(self):
        return "".join([ a for a in self.data if a.lower() in "aeiou" ])

def print_node_chain(a_node):
    if a_node.get_next() == None:
        print(a_node.get_data())
    else:
        print(a_node.get_data(), end=" ")
        return print_node_chain(a_node.get_next())

# def get_reversed(a_node):
#     if a_node.get_next() == None:
#         return [a_node.get_data()]
#     else:
#         return get_reversed(a_node.get_next()) + [a_node.get_data()]

def reverse_node_chain(a_node):
    items = get_reversed(a_node)[::-1]
    
    new_node = Node(items.pop(-1))
    # new_node.add_list_from_last(new_node, items)
    
    def add_after(self, value):
        cache = self.next
        if cache:
            self.next = Node(value)
            self.next.set_next(cache)
        else:
            self.next = Node(value)
    
    def add_list_from_last(self, a_list):
        for pos, i in enumerate(a_list):
                add_after(self, i)
    add_list_from_last(new_node, items)
    
    return new_node

# 1 line


(lambda (self, a_list): [ self.add_after(i) for i in a_list ])
        

def reverse_node_chain(a_node): return new_node if (((items := (get_reversed := lambda a_node: [a_node.get_data()] if a_node.get_next() == None else get_reversed(a_node.get_next()) + [a_node.get_data()])(a_node)[::-1]) and (new_node := Node(items.pop(-1)))) and (lambda self, a_list : ([ self.add_after(i) for i in a_list ]))(new_node, items)) else new_node
    
    

node1 = Node('hello')
node2 = Node('world')
node1.set_next(node2)
result = reverse_node_chain(node1)
print_node_chain(result)
print_node_chain(node1)
if not isinstance(result, Node):
    print("result must be an object of the Node class")
# world hello
# hello world
node1 = Node('hello')
node2 = Node('world')
node3 = Node('goodbye')
node1.set_next(node2)
node2.set_next(node3)
result = reverse_node_chain(node1)
print_node_chain(result)
# goodbye world hello