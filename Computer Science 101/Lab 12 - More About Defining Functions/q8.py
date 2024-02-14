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

def print_grid_b(grid):
    # a grid has 9 length so the indexes are 0-8
    # print the first 3 indexes(0,1,2)
    # e.g. X|O|X
    print(f"{grid[0]}|{grid[1]}|{grid[2]}")
    print("-----") # print divider
    # e.g. X|O|X
    #      -----
    print(f"{grid[3]}|{grid[4]}|{grid[5]}")
    # print the next 3 indexes(3,4,5)
    print("-----") # print divider
    # print the next 3 indexes(6,7,8)
    print(f"{grid[6]}|{grid[7]}|{grid[8]}")