def get_user_selection():
    while True:
        selection = int(input("Enter your selection: "))
        if selection < 0 or selection > 7:
            print("Invalid selection!")
        else:
            return selection
print(get_user_selection())