def get_user_selection():
    selection = int(input("Enter selection: "))
    while selection not in [1,2,3]:
        print("Invalid input!")
        selection = int(input("Enter selection: "))
    return selection