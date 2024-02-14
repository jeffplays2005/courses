number = int(input("Enter a number: "))

prime = number >= 2
divisor = 2
while divisor < number and prime:
    print("CHECK")
    prime = number % divisor != 0
    divisor += 1
    
if prime:
    print(f"{number} is prime")
else:
    print(f"{number} is not prime")
    print(f"{number} is divisible by {divisor - 1}")
