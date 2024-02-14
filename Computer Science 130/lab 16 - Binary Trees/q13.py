class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.data)
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
        
def basic_print(tree):
    if tree != None:
        print(tree.data, end=' ')
        basic_print(tree.left)
        basic_print(tree.right)

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
        return f"-> |{', '.join([str(i) for i in self.items])}| ->"

def print_level_order(tree):
    a_queue = Queue()
    a_queue.enqueue(tree)
    cache_queue = Queue()
    while a_queue.size() != 0 or (a_queue.size() == 0 and cache_queue.size() > 0):
        if a_queue.size() > 0:
            print(a_queue.peek().get_data(), end = " ")
            if a_queue.peek().get_left() != None:
                cache_queue.enqueue(a_queue.peek().get_left())
            if a_queue.peek().get_right() != None:
                cache_queue.enqueue(a_queue.peek().get_right())
            a_queue.dequeue()
        else:
            while cache_queue.size() > 0:
                a_queue.enqueue(cache_queue.dequeue())
    
    # while len(cache) > 0 and dont_exit = True:
    #     for i in cache:
    #         a_queue.queue(i)
    #     while a_queue.peek().get_left() != None and a_queue.peek().get_right() != None:
    #         cache.append(a_queue.peek().get_left())
    #         cache.append(a_queue.peek().get_right())
# Cut down
def print_level_order(tree, a_queue = Queue()):
    a_queue.enqueue(tree)
    while a_queue.size() > 0:
        print(a_queue.peek().get_data(), end = " ")
        if a_queue.peek().get_left() != None:
            a_queue.enqueue(a_queue.peek().get_left())
        if a_queue.peek().get_right() != None:
            a_queue.enqueue(a_queue.peek().get_right())
        a_queue.dequeue()
# 1 line
def print_level_order(tree, a_queue = Queue()): return (a_queue.enqueue(tree) or print_level_order(None, a_queue)) if a_queue.size() <= 0 and tree != None else (print(a_queue.peek().get_data(), end = " ")or (((a_queue.enqueue(a_queue.peek().get_left()) if a_queue.peek().get_left() != None else "") or (a_queue.enqueue(a_queue.peek().get_right()) if a_queue.peek().get_right() != None else "")) or a_queue.dequeue()) and print_level_order(None, a_queue)) if a_queue.size() > 0 else ""

def print_level_order(tree):
    a = Queue()
    a.enqueue(tree)
    while a.is_empty == False:
        r = a.dequeue()
        if r != None:
            print(r.data, end = '')
            a.enqueue(r.left)
            a.enqueue(r.right)

def create_a_bigger_tree():
    tree_lrl = BinaryTree(4)
    tree_lrr = BinaryTree(7)
    tree_lr = BinaryTree(6, tree_lrl, tree_lrr)
    
    tree_ll = BinaryTree(1)
    
    tree_l = BinaryTree(3, tree_ll, tree_lr)
    
    tree_rrl = BinaryTree(13)
    tree_rr = BinaryTree(14, tree_rrl)
    tree_r = BinaryTree(10, None, tree_rr)
    tree = BinaryTree(8, tree_l, tree_r)
    return tree
print_level_order(create_a_bigger_tree())
 # 
 #       8       
 #   3       10   
 # 1   6       14 
 #    4 7     13  
 
 # 8 3 10 1 6 14 4 7 13