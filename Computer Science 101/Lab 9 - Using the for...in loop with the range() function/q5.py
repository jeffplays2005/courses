# take user input
start = int(input("Enter the start: "))
end = int(input("Enter the end: "))
step = int(input("Enter the step: "))
# if the start is larger than end
# e.g. 9 > 3
if start > end:
    # while the end(3) is smaller than start(9)
    while end < start:
        print(end, end = " ")
        # add step to end, e.g. 2
        # 3+2=5
        end += step;
# if the end is larger than the start
# e.g. start = 2
# e.g. end = 7
else:
    # while the start(2) is smaller than end(7)
    while start < end:
        print(start, end = " ")
        # add step
        start += step;
