class Student:

    #__init__ acting as both default and parameterized constructor
    def __init__(self, name = "Default Student Name", age = 20, marks=None):
        if marks is None:
            marks = [10, 20, 30]
        self.name = name
        self.age = age
        self.marks = marks

print("Default Student Data")
default_student = Student()
print("Default Student name: ",default_student.name)
print("Default Student age:  ",default_student.age)
print("Default Student marks: ",default_student.marks)

print("Student 1 Data")
student1 = Student()
student1.name = "George"
student1.age = 30
student1.marks = [33,44,55,66]
print("Student 1 name: ",student1.name)
print("Student 1 age: ",student1.age)
print("Student 1 marks: ",student1.marks)

print("Student 2 Data")
student2 = Student()
student2.name = "George"
student2.age = 23
student2.marks = [67,56,87]
print("Student 2 name: ",student2.name)
print("Student 2 age: ",student2.age)
print("Student 2 marks: ",student2.marks)

print("Student 3 Data")
student3 = Student()
student3.name = "George"
student3.age = 19
student3.marks = [65,34,12,56]
print("Student 3 name: ",student3.name)
print("Student 3 age: ",student3.age)
print("Student 3 marks: ",student3.marks)



