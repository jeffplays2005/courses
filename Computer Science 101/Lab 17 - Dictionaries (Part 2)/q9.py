def print_high_scores(score_dict):
    tuple_list = [];
    for i in score_dict.keys():
        tuple_list.append((i, score_dict[i]))
    tuple_list = sorted(tuple_list)
    tuple_list = sorted(tuple_list, key = lambda x: x[1], reverse = True)
    print("""--------------------
Name           Score
--------------------""")
    for i in range(len(tuple_list)):
        spacing = " "*(18 - len(str(tuple_list[i][0])) - len(str(tuple_list[i][1])))
        print(f"{tuple_list[i][0]}{spacing}{tuple_list[i][1]}")
    print("--------------------")
    
# score_dict = {"Ryu": 500, "Ken": 300, "Gouki": 700, "Dhalsim": 250}
score_dict = {"Ryu": 600, "Ken": 300, "Gouki": 700, "Dhalsim": 250, "Guile": 550,
              "Blanka": 450, "Chun-Li": 300, "Cammy": 250}
print_high_scores(score_dict)