# user input
integer_input = input("Enter a line of integers: ")
# split the integers by a comma into individual items in an array
individual_integers = integer_input.split(",")
# set lowest and highest to the first index of individual_integers
# this is to prevent 1 single integer being entered, e.g. 50
lowest = individual_integers[0];
highest = individual_integers[0];

for number in range(0, len(individual_integers)):
    if number != 0:
        if int(individual_integers[number]) < int(lowest):
            lowest = individual_integers[number]
        elif int(individual_integers[number]) > int(highest):
            highest = individual_integers[number]

print(f"The minimum number is {lowest} and the maximum number is {highest}.")
