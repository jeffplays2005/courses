class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if len(self.items) == 0:
            raise IndexError("ERROR: The queue is empty!")
        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            raise IndexError("ERROR: The queue is empty!")
        return self.items[len(self.items)-1]
# test
try:
    q = Queue()
    q.enqueue(2)
    q.enqueue(1)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
except IndexError as err:
    print(err)
# 2
# 1
# ERROR: The queue is empty!
try:
    q = Queue()
    print(q.peek())
except IndexError as err:
    print(err)
# ERROR: The queue is empty!