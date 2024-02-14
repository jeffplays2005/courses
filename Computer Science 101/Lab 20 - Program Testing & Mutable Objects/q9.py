def multiply_nested_list_by_factors(nested_list, factors):
    for pos, i in enumerate(nested_list): i[:] = [factors[pos] * num for num in i]
    for pos in range(len(nested_list)): nested_list[pos][:] = [factors[pos] * num for num in nested_list[pos]]

nested_list = [[-13, -10, 19], [-9, 1, -3, 14], [-3, 31, 34, 25, -19]]
factors = (3, 8, -1)
multiply_nested_list_by_factors(nested_list, factors)
print(nested_list)
