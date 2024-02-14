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

a_node = Node('hello')
a_node.add_list_from_last(['a', 'b', 'c'])
current = a_node.get_next()
if not isinstance(current, Node):
    print("current must be an object of the Node class")
print(a_node)
print(current)  
current = current.get_next()
print(current)
current = current.get_next()
print(current)
current = current.get_next()
print(current)
# hello
# c
# b
# a
# None
node1 = Node('hello')
node1.add_list_from_last(['a', 'b'])
print(node1)
current = node1.get_next()
print(current)
current = current.get_next()
print(current)
current = current.get_next()
print(current)
print("--------")
# hello
# b
# a
# None
node1 = Node(1)
node2 = Node(2)
node1.set_next(node2)
node1.add_list_from_last([3, 4])
node2.add_after(5)
current = node1
while current:
    print(current)
    current = current.get_next()
# 1
# 4
# 3
# 2
# 5