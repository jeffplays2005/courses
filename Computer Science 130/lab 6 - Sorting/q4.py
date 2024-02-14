def selection_single_pass(data, index):
    largest_pos = data.index(max(data[:index+1]))
    largest = data[largest_pos]
    if largest > data[index]:
        data[largest_pos] = data[index]
        data[index] = largest
# 1 liner
def selection_single_pass(data, index): return ((data[index], data[data.index(max(data[0:index+1]))] = data[data.index(max(data[0:index+1]))], data[index]) or True)

numbers = [76, 53, 48, 24, 12]
selection_single_pass(numbers, 4)
print(numbers)
# [12, 53, 48, 24, 76]
numbers = [12, 24, 48, 53, 76]
selection_single_pass(numbers, 3)
print(numbers)
# [12, 24, 48, 53, 76]
