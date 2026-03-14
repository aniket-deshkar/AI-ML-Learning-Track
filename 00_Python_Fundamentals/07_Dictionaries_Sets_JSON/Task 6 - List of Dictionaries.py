employees = [
    {"name" : "Amit", "salary" : 50000, "dept" : "IT"},
    {"name" : "Neha", "salary" : 60000, "dept":"HR"},
    { "name" : "Rohit", "salary" : 55000, "dept":"IT"},
]

print("Employees in IT: ")
for employee in employees:
    if employee["dept"] == "IT":
        print(employee["name"])

salaries = [employee["salary"] for employee in employees]
type(salaries)
average_salary = sum(salaries)/len(salaries)
print("Average salary: ", average_salary)

for employee in employees:
    if employee["dept"] == "IT":
        employee["salary"] = employee["salary"] + employee["salary"] * 0.1

print("Updated Salaries: ", employees)