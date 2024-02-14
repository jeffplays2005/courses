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
        
    def push_list_from_last(self, a_list):
        for i in a_list[::-1]:
            self.items.append(i)

my_stack = Stack()
mylist = [4, 5, 6]
my_stack.push_list_from_last(mylist)
print(my_stack)
print(my_stack.peek())
print("The stack contains {} items.".format(my_stack.size()))
# [6, 5, 4 <-
# 4
# The stack contains 3 items.
my_stack = Stack()
my_stack.push_list_from_last(['a'])
print(my_stack.peek())
print("The stack contains {} item.".format(my_stack.size()))
# a
# The stack contains 1 item.