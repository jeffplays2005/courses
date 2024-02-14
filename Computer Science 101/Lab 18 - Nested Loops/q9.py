def print_number_pyramid(number_of_rows):
    if number_of_rows == 1:
        return print("1  ")
    elif number_of_rows == 2:
        return print("""   1\n1     1""")
    space = "     "
    aaa = [[1], [1,1]]
    for i in range(number_of_rows - 2):
        previous = aaa[-1]
        doubles = []
        for n in range(len(previous) - 1):
            doubles.append(previous[n:n+2])
        compiled = [1]
        for x in doubles:
            compiled.append(str(int(x[0]) + int(x[-1])))
        compiled.append(1)
        aaa.append(compiled)
    bbb = []
    for i in aaa:
        bbb.append([str(a) for a in i])
    for i in range(len(bbb)):
        start_spacing = (number_of_rows - (i + 1)) * "   "
        joined = space.join(bbb[i])
        print(f"{start_spacing}{joined}")

print_number_pyramid(5)
