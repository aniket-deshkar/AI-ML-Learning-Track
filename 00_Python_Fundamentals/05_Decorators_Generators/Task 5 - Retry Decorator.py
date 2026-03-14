import random
 
def retry_on_exception(retry=3):
    def decorator(func):
        def wrapper(*args):
            for attempt in range(1,retry+1):
                try:
                    print("Attempt:",attempt)
                    return func(*args)
 
                except Exception as e:
                    print("Error:",e)
            print ("All retries failed")
        return wrapper
    return decorator
 
@retry_on_exception(retry=3)
def risky_task():
    if random.choice([True,False]):
        raise ValueError("Random failure")
    return "success"
 
print(risky_task())