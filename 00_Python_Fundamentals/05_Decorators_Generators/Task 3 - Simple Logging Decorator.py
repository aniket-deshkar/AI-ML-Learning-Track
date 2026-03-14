from functools import wraps


def log_function_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__} with args {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_function_call
def greet_user(name, greeting="Hello"):
    print(f"{greeting} {name}!")

greet_user("Aniket")