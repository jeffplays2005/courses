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
    def insert_left(self, new_data):
        if self.left == None:
            self.left = BinarySearchTree(new_data)
        else:
            tree = BinarySearchTree(new_data, left=self.left)
            self.left = tree
    def insert_right(self, new_data):
        if self.right == None:
            self.right = BinarySearchTree(new_data)
        else:
            tree = BinarySearchTree(new_data, right=self.right)
            self.right = tree
    def get_left(self):
        return self.left
    def get_right(self):
        return self.right
    def set_data(self, data):
        self.data = data
    def get_data(self):
        return self.data
    def insert(self, new_data):
        if new_data == self.data:
            return
        elif new_data < self.data:
            if self.left == None:
                self.left = BinarySearchTree(new_data)
            else:
                self.left.insert(new_data)
        else:
            if self.right == None:
                self.right = BinarySearchTree(new_data)
            else:
                self.right.insert(new_data)
    def search(self, find_data):
        if self.data == find_data:
            return True
        elif find_data < self.data and self.left != None:
            return self.left.search(find_data)
        elif find_data > self.data and self.right != None:
            return self.right.search(find_data)
        else:
            return False

def get_sorted_list(search_tree):
    list_of_items = []
    def inner_recursion(tree):
        if tree == None:
            return None
        else:
            list_of_items.append(tree.get_data())
            inner_recursion(tree.get_left())
            inner_recursion(tree.get_right())
            # get_sorted_list()
    inner_recursion(search_tree)
    return sorted(list_of_items)

def get_sorted_list(search_tree):
    if search_tree == None:
        return []
    else:
        return sorted([search_tree.get_data()] + get_sorted_list(search_tree.get_left()) + get_sorted_list(search_tree.get_right()))

def unpack_and_sort(lst):
    result = []

    for item in lst:
        if isinstance(item, list):
            result.extend(unpack_and_sort(item))
        elif item is not None:
            result.append(item)

    return sorted(result)

def get_sorted_list(tree):
    if tree is None:
        return []
    else:
        root_data = tree.get_data()
        if tree.get_left() is None:
            if tree.get_right() is None:
                return [root_data]
            else:
                right_subtree = unpack_and_sort(convert_tree_to_list(tree.get_right()))
                return [root_data, right_subtree]
        elif tree.get_right() is None:
            if tree.get_left() is None:
                return [root_data]
            else:
                left_subtree = unpack_and_sort(convert_tree_to_list(tree.get_left()))
            
        else:
            left_subtree = unpack_and_sort(convert_tree_to_list(tree.get_left()))
            right_subtree = unpack_and_sort(convert_tree_to_list(tree.get_right()))
            
            return unpack_and_sort([root_data, left_subtree, right_subtree])

# testing cases
search_tree = BinarySearchTree(5)
search_tree.insert(9)
search_tree.insert(3)
search_tree.insert(8)
print("Sorted data:", get_sorted_list(search_tree))
# Sorted data: [3, 5, 8, 9]
search_tree = BinarySearchTree(20)
print("Sorted data:", get_sorted_list(search_tree))
# Sorted data: [20]
