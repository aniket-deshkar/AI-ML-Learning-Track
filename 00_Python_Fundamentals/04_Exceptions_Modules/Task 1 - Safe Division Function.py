def safe_divide(a,b):
    try:
        c = a/b
    except ZeroDivisionError as error:
        return "Division by zero is not possible, input denominator greater than 0",error
    return c
    
value_1 = safe_divide(5,1)
print("Value 1: ",value_1)
value_2 = safe_divide(5,0)
print("Value 2: ",value_2)

