n = int(input("Enter a number: "))
if n <= 2:
    print("No prime factors")
else:
    factor = 2
    print(f"The prime factors of {n} are:")
    while factor <= n:
        if n % factor == 0:
            print(factor)
            n = n // factor
        else:
            factor += 1
