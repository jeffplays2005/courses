first = int(input("Enter the length of the first side: "));
second = int(input("Enter the length of the second side: "));
third = int(input("Enter the length of the third side: "));

if(first <= 0 or second <= 0 or third <= 0):
    print("Invalid triangle");
elif(first >= second + third or second >= first + third or third >= first + second):
    print("Invalid triangle");
else:
    print("Valid triangle");
