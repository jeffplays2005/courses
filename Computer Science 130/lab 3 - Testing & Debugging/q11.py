def append_double_to(element, values=None):
    if values == None: values = []
    values.append(element*2)
    return values
# testing
my_list = append_double_to(12)
print(my_list)
my_list = append_double_to(12, my_list)
print(my_list)
my_list = append_double_to(24)
print(my_list)

a = 1
if(a == 1):
    print("a is 1")
elif(a == 2):
    print("a is 2")
else:
    print("a is not 1 or 2")
