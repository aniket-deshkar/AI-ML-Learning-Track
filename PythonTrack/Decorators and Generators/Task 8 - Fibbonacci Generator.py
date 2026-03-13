def fibonacci_generator(n):
    a,b = 0,1
    for _ in range(n):
        yield a
        a,b = b,a+b

fibonacci = fibonacci_generator(10)
print("next(): ", next(fibonacci))
print("next(): ", next(fibonacci))
print("next(): ", next(fibonacci))
print("next(): ", next(fibonacci))
print("next(): ", next(fibonacci))
print("next(): ", next(fibonacci))
