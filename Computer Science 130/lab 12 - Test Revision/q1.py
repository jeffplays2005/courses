def collapse(numbers):
    for i, item in enumerate(numbers):
        if isinstance(item, list):
            try:
                numbers[i] = sum(item)
            except:
                ""
    return

values = [1, 2, 3, 4, 5]
collapse(values)
print(values)
# [1, 2, 3, 4, 5]
values = [1, [2, 3], ['4', 'ten'], 5]
collapse(values)
print(values)
# [1, 5, ['4', 'ten'], 5]