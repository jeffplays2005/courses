def process_student_data(filename):
    file_open = open(filename)
    individual_lines = file_open.read().split('\n')
    file_open.close()
    
    while len(individual_lines) > 0:
        name_and_max = individual_lines.pop(0).split(": ")
        scores = individual_lines.pop(0).split(",")
        name = name_and_max[0]
        maximum_marks = int(name_and_max[1])

        integer_scores = []
        for i in scores:
            integer_scores.append(int(i))
            
        integer_scores = sorted(integer_scores)[::-1]
        integer_scores = integer_scores[0:maximum_marks]
        
        total = 0
        for i in integer_scores:
            total += i
        average = total / len(integer_scores)
        
        print(f"Average of {name}'s best {maximum_marks} marks is {round(average, 2)}")
        
process_student_data("StudentData2.txt")