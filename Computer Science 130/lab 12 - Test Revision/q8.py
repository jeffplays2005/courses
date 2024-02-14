class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if self.is_empty():
            raise IndexError('ERROR: The stack is empty!')
        return self.items.pop()
    def peek(self):
        if self.is_empty():
            raise IndexError('ERROR: The stack is empty!')
        return self.items[len(self.items) - 1]
    def size(self):
        return len(self.items)
    def __str__(self):
        return str(self.items)[:-1] + ' <-'	

def combine_two_stacks(stack1, stack2):
    new_stack = Stack()
    collated_list = []
    while stack1.is_empty() == False:
        collated = f"{stack1.pop()}"
        if stack2.is_empty() == False:
            collated = f"{collated}{stack2.pop()}"
        collated_list.append(collated)
    while stack2.is_empty() == False:
        collated_list.append(stack2.pop())
        
    for i in range(len(collated_list) -1, -1, -1):
        new_stack.push(collated_list[i])
    return new_stack
        
stack1 = Stack()
stack1.push(1)
stack1.push(2)
stack1.push(3)
stack2 = Stack()
stack2.push('a')
stack2.push('b')
data = combine_two_stacks(stack1, stack2)
print(data)
print(data.peek())
stack3 = Stack()
stack3.push(1)
stack3.push(2)
stack4 = Stack()
stack4.push('a')
stack4.push('b')
stack4.push('c')
data2 = combine_two_stacks(stack3, stack4)
print(data2)
print(data2.peek())
# ['1', '2a', '3b' <-
# 3b
# ['a', '1b', '2c' <-
# 2c