#Task 9 - Counting Logic
evennumber = 0
user_input = int(input("Enter a number: "))
print("User input: ", user_input)
print("User input range numbers:")
for i in range(1, user_input + 1):
    print(i, end=" ")

    if user_input % 2 == 0:
         evennumber += i
print()
print("Sum of even numbers: ", evennumber)

