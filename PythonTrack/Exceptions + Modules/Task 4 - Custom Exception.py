from NegativeValueError import NegativeValueError
def check_positive(num):
    if num < 0:
        raise NegativeValueError(f"{num} is Negative.")
    print(f"{num} is positive")
try:
    value_1 = check_positive(2)
    value_2 = check_positive(-33)
except NegativeValueError as error:
    print("Error occured: ", error)
        

