import sys

def even_numbers(n):
    gen = (i for i in range(0,n+1,2))
    print(f"Size of gen : {sys.getsizeof(gen)} bytes")
    even_gen = list(gen)
    print(f"Size of even_gen : {sys.getsizeof(even_gen)} bytes")
    print("Using Generators: ", even_gen)

def even_nums_list(n):
    even_numbers_list = [ i for i in range(0,n+1,2)]
    print(f"Size of list : {sys.getsizeof(even_numbers_list)} bytes")
    print("Using List: ",even_numbers_list)

even_numbers(10)
even_nums_list(10)
    
