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
    def move(self, p1, p2):
        if (p1 == 0) and (p2 == 0):
            pile = self.get_pile(p1)
            if pile.size() > 0:
                top_card = pile.remove_top()
                pile.add_bottom(top_card)
        elif (p1 == 0) and (p2 > 0):
            pile1 = self.get_pile(p1)
            pile2 = self.get_pile(p2)
            if pile1.size() > 0:
                if pile2.size() == 0:
                    top_card = pile1.remove_top()
                    pile2.add_bottom(top_card)
                elif pile1.peek_top() == pile2.peek_bottom() - 1:
                    top_card = pile1.remove_top()
                    pile2.add_bottom(top_card)
        elif (p1 > 0) and (p2 > 0):
            pile1 = self.get_pile(p1)
            pile2 = self.get_pile(p2)
            if pile1.size() > 0 and pile2.size() > 0:
                top_card = pile1.peek_top()
                bottom_card = pile2.peek_bottom()
                if top_card == bottom_card - 1:
                    for i in range(pile1.size()):
                        a = pile1.remove_top()
                        pile2.add_bottom(a)
    def is_complete(self):
        if self.get_pile(0).size() == 0:
            for i in range(self.num_piles):
                if self.get_pile(i).size() == self.num_cards:
                    if self.get_pile(i).items == sorted(self.get_pile(i).items)[::-1]:
                        return True
        return False
    def play(self):
        print("********************** NEW GAME *****************************")
        move_number = 1
        while move_number <= self.max_num_moves and not self.is_complete():
            self.display()
            print("Round", move_number, "out of", self.max_num_moves, end = ": ")
            pile1 = int(input("Move from pile no.: "))
            print("Round", move_number, "out of", self.max_num_moves, end = ": ")
            pile2 = int(input("Move to pile no.: "))
            if(
                pile1 >= 0
                and pile2 >= 0
                and pile1 < self.num_piles
                and pile2 < self.num_piles
            ):
                self.move(pile1, pile2)
                move_number += 1
        if self.is_complete():
            print("You Win in", move_number - 1, "steps!\n")
        else:
            print("You Lose!\n")
