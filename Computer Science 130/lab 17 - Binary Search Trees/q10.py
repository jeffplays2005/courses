def print_tree(t, level):
    print(' ' * (level*4) + str(t.get_data()))
    if t.get_left() != None:
        print('(L)', end = '')
        print_tree(t.get_left(), level + 1)
    if t.get_right() != None:
        print('(R)', end = '')
        print_tree(t.get_right(), level + 1)

class BinarySearchTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

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
    
    def __len__(self):
        counter = 1
        if self.left != None:
            counter += len(self.left)
        if self.right != None:
            counter += len(self.right)
        return counter
        
def insert(self, value):
    if value > self.data:
        # go right
        if self.right == None:
            self.set_right(BinarySearchTree(value))
        else:
            insert(self.get_right(), value)
    elif value < self.data:
        # go left
        if self.left == None:
            self.set_left(BinarySearchTree(value))
        else:
            insert(self.get_left(), value)

def create_bst_from_list(values):
    root = values.pop(0)
    base = BinarySearchTree(root)
    for i in values:
        insert(base, i)
    return base

tree = create_bst_from_list([7, 12, 4, 9, 20])
print_tree(tree, 0)
# 7
# (L)    4
# (R)    12
# (L)        9
# (R)        20
tree = create_bst_from_list([8, 3, 1, 6, 4, 25, 78])
print_tree(tree, 0)
# 8
# (L)    3
# (L)        1
# (R)        6
# (L)            4
# (R)    25
# (R)        78
