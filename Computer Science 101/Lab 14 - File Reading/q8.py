def get_target_numbers(filename):
    input_file = open(filename, "r")
    lines = input_file.read().split('\n')
    input_file.close()

    amount = int(lines.pop(0).strip())
    minimum = int(lines.pop(0).strip())
    maximum = int(lines.pop(0).strip())

    filtered_list = []

    if amount != 0:
        for line in lines:
            line = line.strip()
            if line:
                filtered_list.append(int(line))

    filtered_list = sorted(filtered_list)
    targets = []

    for num in filtered_list:
        if minimum <= num <= maximum:
            targets.append(num)
            if len(targets) == amount:
                break
    return targets

filename = "numbers1.txt"
print(f"List of target numbers: {get_target_numbers(filename)}")
filename2 = "numbers2.txt"
print(f"List of target numbers: {get_target_numbers(filename2)}")
