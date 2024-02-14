first_name = input("Please enter your first name: ")
surname = input("Please enter your surname: ")
whole = "";
whole += first_name[0];
whole += surname[0:3];
if(len(surname[0:3])):
    whole += "*" * (3 - len(surname[0:3]));

print(f"Your username is: {whole}");
