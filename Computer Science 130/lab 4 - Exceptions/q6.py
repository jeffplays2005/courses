def sum_of_multiples_of_3_continue(numbers):
    total = 0
    for i in numbers:
        try:
            if i % 3 == 0:
                total += i
        except:
            ""
    return total

# 1 line
def sum_of_multiples_of_3_continue(numbers): return sum([ i if i % 3 == 0 else 0 for i in numbers if type(i) == int ]) # try: except:

my_list = [-1, 0, 15, 20, 'ten', 35, 45, 105, 20]
print(sum_of_multiples_of_3_continue(my_list))
print(sum_of_multiples_of_3_continue([-1, 0, 10, 20, 'ten', 35, 45, 105, 20]))
# 165
# 150
my_list = [1, 2, 3, 4, "two", 2]
print(sum_of_multiples_of_3_continue(my_list))
# 3
print(sum_of_multiples_of_3_continue([]))
# 0
print(sum_of_multiples_of_3_continue(['NA']))