def rate(n, counter = 4):
    total = 0
    i = 1
    while i < n:
        counter += 3
        total += i
        i *= 2
    print(f"Number of operations: {counter}")
    return total
    
# 1 line
def rate(n, counter = 4, total = 0, i = 1): (((counter := counter + 3) or (total := total + i)) and rate(n, counter, total, i * 2)) if i < n else print(f"Number of operations: {counter}")
rate(2)
# Number of operations: 7
rate(8)
# Number of operations: 13
