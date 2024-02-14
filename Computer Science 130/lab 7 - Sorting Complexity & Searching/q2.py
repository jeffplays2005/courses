def selection_sort(data):
    return ([ i for i in range(1, len(data)) ][::-1], [ 1 for i in range(1,len(data)) ])
        
numbers = [6, 4]
result = selection_sort(numbers)
print(result)
print(numbers)