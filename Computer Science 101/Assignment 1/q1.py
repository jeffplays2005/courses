def get_size(list_of_values):
    # import the math module
    import math
    # we need an integer(non-decimal) and square root the number of values
    return int(math.sqrt(len(list_of_values)))
    
# 1 line
def get_size(list_of_values): return int((len(list_of_values)) ** 0.5)