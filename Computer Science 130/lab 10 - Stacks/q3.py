class Stack():
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop(-1)
        
s = Stack()
s.push(5)
s.push(4)
s.push(9)
n1 = s.pop()
n2 = s.pop()
s.push(n2 * n1)
s.push(3)
n1 = s.pop()
n2 = s.pop()
s.push(n2 + n1)
n1 = s.pop()
n2 = s.pop()
s.push(n2 - n1)

print(s.items)