class TicTacToe:
    def __init__(self, board="         "):
        self.board = [ board[0:3], board[3:6], board[6:9] ]
    def check_row_win(self, player):
        if player * 3 in self.board:
            return True
        else:
            return False
    def check_column_win(self, player):
        grid = "".join(self.board)
        all_combinations_of_methods_to_win = [ 
            f"{grid[0]}{grid[3]}{grid[6]}", f"{grid[1]}{grid[4]}{grid[7]}", f"{grid[2]}{grid[5]}{grid[8]}",
        ]
        if player * 3 in all_combinations_of_methods_to_win:
            return True
        else:
            return False

# 1 line
def check_row_win(self, player):
    if player * 3 in self.board:
        return True
    else:
        return False

TicTacToe = type('TicTacToe', (object,), { '__init__': lambda self, board="         ": (setattr(self, 'board', [board[0:3], board[3:6], board[6:9]])), 'check_column_win': lambda self, player: True if player * 3 in [ f"{''.join(self.board)[0]}{''.join(self.board)[3]}{''.join(self.board)[6]}", f"{''.join(self.board)[1]}{''.join(self.board)[4]}{''.join(self.board)[7]}", f"{''.join(self.board)[2]}{''.join(self.board)[5]}{''.join(self.board)[8]}", ] else False, 'check_row_win':lambda self, player : True if player * 3 in self.board else False })
game1 = TicTacToe("o  xxx oo")
print(game1.check_row_win('x'))
print(game1.check_row_win('o'))
# True
# False

game2 = TicTacToe("ox ox oox")
print(game2.check_column_win('x'))
print(game2.check_column_win('o'))
# False
# True