import os
import random

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
        self.as_cool = AsCool()
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
        print(self.as_cool.color_schemes()['main'])
        print(self.as_cool.get_banner())
        move_number = 1
        while move_number <= self.max_num_moves and not self.is_complete():
            self.display()
            
            print(self.as_cool.get_round(move_number, self.max_num_moves), end = ": ")
            pile1 = int(input(self.as_cool.get_move_input()))
            print(self.as_cool.get_round(move_number, self.max_num_moves), end = ": ")
            pile2 = int(input(self.as_cool.get_move_input()))
            if pile1 >= 0 and pile2 >= 0 and pile1 < self.num_piles and pile2 < self.num_piles:
                self.move(pile1, pile2)
                move_number += 1
        if self.is_complete():
            self.as_cool.add_win()
            print(self.as_cool.get_win(move_number-1))
        else:
            print(self.as_cool.get_loss())

class AsCool:
    def __init__(self):
        self.truecolor = os.environ.get('COLORTERM') != None
        self.twofivesix_color = os.environ.get('TERM') != None
    def get_banner(self):
        return self.color_schemes()['banner']
    def get_loss(self):
        return self.color_schemes()['loss']
    def get_win(self, score):
        win = self.color_schemes()['win']
        return str(score).join(win.split('$'))
    def get_round(self, start, end):
        round = self.color_schemes()['round']
        return str(end).join((str(start).join(round.split("{x}"))).split("{y}"))
    def get_move_input(self):
        return self.color_schemes()['move_input']
    def color_schemes(self):
        # remember to replace $ with the score in win!
        colors = {
            "true_color": {
                "main": '\x1B[38;2;255;87;51m.\x1B[39m\x1B[38;2;223;90;77m▄\x1B[39m\x1B[38;2;191;93;102m▄\x1B[39m\x1B[38;2;159;96;128m \x1B[39m\x1B[38;2;128;100;153m·\x1B[39m\x1B[38;2;96;103;179m \x1B[39m\x1B[38;2;64;106;204m \x1B[39m\x1B[38;2;32;109;230m \x1B[39m\x1B[38;2;0;112;255m \x1B[39m\x1B[38;2;2;117;246m \x1B[39m\x1B[38;2;3;122;238m \x1B[39m\x1B[38;2;5;127;229m \x1B[39m\x1B[38;2;7;132;221m▄\x1B[39m\x1B[38;2;8;137;212m▄\x1B[39m\x1B[38;2;10;142;203m▌\x1B[39m\x1B[38;2;11;147;195m \x1B[39m\x1B[38;2;13;152;186m \x1B[39m\x1B[38;2;40;159;165m▪\x1B[39m\x1B[38;2;67;166;145m \x1B[39m\x1B[38;2;94;173;124m \x1B[39m\x1B[38;2;121;180;103m▄\x1B[39m\x1B[38;2;147;187;83m▄\x1B[39m\x1B[38;2;174;194;62m▄\x1B[39m\x1B[38;2;201;201;41m▄\x1B[39m\x1B[38;2;228;208;21m▄\x1B[39m\x1B[38;2;255;215;0m \x1B[39m\x1B[38;2;227;210;12m▄\x1B[39m\x1B[38;2;198;205;24m▄\x1B[39m\x1B[38;2;170;199;36m▄\x1B[39m\x1B[38;2;142;194;48m·\x1B[39m\x1B[38;2;113;189;59m \x1B[39m\x1B[38;2;85;184;71m▪\x1B[39m\x1B[38;2;57;178;83m \x1B[39m\x1B[38;2;28;173;95m \x1B[39m\x1B[38;2;0;168;107m▄\x1B[39m\x1B[38;2;18;154;100m▄\x1B[39m\x1B[38;2;37;140;93m▄\x1B[39m\x1B[38;2;55;126;85m \x1B[39m\x1B[38;2;73;112;78m \x1B[39m\x1B[38;2;92;98;71m▄\x1B[39m\x1B[38;2;110;84;64m▄\x1B[39m\x1B[38;2;128;70;56m▄\x1B[39m\x1B[38;2;147;56;49m \x1B[39m\x1B[38;2;165;42;42m.\x1B[39m\n' + '\x1B[38;2;255;87;51m▐\x1B[39m\x1B[38;2;223;90;77m█\x1B[39m\x1B[38;2;191;93;102m \x1B[39m\x1B[38;2;159;96;128m▀\x1B[39m\x1B[38;2;128;100;153m.\x1B[39m\x1B[38;2;96;103;179m \x1B[39m\x1B[38;2;64;106;204m▪\x1B[39m\x1B[38;2;32;109;230m \x1B[39m\x1B[38;2;0;112;255m \x1B[39m\x1B[38;2;2;117;246m \x1B[39m\x1B[38;2;3;122;238m \x1B[39m\x1B[38;2;5;127;229m \x1B[39m\x1B[38;2;7;132;221m█\x1B[39m\x1B[38;2;8;137;212m█\x1B[39m\x1B[38;2;10;142;203m•\x1B[39m\x1B[38;2;11;147;195m \x1B[39m\x1B[38;2;13;152;186m \x1B[39m\x1B[38;2;40;159;165m█\x1B[39m\x1B[38;2;67;166;145m█\x1B[39m\x1B[38;2;94;173;124m \x1B[39m\x1B[38;2;121;180;103m•\x1B[39m\x1B[38;2;147;187;83m█\x1B[39m\x1B[38;2;174;194;62m█\x1B[39m\x1B[38;2;201;201;41m \x1B[39m\x1B[38;2;228;208;21m \x1B[39m\x1B[38;2;255;215;0m▐\x1B[39m\x1B[38;2;227;210;12m█\x1B[39m\x1B[38;2;198;205;24m \x1B[39m\x1B[38;2;170;199;36m▀\x1B[39m\x1B[38;2;142;194;48m█\x1B[39m\x1B[38;2;113;189;59m \x1B[39m\x1B[38;2;85;184;71m█\x1B[39m\x1B[38;2;57;178;83m█\x1B[39m\x1B[38;2;28;173;95m \x1B[39m\x1B[38;2;0;168;107m▀\x1B[39m\x1B[38;2;18;154;100m▄\x1B[39m\x1B[38;2;37;140;93m \x1B[39m\x1B[38;2;55;126;85m█\x1B[39m\x1B[38;2;73;112;78m·\x1B[39m\x1B[38;2;92;98;71m▀\x1B[39m\x1B[38;2;110;84;64m▄\x1B[39m\x1B[38;2;128;70;56m.\x1B[39m\x1B[38;2;147;56;49m▀\x1B[39m\x1B[38;2;165;42;42m·\x1B[39m\n' + '\x1B[38;2;255;87;51m▄\x1B[39m\x1B[38;2;223;90;77m▀\x1B[39m\x1B[38;2;191;93;102m▀\x1B[39m\x1B[38;2;159;96;128m▀\x1B[39m\x1B[38;2;128;100;153m█\x1B[39m\x1B[38;2;96;103;179m▄\x1B[39m\x1B[38;2;64;106;204m \x1B[39m\x1B[38;2;32;109;230m▄\x1B[39m\x1B[38;2;0;112;255m█\x1B[39m\x1B[38;2;2;117;246m▀\x1B[39m\x1B[38;2;3;122;238m▄\x1B[39m\x1B[38;2;5;127;229m \x1B[39m\x1B[38;2;7;132;221m█\x1B[39m\x1B[38;2;8;137;212m█\x1B[39m\x1B[38;2;10;142;203m▪\x1B[39m\x1B[38;2;11;147;195m \x1B[39m\x1B[38;2;13;152;186m \x1B[39m\x1B[38;2;40;159;165m▐\x1B[39m\x1B[38;2;67;166;145m█\x1B[39m\x1B[38;2;94;173;124m·\x1B[39m\x1B[38;2;121;180;103m \x1B[39m\x1B[38;2;147;187;83m▐\x1B[39m\x1B[38;2;174;194;62m█\x1B[39m\x1B[38;2;201;201;41m.\x1B[39m\x1B[38;2;228;208;21m▪\x1B[39m\x1B[38;2;255;215;0m▄\x1B[39m\x1B[38;2;227;210;12m█\x1B[39m\x1B[38;2;198;205;24m▀\x1B[39m\x1B[38;2;170;199;36m▀\x1B[39m\x1B[38;2;142;194;48m█\x1B[39m\x1B[38;2;113;189;59m \x1B[39m\x1B[38;2;85;184;71m▐\x1B[39m\x1B[38;2;57;178;83m█\x1B[39m\x1B[38;2;28;173;95m·\x1B[39m\x1B[38;2;0;168;107m▐\x1B[39m\x1B[38;2;18;154;100m▀\x1B[39m\x1B[38;2;37;140;93m▀\x1B[39m\x1B[38;2;55;126;85m▄\x1B[39m\x1B[38;2;73;112;78m \x1B[39m\x1B[38;2;92;98;71m▐\x1B[39m\x1B[38;2;110;84;64m▀\x1B[39m\x1B[38;2;128;70;56m▀\x1B[39m\x1B[38;2;147;56;49m▪\x1B[39m\x1B[38;2;165;42;42m▄\x1B[39m\n' + '\x1B[38;2;255;87;51m▐\x1B[39m\x1B[38;2;223;90;77m█\x1B[39m\x1B[38;2;191;93;102m▄\x1B[39m\x1B[38;2;159;96;128m▪\x1B[39m\x1B[38;2;128;100;153m▐\x1B[39m\x1B[38;2;96;103;179m█\x1B[39m\x1B[38;2;64;106;204m▐\x1B[39m\x1B[38;2;32;109;230m█\x1B[39m\x1B[38;2;0;112;255m▌\x1B[39m\x1B[38;2;2;117;246m.\x1B[39m\x1B[38;2;3;122;238m▐\x1B[39m\x1B[38;2;5;127;229m▌\x1B[39m\x1B[38;2;7;132;221m▐\x1B[39m\x1B[38;2;8;137;212m█\x1B[39m\x1B[38;2;10;142;203m▌\x1B[39m\x1B[38;2;11;147;195m▐\x1B[39m\x1B[38;2;13;152;186m▌\x1B[39m\x1B[38;2;40;159;165m▐\x1B[39m\x1B[38;2;67;166;145m█\x1B[39m\x1B[38;2;94;173;124m▌\x1B[39m\x1B[38;2;121;180;103m \x1B[39m\x1B[38;2;147;187;83m▐\x1B[39m\x1B[38;2;174;194;62m█\x1B[39m\x1B[38;2;201;201;41m▌\x1B[39m\x1B[38;2;228;208;21m·\x1B[39m\x1B[38;2;255;215;0m▐\x1B[39m\x1B[38;2;227;210;12m█\x1B[39m\x1B[38;2;198;205;24m \x1B[39m\x1B[38;2;170;199;36m▪\x1B[39m\x1B[38;2;142;194;48m▐\x1B[39m\x1B[38;2;113;189;59m▌\x1B[39m\x1B[38;2;85;184;71m▐\x1B[39m\x1B[38;2;57;178;83m█\x1B[39m\x1B[38;2;28;173;95m▌\x1B[39m\x1B[38;2;0;168;107m▐\x1B[39m\x1B[38;2;18;154;100m█\x1B[39m\x1B[38;2;37;140;93m•\x1B[39m\x1B[38;2;55;126;85m█\x1B[39m\x1B[38;2;73;112;78m▌\x1B[39m\x1B[38;2;92;98;71m▐\x1B[39m\x1B[38;2;110;84;64m█\x1B[39m\x1B[38;2;128;70;56m▄\x1B[39m\x1B[38;2;147;56;49m▄\x1B[39m\x1B[38;2;165;42;42m▌\x1B[39m\n' + '\x1B[38;2;255;87;51m \x1B[39m\x1B[38;2;223;90;77m▀\x1B[39m\x1B[38;2;191;93;102m▀\x1B[39m\x1B[38;2;159;96;128m▀\x1B[39m\x1B[38;2;128;100;153m▀\x1B[39m\x1B[38;2;96;103;179m \x1B[39m\x1B[38;2;64;106;204m \x1B[39m\x1B[38;2;32;109;230m▀\x1B[39m\x1B[38;2;0;112;255m█\x1B[39m\x1B[38;2;2;117;246m▄\x1B[39m\x1B[38;2;3;122;238m▀\x1B[39m\x1B[38;2;5;127;229m▪\x1B[39m\x1B[38;2;7;132;221m.\x1B[39m\x1B[38;2;8;137;212m▀\x1B[39m\x1B[38;2;10;142;203m▀\x1B[39m\x1B[38;2;11;147;195m▀\x1B[39m\x1B[38;2;13;152;186m \x1B[39m\x1B[38;2;40;159;165m▀\x1B[39m\x1B[38;2;67;166;145m▀\x1B[39m\x1B[38;2;94;173;124m▀\x1B[39m\x1B[38;2;121;180;103m \x1B[39m\x1B[38;2;147;187;83m▀\x1B[39m\x1B[38;2;174;194;62m▀\x1B[39m\x1B[38;2;201;201;41m▀\x1B[39m\x1B[38;2;228;208;21m \x1B[39m\x1B[38;2;255;215;0m \x1B[39m\x1B[38;2;227;210;12m▀\x1B[39m\x1B[38;2;198;205;24m \x1B[39m\x1B[38;2;170;199;36m \x1B[39m\x1B[38;2;142;194;48m▀\x1B[39m\x1B[38;2;113;189;59m \x1B[39m\x1B[38;2;85;184;71m▀\x1B[39m\x1B[38;2;57;178;83m▀\x1B[39m\x1B[38;2;28;173;95m▀\x1B[39m\x1B[38;2;0;168;107m.\x1B[39m\x1B[38;2;18;154;100m▀\x1B[39m\x1B[38;2;37;140;93m \x1B[39m\x1B[38;2;55;126;85m \x1B[39m\x1B[38;2;73;112;78m▀\x1B[39m\x1B[38;2;92;98;71m \x1B[39m\x1B[38;2;110;84;64m▀\x1B[39m\x1B[38;2;128;70;56m▀\x1B[39m\x1B[38;2;147;56;49m▀\x1B[39m\x1B[38;2;165;42;42m \x1B[39m',
                "banner": "\x1B[38;2;34;139;34m*\x1B[39m\x1B[38;2;32;141;32m*\x1B[39m\x1B[38;2;30;142;30m*\x1B[39m\x1B[38;2;29;144;29m*\x1B[39m\x1B[38;2;27;146;27m*\x1B[39m\x1B[38;2;25;147;25m*\x1B[39m\x1B[38;2;23;149;23m*\x1B[39m\x1B[38;2;21;150;21m*\x1B[39m\x1B[38;2;20;152;20m*\x1B[39m\x1B[38;2;18;154;18m*\x1B[39m\x1B[38;2;16;155;16m*\x1B[39m\x1B[38;2;14;157;14m*\x1B[39m\x1B[38;2;13;159;13m*\x1B[39m\x1B[38;2;11;160;11m*\x1B[39m\x1B[38;2;9;162;9m*\x1B[39m\x1B[38;2;7;163;7m*\x1B[39m\x1B[38;2;5;165;5m*\x1B[39m\x1B[38;2;4;167;4m*\x1B[39m\x1B[38;2;2;168;2m*\x1B[39m\x1B[38;2;0;170;0m*\x1B[39m\x1B[38;2;3;172;3m*\x1B[39m\x1B[38;2;5;174;5m*\x1B[39m \x1B[38;2;8;175;8mN\x1B[39m\x1B[38;2;11;177;11mE\x1B[39m\x1B[38;2;13;179;13mW\x1B[39m \x1B[38;2;16;181;16mG\x1B[39m\x1B[38;2;19;183;19mA\x1B[39m\x1B[38;2;21;184;21mM\x1B[39m\x1B[38;2;24;186;24mE\x1B[39m \x1B[38;2;27;188;27m*\x1B[39m\x1B[38;2;30;190;30m*\x1B[39m\x1B[38;2;32;191;32m*\x1B[39m\x1B[38;2;35;193;35m*\x1B[39m\x1B[38;2;38;195;38m*\x1B[39m\x1B[38;2;40;197;40m*\x1B[39m\x1B[38;2;43;199;43m*\x1B[39m\x1B[38;2;46;200;46m*\x1B[39m\x1B[38;2;48;202;48m*\x1B[39m\x1B[38;2;51;204;51m*\x1B[39m\x1B[38;2;54;207;54m*\x1B[39m\x1B[38;2;56;209;56m*\x1B[39m\x1B[38;2;59;212;59m*\x1B[39m\x1B[38;2;62;215;62m*\x1B[39m\x1B[38;2;64;217;64m*\x1B[39m\x1B[38;2;67;220;67m*\x1B[39m\x1B[38;2;70;223;70m*\x1B[39m\x1B[38;2;72;225;72m*\x1B[39m\x1B[38;2;75;228;75m*\x1B[39m\x1B[38;2;78;231;78m*\x1B[39m\x1B[38;2;81;234;81m*\x1B[39m\x1B[38;2;83;236;83m*\x1B[39m\x1B[38;2;86;239;86m*\x1B[39m\x1B[38;2;89;242;89m*\x1B[39m\x1B[38;2;91;244;91m*\x1B[39m\x1B[38;2;94;247;94m*\x1B[39m\x1B[38;2;97;250;97m*\x1B[39m\x1B[38;2;99;252;99m*\x1B[39m\x1B[38;2;102;255;102m*\x1B[39m",
                "loss": "\x1B[38;2;255;0;0mY\x1B[39m\x1B[38;2;255;23;0mo\x1B[39m\x1B[38;2;255;46;0mu\x1B[39m \x1B[38;2;255;69;0mL\x1B[39m\x1B[38;2;217;52;17mo\x1B[39m\x1B[38;2;178;34;34ms\x1B[39m\x1B[38;2;153;17;17me\x1B[39m\x1B[38;2;128;0;0m!\x1B[39m\n",
                "win": "\x1B[38;2;255;215;0mY\x1B[39m\x1B[38;2;246;203;8mo\x1B[39m\x1B[38;2;237;190;16mu\x1B[39m \x1B[38;2;227;178;24mW\x1B[39m\x1B[38;2;218;165;32mi\x1B[39m\x1B[38;2;225;175;26mn\x1B[39m \x1B[38;2;233;185;19mi\x1B[39m\x1B[38;2;240;195;13mn\x1B[39m \x1B[38;2;248;205;6m$\x1B[39m \x1B[38;2;255;215;0ms\x1B[39m\x1B[38;2;248;205;6mt\x1B[39m\x1B[38;2;240;195;13me\x1B[39m\x1B[38;2;233;185;19mp\x1B[39m\x1B[38;2;225;175;26ms\x1B[39m\x1B[38;2;218;165;32m!\x1B[39m\n",
                "round": "\x1B[38;2;255;87;51mR\x1B[39m\x1B[38;2;219;91;80mo\x1B[39m\x1B[38;2;182;94;109mu\x1B[39m\x1B[38;2;146;98;138mn\x1B[39m\x1B[38;2;109;101;168md\x1B[39m \x1B[38;2;73;105;197m{x}\x1B[39m \x1B[38;2;2;118;245mo\x1B[39m\x1B[38;2;4;123;235mu\x1B[39m\x1B[38;2;6;129;225mt\x1B[39m \x1B[38;2;7;135;216mo\x1B[39m\x1B[38;2;9;141;206mf\x1B[39m \x1B[38;2;11;146;196m{y}\x1B[39m",
                "move_input": "\x1B[38;2;134;184;93mM\x1B[39m\x1B[38;2;174;194;62mo\x1B[39m\x1B[38;2;215;205;31mv\x1B[39m\x1B[38;2;255;215;0me\x1B[39m \x1B[38;2;213;207;18mf\x1B[39m\x1B[38;2;170;199;36mr\x1B[39m\x1B[38;2;128;192;54mo\x1B[39m\x1B[38;2;85;184;71mm\x1B[39m \x1B[38;2;43;176;89mp\x1B[39m\x1B[38;2;0;168;107mi\x1B[39m\x1B[38;2;28;147;96ml\x1B[39m\x1B[38;2;55;126;85me\x1B[39m \x1B[38;2;83;105;75mn\x1B[39m\x1B[38;2;110;84;64mo\x1B[39m\x1B[38;2;138;63;53m.\x1B[39m\x1B[38;2;165;42;42m:\x1B[39m "
            },
            "256": {
                "main": """.▄▄ ·       ▄▄▌  ▪  ▄▄▄▄▄ ▄▄▄· ▪  ▄▄▄  ▄▄▄ .
▐█ ▀. ▪     ██•  ██ •██  ▐█ ▀█ ██ ▀▄ █·▀▄.▀·
▄▀▀▀█▄ ▄█▀▄ ██▪  ▐█· ▐█.▪▄█▀▀█ ▐█·▐▀▀▄ ▐▀▀▪▄
▐█▄▪▐█▐█▌.▐▌▐█▌▐▌▐█▌ ▐█▌·▐█ ▪▐▌▐█▌▐█•█▌▐█▄▄▌
 ▀▀▀▀  ▀█▄▀▪.▀▀▀ ▀▀▀ ▀▀▀  ▀  ▀ ▀▀▀.▀  ▀ ▀▀▀ """,
                "banner": "\x1B[38;5;71m*\x1B[39m\x1B[38;5;71m*\x1B[39m\x1B[38;5;71m*\x1B[39m\x1B[38;5;71m*\x1B[39m\x1B[38;5;71m*\x1B[39m\x1B[38;5;34m*\x1B[39m\x1B[38;5;34m*\x1B[39m\x1B[38;5;34m*\x1B[39m\x1B[38;5;34m*\x1B[39m\x1B[38;5;34m*\x1B[39m\x1B[38;5;34m*\x1B[39m\x1B[38;5;34m*\x1B[39m\x1B[38;5;34m*\x1B[39m\x1B[38;5;34m*\x1B[39m\x1B[38;5;34m*\x1B[39m\x1B[38;5;34m*\x1B[39m\x1B[38;5;34m*\x1B[39m\x1B[38;5;34m*\x1B[39m\x1B[38;5;34m*\x1B[39m\x1B[38;5;34m*\x1B[39m\x1B[38;5;34m*\x1B[39m\x1B[38;5;34m*\x1B[39m \x1B[38;5;34mN\x1B[39m\x1B[38;5;34mE\x1B[39m\x1B[38;5;40mW\x1B[39m \x1B[38;5;40mG\x1B[39m\x1B[38;5;40mA\x1B[39m\x1B[38;5;40mM\x1B[39m\x1B[38;5;40mE\x1B[39m \x1B[38;5;77m*\x1B[39m\x1B[38;5;77m*\x1B[39m\x1B[38;5;77m*\x1B[39m\x1B[38;5;77m*\x1B[39m\x1B[38;5;77m*\x1B[39m\x1B[38;5;77m*\x1B[39m\x1B[38;5;77m*\x1B[39m\x1B[38;5;77m*\x1B[39m\x1B[38;5;77m*\x1B[39m\x1B[38;5;77m*\x1B[39m\x1B[38;5;77m*\x1B[39m\x1B[38;5;77m*\x1B[39m\x1B[38;5;77m*\x1B[39m\x1B[38;5;77m*\x1B[39m\x1B[38;5;77m*\x1B[39m\x1B[38;5;77m*\x1B[39m\x1B[38;5;77m*\x1B[39m\x1B[38;5;77m*\x1B[39m\x1B[38;5;77m*\x1B[39m\x1B[38;5;120m*\x1B[39m\x1B[38;5;120m*\x1B[39m\x1B[38;5;120m*\x1B[39m\x1B[38;5;120m*\x1B[39m\x1B[38;5;120m*\x1B[39m\x1B[38;5;120m*\x1B[39m\x1B[38;5;120m*\x1B[39m\x1B[38;5;120m*\x1B[39m\x1B[38;5;120m*\x1B[39m\x1B[38;5;120m*\x1B[39m",
                "loss": "\x1B[38;5;196mY\x1B[39m\x1B[38;5;196mo\x1B[39m\x1B[38;5;202mu\x1B[39m \x1B[38;5;202mL\x1B[39m\x1B[38;5;166mo\x1B[39m\x1B[38;5;131ms\x1B[39m\x1B[38;5;124me\x1B[39m\x1B[38;5;124m!\x1B[39m\n",
                "win": "\x1B[38;5;220mY\x1B[39m\x1B[38;5;220mo\x1B[39m\x1B[38;5;220mu\x1B[39m \x1B[38;5;178mW\x1B[39m\x1B[38;5;179mi\x1B[39m\x1B[38;5;179mn\x1B[39m \x1B[38;5;220mi\x1B[39m\x1B[38;5;220mn\x1B[39m \x1B[38;5;220m$\x1B[39m \x1B[38;5;220ms\x1B[39m\x1B[38;5;220mt\x1B[39m\x1B[38;5;220me\x1B[39m\x1B[38;5;220mp\x1B[39m\x1B[38;5;179ms\x1B[39m\x1B[38;5;179m!\x1B[39m\n",
                "round": "\x1B[38;5;209mR\x1B[39m\x1B[38;5;174mo\x1B[39m\x1B[38;5;174mu\x1B[39m\x1B[38;5;139mn\x1B[39m\x1B[38;5;103md\x1B[39m \x1B[38;5;68m{x}\x1B[39m \x1B[38;5;33mo\x1B[39m\x1B[38;5;33mu\x1B[39m\x1B[38;5;38mt\x1B[39m \x1B[38;5;38mo\x1B[39m\x1B[38;5;38mf\x1B[39m \x1B[38;5;38m{y}\x1B[39m\x1B[38;5;108m:\x1B[39m ",
                # "move_input": "Move from pile no.:"
                "move_input": "\x1B[38;5;150mM\x1B[39m\x1B[38;5;149mo\x1B[39m\x1B[38;5;185mv\x1B[39m\x1B[38;5;220me\x1B[39m \x1B[38;5;184mf\x1B[39m\x1B[38;5;149mr\x1B[39m\x1B[38;5;149mo\x1B[39m\x1B[38;5;113mm\x1B[39m \x1B[38;5;72mp\x1B[39m\x1B[38;5;36mi\x1B[39m\x1B[38;5;72ml\x1B[39m\x1B[38;5;66me\x1B[39m \x1B[38;5;101mn\x1B[39m\x1B[38;5;101mo\x1B[39m\x1B[38;5;131m.\x1B[39m\x1B[38;5;131m:\x1B[39m "
            },
            "default": {
                "main": """.▄▄ ·       ▄▄▌  ▪  ▄▄▄▄▄ ▄▄▄· ▪  ▄▄▄  ▄▄▄ .
            ▐█ ▀. ▪     ██•  ██ •██  ▐█ ▀█ ██ ▀▄ █·▀▄.▀·
            ▄▀▀▀█▄ ▄█▀▄ ██▪  ▐█· ▐█.▪▄█▀▀█ ▐█·▐▀▀▄ ▐▀▀▪▄
            ▐█▄▪▐█▐█▌.▐▌▐█▌▐▌▐█▌ ▐█▌·▐█ ▪▐▌▐█▌▐█•█▌▐█▄▄▌
             ▀▀▀▀  ▀█▄▀▪.▀▀▀ ▀▀▀ ▀▀▀  ▀  ▀ ▀▀▀.▀  ▀ ▀▀▀ """,
                "banner": "********************** NEW GAME *****************************",
                "loss": "You Lose!\n",
                "win": "You Win in $ steps!\n",
                "round": "Round {x} out of {y}: ",
                "move_input": "Move from pile no.: "
            }
        }
        if self.truecolor == True:
            return colors['true_color']
        elif self.twofivesix_color == True:
            return colors['256']
        else:
            return colors['default']
	
cards = [3, 2, 1]
game = Solitaire(cards)
game.play()
