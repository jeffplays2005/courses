def read_multiples_of_3(filename):
    try:
        file = open(filename)
        l = []
        lines = " ".join(file.read().split('\n')).split(' ')
        file.close()
        for i in lines:
            try:
                if int(i) % 3 == 0:
                    l.append(int(i))
            except:
                ""
        return l
    except FileNotFoundError:
        print(f"ERROR: The file '{filename}' does not exist.")
        return []
# 1 line false
# def read_multiples_of_3(filename, a = [ str(i) for i in range(10000) ]):
    # return [ int(i) for i in " ".join(open(filename).read().split("\n")).split(" ") if i in a and int(i) % 3 == 0] # .close
print(read_multiples_of_3("eight_numbers.txt"))
print(read_multiples_of_3('input_unknown.txt'))