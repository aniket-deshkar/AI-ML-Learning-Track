def factorial(n):
    if n < 0:
        print("Zero")
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(f"Factorial of {n} is {fact}")

def is_prime(n):
    if n <= 1:
        print(n, "is not a prime number")
    elif n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                print(n, "is not a prime number")
                break
        else:
            print(n, "is a prime number")
    else:
        print(n, "is not a prime number")
