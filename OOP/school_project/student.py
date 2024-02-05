"""Student class with student name and grades."""


class Student:
    
    def __init__(self, name: str):
        self.name = name
        self.grades = []
        self.id = None
    
    def set_id(self, id: int):
        if self.id == None:
            self.id = id
        
    def get_id(self) -> int:
        return self.id
    
    def add_grade(self, course, grade: int):
        self.grades.append((course, grade))
    
    
    def get_grades(self):
        return self.grades
    
    
    def get_average_grade(self):
        grade_length = len(self.grades)
        total_grades = 0
        
        if grade_length > 0:
            for grade in self.grades:
                total_grades += grade[1]
            return (total_grades / grade_length)
        else:
            return -1


    def __repr__(self) -> str:
        return self.name
