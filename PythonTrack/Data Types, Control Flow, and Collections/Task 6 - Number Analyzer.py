#Task 6 - Number Analyzer

user_input = int(input("Enter a number: "))
print("User input: ", user_input)
if user_input >0 :
    print("Positive Number")
elif user_input <0:
    print("Negative Number")
else:
    print("Number is 0")

if user_input % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")