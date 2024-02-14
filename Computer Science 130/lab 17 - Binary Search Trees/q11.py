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
    
def is_binary_search_tree(my_tree, min_value, max_value):
    if my_tree == None:
        return True
    else:
        if my_tree.get_data() > max_value or my_tree.get_data() < min_value:
            return False
        else:
            return(
            is_binary_search_tree(my_tree.get_left(), min_value, my_tree.get_data())
            and
            is_binary_search_tree(my_tree.get_right(), my_tree.get_data(), max_value)
            )
# Example usage:
tree2 = BinarySearchTree(27)
tree2.set_left(BinarySearchTree(14, BinarySearchTree(10), BinarySearchTree(19)))
tree2.set_right(BinarySearchTree(35, BinarySearchTree(31), BinarySearchTree(42)))

print(is_binary_search_tree(tree2, 0, 100))  # Should return True
