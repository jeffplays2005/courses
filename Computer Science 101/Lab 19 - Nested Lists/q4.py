def replace_negatives(list_of_lists):
    for i in list_of_lists:
        for pos, number in enumerate(i):
            if number < 0:
                i[pos] = 0
                
the_list = [[2, 4, -16, 80, 27], [1, -4, 120, 18, -7], [-20, 14, 70, 8, 130]]
replace_negatives(the_list)
print(the_list)