def main():
    filename = "Contacts1.txt"
    list_of_contacts = get_contacts(filename)
    display_menu()
    selection = get_user_selection()
    while selection != 3:
        if selection == 1:
            name = input("Enter contact's name: ")
            found = get_contact_info(list_of_contacts, name)
            print()
            print_contact_info(found)
            print()
        elif selection == 2:
            add_contact(list_of_contacts)
            print()
        selection = get_user_selection()
    save_contacts(list_of_contacts, 'upi123.txt')
    print("Exiting program ... goodbye!")

def display_menu():
    print("""***********************
Simple Contacts Program
***********************
1. Display contact info
2. Add a new contact
3. Save and Exit
""")

def get_user_selection():
    selection = int(input("Enter selection: "))
    while selection not in [1,2,3]:
        print("Invalid input!")
        selection = int(input("Enter selection: "))
    return selection
    
def get_contacts(filename):
    file = open(filename)
    file_contents = file.read().split('\n')
    file.close()
    list_of_contacts = []
    while len(file_contents) > 0:
        name = file_contents.pop(0)
        phone_number = file_contents.pop(0)
        email = file_contents.pop(0)
        list_of_contacts.append((name, phone_number, email))
    return list_of_contacts

def get_contact_info(contact_list, contact_name):
    for i in contact_list:
        if i[0] == contact_name:
            return i
    return None

def print_contact_info(contact_info):
    if type(contact_info) != tuple:
        print('Contact not found')
    else:
        print(f"Name: {contact_info[0]} Phone: {contact_info[1]} Email: {contact_info[2]}")

def add_contact(contact_list):
    print("Please enter the new contact's details")
    name = input("Contact's Name: ")
    number = input("Contact's Phone Number: ")
    email = input("Contact's Email address: ")
    contact_list.append((name, number, email))
    print("Contact added")
    
def save_contacts(contact_list, filename):
    file = open(filename, 'w')
    concat = []
    for i in contact_list:
        concat.append(f"{i[0]}\n{i[1]}\n{i[2]}")
    file.write("\n".join(concat))
    file.close()
