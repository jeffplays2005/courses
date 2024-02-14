def sum_of_multiples_of_3(list):
    counter = 0
    for i in range(len(list)):
        try:
            if list[i] % 3 == 0:
                counter += list[i]
        except:
            return counter
    return counter

my_list = [1, 2, 3, 4, -1, 9]
print(sum_of_multiples_of_3(my_list))
# 12
my_list = [1, 2, 3, 4, "two", 2, 9]
print(sum_of_multiples_of_3(my_list))
# 3
print(sum_of_multiples_of_3([]))
# 0
print(sum_of_multiples_of_3(['NA']))
# 0