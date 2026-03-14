#Task 7 - Grading System

candidate_marks = int(input("Enter your candidate marks: "))
if candidate_marks >= 90:
    print("Grade A")
elif 70 <= candidate_marks < 90 :
    print("Grade B")
elif 50 <= candidate_marks < 70:
    print("Grade C")
else:
    print("Fail")