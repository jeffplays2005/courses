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
def create_a_bigger_tree(): return BinaryTree(8, BinaryTree(3, BinaryTree(1), BinaryTree(6, BinaryTree(4), BinaryTree(7))), BinaryTree(10, None, BinaryTree(14, BinaryTree(13))))
        
def count_multiple_of_3(my_tree):
    if my_tree == None:
        return 0
    else:
        if my_tree.get_data() % 3 == 0:
            return 1 + count_multiple_of_3(my_tree.get_left()) + count_multiple_of_3(my_tree.get_right())
        else:
            return count_multiple_of_3(my_tree.get_left()) + count_multiple_of_3(my_tree.get_right())

# 1 line
def count_multiple_of_3(my_tree): return 0 if my_tree == None else (1 + count_multiple_of_3(my_tree.get_left()) + count_multiple_of_3(my_tree.get_right())) if my_tree.get_data() % 3 == 0 else count_multiple_of_3(my_tree.get_left()) + count_multiple_of_3(my_tree.get_right())
        
print(count_multiple_of_3(BinaryTree(5)))
# 0
print(count_multiple_of_3(create_a_bigger_tree()))
# 2
print(count_multiple_of_3(BinaryTree(6)))
# 1