# user inputs
start = int(input("Enter the start: "))
end = int(input("Enter the start: "))
# create a blank string
# loop through numnbers in the range of start and end
# the for loop iterates through each number where start ≤ number < end
# in this case, e.g. start = 1 end = 10
# think of this as a while loop but you dont need to set number and you do not have to do number+=1
for number in range(start, end):
    # 1 2 3 4 5 6 7 8 9
    # 2 divides number
    if number % 2 == 0:
        # add to whole string
        print(number, end = " ")
