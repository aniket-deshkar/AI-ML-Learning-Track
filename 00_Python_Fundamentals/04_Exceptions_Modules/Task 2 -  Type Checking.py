def add_numbers(a,b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        print("Enter int or float variables only.")
        raise TypeError
    else:
        return a+b
value_2 = add_numbers(1,2)
print("Value 2: ",value_2)
value_1 = add_numbers("A",4)
print("Value 1: ", value_1)
