def get_positive_list(raw_data):
    # create a new list
    cleaned = []
    
    for item in raw_data:
        if item > 0:
            cleaned.append(item)
    
    return cleaned
