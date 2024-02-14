def validate_username(username):
    # digits = username[-3:len(username) + 1]
    name = ""
    digits = ""
    for i in username:
        if i.isdigit(): digits = f"{digits}{i}"
        else: name += i
        
    if len(username) > 7 or len(digits) != 3:
        raise ValueError (f"ERROR: '{username}' - Invalid Format!")
    d1 = int(digits[0])
    d2 = int(digits[1])
    d3 = int(digits[2])
    
    if ((d1 * 1 + d2 * 2) % 9) % 9 != d3:
        raise ValueError (f"ERROR: '{username}' - Invalid check digit!")
    return d3

print(validate_username('acha455'))
print(validate_username('acha568'))
print(validate_username('kng327'))

try:
    print(validate_username('cbur974'))
    print(validate_username('k1235'))
except ValueError as e:
    print(e)
else:
    print("Well done!")
    
try:
    print(validate_username('achang1235'))
except ValueError as e:
    print(e)
else:
    print("Well done!")

try:
    print(validate_username('12345'))
except ValueError as e:
    print(e)
else:
    print("Well done!")
    
try:
    print(validate_username('12'))
except ValueError as e:
    print(e)
else:
    print("Well done!")