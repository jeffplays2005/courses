def print_table(records):
    for i in records:
        print_me = []
        print_me.append("{:15}".format(i[0]))
        for n in i[1]:
            print_me.append("{:<6}".format(round(n, 1)))        
        print("".join(print_me))
        
# 1 line
def print_table(records): print("\n".join([ "{:15}".format(i[0])+"".join((["{:<6}".format(round(n, 1)) for n in i[1]])) for i in records ]))
        
data = [('Auckland', [73.33, 66.12, 87.34, 99.47, 112.69, 126.47, 145.13, 118.45, 105.13, 100.25, 85.87, 92.88]), ('Hamilton', [76.3, 68.7, 79.4, 80.3, 99.7, 113.2, 118.2, 103.4, 91.5, 91.9, 85.0, 100.7])]
print_table(data)
