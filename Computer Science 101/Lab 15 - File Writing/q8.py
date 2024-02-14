def add_contact(contact_list):
    print("Please enter the new contact's details")
    name = input("Contact's Name: ")
    number = input("Contact's Phone Number: ")
    email = input("Contact's Email address: ")
    contact_list.append((name, number, email))
    print("Contact added")