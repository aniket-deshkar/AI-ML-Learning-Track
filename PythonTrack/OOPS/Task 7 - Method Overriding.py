class Student:
    def __init__(self,marks =None):
        if marks is None:
            self.marks = []
        else:
            self.marks = marks


    def average_marks(self):
        return sum(self.marks)/len(self.marks)


class SpecialStudent(Student):

        def average_marks(self):
            return (sum(self.marks)/len(self.marks)) + 100

bonus_marks = SpecialStudent()
bonus_marks.marks = [10,20,30,40,50]
print("Added 100 to average: ",bonus_marks.average_marks())

#Parent class defines properties, functions, bheaviour of methods.
#Child Class inherits the properties, functions and variables from parent and modifies the functions as per the needs.



