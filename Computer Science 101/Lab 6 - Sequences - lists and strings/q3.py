data = []
new_data = input("Add a word (blank to exit): ")
while new_data != "":
    if new_data not in data:
        data += [new_data]
    new_data = input("Add a word (blank to exit): ")
print(f"Words: {data}")
