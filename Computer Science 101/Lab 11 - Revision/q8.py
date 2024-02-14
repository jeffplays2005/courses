def is_valid_day():
    check_me = input("Enter your birth date (yyyy-mm-dd): ")
    checks = check_me.split('-')
    month = int(checks[1])
    day = int(checks[2])
    
    thirty_one_days = [ 1, 3, 5, 7, 8, 10, 12 ]; # 31
    leap = 2 # 32
    thirty_days = [ 4, 6, 9, 11 ]; # 30
    
    if month in thirty_one_days:
        if day <= 31:
            return True
        else:
            return False
    if month in thirty_days:
        if day <= 30:
            return True
        else:
            return False
    if month == leap:
        if day <= 29:
            return True
        else:
            return False

print(is_valid_day())