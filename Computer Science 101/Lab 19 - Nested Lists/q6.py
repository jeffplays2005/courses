def print_board(board):
    for pos, row in enumerate(board):
        print("|".join(row))
        if pos != len(board) - 1: # rely on this for printing dividers
            print("-----")
# 1 liner
print_board = lambda board: [(print(f"{'|'.join(k)}\n{'-----'}") if (pos != len(board) - 1) else print(f"{'|'.join(k)}")) for pos, k in enumerate(board)]
    
board = [["O", "X", " "],["O", "X", " "],["O", " ", " "]]
print_board(board)
