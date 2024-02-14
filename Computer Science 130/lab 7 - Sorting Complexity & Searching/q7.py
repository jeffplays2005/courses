def bubble_sort_descending(data): 
    for index in range(len(data) - 1, 0, -1):
        for i in range(len(data[:index])):
            if data[i] != data[-1] and data[i] < data[i + 1]:
                cache = data[i + 1]
                data[i + 1] = data[i]
                data[i] = cache

d = [89]
bubble_sort_descending(d)
print(d)
# [89]
d = [2, 16, 7, 11, 1]
bubble_sort_descending(d)
print(d)
# [16, 11, 7, 2, 1]