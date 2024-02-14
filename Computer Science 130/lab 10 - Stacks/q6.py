class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            raise IndexError("ERROR: The stack is empty!")
        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            raise IndexError("ERROR: The stack is empty!")
        return self.items[-1]
        
    def size(self):
        return len(self.items)
try:
    s = Stack()
    print (s.pop())
    print("OK")
except IndexError as err:
    print("ERROR:")
    print (err)
# ERROR:
# ERROR: The stack is empty!
try:
    s = Stack()
    print (s.peek())
except IndexError as err:
    print (err)
# ERROR: The stack is empty!