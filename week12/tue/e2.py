class Student:
    def __init__(self, name):
        self.name = name
        self.grade = "F"
        self.seat = "0"

    def set_grade(self, grade):
        self.grade = grade
    
    def set_seat(self, s):
        self.seat = s


student1 = Student("Alice")
student2 = Student("Bob")

student1.set_grade("A")