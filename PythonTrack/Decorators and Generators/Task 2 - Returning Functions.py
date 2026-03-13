def make_multiplier(n):
    def decorator(func):
        def wrapper(x):
            return func(x) * n
        return wrapper
    return decorator

@make_multiplier(2)
def double(x):
    return x

@make_multiplier(3)
def triple(x):
    return x

print(double(10))
print(triple(10))
