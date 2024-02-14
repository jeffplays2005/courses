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
                self.get_right().insert(value)
        elif value < self.data:
            # go left
            if self.left == None:
                self.set_left(BinarySearchTree(value))
            else:
                self.get_left().insert(value)

tree = BinarySearchTree(15)
tree.insert(99)
tree.insert(199)
tree.insert(6)
print_tree(tree, 0)
# 15
# (L)    6
# (R)    99
# (R)        199
