employees = [
    {"name" : "Amit", "salary" : 50000, "dept" : "IT"},
    {"name" : "Neha", "salary" : 60000, "dept":"HR"},
    { "name" : "Rohit", "salary" : 55000, "dept":"IT"},
]

dictionary_of_lists = {}
for employee in employees:
    department = employee["dept"]
    name = employee["name"]
    if department not in dictionary_of_lists:
        dictionary_of_lists[department] = []
    dictionary_of_lists[department].append(name)
print(dictionary_of_lists)