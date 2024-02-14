def remove_extremes(numbers):
    for i in range(len(numbers)-1, -1, -1):
        if(numbers[i] < -1000 or numbers[i] > 1000):
            print(numbers[i])
            numbers.pop(i)
# 1 line
def remove_extremes(numbers): numbers[:] = [ number for number in numbers if number >= -1000 and number <= 1000 ]

number_list1 = [476, 1656, -1000, 1308, 774, -1175, 1195, 1602, -2800]
number_list2 = [-1551, -1000, -1963, 537, 1780, 1000, -1556, 556, 1344]
remove_extremes(number_list1)
remove_extremes(number_list2)
print("number_list1:", number_list1)
print("number_list2:", number_list2)
