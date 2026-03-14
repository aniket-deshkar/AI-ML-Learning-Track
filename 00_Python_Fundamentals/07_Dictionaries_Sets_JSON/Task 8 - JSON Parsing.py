import json

data = '''{
    "project" : "AI Training",
    "duration_weeks" : 10,
    "students" : ["Amit", "Neha", "Rohit"]
}'''
print(type(data))
print("Converting JSON Strings to Python Object")
student_data = json.loads(data)

student_data["students"].append("Ronin")
print("Added new student",student_data)
student_json = json.dumps(student_data)
print("Python Object to JSON String",student_json)
print(type(student_json))