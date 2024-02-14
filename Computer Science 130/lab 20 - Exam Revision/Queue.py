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
        if self.is_empty():
            raise IndexError("ERROR: The queue is empty!")
        return self.items.pop()
    def peek(self):
        if self.is_empty():
            raise IndexError("ERROR: The queue is empty!")
        return self.items[len(self.items)-1]
    def __str__(self):
        queue_str = "| ->"
        for i in range(len(self.items) - 1, -1, -1):
            if i == len(self.items) - 1:
                queue_str = str(self.items[i]) + queue_str
            else:
                queue_str = str(self.items[i]) + ", " + queue_str
        queue_str = "-> |" + queue_str
        return queue_str
