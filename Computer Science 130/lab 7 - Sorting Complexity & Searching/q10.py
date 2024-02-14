def linear_search(numbers, find):
    x = 0
    for n in range(len(numbers)):
        x+=1
        if find == numbers[n]:
            return (True, x)
    return (False, x)

result = linear_search([54, 26, 93, 17, 77, 20], 32)
print('Found: {} Comparisons: {}'.format(result[0], result[1]))
print(type(result))
# Found: False Comparisons: 6
# <class 'tuple'>

result = linear_search([93, 54, 78, 18, 61, 13, 36, 42, 16, 60, 58, 92], 61)
print('Found: {} Comparisons: {}'.format(result[0], result[1]))
# Found: True Comparisons: 5