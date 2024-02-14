def rate(n, counter = 4):
    total = 0
    i = 1
    while i < n:
        j = n
        counter += 4
        while j > 0:
            counter += 3
            total += j 
            j -= 1
        i *= 2
    print(f"Number of operations: {counter}")
    return total

def rate(n, counter = 4, total = 0, i = 1): (([ ((counter := counter + 3) or (total := total + j)) for i in range(n) ]) and rate(n, counter+4, total, i *2)) if i < n else print(f"Number of operations: {counter}")

rate(2)
# Number of operations: 14
rate(4)
# Number of operations: 36
