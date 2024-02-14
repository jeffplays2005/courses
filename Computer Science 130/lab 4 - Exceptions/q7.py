def get_valid_twenty_sided_dice():
    while (a := input("Enter a valid dice: ")) not in [ '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20' ]:
        a = input("Enter a valid dice: ")
    return int(a) # try: except:

def get_valid_twenty_sided_dice(a = input("Enter a valid dice: ")): return ((get_valid_twenty_sided_dice(input("Enter a valid dice: "))) if a not in [ '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20' ] else a) # try: except:

value = get_valid_twenty_sided_dice()
print('Valid input:', value)
        