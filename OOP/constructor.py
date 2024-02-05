"""Constructor exercise."""


class Empty:
    """An empty class without constructor."""

    pass


class Person:
    """Represent person with firstname, lastname and age."""
    def __init__(self):
        self.firstname = ""
        self.lastname = ""
        self.age = 0

class Student:
    """Represent student with firstname, lastname and age."""
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

if __name__ == '__main__':
    # Loo Empty objekt
    empty_objekt = Empty()

    # 3 x person usage
person1 = Person()
person1.firstname = "Peeter"
person1.lastname = "Pikk"
person1.age = 12

person2 = Person()
person2.firstname = "Madis"
person2.lastname = "Limpsi"
person2.age = 73

person3 = Person()
person3.firstname = "Kaspar"
person3.lastname = "Koorits"
person3.age = 16
    # 3 x student usage
student1 = Student("Michael", "Jordan", 60)
student2 = Student("Luka", "Dončić", 24)
student3 = Student("LeBron", "James", 39)
