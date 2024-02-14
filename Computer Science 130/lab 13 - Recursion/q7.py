def get_sum(n):
    if isinstance(n, tuple) and n[0] == 0:
        return (0, 0)
    else:
        return (n[0] + get_sum((n[0]-1, n[1]))[0], n[1])
# 1 line
def get_sum(n): return (0, 0) if isinstance(n, tuple) and n[0] == 0 else get_sum((n, n)) if not isinstance(n, tuple) else (n[0] + get_sum((n[0]-1, n[1]))[0], n[1])
# print(get_sum(3))
# (6, 3)
# print(get_sum(5))
# (15, 5)
# print(get_sum(8))
# (36, 8)
