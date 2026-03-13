#Task 5 Logical Eligibility Check
age = int(input("Enter your age: "))
experience = int(input("Enter your experience: "))
print("Age: ", age)
print("Years of Experience: ", experience)
if age>=21 and experience>=1:
    print("You are an eligible.")
else:
    print("You are not eligible.")