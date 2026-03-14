#Task 3 - Smart Calculator

first_number = eval(input("Enter 1st number: "))
second_number = eval(input("Enter 2nd number: "))

#Sum
sum_output = first_number + second_number
print("Sum: ",sum_output)

#Product
product = first_number * second_number
print("Product: ",product)

#Greater than
if first_number > second_number:
    largest_number = first_number
else:
    largest_number = second_number

#Less than
if first_number < second_number:
    smallest_number = first_number
else:
    smallest_number = second_number
#equals
if first_number == second_number:
    print("The numbers are equal")
else:
    print("The numbers are not equal")

#difference
difference = largest_number - smallest_number
print("Difference: ",difference)

