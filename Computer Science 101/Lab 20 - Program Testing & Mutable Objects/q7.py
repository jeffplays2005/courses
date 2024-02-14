def reduce_tuple_items(number_tuple, difference): return tuple([ i - difference for i in number_tuple ])
    
number_tuple = (42, 49, 0, 11, 21, -17)
number_tuple = reduce_tuple_items(number_tuple, 5)
print(number_tuple)