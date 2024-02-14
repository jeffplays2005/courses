def compare(value, item_to_insert, counts_list):
    counts_list[0] += 1 #Add 1 to number of comparisons
    return value > item_to_insert

def insertion_sort(a_list):
    comparisons = []
    shifts = []
    for index in range(1, len(a_list)):
        item_to_insert = a_list[index]
        i = index - 1
        aaa = [0, 0]
        # compare(a_list[i], item_to_insert, comparisons)
        while i >= 0 and compare(a_list[i], item_to_insert, aaa):
            aaa[1] += 1
            a_list[i + 1] = a_list[i]
            i -= 1
        shifts.append(aaa[1])
        comparisons.append(aaa[0])
        aaa = [0,0]
        a_list[i + 1] = item_to_insert
    return(comparisons, shifts)

numbers = [50, 63, 11, 79, 22, 70, 65, 39, 97, 48]
result = insertion_sort(numbers)
print(result)
# ([1, 2, 1, 4, 2, 3, 6, 1, 7], [0, 2, 0, 3, 1, 2, 5, 0, 6])
numbers = [92, 86, 77, 66, 51, 42, 33, 23]
result = insertion_sort(numbers)
print(result)
# ([1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7])