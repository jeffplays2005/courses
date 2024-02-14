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
    
    def __str__(self):
        return f"{self.items}"[:-1] + " <-"
    
    def clear(self):
        self.items = []
        
my_stack = Stack()
my_stack.push('a')
my_stack.push('b')
my_stack.push('c')
print(my_stack)
print(my_stack.size())
my_stack.clear()
print(my_stack.size())
# ['a', 'b', 'c' <-
# 3
# 0
s = Stack()
print(s.size())
print(s)
s.push(1)
s.push(2)
print(s)
# 0
# [ <-
# [1, 2 <-