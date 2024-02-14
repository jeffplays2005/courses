def draw_grid(n):
    rows = "│" + (n) * " x │"
    # print start
    print(("┌" + (n - 1) * "───┬") + "───┐")
    # create a counter
    counter = 1
    # while loop for each row number that is less than "n"
    while counter <= n:
        # if the counter is equal, finish the grid with an ending
        if counter == n:
            print(rows)
            # ending
            print("└" + (n - 1) * "───┴" + "───┘")
        else:
            # else continue printing rows and dividers
            print(rows)
            # dividers
            print(("├" + ((n-1) * "───┼") + "───┤"))
        counter += 1