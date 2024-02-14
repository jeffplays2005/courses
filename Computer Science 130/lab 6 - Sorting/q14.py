def insertion_single_pass(data, index):
    value_to_insert = data[index]
    length = len(data)
    data.pop(index)
    for i in range(len(data[:index])):
    # for i in range(len(data) - 1, 0, -1):
        if value_to_insert < data[i]:
            data.insert(i, value_to_insert)
            break
        # if value_to_insert > max(data):
        #     data.insert(len(data), value_to_insert)
        #     break
        # elif value_to_insert < min(data):
        #     data.insert(0, value_to_insert)
        #     break
    if(len(data) != length):
        data.insert(index, value_to_insert)
# def my_insertion_sort(a_list):
#     for index in range(1, len(a_list)):
#         insertion_single_pass(a_list, index)
# def my_insertion_sort(a_list):
#     print("#1")
#     # [20, 27, 69, 10, 15, 41]
#     insertion_single_pass(a_list, 1)
#     print(a_list)
#     print("#2")
#     # 27
#     # doubled: 69
#     # [20, 27, 69, 10, 15, 41]
#     insertion_single_pass(a_list, 2)
#     print(a_list)
#     # [10, 20, 27, 15, 41, 69]
#     print("#3")
#     insertion_single_pass(a_list, 3)
#     print(a_list)
#     # [10, 15, 20, 27, 41, 69]
#     print("#4")
#     insertion_single_pass(a_list, 4)
#     print(a_list)
#     # [10, 15, 20, 27, 41, 69]
#     print("#5")
#     insertion_single_pass(a_list, 5)
#     print(a_list)
#     # [10, 15, 20, 27, 41, 69]
# numbers = [20, 27, 69, 10, 15, 41]
# my_insertion_sort(numbers)
# print(numbers)
# [10, 15, 20, 27, 41, 69]
def my_insertion_sort(a_list):
    for index in range(0, len(a_list)):
        insertion_single_pass(a_list, index)
        
# neater
def insertion_single_pass(data, index):
    value_to_insert = data[index]
    length = len(data)
    data.pop(index)
    for i in range(len(data[:index])):
        if value_to_insert < data[i]:
            data.insert(i, value_to_insert)
            break
    if(len(data) != length):
        data.insert(index, value_to_insert)

def my_insertion_sort(a_list):
    for index in range(0, len(a_list)):
        insertion_single_pass(a_list, index)
        
# 1 liner
# def insertion_single_pass(data, index, value_to_insert = 0, length = 0, stop = False):
#     ((value_to_insert := data[index]) and (length := len(data)) and data.pop(index)) and ([((stop := True) and data.insert(i, value_to_insert)) for i in range(len(data[:index])) if (value_to_insert < data[i] and stop == False) ] or (data.insert(index, value_to_insert) if(len(data) != length) else ""))
        
def my_insertion_sort(a_list): [ (lambda data, index, value_to_insert, length, stop: (((value_to_insert := data[index]) and (length := len(data)) and data.pop(index)) and ([((stop := True) and data.insert(i, value_to_insert)) for i in range(len(data[:index])) if (value_to_insert < data[i] and stop == False) ] or (data.insert(index, value_to_insert) if(len(data) != length) else ""))))(a_list, index, 0, 0, False) for index in range(0, len(a_list))]

numbers = [33, 63, 6, 66, 77, 74, 51, 30, 86]
my_insertion_sort(numbers)
print(numbers)
# [6, 30, 33, 51, 63, 66, 74, 77, 86]
