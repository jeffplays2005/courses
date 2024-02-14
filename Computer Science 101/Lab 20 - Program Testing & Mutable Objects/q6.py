def remove_multiples(numbers, target):
    counter = len(numbers) - 1
    while counter >= 0:
        if numbers[counter] % target == 0:
            numbers.pop(counter)
        counter -= 1
# 1 liner
def remove_multiples(numbers, target): numbers[:] = [num for num in numbers if num % target != 0]
        
numbers = [8, 36, 1, 37, 25]
remove_multiples(numbers, 2)
print(numbers)
