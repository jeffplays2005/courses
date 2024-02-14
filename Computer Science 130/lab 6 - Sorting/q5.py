def my_selection_sort(data):	
    for index in range(len(data) - 1, 0, -1):
        selection_single_pass(data, index)
        
def selection_single_pass(data, index):
    largest_pos = numbers.index(max(numbers[:index+1]))
    largest = data[largest_pos]
    if largest > data[index]:
        data[largest_pos] = data[index]
        data[index] = largest
        
numbers = [76, 53, 48, 24, 12]
my_selection_sort(numbers)
print(numbers)
# [12, 24, 48, 53, 76]
