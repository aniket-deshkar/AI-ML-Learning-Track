class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        return f"Name: {self.name}, Age: {self.age}"

class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        Person.__init__(self,name, age)
        self.subject = subject
        self.salary = salary

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Subject:", self.subject)
        print("Salary:", self.salary)

teacher = Teacher("Alex",20,"Math",50000)
teacher.display()