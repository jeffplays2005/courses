# ask for user inputs
lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))
# set a counter
total = 0
# for each number in the range of the lower and upper bound
for number in range(lower_bound, upper_bound + 1):
    # this is for each number in between lower_bound and upper_bound
    if (number % 3) == 0:
        # if the number is divisible by 3, add to the counter
        total += number
    elif number % 5 == 0:
        # if the number is divisible by 5, add to the number
        total += number
# print an output
print(f"Sum of multiples within [{lower_bound}, {upper_bound}] is {total}.")
