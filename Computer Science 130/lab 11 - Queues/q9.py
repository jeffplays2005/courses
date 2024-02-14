class CircularQueue:
    def __init__(self, capacity = 8):
       self.items = [None] * capacity
       self.front = 0
       self.back = capacity - 1
       self.capacity = capacity
       self.count = 0
    def is_full(self):
        return len(self.items) == self.capacity
    def is_empty(self):
        return self.count == 0
    def show_contents(self):
        return f"{self.items}, front:{self.front}, back:{self.back}, count:{self.count}"

q1 = CircularQueue()
print(q1.show_contents())
print(q1.is_empty())
print(type(q1))
# [None, None, None, None, None, None, None, None], front:0, back:7, count:0
# [None, None, None, None, None, None, None, None], front:0, back: 7, count:0
# True
# <class '__main__.CircularQueue'>
q1 = CircularQueue(5)
print(q1.show_contents())
# [None, None, None, None, None], front:0, back:4, count:0