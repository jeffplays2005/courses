"""
Continuing on with your LinkedList class implementation, extend the LinkedList class 
by adding the method __iter__(self) which returns a LinkedListIterator object, 
passing it the head of the list, self.head.
Define a class name LinkedListIterator to represent a linked list iterator so that we can use 
a for loop to iterate through the elements in a linked list. The following code fragment uses 
the linked list iterator and prints the elements one by one.
```
for value in values:
    print(value)
```
The LinkedListIterator class contains the following:
* A field named current that defines the current node in a linked list.
* A constructor/initializer that takes a Node object (head) as a parameter and creates 
  an iterator object
* The __next__(self) method which returns the next element in the linked list. If there are 
  no more elements (in other words, if the traversal has finished) then a StopIteration exception 
  is raised.
Notes:
* You can assume that the Node class is already given.
* Submit the entire LinkedList and LinkedListIterator classes and definitions in the answer 
  box below.
"""

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

    def search(self, search_value):
        cache = self.get_head()
        counter = self.length
        while counter > 0:
            if cache.get_data() == search_value:
                return True
            else:
                cache = cache.get_next()
            counter -= 1
        return False
    def __iter__(self):
        return LinkedListIterator(self.head, self.length)

class LinkedListIterator:
    def __init__(self, head, length):
        self.head = head
        self.length = length
        self.current_iteration = 0
    def __next__(self):
        if self.current_iteration < self.length:
            self.current_iteration += 1
            current = self.head
            self.head = self.head.get_next()
            return current
        else:
            raise StopIteration()

# testing cases
values = LinkedList()
values.add('cherry')
values.add('banana')
values.add('apple')
for value in values:
    print(value)
# apple
# banana
# cherry
values = LinkedList()
values.add(1)
values.add(2)
values.add(3)
for value in values:
    print(value)
# 3
# 2
# 1