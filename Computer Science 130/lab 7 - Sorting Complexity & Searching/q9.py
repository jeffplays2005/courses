def selection_sort_descending(data):	
    for index in range(len(data) - 1, 0, -1):
        largest_pos = numbers.index(min(numbers[:index+1]))
        largest = data[largest_pos]
        if largest < data[index]:
            data[largest_pos], data[index] = data[index], largest

numbers = [2, 16, 7, 11, 1]
selection_sort_descending(numbers)
print(numbers)
# [16, 11, 7, 2, 1]

[16, 11, 7, 2, 1]