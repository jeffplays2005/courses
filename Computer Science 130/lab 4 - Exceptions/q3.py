def sum_of_odd_numbers(numbers, start_index, end_index):
    try:
        counter = 0
        for i in range(start_index, end_index+1):
            if numbers[i] % 2 != 0:
                counter += numbers[i]
        return counter
    except IndexError:
        print("ERROR: Out of range!")
        return 0
    except TypeError:
        print("ERROR: Invalid number!")
        return 0
        
list1 = [1, 5, 9, 2, 8, 3, 9, 6]
print(sum_of_odd_numbers(list1, 5, 6)) #3 + 9
# 12
list1 = [1, 2, 3]
print(sum_of_odd_numbers(list1, 2, 6))
# ERROR: Out of range!
# 0
list2 = [1, 'A', 2]
print(sum_of_odd_numbers(list2, 1, 2))

list1 = [1, 2, 3]
print(sum_of_odd_numbers(list1, 1, 2))