def draw_row(data_list):
    # create a string template as the string always starts with │
    string_template = "│"
    # scan through the list
    for item in data_list:
        # if the item's length is 0, meaning there was no number
        if len(item) == 0:
            # add blank 4 dashes to indicate
            string_template += "----│"
        # if the item's length is 1, meaning there was a single digit
        elif len(item) == 1:
            # add --x-│ to string template
            string_template += f"--{item}-│"
        # if the item's length is 2, meaning there was a double digit
        elif len(item) == 2:
            # add -xx-│ to string template
            string_template += f"-{item}-│"
    # end the function by returning string_template
    return string_template
