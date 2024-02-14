def print_bar_chart(data_dict):
    for i in sorted(data_dict.keys()):
        print(f"{i}|{data_dict[i] * '#'}{data_dict[i]}")
        
data_dict = {8: 15, 7: 17, 6: 10, 5: 8, 4: 12, 3: 13, 2: 11, 1: 9}
print_bar_chart(data_dict)