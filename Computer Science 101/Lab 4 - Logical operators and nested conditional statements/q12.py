month = input("Enter the month: ")
year = int(input("Enter the year: "))

thirty_one_days = [ "January", "March", "May", "July", "August", "October", "December" ]
leap = [ "February" ]
thirty_days = [ "April", "June", "September", "November" ]

if month in thirty_one_days:
    print(f"{month} has 31 days.");
elif month in thirty_days:
    print(f"{month} has 30 days.");
elif month in leap:
    if (year % 400) == 0:
        print(f"{month} has 29 days.")
    elif ((year%400) % 100) == 0:
        print(f"{month} has 28 days.")
    elif ((year%400) % 4) == 0:
        print(f"{month} has 29 days.")
    else:
        print(f"{month} has 28 days.")
else:
    print("Invalid month.")
    
# vicky's code
# ask for month and year first
m = input("Enter the month: ")
y = int(input("Enter the year: "))
# check if its in any of the months, we dont care about the year!
if m in ["January", "March", "May", "July", "August", "October", "December"]:
    print(f"{m} has 31 days.")
elif m in ["February"]:
    # since its in february, we care about the year
    # your other code in here
    if (y % 400) == 0:
        print(f"{m} has 29 days.")
    elif ((y%400) % 100) == 0:
        print(f"{m} has 28 days.")
    elif ((y%400) % 4) == 0:
        print(f"{m} has 29 days.")
    else:
        print(f"{m} has 28 days.")
elif m in ["April", "June", "September", "November"]:
    # we dont care about the year because its not february
    print(f"{m} has 31 days.")
else:
    # its not a month
    print("Invalid month.")
