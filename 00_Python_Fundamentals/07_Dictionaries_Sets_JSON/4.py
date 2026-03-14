import json

student1 = {"id": 101, "first_name": "Amit", "last_name": "Sharma", "marks": 92}
student2 = {"id": 102, "first_name": "Neha", "last_name": "Verma", "marks": 88}
student3 = {"id": 103, "first_name": "Rohit", "last_name": "Khanna", "marks": 74}
student4 = {"id": 104, "first_name": "Sanya", "last_name": "Malhotra", "marks": 95}
student5 = {"id": 105, "first_name": "Vikram", "last_name": "Singh", "marks": 62}

students = [student1, student2, student3, student4, student5]

with open("students_data.json", "w") as file:
    json.dump(students, file)

with open("students_data.json") as file:
    student_data = json.load(file)

for student in student_data:
    if student["marks"] > 80:
        print("Students scoring more than 80: ", student["first_name"])
