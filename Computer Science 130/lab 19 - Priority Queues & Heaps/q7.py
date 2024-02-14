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
        

priority_queue3 = PriorityQueue()
priority_queue3.insert(6)
priority_queue3.insert(9)
priority_queue3.insert(8)
priority_queue3.insert(5)
print(priority_queue3)
print(len(priority_queue3))
print(priority_queue3.number_of_swaps)
# [0, 5, 6, 8, 9]
# 4
# 2
priority_queue4  = PriorityQueue()
numbers = [49, 42, 45, 53, 35, 37, 23]
for number in numbers:
    priority_queue4.insert(number)
print(priority_queue4)
print(priority_queue4.number_of_swaps)
# [0, 23, 42, 35, 53, 49, 45, 37]
# 6
