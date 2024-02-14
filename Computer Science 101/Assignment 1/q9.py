def milestone_1(input_tiles):
    # use for sqrt
    import math
    # get n(e.g. 3x3, n = 3)
    n = int(math.sqrt(len(input_tiles.split(','))))
    #
    # create the top opening and bottom opening(dynamic changing according to n)
    # e.g. n = 3:
    # ┌────┬────┬────┬────┐
    opening = "┌" + ((n - 1) * "────┬") + "────┐"
    divider = "├" + ((n-1) * "────┼") + "────┤"
    # └────┴────┴────┴────┘
    closing = "└"+((n - 1) * "────┴") + "────┘"
    #
    # now create the middle sections
    individual_tiles = input_tiles.split(',')
    # create an empty list
    # we want something like this(list of lists):
    # [['1', '2', '3', '4'], ['5', '6', '7', '8'], ['9', '10', '', '12'], ['13', '14', '11', '15']]
    list_of_rows = []
    # iterate through each position
    # the start is set as 0 because of indexing, range ≠ i, when i = range, it stops. 
    # e.g. 
    # [ 1,2,3 ]
    # indexes: 0,1,2
    # index ≠ 3, so it ends on 2!
    for i in range(0, len(individual_tiles), n):
        # append a list of items between **i** and **whatever n is**
        list_of_rows.append(individual_tiles[i:i+n])
    # print top
    print(opening)
    # iterate through each list in the list of lists
    # [['1', '2', '3', '4'], ['5', '6', '7', '8'], ['9', '10', '', '12'], ['13', '14', '11', '15']]
    # -> ['1', '2', '3', '4'] and so on...
    for i, row in enumerate(list_of_rows):
        formatted_row = []
        for number in row:
            if len(str(number)) == 2:
                formatted_row.append(f" {number} ")
            elif len(str(number)) == 1:
                formatted_row.append(f"  {number} ")
            else:
                formatted_row.append("    ")
        if i != 0:
            print(divider)
        print("│" + "│".join(formatted_row) + "│")
    # print bottom
    print(closing)

milestone_1("1,2,3,4,5,6,7,8,9,10,,12,13,14,11,15")
