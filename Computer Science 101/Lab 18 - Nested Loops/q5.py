def print_ox_xo_pattern(number_of_rows, number_of_columns):
    a = "o"
    for i in range(number_of_rows):
        clone = a
        to_print = []
        for i in range(number_of_columns):
            to_print.append(a)
            a = "o" if a == "x" else "x"
        print("".join(to_print))
        a = "o" if clone == "x" else "x"

print_ox_xo_pattern(5, 4)
print_ox_xo_pattern(2, 3)