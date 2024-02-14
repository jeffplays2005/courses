def save_contacts(contact_list, filename):
    file = open(filename, 'w')
    concat = []
    for i in contact_list:
        concat.append(f"{i[0]}\n{i[1]}\n{i[2]}")
    file.write("\n".join(concat))
    file.close()
    
contact_list = [('Ann Cameron', '022-7654321', 'ann@bmail.com'),
                 ('Damir Azhar', '021-1234567', 'damir@emailprovider.com')]
save_contacts(contact_list , 'upi123.txt')
