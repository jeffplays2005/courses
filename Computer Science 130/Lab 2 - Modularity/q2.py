def get_user_option_input():
    selection = int(input("Enter selection: "))
    while selection > 3 or selection < 0:
        selection = int(input("Enter selection: "))
    return selection
# 1 line
def get_user_option_input(): return selection if (selection := int(input("Enter selection: "))) <= 3 and selection >= 0 else get_user_option_input()
# test
number = get_user_option_input()
print(number)