def insertion_single_pass(data, index):
    value_to_insert = data[index]
    position_to_change = 0
    data.pop(index)
    for i in range(len(data)):
        if data[i] < value_to_insert and data[i] > data[position_to_change]:
            position_to_change = i
    if max(data) == data[position_to_change]:
        # clone position_to_change
        data.insert(position_to_change, data[position_to_change])
    elif data[position_to_change] > value_to_insert:
        data.insert(position_to_change, data[position_to_change])
    else:
        # clone + 1
        position_to_change += 1
        data.insert(position_to_change, data[position_to_change])
    data[position_to_change] = value_to_insert

def insertion_single_pass(data, index):
    value_to_insert = data[index]
    position_to_change = 0
    data.pop(index)
    for i in range(len(data)):
        if data[i] < value_to_insert and data[i] > data[position_to_change]:
            position_to_change = i
    if max(data) == data[position_to_change]:
        # clone position_to_change
        data.insert(position_to_change, data[position_to_change])
    elif data[position_to_change] > value_to_insert:
        data.insert(position_to_change, data[position_to_change])
    else:
        # clone + 1
        position_to_change += 1
        data.insert(position_to_change, data[position_to_change])
    data[position_to_change] = value_to_insert

numbers = [20, 27, 69, 10, 15, 41]
insertion_single_pass(numbers, 3)
print(numbers)
# [10, 20, 27, 69, 15, 41]
numbers = [10, 15, 20, 27, 69, 41]
insertion_single_pass(numbers, 5)
print(numbers)
# [10, 15, 20, 27, 41, 69]