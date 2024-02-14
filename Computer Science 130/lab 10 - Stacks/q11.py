class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            raise IndexError("ERROR: The stack is empty!")
        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            raise IndexError("ERROR: The stack is empty!")
        return self.items[-1]
        
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return f"{self.items}"[:-1] + " <-"
    
    def clear(self):
        self.items = []
        
    def push_list_from_last(self, a_list):
        for i in a_list[::-1]:
            self.items.append(i)
            
def simple_balanced_brackets(text):
    brackets = Stack()
    for pos,i in enumerate(list(text)):
        if i == "(":
            brackets.push(i)
        elif i == ")":
            try:
                brackets.pop()
            except:
                return False
    if brackets.is_empty():
        return True
    else:
        return False
        
def simple_balanced_brackets(text):
    brackets = Stack()
    for i in list(text):
        if i == "(":
            brackets.push(i)
        elif i == ")":
            try:
                brackets.pop()
            except:
                return False
    if brackets.is_empty():
        return True
    else:
        return False
# testing
print(simple_balanced_brackets('(x)(())()'))
# True
print(simple_balanced_brackets('x(y)z('))
# # False
print(simple_balanced_brackets('xy)(z'))
# False