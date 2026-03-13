from functools import wraps


def cache_result(func):
    cache = {}

    @wraps(func)
    def wrapper(*args):
        if args in cache:
            print("Returning cached result")
            return cache[args]

        print("Computing result")
        result = tuple(func(*args))
        cache[args] = result
        return result

    return wrapper


@cache_result
def generator_squares(n):
    for i in range(1, n + 1):
        print(f"Generating Square of {i}")
        yield i * i


res1 = generator_squares(5)
print(res1)

res2 = generator_squares(5)
print(res2)