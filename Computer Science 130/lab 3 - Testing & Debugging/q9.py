def get_tuple_at(names, index): return (names[index],)
    
my_tuple = get_tuple_at(['May', 'Amy', 'Alan'], 1)
print(my_tuple)
print(type(my_tuple))
print(get_tuple_at(['May', 'Amy', 'Alan'], 0))

my_tuple = get_tuple_at(['Caleb', 'Bastian', 'John', 'David', 'Alan'], 0)
print(my_tuple)