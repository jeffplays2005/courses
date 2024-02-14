def print_grid(grid):
    grid_list = list(grid)
    new_list_of_grids = []
    for i in range(0, len(grid_list), 3):
        new_list_of_grids.append(grid_list[i:i+3])
    
    formatted = []
    for i in new_list_of_grids:
        a = []
        for t in i:
            a.append(t)
        formatted.append("|".join(a))
    print("\n-----\n".join(formatted))
    
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

def main():
    grid = input("Please enter a string representing TicTacToe grid: ")
    print("TicTacToe Grid:")
    print()
    print_grid(grid)
    
    player1 = "X"
    player2 = "O"
    print()
    print(f"Player {player1} has won: {check_win(grid, player1)}")
    print(f"Player {player2} has won: {check_win(grid, player2)}")
    
main()