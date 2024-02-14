array = [];
def prompt():
    check = input("Please enter an item for your shopping list or end to print the list: ")
    if(check != "end"):
        array.append(check)
        prompt();
    else:
        obj_with_ids = []
        array2= sorted(array)
        for i, item in enumerate(array2):
            obj_with_ids.append({"pos": i+1, "item": item})
        result = list(map(lambda c: f"{c['pos']}) {c['item']}", obj_with_ids))
        print("")
        print("Shopping List:")
        print("==============")
        print("\n".join(result))
prompt()
