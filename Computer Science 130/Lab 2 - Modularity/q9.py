def main(option = input("Enter a filename: ")):
    data = read_data(option)
    display_menu()
    while (option := int(input("Enter selection: "))) != 0:
        if option == 1:
            print_table(data)
            display_menu()
        elif option == 2:
            print_dictionary(create_region_dictionary(data))
            # for key in (a_dict := create_region_dictionary(data)):
                # print(key, "{:.2f}".format(a_dict[key]))
            display_menu()
        elif option == 3:
            for key in (a_dict := create_month_dictionary(data)):
                print("{} {name:.2f}".format(key, name=a_dict[key]))
            display_menu()
            
def read_data(filename): return [ (line.split(":")[0], ([float(value) for value in line.split(":")[1].split("\t")])) for line in open(filename).read().split("\n") ] # file.close()
def display_menu(): print("""********************************************\nNew Zealand Mean Monthly Rainfall Statistics\n1. Print Table\n2. Rainfall by Region\n3. Rainfall by Month\n0. Exit\n********************************************""")
def print_table(records): print("\n".join([ "{:15}".format(i[0])+"".join((["{:<6}".format(round(n, 1)) for n in i[1]])) for i in records ]))
def create_region_dictionary(records_list): return { i[0]: sum(i[1]) for i in records_list }
def print_dictionary(a_dict): print("\n".join([ "{:<{}} {:.2f}".format(i[0], max([ len(str(i)) for i in a_dict.keys() ]), (i[1])) for i in a_dict.items() ]))
def create_month_dictionary(records_list): return { value:sum([records_list[i][1][key] for i in range(len(records_list))]) for (key, value) in { 0: "JAN", 1: "FEB", 2: "MAR", 3: "APR", 4: "MAY", 5: "JUN", 6: "JUL", 7: "AUG", 8: "SEP", 9: "OCT", 10: "NOV", 11: "DEC" }.items() }

# 1 line working
def main(filename = input("Enter a filename: "), banner = "********************************************\nNew Zealand Mean Monthly Rainfall Statistics\n1. Print Table\n2. Rainfall by Region\n3. Rainfall by Month\n0. Exit\n********************************************"):
    while (option := int(input(banner+"\nEnter selection: "))) != 0:
        if option == 1:
            print("\n".join([ "{:15}".format(i[0])+"".join((["{:<6}".format(round(n, 1)) for n in i[1]])) for i in [ (line.split(":")[0], ([float(value) for value in line.split(":")[1].split("\t")])) for line in open(filename).read().split("\n") ] ]))
        elif option == 2:
            print("\n".join([ "{:<{}} {:.2f}".format(i[0], max([ len(str(i)) for i in { i[0]: sum(i[1]) for i in [ (line.split(":")[0], ([float(value) for value in line.split(":")[1].split("\t")])) for line in open(filename).read().split("\n") ] }.keys() ]), (i[1])) for i in { i[0]: sum(i[1]) for i in [ (line.split(":")[0], ([float(value) for value in line.split(":")[1].split("\t")])) for line in open(filename).read().split("\n") ] }.items() ]))
        elif option == 3:
            print("\n".join(["{} {name:.2f}".format(key, name={ value:sum([[ (line.split(":")[0], ([float(value) for value in line.split(":")[1].split("\t")])) for line in open(filename).read().split("\n") ][i][1][key] for i in range(len([ (line.split(":")[0], ([float(value) for value in line.split(":")[1].split("\t")])) for line in open(filename).read().split("\n") ]))]) for (key, value) in { 0: "JAN", 1: "FEB", 2: "MAR", 3: "APR", 4: "MAY", 5: "JUN", 6: "JUL", 7: "AUG", 8: "SEP", 9: "OCT", 10: "NOV", 11: "DEC" }.items() }[key]) for key in ({ value:sum([[ (line.split(":")[0], ([float(value) for value in line.split(":")[1].split("\t")])) for line in open(filename).read().split("\n") ][i][1][key] for i in range(len([ (line.split(":")[0], ([float(value) for value in line.split(":")[1].split("\t")])) for line in open(filename).read().split("\n") ]))]) for (key, value) in { 0: "JAN", 1: "FEB", 2: "MAR", 3: "APR", 4: "MAY", 5: "JUN", 6: "JUL", 7: "AUG", 8: "SEP", 9: "OCT", 10: "NOV", 11: "DEC" }.items() })]))

