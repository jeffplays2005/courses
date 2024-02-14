def calculate_fee(age, is_enrolled):
    if is_enrolled:
        if age >= 65:
            fee = 43
        elif age >= 45:
            fee = 50
        elif age >= 18:
            fee = 60
        elif age >= 13:
            fee = 40
        else:
            fee = 0
        return fee
    else:
        if age >= 13:
            fee = 70
        elif age >= 5:
            fee = 40
        else:
            fee = 30
        return fee
