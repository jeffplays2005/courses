def create_month_number_of_days_dictionary(months, number_of_days):
    return { months[index] : number_of_days[index] for index in range(len(months)) }

words1 = ['JAN', 'FEB', 'MAR']
list2 = [31, 28, 31]
a_dict = create_month_number_of_days_dictionary(words1, list2)
print(a_dict)
for key in sorted(a_dict.keys()):
    print(key, a_dict[key])
# 1 liner
def create_month_number_of_days_dictionary(months, number_of_days): return { months[n]:number_of_days[n] for n in range(len(months)) }
