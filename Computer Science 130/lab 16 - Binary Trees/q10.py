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

def convert_tree_to_list(tree):
    if tree == None:
        return None
    else:
        return [ tree.get_data(), convert_tree_to_list(tree.get_left()), convert_tree_to_list(tree.get_right()) ]
    
# 1 line
def convert_tree_to_list(tree): return None if tree == None else [ tree.get_data(), convert_tree_to_list(tree.get_left()), convert_tree_to_list(tree.get_right()) ]
        
result = convert_tree_to_list(create_a_bigger_tree())
print(result)
