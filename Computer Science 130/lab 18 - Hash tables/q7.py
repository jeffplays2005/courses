def get_simple_numeric_hash(key, table_size):
    return int(str(key ** 2)[1:-1]) % table_size

print(get_simple_numeric_hash(655, 13))
print(get_simple_numeric_hash(654, 13))
print(get_simple_numeric_hash(653, 13))
# 3
# 2
# 1
print(get_simple_numeric_hash(1000, 19))
print(get_simple_numeric_hash(1001, 19))
print(get_simple_numeric_hash(1002, 19))
# 0
# 10
# 1
