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
    return (len(data), sum(comparisons), sum(swaps))
    
def bubble_sort_fast(data):
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
        if(swap_count == 0):
            return (len(data), sum(comparisons), sum(swaps))
    return (len(data), sum(comparisons), sum(swaps))
    
d1 = [12, 15, 19, 37, 39]
result1 = bubble_sort(d1)
print('Normal Bubble Sort: Length: {} Comparisons: {} Swaps: {}'.format(result1[0], result1[1], result1[2]))
d2 = [12, 15, 19, 37, 39]
result2 = bubble_sort_fast(d2)
print('Fast Bubble Sort: Length: {} Comparisons: {} Swaps: {}'.format(result2[0], result2[1], result2[2]))
# Normal Bubble Sort: Length: 5 Comparisons: 10 Swaps: 0
# Fast Bubble Sort: Length: 5 Comparisons: 4 Swaps: 0

d1 = [84, 62, 38, 36, 24]
result1 = bubble_sort(d1)
print('Normal Bubble Sort: Length: {} Comparisons: {} Swaps: {}'.format(result1[0], result1[1], result1[2]))
d2 = [84, 62, 38, 36, 24]
result2 = bubble_sort_fast(d2)
print('Fast Bubble Sort: Length: {} Comparisons: {} Swaps: {}'.format(result2[0], result2[1], result2[2]))
# Normal Bubble Sort: Length: 5 Comparisons: 10 Swaps: 10
# Fast Bubble Sort: Length: 5 Comparisons: 10 Swaps: 10