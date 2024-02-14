def triangular_number(n):
    if n == 0:
        return 0
    else:
        if n == 1:
            return 1
        else:
            if n == 2:
                return 3
            else:
                return 3*(triangular_number(n-1)) - 3*(triangular_number(n-2))+triangular_number(n-3)

print(triangular_number(0))
# 0
print(triangular_number(3))
# 6