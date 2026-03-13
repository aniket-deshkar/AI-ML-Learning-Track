import json

student = {"id": 101, "first_name": "Amit", "last_name": "Sharma", "marks": 92}

student_json_string = json.dumps(student)

with open("student1.json", "w") as file:
    json.dump(student, file, indent=2)



