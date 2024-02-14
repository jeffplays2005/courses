def get_line_averages(filename):
    averages = []
    file = open(filename)
    lines = file.read().split('\n')
    file.close()
    for i in lines:
        if len(i.strip()) > 0:
            total = 0
            splitted = i.split()
            for n in splitted:
                total += int(n)
            averages.append(round(total / len(splitted), 2))
    return averages

filename = "Data1.txt"
line_averages = get_line_averages(filename)
print("Line averages:", line_averages)
print("Checking return type:", type(line_averages))
