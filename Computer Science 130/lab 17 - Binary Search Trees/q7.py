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

def create_a_bigger_tree():
    tree_lrl = BinarySearchTree(4)
    tree_lrr = BinarySearchTree(7)
    tree_lr = BinarySearchTree(6, tree_lrl, tree_lrr)
    
    tree_ll = BinarySearchTree(1)
    
    tree_l = BinarySearchTree(3, tree_ll, tree_lr)
    
    tree_rrl = BinarySearchTree(13)
    tree_rr = BinarySearchTree(14, tree_rrl)
    tree_r = BinarySearchTree(10, None, tree_rr)
    tree = BinarySearchTree(8, tree_l, tree_r)
    return tree

my_tree = BinarySearchTree(15)
print(len(my_tree))
print(len(create_a_bigger_tree()))
