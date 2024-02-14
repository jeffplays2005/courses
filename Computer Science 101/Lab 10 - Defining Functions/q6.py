def filter_positive_list(raw_data):
    # create a new list
    for i in range(len(raw_data) -1, -1, -1):
        if raw_data[i] <= 0:
            raw_data.pop(i)
    
    return raw_data
