def get_sum_over(list1, list2, target):
    return [ n for n in  [n + i for n in list1 for i in list2] if n > target ]
# testing
print(get_sum_over([1, 2, 3], [2, 4], 10))
# []
print(get_sum_over([1, 2, 3], [2, 4, 6], 2))
# [3, 5, 7, 4, 6, 8, 5, 7, 9]
print(get_sum_over([11, 12], [2, 4, 6, 9], 7))
# [13, 15, 17, 20, 14, 16, 18, 21]
