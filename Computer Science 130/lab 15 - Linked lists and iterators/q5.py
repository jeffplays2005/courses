class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def set_data(self, new_data):
        self.data = new_data
    def set_next(self, new_next):
        self.next = new_next
    def add_after(self, value):
        new_node = Node(value,self.next)
        self.next = new_node
    def remove_after(self):
        self.next = self.next.get_next()
    def __str__(self):
        return str(self.data)

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
    # q5
    def remove_from_head(self):
        current_head = self.get_head()
        if current_head != None:
            next = current_head.get_next()
            self.head = next
            self.length -= 1
            return current_head
        else:
            return None
    def remove_from_tail(self):
        if self.length == 0: # do nothing
            return None
        # subtract 1 from length first
        self.length -= 1
        current = self.get_head() # the node that's before current
        previous = None # the one thats gonna be deleted

        while current.get_next() is not None:
            previous = current
            current = current.get_next()
        if previous is None:
            self.head = None
        else:
            current.set_next(None)
        return next.get_data()
        
fruits = LinkedList()
fruits.add('cherry')
fruits.add('banana')
fruits.add('apple')
print(fruits)
fruit = fruits.remove_from_head()
print(fruits)
print(fruit)
print(len(fruits))
print(type(fruits))
# Head: apple --> banana --> cherry
# Head: banana --> cherry
# apple
# 2
# <class '__main__.LinkedList'>
fruits = LinkedList()
fruits.add('cherry')
fruits.add('banana')
fruits.add('apple')
print(fruits)
fruit = fruits.remove_from_tail()
print(fruits)
print(fruit)
print(len(fruits))
print(type(fruits))
# Head: apple --> banana --> cherry
# Head: apple --> banana
# cherry
# 2
# <class '__main__.LinkedList'>

a_list = LinkedList()
print(a_list.remove_from_head())
print(a_list.remove_from_tail())
print(len(a_list))
# None
# None
# 0
print("=======================")
items = LinkedList()
items.add("PlayStation")
print("Items:", items)
print("Removed from tail:", items.remove_from_tail())
print("Items:", items)
# Items: Head: PlayStation↩
# Removed from tail: PlayStation↩
# Items: