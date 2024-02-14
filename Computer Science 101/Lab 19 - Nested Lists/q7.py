def check_win(board, player):
    grid = []
    for i in board:
        for n in i:
            grid.append(n)
    horizontal_row_1 = f"{grid[0]}{grid[1]}{grid[2]}"
    horizontal_row_2 = f"{grid[3]}{grid[4]}{grid[5]}"
    horizontal_row_3 = f"{grid[6]}{grid[7]}{grid[8]}"
    vertical_column_1 = f"{grid[0]}{grid[3]}{grid[6]}"
    vertical_column_2 = f"{grid[1]}{grid[4]}{grid[7]}"
    vertical_column_3 = f"{grid[2]}{grid[5]}{grid[8]}"
    diagonal_1 = f"{grid[0]}{grid[4]}{grid[8]}"
    diagonal_2 = f"{grid[2]}{grid[4]}{grid[6]}"
    all_combinations_of_methods_to_win = [ 
        horizontal_row_1, horizontal_row_2, horizontal_row_3,
        vertical_column_1, vertical_column_2, vertical_column_3,
        diagonal_1, diagonal_2
    ]
    if player * 3 in all_combinations_of_methods_to_win:
        return True
    else:
        return False
        
board = [["O", "X", " "],["O", "X", " "],["O", " ", " "]]
player1, player2 = "O", "X"
print(f"Player {player1} has won? {check_win(board, player1)}")
print(f"Player {player2} has won? {check_win(board, player2)}")