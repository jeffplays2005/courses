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

def create_stack(numbers):
    a = Stack()
    for i in numbers:
        a.push(i)
    return a

def pop_two_and_subtract(a_stack):
    a = a_stack.pop()
    b = a_stack.pop()
    return (b-a)
    
stack1 = Stack()
stack1.push(2)
stack1.push(9)
print(pop_two_and_subtract(stack1))
try:
    print(pop_two_and_subtract(stack1))
except IndexError as err:
    print (err)
# -7
# ERROR: The stack is empty!
a_stack = create_stack([45, 123, 76, -3, 56, 13, -8, 9, 23, 3, 1, -9, -45])
print(pop_two_and_subtract(a_stack))
print(pop_two_and_subtract(a_stack))
print(pop_two_and_subtract(a_stack))
# 36
# 2
# -14
a_stack = create_stack([45, 123, 76, -3, 56, 13, -8, 9, 23, 3, 1, -9, -45])
a_stack.pop()
print(pop_two_and_subtract(a_stack))
print(pop_two_and_subtract(a_stack))
print(pop_two_and_subtract(a_stack))
print(a_stack)
# 10
# 20
# -17
# [45, 123, 76, -3, 56, 13 <-