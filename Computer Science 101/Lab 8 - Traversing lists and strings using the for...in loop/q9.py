temp_input = input("Enter a line of temperature values: ")
# create a blank list for extreme temperatures
extreme_temps = []
# split to individual temperatures
individual_temps = temp_input.split(",")
# loop
for temp in individual_temps:
    # when the temp is less than equal to 10
    if int(temp) <= -10:
        extreme_temps.append(int(temp))
    # when the temperature is higher than equal 40
    elif int(temp) >= 40:
        extreme_temps.append(int(temp))

# sort this list of integers
extreme_temps.sort()
# create a new list
string_extreme = []
# loop through each temperature in the extreme temps
for temp in extreme_temps:
    # append a **string** into the list
    string_extreme.append(str(temp))
# output
# can only join a list of strings, not integers...
print(f'The extreme temperatures are: {", ".join(string_extreme)}')

# 1 liner
print(f'The extreme temperatures are: {", ".join([str(i) for i in sorted([t for t in input("Enter a line of temperature values: ").split(",") if int(t) <= -10 or int(t) >= 40 ])])}')
