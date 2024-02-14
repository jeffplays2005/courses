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
def print_tree(t, level):
    print(' ' * (level*4) + str(t.get_data()))
    if t.get_left() != None:
        print('(L)', end = '')
        print_tree(t.get_left(), level + 1)
    if t.get_right() != None:
        print('(R)', end = '')
        print_tree(t.get_right(), level + 1)

def get_count_internal_nodes(tree):
    if tree == None:
        return 0
    else:
        if tree.get_left() != None:
            return 1 + get_count_internal_nodes(tree.get_right()) + get_count_internal_nodes(tree.get_left())
        elif tree.get_right() != None:
            return 1 + get_count_internal_nodes(tree.get_right()) + get_count_internal_nodes(tree.get_left())
        else:
            return 0

example_tree = BinaryTree("a")
example_tree.left = BinaryTree("b")
example_tree.right = BinaryTree("c")
print(f"Internal node count: {get_count_internal_nodes(example_tree)}")
# Internal node count: 1
tree1 = BinaryTree(7)
tree1.left = BinaryTree(2)
tree1.right = BinaryTree(9)
tree1.left.left = BinaryTree(1)
tree1.left.right = BinaryTree(5)
tree1.right.right = BinaryTree(14)
print_tree(tree1, 0)
print(f"Internal node count: {get_count_internal_nodes(tree1)}")
# 7
# (L)    2
# (L)        1
# (R)        5
# (R)    9
# (R)        14
# Internal node count: 3
