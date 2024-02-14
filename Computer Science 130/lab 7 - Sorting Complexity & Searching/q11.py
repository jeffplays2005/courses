def linear_search_sorted(numbers, find):
    x = 0
    for n in numbers:
        x+=1
        if find == n:
            return (True, x)
        elif n > find:
            return (False, x)
    return (False, x)

result = linear_search_sorted([2, 3, 5, 6, 7, 8, 9], 4)
print(type(result))
print('Found: {} Equality Comparisons: {}'.format(result[0], result[1]))
# <class 'tuple'>
# Found: False Equality Comparisons: 3
result = linear_search_sorted([2, 3, 5, 6, 7, 8, 9], 6)
print('Found: {} Equality Comparisons: {}'.format(result[0], result[1]))
# Found: True Equality Comparisons: 4