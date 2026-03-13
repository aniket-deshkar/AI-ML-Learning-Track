students = {
    "Amit" : 78,
    "Neha" : 85,
    "Rohit" : 72
}

print(f"Given Students: {students}")
students.update({"Rohan" : 85})
print(f"Updated Students: {students}")
students.update({"Neha" : 78})
print(f"Updated Students: {students}")
students.pop("Rohit")
print(f"Updated Students: {students}")
print(f"Student Keys - {students.keys()}")
print(f"Student Values - {students.values()}")
print(f"Student items - {students.items()}")