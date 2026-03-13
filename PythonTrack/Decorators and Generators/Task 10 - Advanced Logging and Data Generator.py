
from functools import wraps
import time
import random

filename = "numbers.txt"
num_integers = 1000000

# Open the file in write mode ('w')
with open(filename, 'w') as outfile:
    for _ in range(num_integers):
        # Generate a random integer and write it as a string followed by a newline
        random_int = random.randint(0, 1000)
        outfile.write(str(random_int) + '\n')

print(f"Generated {num_integers} random integers in {filename}")
    
def read_number(filename):
    with open(filename, "r") as file:
        for line in file:
            yield int(line.strip())

def deco_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        starttime = time.perf_counter()
        result = func(*args, **kwargs)
        endtime = time.perf_counter()
        print(f"Function {func.__name__} took {endtime - starttime:.2f} seconds")
        return result
    return wrapper

def retry_on_failure(retries = 3):

    def deco_retry(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attemp in range(1, retries + 1):
                try:
                    return func(*args , **kwargs)
                except Exception as e:
                    print(f"Retry {attemp} | Error: {e}")
                    if attemp == retries:
                        raise
        return wrapper
    return deco_retry

@retry_on_failure()
@deco_time
def compute_stats(numbers):
    total = 0
    count = 0
    minimum = None
    maximum = None

    for num in numbers:
        total += num
        count += 1

        if minimum is None or num < minimum:
            minimum = num

        if maximum is None or num > maximum:
            maximum = num
    average = total / count if count else 0

    return {
        "sum": total,
        "average" : average,
        "min": minimum,
        "max":maximum

    }


numbers = read_number("numbers.txt")
result = compute_stats(numbers)

print(result)