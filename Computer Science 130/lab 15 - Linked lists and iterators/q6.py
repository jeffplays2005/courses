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
            

values = LinkedList()
print(values.search('hello'))
# False
values = LinkedList()
values.add('hello')
values.add('world')
print(values.search('hello'))
# True