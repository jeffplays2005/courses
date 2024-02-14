names = ["John", "Jane", "Peter", "Paul", "Michael", "Mary", "Robert", "Roland"]
def prompt():
    # print current names
    print(f"Current list of names: {names}");
    option = input("Enter A to add a name or D to delete a name: ");
    if(option == "A"):
        # add
        new_name = input("Enter a new name: ");
        after_me = check("Enter the name you want to insert the new name before: ", names);
        position = names.index(after_me);
        names.insert(position, new_name);
        print(f"Updated list of names: {names}");
    else:
        # delete
        e = check("Enter a name to delete: ", names);
        names.remove(e);
        print(f"Updated list of names: {names}");
        
def check(query, list_of_things):
    check_me = input(query)
    if(check_me not in list_of_things):
        print(f"{check_me} is not in the list of names!");
        return check(query, list_of_things);
    else:
        return check_me;
        
prompt();
