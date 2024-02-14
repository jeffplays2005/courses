password = input("Kia ora. Enter your passwsord: ")
verification = input("Verify your password: ")
if password == verification:
    print("Passwords match.")
elif password == input("Passwords do not match. Second verification: "):
    print("Passwords match.")
elif password == input("Passwords do not match. Third verification: "):
    print("Passwords match.")
else:
    print("Passwords do not match. You cannot verify again.")
# 
password = input("Kia ora. Enter your passwsord: ")
verification = input("Verify your password: ")
if password == verification:
    print("Passwords match.")
else:
    verification = input("Passwords do not match. Second verification: ")
    if password == verification:
        print("Passwords match.")
    else:
        verification = input("Passwords do not match. Third verification: ")
        if password == verification:
            print("Passwords match.")
        else:
            print("Passwords do not match. You cannot verify again.")

p = input('Kia ora. Enter your password: ')
p2 = input('Verify your password: ')
p22 = input('Passwords do not match. Second verification: ')
p33 = input('Passwords do not match. Third verification: ')

if p2 != p:
    p22 = input('Passwords do not match. Second verification: ')
elif p22 != p:
    p33 = input('Passwords do not match. Third verification: ')
elif p33 != p:
    print('Passwords do not match. You cannot verify again.')
else:
    print('Passwords match.')