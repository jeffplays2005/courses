class BinaryTree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
    def insert_left(self, new_data):
        if self.left == None:
            self.left = BinaryTree(new_data)
        else:
            t = BinaryTree(new_data, left = self.left)
            self.left = t
    def insert_right(self, new_data):
        if self.right == None:
            self.right = BinaryTree(new_data)
        else:
            t = BinaryTree(new_data, right = self.right)
            self.right = t
    def get_data(self):
        return self.data
    def get_left(self):
        return self.left
    def get_right(self):
        return self.right

def create_a_tiny_tree():
    t = BinaryTree('a')
    t.insert_left('b')
    t.insert_right('c')
    return t
def create_a_bigger_tree():
    t = BinaryTree('a')
    t.insert_left('b')
    t.insert_right('c')
    x = t.get_left()
    x.insert_left('d')
    x.insert_right('e')
    y = x.get_left()
    y.insert_right('f')
    y = x.get_right()
    y.insert_right('g')
    return t
def create_a_tree():
    t = BinaryTree(7)
    t.insert_left(2)
    t.insert_right(9)
    x = t.get_left()
    x.insert_left(1)
    x.insert_right(5)
    y = t.get_right()
    y.insert_right(14)
    return t
def print_tree(t, level):
    print(' ' * (level*4) + str(t.get_data()))
    if t.get_left() != None:
        print('(L)', end = '')
        print_tree(t.get_left(), level + 1)
    if t.get_right() != None:
        print('(R)', end = '')
        print_tree(t.get_right(), level + 1)
        
def create_tree_from_nested_list(node_list):
    if node_list == None:
        return None
    else:
        return BinaryTree(node_list[0], create_tree_from_nested_list(node_list[1]), create_tree_from_nested_list(node_list[2]))

def create_tree_from_nested_list(node_list):
    if node_list == None:
        return None
    else:
        a_tree = BinaryTree(node_list[0])
        
    
# 1 line
def create_tree_from_nested_list(node_list): return None if node_list == None else BinaryTree(node_list[0], create_tree_from_nested_list(node_list[1]), create_tree_from_nested_list(node_list[2]))
        
tree = create_tree_from_nested_list([10, [5, None, None], None])
print(tree)
print_tree(tree, 0)
# 10
# (L)    5
tree = create_tree_from_nested_list([10, [5, None, None], [15, [11, None, None], [22, None, None]]])
print_tree(tree, 0)
# 10
# (L)    5
# (R)    15
# (L)        11
# (R)        22

# file = open(__file__)
# print(file.read())
