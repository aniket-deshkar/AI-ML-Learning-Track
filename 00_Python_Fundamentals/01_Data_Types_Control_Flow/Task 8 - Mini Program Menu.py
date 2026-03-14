#Task 8 - Mini Program Menu
while True:
    user_input = input("Enter a number or type 'exit' to exit: ")
    if user_input.lower() == "exit":
        print("Exiting!")
        break
    number = eval(user_input)
    square = number ** 2
    print("Square: ", square)
    cube = number ** 3
    print("Cube: ", cube)