class PriorityQueueMax:
    def __init__(self):
        self.binary_heap = [0]
        self.size = 0

    def insert(self, value):
        self.binary_heap.append(value)
        self.size += 1
        self.percolate_up(self.size)

    def delete_maximum(self):
        if not self.is_empty():
            heap_root_index = 1
            maximum_value = self.binary_heap[heap_root_index]
            self.binary_heap[heap_root_index] = self.binary_heap[self.size]
            self.binary_heap.pop()
            self.size -= 1
            self.percolate_down(heap_root_index)
            return maximum_value

    def peek(self):
        if not self.is_empty():
            heap_root_index = 1
            maximum_value = self.binary_heap[heap_root_index]
            return maximum_value

    def is_empty(self):
        return self.size == 0

    def percolate_up(self, index):
        while index // 2 > 0:
            if self.binary_heap[index].course_mark > self.binary_heap[index // 2].course_mark:
                self.binary_heap[index], self.binary_heap[index//2] = self.binary_heap[index//2], self.binary_heap[index]
            index = index // 2

    def percolate_down(self, index):
        while (index * 2) <= self.size:
            largest_child = self.get_larger_child_index(index)
            if self.binary_heap[index].course_mark < self.binary_heap[largest_child].course_mark:
                self.binary_heap[index], self.binary_heap[largest_child] = self.binary_heap[largest_child], self.binary_heap[index]
            index = largest_child

    def get_larger_child_index(self, index):
        if index * 2 + 1 > self.size:
            return index * 2
        else:
            if self.binary_heap[index*2].course_mark > self.binary_heap[index*2+1].course_mark:
                return index * 2
            else:
                return index * 2 + 1
