def print_prime_factors(number):
    if number < 2:
        print("No prime factors")
    else:
        print(f"The prime factors of {number} are:")
        factor = 2
        while factor <= number:
            if number % factor == 0:
                print(factor)
                number //= factor
            else:
                factor += 1
