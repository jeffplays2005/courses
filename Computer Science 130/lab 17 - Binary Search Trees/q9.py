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

def create_a_bigger_bst():
    base = BinarySearchTree(7)
    insert(base, 3)
    insert(base, 10)
    insert(base, 1)
    insert(base, 4)
    insert(base, 8)
    insert(base, 13)
    return base

 #       7
 #   3       10
 # 1   4   8   13
tree = create_a_bigger_bst()
print(tree.get_data())
print(tree.get_left().get_data())
print(tree.get_right().get_data())
print(tree.get_left().get_right().get_data())
# 7
# 3
# 10
# 4
