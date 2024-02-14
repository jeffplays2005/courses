class CardPile:
    def __init__(self):
        self.items = []
    def add_top(self, item):
        self.items.insert(0, item)
    def add_bottom(self, item):
        self.items.append(item)
    def remove_top(self):
        return self.items.pop(0)
    def remove_bottom(self):
        return self.items.pop(-1)
    def size(self):
        return len(self.items)
    def peek_top(self):
        return self.items[0]
    def peek_bottom(self):
        return self.items[-1]
    def print_all(self, index):
        if index == 0:
            items = []
            if len(self.items) > 1:
                items += [ str(self.items[0]) ] + [ "*" for i in self.items[1:] ]
            elif len(self.items) == 1:
                items += [ str(self.items[0]) ]
            return print(" ".join(items))
        else:
            return print(" ".join([str(i) for i in self.items]))
