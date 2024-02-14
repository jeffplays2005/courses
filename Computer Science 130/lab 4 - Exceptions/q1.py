def is_eligible(number):
    try:
        n = int(number)
        return (True if n >=65 else False,n)
    except ValueError:
        return (False, 'ERROR: The value is invalid!')
    except TypeError:
        return (False, 'ERROR: The type is incorrect!')