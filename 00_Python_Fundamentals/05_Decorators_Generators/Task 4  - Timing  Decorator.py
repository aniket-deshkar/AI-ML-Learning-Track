import time,functools

def time_it(func):
    @functools.wraps(func)
    def time_keeper(*args,**kwargs):
        start_time = time.perf_counter()
        func(*args,**kwargs)
        end_time = time.perf_counter()
        print(f"Time taken: {end_time - start_time:.2f}s")
    return time_keeper

@time_it
def slow_down():
    print("Slowdown of 5 seconds.")
    time.sleep(5)
    return "Done!"

def log_function_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__} with args {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_function_call
@time_it
def combined_function_call(x):
    time.sleep(5)
    print(x * 2)

slow_down()
print("Output: ",combined_function_call(10))

