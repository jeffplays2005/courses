def add_number_per_row(list_of_lists, number):
    for i in range(len(list_of_lists)):
        list_of_lists[i].append(number)
    
# 1 liner    
def add_number_per_row(list_of_lists, number): [list_of_lists[i].append(number) for i in range(len(list_of_lists))]

numbers = [[1, 2, 3], [4, 5], [6]]
add_number_per_row(numbers, 8)
print(numbers)
