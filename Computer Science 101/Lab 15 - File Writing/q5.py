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

def get_contacts(filename):
    file = open(filename)
    file_contents = file.read().split('\n')
    file.close()    
    list_of_contacts = []
    for i in range(0, len(file_contents), 3):
        name = file_contents[i]
        number = file_contents[i+1]
        email = file_contents[i+2]
        list_of_contacts.append((name, number, email))
    return list_of_contacts
contact_list = get_contacts("Contacts1.txt")
print(contact_list)
