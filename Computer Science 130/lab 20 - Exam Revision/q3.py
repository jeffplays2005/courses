def evaluate_f(n):
    if n == 0:
        return (-1, 0)
    else:
        if n == 1:
            return (2, 0)
        else:
            f1, count1 = evaluate_f(n-1)
            f2, count2 = evaluate_f(n-2)
            total = f1 + 3 * f2
            
            result = (total, count1+count2+2)
            return result

print(evaluate_f(0))
print(evaluate_f(3))
print(evaluate_f(2))
print(evaluate_f(7))
# (-1, 0)
# (5, 4)
# (-1, 2)
# (74, 40)
