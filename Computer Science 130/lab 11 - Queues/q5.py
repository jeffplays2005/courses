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
        list_to_join = []
        for i in self.items:
            if isinstance(i, int):
                list_to_join.append(str(i))
            else:
                list_to_join.append(f"'{i}'")
        return f"-> |{', '.join(list_to_join)}| ->"
        
    def enqueue_list_from_last(self, a_list):
        for i in a_list[::-1]:
            self.enqueue(i)
            
carBrand = Queue()
carlist = ['Audi', 'Honda', 'Toyota', 'Mercedes']
carBrand.enqueue_list_from_last(carlist)
print(carBrand)
# -> |'Audi', 'Honda', 'Toyota', 'Mercedes'| ->

card = Queue()
cardlist = ['AS', 'AH', 'AC', 'AD', '2S', '2H', '2C', '2D']
card.enqueue_list_from_last(cardlist)
print(card)
print("The queue contains {} items.".format(card.size()))
# -> |'AS', 'AH', 'AC', 'AD', '2S', '2H', '2C', '2D'| ->↩
# The queue contains 8 items.
	
values = Queue()
values.enqueue(100)
studentlist = ['Aaron', 'Julia', 'Wendy', 'Paul']
values.enqueue_list_from_last(studentlist)
print(values)
# -> |'Aaron', 'Julia', 'Wendy', 'Paul', 100| ->
