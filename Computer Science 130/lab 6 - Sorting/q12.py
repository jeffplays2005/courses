def shifting(data, index):
    value_to_insert = data[index]
    max = 0
    data.pop(index)
    for i in range(len(data)):
        if data[i] < value_to_insert and data[i] > data[0]:
            max = i
    if data[max] > value_to_insert:
        data.insert(max, data[max])
    else:
        data.insert(max + 1, data[max + 1])
    # print(data[max])
# better:
def shifting(data, index):
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
    # print(position_to_change)
            
# 1 line
def shifting(data, index, value_to_insert = 0, max = 0):
    (((value_to_insert := data[index]) and data.pop(index)) and ([ (max := i) for i in range(len(data)) if data[i] < value_to_insert and data[i] > data[0] ])) and (data.insert(max, data[max]) if data[max] > value_to_insert else data.insert(max + 1, data[max + 1]))
    
def shifting(data, index, value_to_insert = 0, position_to_change = 0):
    (((value_to_insert := data[index]) and (data.pop(index))) and [(position_to_change := i) for i in range(len(data)) if data[i] < value_to_insert and data[i] > data[position_to_change]])
    data.insert(position_to_change, data[position_to_change]) if max(data) == data[position_to_change] else (data.insert(position_to_change, data[position_to_change]) if data[position_to_change] > value_to_insert else (position_to_change := position_to_change + 1) and data.insert(position_to_change, data[position_to_change]))
        
"""
[20, 27, 27, 69, 15, 41]
[10, 15, 20, 27, 69, 69]
[54, 54, 78, 93, 61, 13]
[33, 33, 63, 66, 77, 74, 51, 30, 86]
"""

numbers = [20, 27, 69, 25, 15, 41]
shifting(numbers, 3)
print(numbers)
# [20, 27, 27, 69, 15, 41]
numbers = [10, 15, 20, 27, 69, 41]
shifting(numbers, 5)
print(numbers)
# [10, 15, 20, 27, 69, 69]
numbers = [54, 78, 93, 18, 61, 13]
shifting(numbers, 3)
print(numbers)
# [54, 54, 78, 93, 61, 13]
numbers = [33, 63, 6, 66, 77, 74, 51, 30, 86]
shifting(numbers, 2)
print(numbers)
# [33, 33, 63, 66, 77, 74, 51, 30, 86]
