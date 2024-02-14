import math
#  user input
start = int(input("Enter the start: "))
end = int(input("Enter the end: "))

for number in range(start, end):
    if math.sqrt(number) == int(math.sqrt(number)):
        print(number, end = " ")
    start+=1
