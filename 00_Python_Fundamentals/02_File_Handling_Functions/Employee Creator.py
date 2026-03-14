def create_employee(**kwargs):
    print("Key-Value Pairs:")
    print("Keys: ", kwargs.keys())
    print("Values: ", kwargs.values())
    emp_dict = dict()
    emp_dict.update(kwargs)
    return emp_dict
print(create_employee(name="Amit",age=25,dept="IT",salary=5000))

