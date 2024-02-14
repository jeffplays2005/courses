def get_weighted_hash(key, table_size):
    total = 0
    for i, char in enumerate(key):
        total += ord(char) * (i+1)
    return total % table_size

# 1 liner
def get_weighted_hash(key, table_size, total = 0): return sum([ord(char) * (i+1) for i, char in enumerate(key)]) % table_size

print(get_weighted_hash('cat', 13))
print(get_weighted_hash('dog', 13))
# 4
# 7
print(get_weighted_hash('dog', 13))
print(get_weighted_hash('god', 13))
# 7
# 1
