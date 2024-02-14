def multiply_two_lists(list1, list2):
    multi_list = []
    for i in list2:
        for n in list1:
            multi_list.append(i * n)
    return multi_list

list1 = [6, -10, -2]
list2 = [-2, 19]
print("List product =", multiply_two_lists(list1, list2))

list1 = [16]
list2 = [-3, 9]
print("List product =", multiply_two_lists(list1, list2))
