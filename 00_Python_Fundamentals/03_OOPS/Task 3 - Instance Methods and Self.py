class Student:

    def __init__(self,marks =None):
        if marks is None:
            self.marks = []
        else:
            self.marks = marks


    def average_marks(self):
        return sum(self.marks)/len(self.marks)


    def display(self,average_marks):
        print("Average Marks: ",average_marks)

student = Student()
student.marks = [1,2,3,4,5]
average = student.average_marks()
student.display(average)