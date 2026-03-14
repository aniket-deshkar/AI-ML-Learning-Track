#Task 13 - Number Triangle

user_input = int(input("number of lines: "))

for i in range(1, user_input + 1):
    for j in range(i):
        print(j+1, end=" ")
    print()