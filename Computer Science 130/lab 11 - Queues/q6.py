class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if len(self.items) == 0:
            raise IndexError("ERROR: The queue is empty!")
        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            raise IndexError("ERROR: The queue is empty!")
        return self.items[len(self.items)-1]
    
    def clear(self):
        self.items = []
    
    def __str__(self):
        list_to_join = []
        for i in self.items:
            if isinstance(i, int):
                list_to_join.append(str(i))
            else:
                list_to_join.append(f"'{i}'")
        return f"-> |{', '.join(list_to_join)}| ->"
        
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
    for i in range(len(a_list)-1, -1, -1):
        self.push(a_list[i])

def merge_stack_queue_list(a_stack, a_queue, a_list):
    cringe_list = []
    queues = []
    while not a_queue.is_empty():
        queues.append(a_queue.dequeue())
    for i, item in enumerate(a_list):
        cringe_list.append(f"{item}{queues[i]}")
        
    stacks = []
    while not a_stack.is_empty():
        stacks.append(a_stack.pop())
    stacks[:] = stacks[::-1]
    for i in range(len(stacks) - 1, -1,-1):
        cringe_list.append(f"{stacks[i]}{a_list[i]}")
    return cringe_list

a_stack = Stack()
a_stack.push(1)
a_stack.push(2)
a_queue = Queue()
a_queue.enqueue(3)
a_queue.enqueue(4)
a_list = ['a', 'b']
print(merge_stack_queue_list(a_stack, a_queue, a_list))
# ['a3', 'b4', '2b', '1a']

a_queue = Queue()
for value in [45, 13, 76, 32, 56]:
    a_queue.enqueue(value)
a_stack = Stack()
for value in [19, 23, 23, 15, 29]:
    a_stack.push(value)
print(merge_stack_queue_list(a_stack, a_queue, [1, 8, 3, 2, 5]))
# ['145', '813', '376', '232', '556', '295', '152', '233', '238', '191']