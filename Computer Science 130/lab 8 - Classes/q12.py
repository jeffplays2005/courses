class TicTacToe:
    def __init__(self, board="         "):
        self.board = [ board[0:3], board[3:6], board[6:9] ]
    def check_win(self, player):
        grid = "".join(self.board)
        all_combinations_of_methods_to_win = [
            # horizontal
            f"{grid[0:3]}", f"{grid[3:6]}", f"{grid[6:9]}",
            # vertical
            f"{grid[0]}{grid[3]}{grid[6]}", f"{grid[1]}{grid[4]}{grid[7]}", f"{grid[2]}{grid[5]}{grid[8]}",
            # diagonal
            f"{grid[0]}{grid[4]}{grid[8]}", f"{grid[2]}{grid[4]}{grid[6]}"
        ]
        if player * 3 in all_combinations_of_methods_to_win:
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
# 1 liners
TicTacToe = type('TicTacToe', (object,), { '__init__': lambda self, board="         ": (setattr(self, 'origin', board) and setattr(self, 'board', [board[0:3], board[3:6], board[6:9]])), 'check_win': lambda self, player : True if player * 3 in [ f"{self.origin[0:3]}", f"{self.origin[3:6]}", f"{self.origin[6:9]}", f"{self.origin[0]}{self.origin[3]}{self.origin[6]}", f"{self.origin[1]}{self.origin[4]}{self.origin[7]}", f"{self.origin[2]}{self.origin[5]}{self.origin[8]}", f"{self.origin[0]}{self.origin[4]}{self.origin[8]}", f"{self.origin[2]}{self.origin[4]}{self.origin[6]}" ] else False, 'check_column_win': lambda self, player: True if player * 3 in [ f"{self.origin[0]}{self.origin[3]}{self.origin[6]}", f"{self.origin[1]}{self.origin[4]}{self.origin[7]}", f"{self.origin[2]}{self.origin[5]}{self.origin[8]}", ] else False })
class TicTacToe:
    def __init__(self, board="         "): self.origin, self.board = board, [ board[0:3], board[3:6], board[6:9] ]
    def check_win(self, player): return True if player * 3 in [ f"{self.origin[0:3]}", f"{self.origin[3:6]}", f"{self.origin[6:9]}", f"{self.origin[0]}{self.origin[3]}{self.origin[6]}", f"{self.origin[1]}{self.origin[4]}{self.origin[7]}", f"{self.origin[2]}{self.origin[5]}{self.origin[8]}", f"{self.origin[0]}{self.origin[4]}{self.origin[8]}", f"{self.origin[2]}{self.origin[4]}{self.origin[6]}" ] else False
    def check_column_win(self, player): return True if player * 3 in [ f"{self.origin[0]}{self.origin[3]}{self.origin[6]}", f"{self.origin[1]}{self.origin[4]}{self.origin[7]}", f"{self.origin[2]}{self.origin[5]}{self.origin[8]}", ] else False
# test
game1 = TicTacToe("o  xxx oo")
print(game1.check_win('x'))
print(game1.check_win('o'))
# True
# False
