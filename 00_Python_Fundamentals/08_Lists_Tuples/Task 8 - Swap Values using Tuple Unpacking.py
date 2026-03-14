#Task 8 - Swap Values using Tuple Unpacking
first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

first_tuple = (first_number,second_number)
print("First Tuple: ",first_tuple)
(second_number,first_number) = first_tuple
second_tuple = (first_number,second_number)
print("Second Tuple: ",second_tuple)