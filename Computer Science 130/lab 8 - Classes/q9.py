# 1 line
TicTacToe = type('TicTacToe', (object,), {'__init__': lambda self, board="         ": setattr(self, 'board', [board[0:3], board[3:6], board[6:9]]) })