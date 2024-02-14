def rate(n):
    total = 0
    i = n
    runs = 4
    while i > 0:
        runs += 3
        total += i
        i -= 2
    print(f"Number of operations: {runs}")
    return total
# 1 line
def rate(n, total = 0, runs = 4): (((runs := runs + 3) or (total := total + n)) and rate(n -2, total, runs)) if(n > 0) else print(f"Number of operations: {runs}")
    
# testing
rate(2)
# Number of operations: 7
rate(4)
# Number of operations: 10