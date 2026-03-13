#Task 10 - Reverse Number
input_number = input("Enter a number")
print("User input: ", input_number)
if int(input_number) < 10:
    print("Enter a double digit or higher number.")
else:
    print("Reversed number:",input_number[::-1])

