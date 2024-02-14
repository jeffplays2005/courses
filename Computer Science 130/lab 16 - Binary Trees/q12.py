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

# def print_inorder(tree):
#     if tree == None:
#         return ""
#     else:
#         return print(f"{print_inorder(tree.get_left())} {'' if tree.get_data() == None else tree.get_data()} {print_inorder(tree.get_right())}")

def print_inorder(tree):
    if tree == None:
        return ""
    else:
        print_inorder(tree.get_left()) 
        print(tree.data, end = ' ')
        print_inorder(tree.get_right())

def print_inorder(tree): return "" if tree == None else (print_inorder(tree.get_left()) or print(tree.data, end = ' ') or print_inorder(tree.get_right()))

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

print_inorder(create_a_bigger_tree())