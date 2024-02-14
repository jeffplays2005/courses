def print_contact_info(contact_info):
    if type(contact_info) != tuple:
        print('Contact not found')
    else:
        print(f"Name: {contact_info[0]} Phone: {contact_info[1]} Email: {contact_info[2]}")
        
contact_info = None
print_contact_info(contact_info)
contact_info = ('Damir Azhar', '021-1234567', 'damir@emailprovider.com')
print_contact_info(contact_info)