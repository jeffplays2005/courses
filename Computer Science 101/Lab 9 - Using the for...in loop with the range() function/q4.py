# take user input
start = int(input("Enter the start: "))
end = int(input("Enter the end: "))
# loop through each number between start and end and reduce the number by 1 each time.
# subtract 1 from end because if start == end, the for loop skips the number
for number in range(start, end - 1, -1):
    print(number, end = " ")
