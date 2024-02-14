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

a_node = Node('hello')
print(a_node.get_data())
print(a_node)
print(a_node.get_next())
# hello
# hello
# None
node2 = Node('world')
node1 = Node('hello', node2)
print(node1.get_data())
print(node1.get_next().get_data())
print(node1)
print(node2)
# hello
# world
# hello
# world
a_node = Node(1)
print(a_node)
print(a_node.get_next())
# 1
# None