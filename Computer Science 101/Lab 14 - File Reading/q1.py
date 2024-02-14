def create_tuples_list(n):
    counter = 0;
    list_of_tuples = []
    for i in range(1, n+1):
        counter += i
        list_of_tuples.append((i, counter))
    return list_of_tuples

    
a_list = create_tuples_list(3)
print(a_list)
