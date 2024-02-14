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

priority_queue = PriorityQueue()
priority_queue.add_all_ignore_order([11, 9, 5])
priority_queue.percolate_up(3)
print(priority_queue)
print(len(priority_queue))
print(priority_queue.number_of_swaps)
# [0, 5, 9, 11]
# 3
# 1
priority_queue = PriorityQueue()
priority_queue.add_all_ignore_order([6, 7, 8, 9, 22, 45, 1])
priority_queue.percolate_up(7)
print(priority_queue)
print(priority_queue.number_of_swaps)
# [0, 1, 7, 6, 9, 22, 45, 8]
# 2
priority_queue = PriorityQueue()
priority_queue.add_all_ignore_order([5, 23, 29, 32, 34, 4, 39, 45, 49, 42, 48])
priority_queue.percolate_up(6)
print(priority_queue)
print(priority_queue.number_of_swaps)
# [0, 4, 23, 5, 32, 34, 29, 39, 45, 49, 42, 48]
# 2
