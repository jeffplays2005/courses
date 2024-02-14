def print_students_with_target_grade(grade_dict, target_grade):
    names = []
    for i in grade_dict.keys():
        if grade_dict[i] == target_grade:
            names.append(i)
    if len(names) > 0:
        names = sorted(names)
        joined = " ".join(names)
        print(f"The following students have the target grade {target_grade}: {joined}")
    else:
        print(f"No students have the target grade {target_grade}")
        
grade_dict = {"Peter":"B", "Jane":"A", "Kathy":"A", "Mark":"A", "Tom":"C"}
target_grade = "A"
print_students_with_target_grade(grade_dict, target_grade)


grade_dict = {"Peter":"B", "Jane":"A", "Kathy":"A", "Mark":"A", "Tom":"C"}
target_grade = "D"
print_students_with_target_grade(grade_dict, target_grade)

grade_dict = {"Peter":"B", "Jane":"A", "Kathy":"A", "Mark":"A", "Tom":"C"}
target_grade = "B"
print_students_with_target_grade(grade_dict, target_grade)
target_grade = "C"
print_students_with_target_grade(grade_dict, target_grade)