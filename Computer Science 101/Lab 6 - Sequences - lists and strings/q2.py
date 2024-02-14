data = [56, -2, 13, 0, 10, -7, 4, 6]
clean_data = []
count = 0
while count < len(data):
    number = data[count]
    if number >= 0:
        clean_data += [number]
    count += 1
print(f"Non negative data: {clean_data}")
