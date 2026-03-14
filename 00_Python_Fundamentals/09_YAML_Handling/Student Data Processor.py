import yaml, json

json_file_path = "/home/aniket-deshkar/PycharmProjects/Path2AI/PythonTrack/YAML Handling and Comprehensions/student_details.json"
yaml_output_path = "/home/aniket-deshkar/PycharmProjects/Path2AI/PythonTrack/YAML Handling and Comprehensions/student_details.yaml"
with open(json_file_path, "r") as student_details_json:
    student_details_json = json.load(student_details_json)

def grade_mapper(student_marks):
    if student_marks >= 90:
       return "Grade A"
    elif student_marks >= 70:
         return "Grade B"
    elif student_marks >= 50:
        return "Grade C"
    else:
         return "Fail"

for college in student_details_json["college"]:
    for branch in college["branches"]:
        for student in branch["students"]:

            marks = int(input(f"Enter Marks for {student['name']} :"))
            if marks > 100:
                marks = int(input("Please enter marks less than 100 :"))
                student["marks"] = marks

            age = int(input(f"Enter age for {student['name']} :"))
            if age > 40:
                 age=int(input("Please Enter the age less than 40:"))
            student["grade"] = grade_mapper(marks)
            if age >= 18:
                    student["age"] = age
                    print(student["name"],"is Adult & eligible for admission" )
            else:
                    student["age"] = age
                    print(student["name"],"is Minor. Hence, not eligible for admission")


with open(yaml_output_path,"w") as student_yaml:
    yaml.dump(student_details_json,student_yaml, sort_keys=False)

