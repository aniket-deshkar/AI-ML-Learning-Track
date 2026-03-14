import json

in_file_path = "/home/aniket-deshkar/PycharmProjects/Path2AI/PythonTrack/File Handling + Functions/employees.csv"
out_file_path = "/home/aniket-deshkar/PycharmProjects/Path2AI/PythonTrack/File Handling + Functions/employees_export.csv"

def employees_data(file_path):
    employees = []
    with open(file_path,"r") as employee_file:
        lines = employee_file.readlines()

    headers = lines[0].strip().split(',')

#converting to dictionary
    for i in range(1,len(lines)):
        if not lines[i].strip():
            continue

        emp_values = lines[i].strip().split(',')
        emp_dict = {}

        for  index in range(len(headers)):
            emp_dict[headers[index]] = emp_values[index]
        employees.append(emp_dict)
    return employees

#Salary Operations
def calculate_salary(*salary_data):
     total = 0
     highest_salary = float(salary_data[0])

     for salary in salary_data:
         value = float(salary)
         total += value
         if value > highest_salary:
             highest_salary = value

     average_salary = total / len(salary_data)
     return average_salary,highest_salary

#Updating Employee Details
def update_employee_details(employee_list, target_employee, **updates):
    for employee in employee_list:
        if employee["id"] == str(target_employee):
            for key, value in updates.items():
                if key in employee:
                    employee[key] = str(value)
            return True
    return False

#Writing to a new file
def save_employee_details(file_path, employee_list):
    with open(file_path,"w") as employee_file:
        headers = list(employee_list[0].keys())
        employee_file.write(",".join(headers) + "\n")
        for employee in employee_list:
            row = []
            for h in headers:
                row.append(employee[h])
            employee_file.write(",".join(row) + "\n")

#Calling Functions

data = employees_data(in_file_path)
salaries_only = []
for employee in data:
    salaries_only.append(employee["salary"])
avg, high= calculate_salary(*salaries_only)
print(f"Average Salary: {avg}")
print(f"Highest Salary: {high}")
update_employee_details(data,102,salary = 70000)
save_employee_details(out_file_path,data)