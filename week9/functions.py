#takes in the avg grade and prints out the letter grade
def print_grade(grade):
    if grade >= 90:
        print("A")
    elif grade >= 80:
        print("B")
    elif grade >= 70:
        print("C")
    else:
        print("F")

#takes in the avg grade and returns the letter grade as a string
def get_grade(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    else:
        return "F"




student1 = 85
student2 = 90
student3 = 78

print("student1")
print_grade(student1)
g = get_grade(student1)
print(g)

