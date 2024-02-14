def get_pell_number(n):
    # set the temporary pell as 0
    temp_pell = 0 # 0
    # set the previous pell as 0, we are starting on(1st pell) 1 so set the first(0th) pell as 0
    previous_pell = 0 # 1st
    # set the current pell as the 1st pell
    current_pell = 1 # 2nd
    # so for each number in the pell number,
    # e.g. n = 10
    # we iterate through 0 - 9(still 10 values, 0,1,2,3,4,5,6,7,8,9)
    for number in range(n - 1):
        # set the temporary pell as the current one, you'll see why later
        temp_pell = current_pell
        # the current pell is set as the current_pell times 2 and then add the previous pell
        current_pell = current_pell * 2 + previous_pell
        # we then set the previous pell as temporary pell, this is because
        # we cant just directly set previous_pell = current_pell
        # we need to do previous_pell = temp_pell, where temp_pell = current_pell
        # and this current_pell is before the number changed in the 2nd line
        previous_pell = temp_pell
    if n == 0:
        # if the pell is 0, return 0
        # this is because the current_pell was set to 1 at the start of this script...
        return 0
    else:
        # return the results!
        return current_pell

p = int(input("pell number: "))
print(get_pell_number(p))
