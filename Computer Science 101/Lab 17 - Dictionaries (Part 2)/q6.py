def update_dictionary(a_dict, target_value):
    keys = list(a_dict.keys());
    while len(keys) > 0:
        if a_dict[keys[0]] == target_value:
            del(a_dict[keys[0]])
        keys.pop(0)
            
a_dict = {"a":0, "b":0, "c":1, "d":1, "e":5}
print("Before:", end=" ")
keys = list(a_dict.keys())
for key in keys:
    print(f"{key}:{a_dict[key]}", end=" ")
print()
update_dictionary(a_dict, 0)
print("After:", end=" ")
keys = list(a_dict.keys())
for key in keys:
    print(f"{key}:{a_dict[key]}", end=" ")
print()