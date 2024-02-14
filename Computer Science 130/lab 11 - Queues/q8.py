q = CircularQueue(4)
q.enqueue(5)
q.enqueue(8)
q.enqueue(6)
q.enqueue(3)
n1 = q.dequeue()
n2 = q.dequeue()
n3 = q.dequeue()
q.enqueue(4)
print(q)

[None, None, None, None]
[5, None, None, None]
[5, 8, None, None]
[5, 8, 6, None]
[5, 8, 6, 3]
[8, 6, 3, None]
[6, 3, None, None ]
[3, None, None, None]
[3, 4, None, None]