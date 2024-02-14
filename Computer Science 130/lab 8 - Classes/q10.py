class TicTacToe:
    def __init__(self, board="         "):
        self.board = [ board[0:3], board[3:6], board[6:9] ]
    def __str__(self):
        collated = ["-------\n"]
        for i in self.board:
            collated.append(f"|{i[0]}|{i[1]}|{i[2]}|\n")
            collated.append("-------\n")
        return "".join(collated)

# 1 line
TicTacToe = type('TicTacToe', (object,), { '__init__': lambda self, board="         ": setattr(self, 'board', [board[0:3], board[3:6], board[6:9]]), '__str__': lambda self: ("-------\n" + "".join([ f"|{i[0]}|{i[1]}|{i[2]}|\n-------\n" for i in self.board])) })

game1 = TicTacToe()
print(game1)
game2 = TicTacToe("ox ox ox ")
print(game2)
print("DONE")
# -------
# | | | |
# -------
# | | | |
# -------
# | | | |
# -------
#
# -------
# |o|x| |
# -------
# |o|x| |
# -------
# |o|x| |
# -------
#
# DONE
