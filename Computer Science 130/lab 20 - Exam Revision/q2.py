def get_products_sum(list1, list2, k):
    corresponding1 = list1[k]
    corresponding2 = list2[k]
    total = 0
    for pos, i in enumerate(corresponding1):
        corresponding = corresponding2[pos]
        try:
            total += corresponding * i
        except:
            continue
    return total

list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list2 = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
print(get_products_sum(list1, list2, 0))
print(get_products_sum(list1, list2, 1))
print(get_products_sum(list1, list2, 2))
# 50
# 77
# 50
list1 = [['a', 2, 3], [1, 'a', 2], [1, 2, 'a']]
list2 = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
print("============================")
print(get_products_sum(list1, list2, 0))
print(get_products_sum(list1, list2, 1))
print(get_products_sum(list1, list2, 2))
# 43
# 16
# 5
list1 = [['a', 2, 3], [1, 'a', 2], [1, 'a', 'a']]
list2 = [[7, 'b', 'c'], [4, 5, 'c'], ['b', 2, 3]]
print("============================")
print(get_products_sum(list1, list2, 0))
print(get_products_sum(list1, list2, 1))
print(get_products_sum(list1, list2, 2))
# 0
# 4
# 0
