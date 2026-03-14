import json

with open('YAML Handling and Comprehensions/students.json', 'r') as students_input:
    students = json.load(students_input)

    no_of_students = len(students)
    print("Number of students: ",no_of_students)

    avg_marks = {name: sum(score) / len(name) for name, score in students.items()}
    print(f"Average per student:", avg_marks)