def main(filename = input("Enter a filename: "), banner = "********************************************\nNew Zealand Mean Monthly Rainfall Statistics\n1. Print Table\n2. Rainfall by Region\n3. Rainfall by Month\n0. Exit\n********************************************"):
    while (option := int(input(banner+"\nEnter selection: "))) != 0:
        print("\n".join([ "{:15}".format(i[0])+"".join((["{:<6}".format(round(n, 1)) for n in i[1]])) for i in [ (line.split(":")[0], ([float(value) for value in line.split(":")[1].split("\t")])) for line in open(filename).read().split("\n") ] ])) if option == 1 else print("\n".join([ "{:<{}} {:.2f}".format(i[0], max([ len(str(i)) for i in { i[0]: sum(i[1]) for i in [ (line.split(":")[0], ([float(value) for value in line.split(":")[1].split("\t")])) for line in open(filename).read().split("\n") ] }.keys() ]), (i[1])) for i in { i[0]: sum(i[1]) for i in [ (line.split(":")[0], ([float(value) for value in line.split(":")[1].split("\t")])) for line in open(filename).read().split("\n") ] }.items() ])) if(option == 2) else print("\n".join(["{} {name:.2f}".format(key, name={ value:sum([[ (line.split(":")[0], ([float(value) for value in line.split(":")[1].split("\t")])) for line in open(filename).read().split("\n") ][i][1][key] for i in range(len([ (line.split(":")[0], ([float(value) for value in line.split(":")[1].split("\t")])) for line in open(filename).read().split("\n") ]))]) for (key, value) in { 0: "JAN", 1: "FEB", 2: "MAR", 3: "APR", 4: "MAY", 5: "JUN", 6: "JUL", 7: "AUG", 8: "SEP", 9: "OCT", 10: "NOV", 11: "DEC" }.items() }[key]) for key in ({ value:sum([[ (line.split(":")[0], ([float(value) for value in line.split(":")[1].split("\t")])) for line in open(filename).read().split("\n") ][i][1][key] for i in range(len([ (line.split(":")[0], ([float(value) for value in line.split(":")[1].split("\t")])) for line in open(filename).read().split("\n") ]))]) for (key, value) in { 0: "JAN", 1: "FEB", 2: "MAR", 3: "APR", 4: "MAY", 5: "JUN", 6: "JUL", 7: "AUG", 8: "SEP", 9: "OCT", 10: "NOV", 11: "DEC" }.items() })])) if option == 3 else None
# 1 line
def main(filename = input("Enter a filename: "), banner = "********************************************\nNew Zealand Mean Monthly Rainfall Statistics\n1. Print Table\n2. Rainfall by Region\n3. Rainfall by Month\n0. Exit\n********************************************"): ((print("\n".join([ "{:15}".format(i[0])+"".join((["{:<6}".format(round(n, 1)) for n in i[1]])) for i in [ (line.split(":")[0], ([float(value) for value in line.split(":")[1].split("\t")])) for line in open(filename).read().split("\n") ] ])) if option == 1 else print("\n".join([ "{:<{}} {:.2f}".format(i[0], max([ len(str(i)) for i in { i[0]: sum(i[1]) for i in [ (line.split(":")[0], ([float(value) for value in line.split(":")[1].split("\t")])) for line in open(filename).read().split("\n") ] }.keys() ]), (i[1])) for i in { i[0]: sum(i[1]) for i in [ (line.split(":")[0], ([float(value) for value in line.split(":")[1].split("\t")])) for line in open(filename).read().split("\n") ] }.items() ])) if(option == 2) else print("\n".join(["{} {name:.2f}".format(key, name={ value:sum([[ (line.split(":")[0], ([float(value) for value in line.split(":")[1].split("\t")])) for line in open(filename).read().split("\n") ][i][1][key] for i in range(len([ (line.split(":")[0], ([float(value) for value in line.split(":")[1].split("\t")])) for line in open(filename).read().split("\n") ]))]) for (key, value) in { 0: "JAN", 1: "FEB", 2: "MAR", 3: "APR", 4: "MAY", 5: "JUN", 6: "JUL", 7: "AUG", 8: "SEP", 9: "OCT", 10: "NOV", 11: "DEC" }.items() }[key]) for key in ({ value:sum([[ (line.split(":")[0], ([float(value) for value in line.split(":")[1].split("\t")])) for line in open(filename).read().split("\n") ][i][1][key] for i in range(len([ (line.split(":")[0], ([float(value) for value in line.split(":")[1].split("\t")])) for line in open(filename).read().split("\n") ]))]) for (key, value) in { 0: "JAN", 1: "FEB", 2: "MAR", 3: "APR", 4: "MAY", 5: "JUN", 6: "JUL", 7: "AUG", 8: "SEP", 9: "OCT", 10: "NOV", 11: "DEC" }.items() })])) if option == 3 else None) or main(filename, banner)) if (option := int(input(banner+"\nEnter selection: "))) != 0 else None

main()
