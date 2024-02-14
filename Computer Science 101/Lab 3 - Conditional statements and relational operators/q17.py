y = int(input("Enter the year: "));
if (y % 400) == 0:
    print(f"{y} is a leap year");
elif ((y%400) % 100) == 0:
    print(f"{y} is not a leap year");
elif ((y%400) % 4) == 0:
    print(f"{y} is a leap year");
else:
    print(f"{y} is not a leap year");
    
year = int(input("Enter the year: "));
# Any year that is divisible by 400 is a leap year.
if (year % 400) == 0:
    print(f"{year} is a leap year")
# Of the remaining years, any year that is divisible by 100 is not a leap year.
elif ((year % 400) % 100) == 0:
    print(f"{year} is not a leap year")
# Of the remaining years, any year that is divisible by 4 is a leap year.
elif ((year%400) % 4) == 0:
    print(f"{year} is a leap year")
    # All other years are not leap years.
else:
    print(f"{y} is not a leap year");
