def digital_root(number):
    total = 0 # set the total to 0
    for i in str(number): # go through each number in the number string
        total += int(i) # add to total
        
    digital_number = 0 # create the digital number
    for i in str(total):
        digital_number += int(i) # get the 
    for i in range(len(str(digital_number))):
        total = digital_number
        digital_number = 0
        for i in str(total):
            digital_number += int(i)
    return digital_number
    
number = 123456
print(f"Digital Root of {number} = {digital_root(number)}")
print(f"Function return type = {type(digital_root(number))}")

number = 778925
print(f"Digital Root of {number} = {digital_root(number)}")
