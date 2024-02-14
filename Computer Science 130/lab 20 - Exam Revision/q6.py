class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    def insert_left(self, new_data):
        if self.left == None:
            self.left = BinaryTree(new_data)
        else:
            t = BinaryTree(new_data, left=self.left)
            self.left = t
    def insert_right(self, new_data):
        if self.right == None:
            self.right = BinaryTree(new_data)
        else:
            t = BinaryTree(new_data, right=self.right)
            self.right = t
    def get_left(self):
        return self.left
    def get_right(self):
        return self.right
    def set_data(self, data):
        self.data = data
    def get_data(self):
        return self.data
    def set_left(self, left):
        self.left = left
    def set_right(self, right):
        self.right = right
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
        if self.is_empty():
            raise IndexError("ERROR: The queue is empty!")
        return self.items.pop()
    def peek(self):
        if self.is_empty():
            raise IndexError("ERROR: The queue is empty!")
        return self.items[len(self.items)-1]
    def __str__(self):
        queue_str = "| ->"
        for i in range(len(self.items) - 1, -1, -1):
            if i == len(self.items) - 1:
                queue_str = str(self.items[i]) + queue_str
            else:
                queue_str = str(self.items[i]) + ", " + queue_str
        queue_str = "-> |" + queue_str
        return queue_str
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

def reverse_level_order(tree):
    a_stack = Stack()
    a_queue = Queue()
    a_queue.enqueue(tree)
    while a_queue.size() > 0:
        peek = a_queue.peek()
        a_stack.push(str(peek.get_data()))
        left = peek.get_left()
        right = peek.get_right()
        if left != None:
            a_queue.enqueue(left)
        if right != None:
            a_queue.enqueue(right)
        a_queue.dequeue()
    while a_stack.is_empty() == False:
        popped = a_stack.pop()
        print(popped, end = " ")
        

example_tree = BinaryTree(64)
example_tree.left = BinaryTree(84)
example_tree.right = BinaryTree(66)
example_tree.left.left = BinaryTree(32)
example_tree.left.right = BinaryTree(40)
example_tree.right.left = BinaryTree(20)
example_tree.right.right = BinaryTree(55)
print("Reverse level-order:", end=" ")
reverse_level_order(example_tree)
# Reverse level-order: 55 20 40 32 66 84 64
tiny_tree = BinaryTree("a")
tiny_tree.left = BinaryTree("b")
tiny_tree.right = BinaryTree("c")
print("Reverse level-order:", end=" ")
reverse_level_order(tiny_tree)
# Reverse level-order: c b a
