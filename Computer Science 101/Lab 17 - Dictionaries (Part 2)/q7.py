def merge_dictionaries(email_dict, phone_num_dict):
    new_dict = {}
    for i in email_dict.keys():
        new_dict[i] = (email_dict[i], phone_num_dict[i])
    return new_dict
    
email_dict = {"Damir":"damir@mail.com", "Ann":"ann@mail.com"}
phone_num_dict = {'Damir':"021-1234567", "Ann":"022-1234567"}
contacts_dict = merge_dictionaries(email_dict, phone_num_dict)
for key in sorted(contacts_dict):
    print(key, contacts_dict[key])
print(type(contacts_dict))

email_dict = {"Damir":"damir@mail.com", "Ann":"ann@mail.com",
              "Andrew":"andrew@mail.com", "Angela":"angela@mail.com"}
phone_num_dict = {"Andrew":"023-7654321", 'Damir':"021-1234567",
                  "Angela":"024-1112223", "Ann":"022-1234567"}
contacts_dict = merge_dictionaries(email_dict, phone_num_dict)
for key in sorted(contacts_dict):
    print(key, contacts_dict[key])    
# explanation
def merge_dictionaries(email_dict, phone_num_dict):
    # create a new dictionary
    new_dict = {}
    # as both the dictionaries have the same keys, we can simply iterate 
    # through one of the dictionaries
    for i in email_dict.keys():
        # i is the dictionary key
        # simply create a new key and value in the new_dict 
        # set this value as the tuple of the element from email and phone number dictionary
        # based on i(which is the key)
        new_dict[i] = (email_dict[i], phone_num_dict[i])
    # return the dictionary
    return new_dict