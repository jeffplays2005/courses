def count_multiples_of_3(numbers):
    if len(numbers) == 0:
        return 0;
    if numbers[0] % 3 == 0:
        return 1+count_multiples_of_3(numbers[1:])
    else:
        return count_multiples_of_3(numbers[1:])
        
def count_multiples_of_3(numbers):
    return 0 if len(numbers) == 0 else 1+count_multiples_of_3(numbers[1:]) if numbers[0] % 3 == 0 else count_multiples_of_3(numbers[1:])
print('%s : %d' % ([2, 3, 5, 6], count_multiples_of_3([2, 3, 5, 6])))
# [2, 3, 5, 6] : 2
print('%s : %d' % ([2], count_multiples_of_3([2])))
# [2] : 0
