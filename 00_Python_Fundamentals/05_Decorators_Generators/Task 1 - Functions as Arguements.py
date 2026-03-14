def parent_decorator(func):
    def apply_operation(a,b):
           return func(a,b)
    return apply_operation

@parent_decorator
def add_numbers(a,b):
    return a+b
print(add_numbers(3,4))

@parent_decorator
def multiply_numbers(a,b):
    return a*b
print(multiply_numbers(3,4))