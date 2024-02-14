import math

def get_min_median_max(numbers):
    minimum = min(numbers)
    median = 0
    maximum = max(numbers)
    numbers = sorted(numbers)
    
    if len(numbers) % 2 == 0:
        middle_lower = numbers[int(len(numbers) / 2) - 1]
        middle_upper = numbers[int((len(numbers) / 2))]
        median = (middle_lower + middle_upper) / 2
    else:
        median = numbers[math.ceil(len(numbers) / 2) - 1]
    
    return minimum, median, maximum
    
print(get_min_median_max([-3, 6, 9, 4, 5]))
print(get_min_median_max([2, -4, 99, 12, 56, 25]))