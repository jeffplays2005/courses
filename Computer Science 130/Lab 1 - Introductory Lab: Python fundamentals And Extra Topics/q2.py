feet = int(input("Enter the feet: "));
inches = int(input("Enter the inches: "));
print(f"{feet} feet {inches} inches is approximately {round(2.54 * (inches + 12 * feet))} centimetres.")

# 1 line
print(f"{(feet := int(input('Enter the feet: ')))} feet {(inch := int(input('Enter the inches: ')))} inches is approximately {round(2.54 * (inch + 12 * feet))} centimetres.")
