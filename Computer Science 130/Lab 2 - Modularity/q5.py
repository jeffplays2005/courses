def create_month_dictionary(records_list):
    months = { 0: "JAN", 1: "FEB", 2: "MAR", 3: "APR", 4: "MAY", 5: "JUN", 6: "JUL", 7: "AUG", 8: "SEP", 9: "OCT", 10: "NOV", 11: "DEC" }
    return { value:sum([records_list[i][1][key] for i in range(len(records_list))]) for (key, value) in months.items() }
    
# 1 line
def create_month_dictionary(records_list): return { value:sum([records_list[i][1][key] for i in range(len(records_list))]) for (key, value) in { 0: "JAN", 1: "FEB", 2: "MAR", 3: "APR", 4: "MAY", 5: "JUN", 6: "JUL", 7: "AUG", 8: "SEP", 9: "OCT", 10: "NOV", 11: "DEC" }.items() }
    
data = [('Auckland', [73.3, 66.1, 87.3, 99.4, 112.6, 126.4, 145.1, 118.4, 105.1, 100.2, 85.8, 92.8]), ('Hamilton', [76.3, 68.7, 79.4, 80.3, 99.7, 113.2, 118.2, 103.4, 91.5, 91.9, 85.0, 100.7])]
a_dict = create_month_dictionary(data)
for key in sorted(a_dict):
    print("{}: {name:.2f}".format(key, name=a_dict[key]))

def create_month_dictionary(records_list):
    months = { 0: "JAN", 1: "FEB", 2: "MAR", 3: "APR", 4: "MAY", 5: "JUN", 6: "JUL", 7: "AUG", 8: "SEP", 9: "OCT", 10: "NOV", 11: "DEC" }
    return { name: sum([ records_list[i][1][pos] for i in range(len(records_list)) ]) for (pos, name) in months.items() }