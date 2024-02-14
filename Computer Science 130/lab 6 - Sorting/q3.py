def get_position_of_largest(data, index): return numbers.index(max(numbers[:index+1]))

numbers = [76, 53, 48, 24, 12]
print(get_position_of_largest(numbers, 4))
# 0
numbers = [53, 48, 24, 76, 28]
print(get_position_of_largest(numbers, 3))
# 3
numbers = [20, 27, 69, 10, 76, 41]
print(get_position_of_largest(numbers, 2))
# 2