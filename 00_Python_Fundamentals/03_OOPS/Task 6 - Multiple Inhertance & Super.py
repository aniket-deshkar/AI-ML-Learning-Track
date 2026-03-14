class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        return f"Name: {self.name}, Age: {self.age}"

class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary

    def display(self):
        #Display of Person class
        super().display()
        print("Subject:", self.subject)
        print("Salary:", self.salary)

class Department(Teacher):
    def __init__(self, name, age, subject, salary,dept_name):
        super().__init__(name,age,subject,salary)
        self.dept_name = dept_name
    def display(self):
        #display method of Teacher class
        super().display()
        print("Department:", self.dept_name)

output = Department(name="Alex",age=20,subject="Math",salary=500,dept_name="Path2AI")
output.display()