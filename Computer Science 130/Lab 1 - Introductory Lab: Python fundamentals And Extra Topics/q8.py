file = open(input("Enter a filename: "));
lines = file.read().split("\n");
file.close();
for i in lines:
    words = i.split()
    crafted = [];
    for n in words:
        crafted += [n[0], n[-1]];
    print(("".join(crafted)).lower());
