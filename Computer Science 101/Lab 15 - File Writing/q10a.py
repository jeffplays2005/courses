def main():
    filename = "Contacts1.txt"
    list_of_contacts = get_contacts(filename)
    display_menu()
    print()
    selection = get_user_selection()
    while selection != 3:
        if selection == 1:
            name = input("Enter contact's name: ")
            found_user = get_contact_info(list_of_contacts, name)
            print()
            print_contact_info(found_user)
            print()
        elif selection == 2:
            add_contact(list_of_contacts)
            print()
        selection = get_user_selection()
    save_contacts(list_of_contacts, 'upi123.txt')
    print("Exiting program ... goodbye!")
    
def display_menu():
    print("***********************")
    print("Simple Contacts Program")
    print("***********************")
    print("1. Display contact info")
    print("2. Add a new contact")
    print("3. Save and Exit")
    
def get_user_selection():
    while True:
        selection = int(input("Enter selection: "))
        if selection == 1 or selection == 2 or selection == 3:
            break
        else:
            print(f"Invalid input!")
    return selection
    
def get_contacts(filename):
    input_file = open(filename, "r")
    contents = input_file.read().split("\n")
    input_file.close()
    new_list = []
    for i in range(0, len(contents), 3):
        new_list.append((contents[i], contents[i + 1], contents[i + 2]))
    return new_list
    
def get_contact_info(contact_list, contact_name):
    for contact in contact_list:
        if contact[0] == contact_name:
            return contact[:]
    return None

def print_contact_info(contact_info):
    if contact_info != None:
        print(f"Name: {contact_info[0]} Phone: {contact_info[1]} Email: {contact_info[2]}")
    else:
        print("Contact not found")
    return

def add_contact(contact_list):
    print("Please enter the new contact's details")
    name = input("Contact's Name: ")
    phone = input("Contact's Phone Number: ")
    email = input("Contact's Email address: ")
    contact = (name, phone, email)
    contact_list.append(contact)
    print(f"Contact added")
    
def save_contacts(contact_list, filename):
    output_file = open(filename, "w")
    for i in contact_list:
        output_file.write(str(i[0]) + "\n" + str(i[1]) + "\n" + str(i[2]) + "\n")
    output_file.close()
