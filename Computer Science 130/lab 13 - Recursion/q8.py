# def binary_search(numbers, item):
#     if (len(numbers) == 1 and numbers[0] != item) or len(numbers) == 0:
#         print(f"{numbers[:len(numbers) // 2]} {numbers[len(numbers) // 2]} {numbers[len(numbers) // 2+1:]}")
#         return False
#     else:
#         midpoint = len(numbers) // 2
#         print(f"{numbers[:midpoint]} {numbers[midpoint]} {numbers[midpoint+1:]}")
#         if item > numbers[midpoint]:
#             return binary_search(numbers[midpoint+1:], item)
#         else:
#             if item == numbers[midpoint]:
#                 return True
#             else: # item < mid
#                 if item < numbers[midpoint]:
#                     return binary_search(numbers[:midpoint], item)
#                 else:
#                     return False

# 1 line
def binary_search(numbers, item): return (False if (print(f"{numbers[:len(numbers) // 2]} {numbers[len(numbers) // 2]} {numbers[len(numbers) // 2+1:]}")) else False) if ((len(numbers) == 1 and numbers[0] != item) or len(numbers) == 0) else binary_search(numbers[len(numbers) // 2+1:], item) if (print(f"{numbers[:len(numbers) // 2]} {numbers[len(numbers) // 2]} {numbers[len(numbers) // 2+1:]}") or item > numbers[len(numbers) // 2]) else True if item == numbers[len(numbers) // 2] else binary_search(numbers[:len(numbers) // 2], item) if item < numbers[len(numbers) // 2] else False

test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binary_search(test_list, 3))
print(binary_search(test_list, 13))
# [0, 1, 2, 8] 13 [17, 19, 32, 42]
# [0, 1] 2 [8]
# [] 8 []
# False
# [0, 1, 2, 8] 13 [17, 19, 32, 42]
# True