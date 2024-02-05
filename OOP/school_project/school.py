"""School class which stores information about courses and students."""


class School:
    
    
    def __init__(self, name):
        self.students = []
        self.courses = []
        self.name = name
    
    
    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
    
    
    def add_student(self, student):
        if student not in self.students:
            student.set_id(len(self.students) + 1)
            self.students.append(student)
    
    
    def add_student_grade(self, student, course, grade: int):
        if course in self.courses and student in self.students:
            student.add_grade(course, grade)
            course.grade.append((student, grade))
    
    
    def get_students(self):
        return self.students
    
    
    def get_courses(self):
        return self.courses
    
    
    def get_students_ordered_by_average_grade(self):
        students_ordered = sorted(self.students, key=lambda student: student.get_average_grade(), reverse=True)
        return students_ordered
