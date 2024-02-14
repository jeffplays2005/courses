def round_temperatures(temperatures_list):
    return [ round(temp) for temp in temperatures_list ]
# testing
temperatures = [17.1, 22.8, 18.4, 19.1, 23.5]
values = round_temperatures(temperatures )
print(temperatures)
print(values)
