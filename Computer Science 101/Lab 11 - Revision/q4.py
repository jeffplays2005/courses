first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

total = first_number + second_number
square_rooted = math.sqrt(total)
is_integer = square_rooted.is_integer()
if is_integer:
     print(f"The sum of {first_number} and {second_number} is a square number.")
else:
     print(f"The sum of {first_number} and {second_number} is not a square number.")
