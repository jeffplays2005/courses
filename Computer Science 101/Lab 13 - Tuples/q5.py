def get_sum_evens_odds(numbers_list):
    even_sum = 0
    odd_sum = 0
    for i in numbers_list:
        if (i % 2) == 0: #even case
            even_sum += i
        else:
            odd_sum += i
    return (even_sum, odd_sum)
    
    
numbers = [4, -5, 2, 8, 0, -4, ]
data = get_sum_evens_odds(numbers)
print(data)
print(type(data))