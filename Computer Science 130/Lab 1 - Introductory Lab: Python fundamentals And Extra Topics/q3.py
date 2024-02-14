def running_sum(numbers):
    for numbers_index in range(1, len(numbers)):
        numbers[numbers_index] += numbers[numbers_index - 1]

# 1 line
def running_sum(numbers): for index in range(1, len(numbers)): numbers[index] += numbers[index - 1]

# testing cases
numbers = [3, 2, 4, 7]
running_sum(numbers)
print(numbers)
