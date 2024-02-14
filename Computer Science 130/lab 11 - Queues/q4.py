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
    
    def clear(self):
        self.items = []
    
    def __str__(self):
        return f"-> |{', '.join([str(i) for i in self.items])}| ->"

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q)
q.clear()
print(q)
# -> |3, 2, 1| ->
# -> || ->