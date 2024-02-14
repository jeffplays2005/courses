def rate(n, counter = 4):
    total = 0
    i = n
    while i > 1:
        j = 1
        counter += 4
        while j < n:
            counter += 3
            total += j
            j *= 2
        i //= 2
    print(f"Number of operations: {counter}")
    return total
# 1 line
def rate(n, counter = 4, total = 0): ([((counter := counter + 3) or (total := total + j)) for i in range(n // 2 + (1 if n % 2 == 1 else 0))]) and rate(n//2, counter + 4, total) if n > 1 else print(f"Number of operations: {counter}")
# testing cases
rate(2)
# Number of operations: 11
rate(8)
# Number of operations: 43
rate(64)
# Number of operations: 136
rate(128)
# Number of operations: 179
