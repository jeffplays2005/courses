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
    
    def percolate_down(self, index):
        while (index * 2) <= len(self.binary_heap):
            smallest_child = self.get_smaller_child_index(index)
            if self.binary_heap[index] > self.binary_heap[smallest_child]:
                self.binary_heap[index], self.binary_heap[smallest_child] = self.binary_heap[smallest_child], self.binary_heap[index]
                index = smallest_child
                self.number_of_swaps += 1
            else:
                break

pq2 = PriorityQueue()
pq2.add_all_ignore_order([2, 7, 26, 25, 19, 17, 1, 90, 3, 36])

print(pq2)
pq2.percolate_down(5)
print(pq2)
pq2.percolate_down(4)
print(pq2)
pq2.percolate_down(3)
print(pq2)
pq2.percolate_down(2)
print(pq2)
pq2.percolate_down(1)
print(pq2)
print(pq2.number_of_swaps)
# [0, 2, 7, 26, 25, 19, 17, 1, 90, 3, 36]
# [0, 2, 7, 26, 25, 19, 17, 1, 90, 3, 36]
# [0, 2, 7, 26, 3, 19, 17, 1, 90, 25, 36]
# [0, 2, 7, 1, 3, 19, 17, 26, 90, 25, 36]
# [0, 2, 3, 1, 7, 19, 17, 26, 90, 25, 36]
# [0, 1, 3, 2, 7, 19, 17, 26, 90, 25, 36]
# 4
