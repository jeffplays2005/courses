class CircularQueue:
    def __init__(self, capacity = 8):
       self.items = [None] * capacity
       self.front = 0
       self.back = capacity - 1
       self.capacity = capacity
       self.count = 0
    def __str__(self):
        # aaa = []
        # for i in range(len(self.items)-1,-1,-1):
        #     if self.items[(self.front + i) % self.capacity] != None:
        #         aaa.append(str(self.items[(self.front + i) % self.capacity]))
        # return f"-> |{', '.join(aaa)}| ->"
        aaa = []
        front = self.front
        back = self.back
        if front > back and self.count != 0:
            maximum = []
            back = self.items[0:self.back+1][::-1]
            front = self.items[self.front:len(self.items)]
            maximum += front
            maximum += back
            for i in range(len(maximum)-1,-1,-1):
                 aaa.append(str(maximum[i]))
            return f"-> |{', '.join(aaa)}| ->"
        else:
            maximum = self.items[front:back+1]
            maximum = [ i for i in maximum if i != None ]
            for i in range(len(maximum)-1,-1,-1):
                 aaa.append(str(maximum[i]))
            return f"-> |{', '.join(aaa)}| ->"
    def enqueue(self, item):
        if not self.is_full():
            self.back = (self.back + 1) % self.capacity
            self.items[self.back] = item
            self.count += 1
        else:
            raise IndexError("ERROR: The queue is full.")
    def dequeue(self):
        if not self.is_empty():
            item = self.items[self.front]
            # self.items[self.front] = None
            self.front = (self.front + 1) % self.capacity
            self.count -= 1
            return item
        else:
            raise IndexError("ERROR: The queue is empty.")
    def is_full(self):
        return self.count == self.capacity
    def is_empty(self):
        return self.count == 0
    def show_contents(self):
        return f"{self.items}, front:{self.front}, back:{self.back}, count:{self.count}"
# test
# q1 = CircularQueue(4)
# print(q1)
# q1.enqueue(1)
# print(q1)
# q1.enqueue(2)
# print(q1)
# q1.enqueue(3)
# print(q1)
# q1.enqueue(4)
# print(q1)
# print("Full?", q1.is_full())
# print("Empty?", q1.is_empty())
# # -> || ->
# # -> |1| ->
# # -> |2, 1| ->
# # -> |3, 2, 1| ->
# # -> |4, 3, 2, 1| ->
# # Full? True
# # Empty? False
# 
# try:
#     q1 = CircularQueue(4)
#     q1.enqueue("A")
#     print(q1)
#     q1.enqueue("B")
#     print(q1)
#     print("Dequeued item: ", q1.dequeue())
#     print(q1)
#     print("Dequeued item: ", q1.dequeue())
#     print(q1)
#     print("Full?", q1.is_full())
#     print("Empty?", q1.is_empty())
# except IndexError as err:
#     print(err) 
# # -> |A| ->
# # -> |B, A| ->
# # Dequeued item:  A
# # -> |B| ->
# # Dequeued item:  B
# # -> || ->
# # Full? False
# # Empty? True
# try:
#     q1 = CircularQueue(3)
#     print("Dequeued item:", q1.dequeue())
#     print(q1)
# except IndexError as err:
#     print(err)
# # ERROR: The queue is empty.
# # #####
# 
# try:
#     q1 = CircularQueue(3)
#     q1.enqueue("A")
#     print(q1)
#     q1.enqueue("B")
#     print(q1)
#     q1.enqueue("C")
#     print(q1)
#     q1.enqueue("D")
#     print(q1)
# except IndexError as err:
#     print(err)
# # -> |A| ->
# # -> |B, A| ->
# # -> |C, B, A| ->
# # ERROR: The queue is full.
# 
# try:
#     q1 = CircularQueue(3)
#     print("Dequeued item:", q1.dequeue())
#     print(q1)
# except IndexError as err:
#     print(err)
# # ERROR: The queue is empty.

try:
    q1 = CircularQueue(4)
    print(q1)
    q1.enqueue(1)
    print(q1)
    q1.enqueue(2)
    print(q1)
    q1.enqueue(3)
    print(q1)
    print("Dequeued item:", q1.dequeue())
    print(q1)
    q1.enqueue(4)
    print(q1)
    print("Dequeued item:", q1.dequeue())
    print(q1)
    q1.enqueue(5)
    print(q1)
except IndexError as err:
    print(err)
    
# -> || ->
# -> |1| ->
# -> |2, 1| ->
# -> |3, 2, 1| ->
# Dequeued item: 1
# -> |3, 2| ->
# -> |4, 3, 2| ->
# Dequeued item: 2
# -> |4, 3| ->
# -> |5, 4, 3| ->