import yaml

with open("YAML Handling and Comprehensions/students.yaml", 'r') as stream:
    students = yaml.safe_load(stream)
    print("Students:", students)
    print("type of data: ",type(students))
    print("Name of Students:")
    for name in students["students"]:
        print(name["name"])