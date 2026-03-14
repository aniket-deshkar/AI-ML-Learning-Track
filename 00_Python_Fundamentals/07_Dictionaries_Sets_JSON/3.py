student1 = {"first_name": "John", "last_name": "Doe", "marks": 50}
print("Student 1: ", student1)
student2 = {"first_name": "John", "last_name": "Snow", "marks": 60}
print("Student 2: ", student2)
student3 = {"first_name": "John","second_name":"Snow","marks":70}
print("Student 3: ", student3)
student4 = {"first_name":"John","second_name":"Snow","marks":80}
print("Student 4: ", student4)
student5 = {"first_name":"John","second_name":"Snow","marks":75}
print("Student 5: ", student5)

all_students = [student1, student2, student3, student4, student5]

max_score = max(student["marks"] for student in all_students)

highest_score =0

for topper in all_students:
    if topper["marks"] == max_score:
        highest_score = topper
        break

print(f"Highest marks: {highest_score["marks"]} - {highest_score['first_name']}")
