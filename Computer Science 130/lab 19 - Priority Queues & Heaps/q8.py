class PriorityQueue:
    def __init__(self):
        self.binary_heap = [0]
        self.size = 0
        self.number_of_swaps = 0

    def __str__(self):
        return str(self.binary_heap)

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size
    
    def add_all_ignore_order(self, a_list):
        for i in a_list:
            self.binary_heap.append(i)
            self.size += 1
    
    def percolate_up(self, index):
        while index // 2 > 0:
            parent_index = index // 2
            if self.binary_heap[index] < self.binary_heap[parent_index]:
                self.binary_heap[index], self.binary_heap[parent_index] = self.binary_heap[parent_index], self.binary_heap[index]
                self.number_of_swaps += 1
                index = parent_index
            else:
                break

    def insert(self, element):
        self.binary_heap.append(element)
        self.size += 1
        self.percolate_up(len(self.binary_heap)-1)
    
    def get_smaller_child_index(self, index):
        left_child_index = 2 * index
        right_child_index = 2 * index + 1

        if right_child_index <= self.size:
            if self.binary_heap[left_child_index] < self.binary_heap[right_child_index]:
                return left_child_index
            else:
                return right_child_index
        elif left_child_index <= self.size:
            return left_child_index
        else:
            return None

priority_queue2 = PriorityQueue()
for i in [1, 3, 2, 4, 6, 7, 5]:
    priority_queue2.insert(i)

print(priority_queue2)
print(priority_queue2.get_smaller_child_index(3))
# [0, 1, 3, 2, 4, 6, 7, 5]
# 7
