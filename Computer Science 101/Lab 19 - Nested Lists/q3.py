def get_one_d_unique_list(list_of_lists):
    unique_list = []
    for i in list_of_lists:
        for n in i:
            if n not in unique_list:
                unique_list.append(n)
    return sorted(unique_list)
# semi 1 liner
def get_one_d_unique_list(list_of_lists):
    return sorted(list(set([num for sublist in list_of_lists for num in sublist])))

    
numbers = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
print(get_one_d_unique_list(numbers))
