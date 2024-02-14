password = input("Please enter your password: ").strip()
if(password[0].lower().isalpha() and len(password) >= 8):
    num_digits = 0
    num_alphacars = 0
    for character in password:
        if character.isdigit(): num_digits += 1
        else: num_alphacars +=1

    if num_digits >= 3 and num_alphacars >= 4: print("Your password is valid!")
    else: print("Your password is invalid!")
else:
    print("Your password is invalid!")
