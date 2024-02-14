def read_countries(filename):
    try:
        file = open(filename)
        lines = file.read().split('\n')
        file.close()
        dict = {}
        for i in lines:
            if len(i.strip()) > 0:
                try:
                    n = i.split(',')
                    if len(n) == 1:
                        print(f'ERROR: Invalid \'{n[0]}\'!')
                    else:
                        dict[n[0]] = n[1]
                except:
                    ""
        return dict
    except FileNotFoundError:
        print(f"ERROR: The file '{filename}' does not exist.")
        return {}
        
print(read_countries('countries.txt'))