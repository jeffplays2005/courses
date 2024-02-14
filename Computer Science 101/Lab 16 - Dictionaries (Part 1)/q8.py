def get_inventory(filename):
    dict = {}
    input_file = open(filename, "r")
    lines = input_file.read().split('\n')
    lines.pop(0)
    input_file.close()
    for line in lines:
        splitted = line.split("\t")
        dict[splitted[0]] = float(splitted[-1])
    return dict
    
filename = "Inventory1.txt"
inventory = get_inventory(filename)
for item in sorted(inventory):
    print(f"{item} => ${inventory[item]}")
