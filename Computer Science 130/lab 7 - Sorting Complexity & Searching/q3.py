def bubble_sort(data):
    comparisons = []
    swaps = []
    for pass_num in range(len(data) - 1, 0, -1):
        comparisons.append(pass_num)
        swap_count = 0
        for i in range(0, pass_num):
            if data[i] > data[i+1]:
                swap_count += 1
                data[i], data[i+1] = data[i+1], data[i]
        swaps.append(swap_count)
    return (comparisons, swaps)

numbers = [12, 78, 81, 99, 91]
result = bubble_sort(numbers)
print(result)
# ([4, 3, 2, 1], [1, 0, 0, 0])
numbers = [92, 33, 63, 6, 66, 77, 74, 51, 30, 86]
result = bubble_sort(numbers)
print(result)
# ([9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 4, 3, 2, 2, 1, 1, 0, 0])