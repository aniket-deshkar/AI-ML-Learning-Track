def format_output(uppercase=False):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if uppercase:
                return result.upper()
            else:
                return result

        return wrapper

    return decorator


@format_output(uppercase=True)
def greet():
    return "Hello World!"


print(greet())