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

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    
    def __len__(self):
        return self.length
    
    def get_head(self):
        return self.head

    def add(self, item):
        self.head = Node(item, self.head)
        self.length += 1
    # q4
    def clear(self):
        self.head = None
        self.length = 0
    
    def is_empty(self):
        return self.head == None
    
    def __str__(self):
        if self.head == None:
            return ""
        else:
            formatted = []
            current = self.head
            data = []
            data = data + [str(current.get_data())]
            next = current.get_next()
            while next != None:
                data = data + [str(next.get_data())]
                next = next.get_next()
            return "Head: "+" --> ".join([str(i) for i in data])
        
l_list = LinkedList()
print(l_list.is_empty())
l_list.add(1)
l_list.add(2)
print(l_list)
print(l_list.is_empty())
print(type(l_list))
# True
# Head: 2 --> 1
# False
# <class '__main__.LinkedList'>
l_list = LinkedList()
l_list.add("hello")
l_list.add("world")
print(l_list)
l_list.clear()
print(l_list)
print(len(l_list))
# Head: world --> hello

# 0

l_list = LinkedList()
l_list.add(1)
print(l_list.is_empty())
print(l_list)
l_list.clear()
print(l_list.is_empty())
# False↩
# Head: 1↩
# True
l_list = LinkedList()
l_list.add('a')
l_list.add('b')
l_list.add('c')
print(l_list.is_empty())
print(l_list)
l_list.clear()
print(l_list.is_empty())
# False
# Head: c --> b --> a
# True