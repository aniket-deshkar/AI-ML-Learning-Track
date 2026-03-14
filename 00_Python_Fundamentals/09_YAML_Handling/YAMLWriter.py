import yaml

print("Input Dictionary:")
courses = {
    1: {"name": "Python", "duration": "4 weeks"},
    2: {"name": "Java", "duration": "6 weeks"},
    3: {"name": "Web Development", "duration": "8 weeks"},
    4: {"name": "Data Science", "duration": "10 weeks"}
}

print(courses)

with open("courses_export.yaml", 'w') as file:
    yaml.dump(courses,file)

print("After writing into YAML:")

with open("courses_export.yaml", 'r') as file:
    courses = yaml.safe_load(file)
    print(courses)