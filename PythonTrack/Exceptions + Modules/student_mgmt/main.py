from student_exceptions import InvalidMarksError, DuplicateIDError
from students import Student
from utils import top_scorer,average_marks
import json

outfile_path = "/home/aniket-deshkar/PycharmProjects/Path2AI/PythonTrack/Exceptions + Modules/student_mgmt/students_output.json"

students = []
def add_student(id, name, marks):
    try:
        students.append(Student(id, name, marks))
    except(InvalidMarksError, DuplicateIDError) as error:
        print("Student creation failed due to ", error)


add_student(101, 'Alex', [45,54,76])
add_student(102, 'Charlie', [65,87,88])
add_student(103, 'Bob', [78,45,88])
add_student(101, 'Alice', [65,34,87])
add_student(104, 'Ross', [54,56,76])
add_student(105, 'Austin', [45,23,54])
add_student(106, 'Steve', [45,23,56])

print()
print('Student data:')
for index in students:
    print(index.id, index.name, index.marks)
print()

with open(outfile_path, "w") as outfile:
    try:
        json.dump([student.to_dict() for student in students], outfile, indent=4)
    except AttributeError as error:
        print(error)
loaded_student_data = []
try:
    with open(outfile_path, 'r') as f:
        data = json.load(f)
except FileNotFoundError as error:
    print(error)
topper = top_scorer(data)
print(topper)