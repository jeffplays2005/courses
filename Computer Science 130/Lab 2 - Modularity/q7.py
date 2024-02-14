def get_longest_string_length(dictionary): return max([ len(str(i)) for i in dictionary.keys() ])
    
data = {'apple':2, 'banana':6, 'strawberry':3, 'orange':4}
print(get_longest_string_length(data))
a_dict = {23: 'apple', 3456: 'banana', 1: 'strawberry', 56: 'orange'}
print(get_longest_string_length(a_dict))
print(get_longest_string_length({2345678: 'apple', 3456: 'banana', 1:'cat'}))
data = {'standard':21, 'extra':34, 'test':84, 'property':20, 'case':3, 'output':62, 'expected':99, 'information':87}
print(get_longest_string_length(data))