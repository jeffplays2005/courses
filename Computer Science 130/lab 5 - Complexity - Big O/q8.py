def rate(n, counter = 4):
    total = 0
    i = n
    while i > 0:
        counter += 4
        j = 0
        while j < n:
            counter += 3
            total += j 
            j += 2
        i -= 1
    print(f"Number of operations: {counter}")
    return total

def rate(n, counter = 4):
    total = 0
    i = n
    while i > 0:
        counter += 4
        j = 0
        while j < n:
            (((counter := counter + 3) or (total := total + j)) and (j := j + 2))
        i -= 1
    print(f"Number of operations: {counter}")
    return total
# big brain
def rate(n): print(f"Number of operations: {n*((((n//2) + (1 if n % 2 == 1 else 0)) * 3) + 4) + 4}")
    
rate(2)
# Number of operations: 18
rate(5)
# Number of operations: 69
