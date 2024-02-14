import math
def get_size(list_of_values):
    return int(math.sqrt(len(list_of_values)))

def divide_list(tile_list, n):
    list_of_rows = []
    for i in range(0, len(tile_list), n): # for each item in between the range of 0 and length and incrementing by n each time
        list_of_rows.append(tile_list[i:i+n]) # adding the row to the list_of_rows list
    return list_of_rows # return the data
    
def create_formatted_row_list(row):
    formatted_row = [] # create a blank list
    for number in row: # for each number in the row
        if len(str(number)) == 2: # if the length is 2
            formatted_row.append(f" {number} ") # add in between 1 space
        elif len(str(number)) == 1: # if length is 1
            formatted_row.append(f"  {number} ") # add between 2 spaces and 1 space at the end
        else: # no length, no number
            formatted_row.append("    ") # blank space
    return formatted_row
    
def draw_grid(input_tiles):
    individual_tiles = input_tiles.split(',') # create a list of individual tiles
    n = get_size(individual_tiles) # get n
    individual_list_of_rows = divide_list(individual_tiles, n) # divide the list into lists of tile rows
    print("┌" + ((n - 1) * "────┬") + "────┐") # print the top of the tiles
    for i, row in enumerate(individual_list_of_rows): # for each row...
        formatted_row = create_formatted_row_list(row) # create a list of formatted rows
        if i != 0: # avoids printing an extra divider
            print("├" + ((n-1) * "────┼") + "────┤") # the dividers
        print("│" + "│".join(formatted_row) + "│") # print the formatted list of rows
    print("└"+((n - 1) * "────┴") + "────┘") # print the closing tile design

def prompt_with_checks(question, list_of_valid_moves):
    user_move = input("Your move: ")
    
    if user_move not in list_of_valid_moves:
        print(f"{user_move} is not valid. Try again.")
        return prompt_with_checks(question, list_of_valid_moves)
    return user_move

def positions_to_check(user_move, tile_index, divisor, individual_tiles):
    list_of_positions_to_check = []
    # add top and bottom rows
    add_vertically_adjacent_tiles(list_of_positions_to_check, tile_index, individual_tiles)
    add_horizontally_adjacent_tiles(list_of_positions_to_check, divisor, tile_index, individual_tiles)

    return list_of_positions_to_check

def add_vertically_adjacent_tiles(list, tile_index, individual_tiles):
    # add top and bottom row
    if tile_index - int(math.sqrt(len(individual_tiles))) > 0:
        list.append(tile_index - int(math.sqrt(len(individual_tiles))))
    if tile_index + int(math.sqrt(len(individual_tiles))) <= len(individual_tiles) - 1:
        list.append(tile_index + int(math.sqrt(len(individual_tiles))))
    return
    
def add_horizontally_adjacent_tiles(list, divisor, tile_index, individual_tiles):
    if divisor == 0: # only check the item on the left as this is the most right tile
        list.append(tile_index - 1)
    elif divisor == 1: # only check the item on the right as this is the most left tile
        list.append(tile_index + 1)
    else: # the item is somewhere in the middle, check both left and right tiles
        list.append(tile_index + 1)
        list.append(tile_index - 1)
    return

def check_if_valid_adjacent(list_to_check, tiles, user_move):
    valid = False # set valid to true first
    for position_to_check in list_to_check:
        if tiles[position_to_check] == "":
            valid = True
    if valid == True:
        return True
    else:
        print(f"{user_move} is not valid. Try again.")
        return False
    
def get_valid_move(input_tiles):
    individual_tiles = input_tiles.split(',') # split the tiles into individual tiles
    while True: # while loop prompt
        user_move = prompt_with_checks("Your move: ", individual_tiles)
        tile_index = individual_tiles.index(user_move)
        divisor = (int(tile_index) + 1) % int(math.sqrt(len(individual_tiles)))
        list_of_positions_to_check = positions_to_check(user_move, tile_index, divisor, individual_tiles)
        adjacent_check = check_if_valid_adjacent(list_of_positions_to_check, individual_tiles, user_move)
        if adjacent_check == True:
            return user_move

def generate_correct_tiles(input_tiles):
    individual_tiles = input_tiles.split(',')
    ordered_tiles = "1"
    for number in range(2,len(individual_tiles)):
        ordered_tiles = f"{ordered_tiles},{number}"
    ordered_tiles+=","
    return ordered_tiles
    
def swap_tile(input_tiles, tile_to_swap):
    individual_tiles = input_tiles.split(',')
    free_space_index = individual_tiles.index('')
    tile_to_swap_index = individual_tiles.index(tile_to_swap)
    
    individual_tiles[free_space_index] = tile_to_swap
    individual_tiles[tile_to_swap_index] = ""

    return ','.join(individual_tiles)

def main(input_tiles):
    moves = 0
    while True:
        draw_grid(input_tiles)
        if generate_correct_tiles(input_tiles) == input_tiles:
            break
        player_move = get_valid_move(input_tiles)
        moves += 1
        input_tiles = swap_tile(input_tiles, player_move)
    return print(f"You won in {moves} moves. Congratulations!")

main("1,2,3,4,5,6,7,8,9,10,12,,13,14,11,15")
# main("1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,")
# main("1,3,,5,2,6,4,7,8")
# main(",1,3,4,5,7,2,8,9,10,6,11,13,14,15,16,12,17,19,20,21,22,18,23,24")
