class CourseRankings:
    def __init__(self, course_code):
        self.course_code = course_code
        self.course_roster = []

    def enrol_student(self, student):
        self.course_roster.append(student)

    def enrol_students(self, student_list):
        for student in student_list:
            self.course_roster.append(student)

    def __str__(self):
        new_string = ""
        new_string += "COMPSCI 130 Student Ranking\n===========================\n\n"
        pqueue = PriorityQueueMax()
        for student in self.course_roster:
            pqueue.insert(student)

        new_list = []
        for i in range(1, pqueue.size+1):
            new_list.append(pqueue.delete_maximum())
       
        for i in range(len(new_list)):
            new_string += "{: <4}{}".format(i+1, new_list[i])
            new_string += "\n"
            
        return new_string.strip()
