def bubble_single_pass(data, index):
    for i in range(len(data[:index])):
        if data[i] != data[-1] and data[i] > data[i + 1]:
            data[i + 1], data[i] = data[i], data[i + 1]
        
numbers = [76, 53, 48, 24, 12]
bubble_single_pass(numbers, 4)
print(numbers)
# [53, 48, 24, 12, 76]
numbers = [76, 53, 48, 24, 12]
bubble_single_pass(numbers, 1)
print(numbers)
# [53, 76, 48, 24, 12]
