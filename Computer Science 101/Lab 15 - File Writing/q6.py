def get_contact_info(contact_list, contact_name):
    for i in contact_list:
        if i[0] == contact_name:
            return i
contact_list = [('Damir Azhar', '021-1234567', 'damir@emailprovider.com'),
                ('Ann Cameron', '022-7654321', 'ann@bmail.com')]
contact_info = get_contact_info(contact_list, "Ann Cameron")
print(contact_info)