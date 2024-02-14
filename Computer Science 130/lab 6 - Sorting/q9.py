def my_bubble_sort(data): 
    for index in range(len(data) - 1, 0, -1):
        bubble_single_pass(data, index)
def bubble_single_pass(data, index):
    for i in range(len(data[:index])):
        if data[i] != data[-1] and data[i] > data[i + 1]:
            cache = data[i + 1]
            data[i + 1] = data[i]
            data[i] = cache

numbers = [76, 53, 48, 24, 12]
my_bubble_sort(numbers)
print(numbers)
# [12, 24, 48, 53, 76]