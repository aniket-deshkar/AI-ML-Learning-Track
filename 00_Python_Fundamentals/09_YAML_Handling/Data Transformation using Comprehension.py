import json, yaml
with open("YAML Handling and Comprehensions/students.json") as file:
    students = json.load(file)

    above_sixty = {name: sum(marks)/len(marks) for name, marks in students.items() if sum(marks)/len(marks) > 60}
    print(f"Above sixty: {above_sixty}")

    output = {name : {"Average": sum(marks)/len(marks),"Status" :"Pass" if sum(marks)/len(marks) > 50 else "Fail"} for name, marks in students.items()}
    print("New Structure: ", output)
