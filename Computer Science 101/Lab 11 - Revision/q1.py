def to_the_power_of():
    number_one = int(input("Number 1: "))
    number_two = int(input("Number 2: "))
    
    output = number_one ** number_two
    
    return f"{number_one} to the power of {number_two} is {output}"

print(to_the_power_of())