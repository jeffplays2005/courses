data = [5, -2, 10, 0, -2, 4, 10, 6]
smallest = 0
count = 0
while count < len(data):
    if data[count] < data[smallest]:
        smallest = count
    count += 1

biggest = len(data) - 1
count = biggest
while count >= 0:
    if data[count] > data[biggest]:
        biggest = count
    count -= 1

subsequence = data[smallest:biggest+1]
print(subsequence)
