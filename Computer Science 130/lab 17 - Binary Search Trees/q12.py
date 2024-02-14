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

import math
def create_bst_from_sorted_list(sorted_list):
    root_node = math.ceil(len(sorted_list) / 2) if len(sorted_list) % 2 == 0 else math.floor(len(sorted_list) / 2)
    if not len(sorted_list):
        return None
    else:
        return BinaryTree(sorted_list[root_node], create_bst_from_sorted_list(sorted_list[:root_node]), create_bst_from_sorted_list(sorted_list[root_node+1:] if root_node+1 < len(sorted_list) else []))

# [1,2,3,4,5,6]
# [0,1,2,3,4,5]
# First:
# Grab 3:
# [0,1,2]
#
# [4,5]


tree = create_bst_from_sorted_list([1, 3, 5, 7, 9, 11, 13])
print_tree(tree, 0)
# 7
# (L)    3
# (L)        1
# (R)        5
# (R)    11
# (L)        9
# (R)        13
tree = create_bst_from_sorted_list([1,2,3,4,5,6])
print_tree(tree, 0)
# 4
# (L)    2
# (L)        1
# (R)        3
# (R)    6
# (L)        5
