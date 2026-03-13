import json

employee1=  {"name" : "Amit", "salary" : 50000, "dept" : "IT"}
employee2 = {"name" : "Neha", "salary" : 60000, "dept":"HR"}
employee3= { "name" : "Rohit", "salary" : 55000, "dept":"IT"}

employees= [employee1, employee2, employee3]
print("Employee List: ",employees)

with open("employees.json", "w") as file:
    json.dump(employees, file, indent=2)

with open("employees.json") as file:
    employees = json.load(file)
print("Reading from employees.json",employees)