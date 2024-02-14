def count_up(n):
    if n == 0:
        print("Go!")
    else:
        count_up(n - 1)
        print(n)

def count_up(n): print("Go!") if n == 0 else (count_up(n - 1) or print(n))

# def get_all_vowels(words):
#     if not words:
#         return []
#     else:
#         new_list = words[0]
#         return [get_vowels(new_list)] + get_all_vowels(words[1:])

count_up(3)
# Go!
# 1
# 2
# 3
count_up(0)
# Go!