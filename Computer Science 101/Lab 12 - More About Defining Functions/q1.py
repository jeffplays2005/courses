def move_largest_to_end(number_list):
    largest = 0
    pos = 0
    for i in range(len(number_list)):
        if number_list[i] >= largest:
            largest = number_list[i]
            pos = i
    number_list[pos] = number_list[-1]
    number_list[-1] = largest
    
num_list = [11, 25, 64, 22, 9]
print(f"Before: {num_list}")
move_largest_to_end(num_list)
print(f"After: {num_list}")

num_list = [19, 17, -1, 4, 5, 0, 4, -4, 13, 5, -4, 19, 17, -5, 8]
print(f"Before: {num_list}")
move_largest_to_end(num_list)
print(f"After: {num_list}")
num_list = [24, 19, 23, 15, 27, -6, 26, 7, 19, 28, 6, 16, 8, -2, -8]
print(f"Before: {num_list}")
move_largest_to_end(num_list)
print(f"After: {num_list}")