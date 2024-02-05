"""Course class with name and grades."""


class Course:
    
    
    def __init__(self, name: str):
        self.name = name
        self.grade = []
    
    
    def get_grades(self):
        return self.grade
    
    
    def get_average_grade(self) -> float:
        grade_length = len(self.grade)
        total_grades = 0
        if grade_length > 0:
            for grade in self.grade:
                total_grades += grade[1]
            return (total_grades / grade_length)
        else:
            return -1
    
    
    def __repr__(self):
        return self.name
