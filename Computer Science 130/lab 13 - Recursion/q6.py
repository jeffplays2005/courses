def no_odds(numbers):
    if not numbers:
        return True
    else:
        if numbers[0]%2 != 0:
            return False
        else:
            return no_odds(numbers[1:])
# 1 line
def no_odds(numbers): return True if not numbers else False if numbers[0] % 2 != 0 else no_odds(numbers[1:])
print(no_odds([2, 3, 5, 6]))
# False
print(no_odds([2]))
# True
print(no_odds([2, 4, 6, 8, 10]))
# True