def check_win(grid, player):
    tiles = []
    # horizontal tiles
    for i in range(0, len(grid), 3):
        tiles.append(grid[i:i+3])

    column1 = ""
    column2 = ""
    column3 = ""
    # vertical tiles
    for i in range(0, len(grid)):
        if i % 3 == 1:
            column1 += grid[i]
        elif i % 3 == 2:
            column2 += grid[i]
        else:
            column3 += grid[i]
    # add to list
    tiles += [ column1, column2, column3 ]
    # diagonal tiles
    tiles += [ grid[0] + grid[4] + grid[8] ]
    tiles += [ grid[2] + grid[4] + grid[6] ]
    if player * 3 in tiles:
        return True
    else:
        return False
        
def check_win(grid, player):
    # positions diagram
    # +---+---+---+
    # | 0 | 1 | 2 |
    # +---+---+---+
    # | 3 | 4 | 5 |
    # +---+---+---+
    # | 6 | 7 | 8 |
    # +---+---+---+
    # horizontal rows
    horizontal_row_1 = f"{grid[0]}{grid[1]}{grid[2]}"
    horizontal_row_2 = f"{grid[3]}{grid[4]}{grid[5]}"
    horizontal_row_3 = f"{grid[6]}{grid[7]}{grid[8]}"
    # vertical columns
    vertical_column_1 = f"{grid[0]}{grid[3]}{grid[6]}"
    vertical_column_2 = f"{grid[1]}{grid[4]}{grid[7]}"
    vertical_column_3 = f"{grid[2]}{grid[5]}{grid[8]}"
    # diagonal
    diagonal_1 = f"{grid[0]}{grid[4]}{grid[8]}"
    diagonal_2 = f"{grid[2]}{grid[4]}{grid[6]}"
    # create a new list of grids to check, basically just concats all of the 
    # horizontal, vertical and diagonal squares
    all_combinations_of_methods_to_win = [ 
        horizontal_row_1, horizontal_row_2, horizontal_row_3,
        vertical_column_1, vertical_column_2, vertical_column_3,
        diagonal_1, diagonal_2
    ]
    # player could be X or O
    # so the winning tile would be player * 3
    # e.g. XXX or OOO
    # check if it is XXX or OOO
    if player * 3 in all_combinations_of_methods_to_win:
        return True
    else:
        return False

grid = "XO XOX OO"
player1 = "X"
player2 = "O"
print(f"Player {player1} has won: {check_win(grid, player1)}")
print(f"Player {player2} has won: {check_win(grid, player2)}")