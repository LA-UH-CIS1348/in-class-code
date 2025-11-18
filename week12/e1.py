student1name = "Alice"
student1grade = "A"
student1seat = "E5"

student2name = "Bob"
student2grade = "B"
student2seat = "E6"

studentnames = ["Alice", "Bob"]
studentgrades = ["A","B"]
studentseats = {"E5","E6"}

class Student:
    def __init__(self, name):
        self.name = name
        self.grade = "F"
        self.seat = "0"


student1 = Student("Alice")
student2 = Student("Bob")

student1.grade = "A"
student1.seat = "A7"