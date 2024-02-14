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
            return print(" ".join([ str(i) for i in self.items ]))
            
class Solitaire:
    def __init__(self, cards):
        self.piles = []
        self.num_cards = len(cards)
        self.num_piles = (self.num_cards // 8) + 3
        self.max_num_moves = self.num_cards * 2
        for i in range(self.num_piles):
            self.piles.append(CardPile())
        for i in range(self.num_cards):
            self.piles[0].add_bottom(cards[i])
    def get_pile(self, i):
        return self.piles[i]
    def display(self):
        for i in range(self.num_piles):
            print(i, end = ": ")
            self.piles[i].print_all(i)
