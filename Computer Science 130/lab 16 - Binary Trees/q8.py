def create_a_bigger_tree(): return BinaryTree(8, BinaryTree(3, BinaryTree(1), BinaryTree(6, BinaryTree(4), BinaryTree(7))), BinaryTree(10, None, BinaryTree(14, BinaryTree(13))))
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

def get_height(tree):
    if tree == None:
        return -1
    else:
        if get_height(tree.get_left()) >= get_height(tree.get_right()):
            return get_height(tree.get_left()) + 1
        else:
            return get_height(tree.get_right()) + 1

# 1 line
def get_height(tree): return -1 if tree == None else get_height(tree.get_left()) + 1 if get_height(tree.get_left()) >= get_height(tree.get_right()) else get_height(tree.get_right()) + 1

print(get_height(BinaryTree(6)))
# 0
print(get_height(create_a_bigger_tree()))
# 3