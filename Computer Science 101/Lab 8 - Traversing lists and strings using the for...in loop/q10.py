# ask for user inputs
assignment_data = input("Enter assignment data: ")
missed = 0
# split by a comma
individual_assigns = assignment_data.split(",")
# loop through each
counter = 0
for assign in individual_assigns:
    if assign != "":
        counter += float(assign)
    else:
        missed += 1

# if the counter is > 0(where there was actual assignments turned in)
if counter != 0:
    # when there were no misses
    if missed == 0:
        print("Assignments missed: 0")
        print(f"Assignment average: {counter}")
    else:
    # when there are assignments missed
        print(f"Assignments missed: {missed}")
        average = round(counter / (len(individual_assigns) - missed), 2)
        print(f"Assignment average: {average}")
else:
    print(f"Assignments missed: {missed}")
    print("Assignment average: Undefined")
