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
def basic_print(tree):
    if tree != None:
        print(tree.data, end=' ')
        basic_print(tree.left)
        basic_print(tree.right)

def create_a_bigger_tree(): return BinaryTree(8, BinaryTree(3, BinaryTree(1), BinaryTree(6, BinaryTree(4), BinaryTree(7))), BinaryTree(10, None, BinaryTree(14, BinaryTree(13))))

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

tree = create_a_bigger_tree()
print(tree.get_data())
print(tree.get_left().get_data())
print(tree.get_right().get_data())
print(tree.get_left().get_right().get_data())
# 8
# 3
# 10
# 6