import json

file_path = "/home/aniket-deshkar/PycharmProjects/Path2AI/PythonTrack/File Handling + Functions/employees.csv"

print("Reading employees data from employees.csv:" )
with open(file_path, "r") as employees_csv:
    employees_data = employees_csv.read()
    employees_data.split("\n")
    print(employees_data)
    print(type(employees_data))

print("Data after skipping headers:")

with open(file_path, "r") as employees_csv:
    next(employees_csv)
    employees_data = employees_csv.read()
    employees_data.split("\n")
    print(employees_data)
    print(type(employees_data))

employees_mapping = {}
with open(file_path, "r") as employees_csv:
    employees_data = employees_csv.read()
    employees_data.split("\n")
    for i in range(1,len(employees_data)):
        if not employees_data[i].strip():
            continue

        emp_values = employees_data[i].strip().split(',')
        emp_dict = {}
        for index in range(0,len(employees_data)):
            emp_dict[employees_data[index]] = emp_values[index]

        print(emp_dict.items())






